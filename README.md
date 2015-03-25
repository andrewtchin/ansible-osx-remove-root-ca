# ansible-osx-root-ca
Remove untrusted root CAs from OS X System Roots

### Backup existing System Roots
cp /System/Library/Keychains/SystemRootCertificates.keychain /System/Library/Keychains/SystemRootCertificates.keychain.bak

### Run
ansible-playbook -vvv playbooks/osx-root-ca.yml --ask-sudo-pass -i "localhost," -c local

### Default trusted root certs
https://support.apple.com/en-us/HT202858
