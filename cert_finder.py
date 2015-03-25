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


def main():
    certs = get_all_certs()
    cert_map = parse_certs(certs)
    pprint.pprint(cert_map)


if __name__ == '__main__':
    main()
