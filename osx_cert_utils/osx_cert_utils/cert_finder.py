#!/usr/bin/env python

"""
Find certificates in SystemRootCertificates keychain in OS X to remove.
"""

import pprint

import osx_cert_utils

def main():
    certs = osx_cert_utils.get_all_certs()
    cert_map = osx_cert_utils.get_cert_name_map(certs)
    # pprint.pprint(cert_map)
    error_certs = []

    for cert in cert_map:
        try:
            cert = osx_cert_utils.get_cert(cert_map[cert])
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
