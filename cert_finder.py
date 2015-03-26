import pprint
import shlex
import StringIO
import subprocess


def get_all_certs():
    all_certs_cmd = shlex.split('security find-certificate -a -Z /System/Library/Keychains/SystemRootCertificates.keychain')
    output = subprocess.check_output(all_certs_cmd)
    return output


def parse_certs(certs):
    cert_map = dict()
    sha = None
    name = None

    s = StringIO.StringIO(certs)
    for line in s:
        if line.startswith('SHA-1 hash:'):
            sha = line.split()[-1]
        if '"labl"<blob>="' in line:
            name = line.split('=')[-1].strip('\n"')
            cert_map[sha] = name

    return cert_map


def get_cert(name, pem=False):
    if pem:
        get_cert_cmd = shlex.split('security find-certificate -p -c {} /System/Library/Keychains/SystemRootCertificates.keychain'.format(name))
    else:
        get_cert_cmd = shlex.split('security find-certificate -c {} /System/Library/Keychains/SystemRootCertificates.keychain'.format(name))
    output = subprocess.check_output(get_cert_cmd)
    return output


def pem_to_der(infile_path, outfile_path):
    convert_cmd = shlex.split('openssl x509 -in {} -out {} -inform PEM -outform DER'.format(infile_path, outfile_path))
    subprocess.check_call(convert_cmd)


def add_cert(cert_path):
    """Add a certificate to the SystemRootCertificates keychain.
    Input must be in DER format.
    Requires root privileges.
    Args:
        cert_path: path to input der file
    """
    add_cmd = shlex.split('security add-certificates -k /System/Library/Keychains/SystemRootCertificates.keychain {}'.format(cert_path))
    subprocess.check_call(add_cmd)


def get_country(cert):
    pass


def main():
    certs = get_all_certs()
    cert_map = parse_certs(certs)
    # pprint.pprint(cert_map)
    error_certs = []

    for cert in cert_map:
        try:
            cert = get_cert(cert_map[cert])
            print cert
        except subprocess.CalledProcessError as e:
            if e.returncode == 44:
                print e.output
                error_certs.append(cert)
            else:
                raise

    print '===== Error count: {} ====='.format(len(error_certs))
    for cert in error_certs:
        print cert, cert_map[cert]


if __name__ == '__main__':
    main()
