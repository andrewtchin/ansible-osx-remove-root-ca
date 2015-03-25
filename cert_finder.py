import shlex
import StringIO
import subprocess


def get_all_certs():
    all_certs_cmd = shlex.split('security find-certificate -a -Z /System/Library/Keychains/SystemRootCertificates.keychain')
    output = subprocess.check_output(all_certs_cmd)
    return output


def parse_certs(certs):
    num_certs = 0
    cert_map = dict()

    s = StringIO.StringIO(certs)
    for line in s:
        if line.startswith('SHA-1 hash:'):
            sha = line.split()[-1]
            print sha
            num_certs = num_certs + 1
        else:
            pass
    print('Parsed {} certificates.'.format(num_certs))


def main():
    certs = get_all_certs()
    parse_certs(certs)


if __name__ == '__main__':
    main()
