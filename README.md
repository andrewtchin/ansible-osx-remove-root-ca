# ansible-osx-remove-root-ca
Remove untrusted root CAs from OS X System Roots

### Backup existing System Roots

```
cp /System/Library/Keychains/SystemRootCertificates.keychain /System/Library/Keychains/SystemRootCertificates.keychain.bak
```

### Define root certs to remove

Add SHA-1 hash of certificate to remove as a variable in playbooks/roles/remove-certs/vars/main.yml

#### Generate a vars file

See https://github.com/andrewtchin/osx-cert-utils

Included default vars file was generated with:
```
python osx_cert_utils/cert_finder.py --whitelist-apple --whitelist-qualys --outfile main.yml --ansible-vars
```

### Run

```
ansible-playbook -vvv playbooks/osx-remove-root-ca.yml --ask-sudo-pass -i "localhost," -c local
```

### Sources

* https://support.apple.com/en-us/HT202858 - Default trusted root certs
