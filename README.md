# ansible-osx-root-ca
Remove untrusted root CAs from OS X System Roots

### Status
Playbook removes specified root certs - Complete
cert_finder.py - generate list of certs to remove (all certs) - In Progress
cert_finder.py - whitelist certs to keep
cert_finder.py - filter based on country

### Backup existing System Roots
cp /System/Library/Keychains/SystemRootCertificates.keychain /System/Library/Keychains/SystemRootCertificates.keychain.bak

### Define root certs to remove
Add SHA-1 hash of certificate to remove as a variable in playbooks/roles/remove-certs/vars/main.yml

### Run
ansible-playbook -vvv playbooks/osx-root-ca.yml --ask-sudo-pass -i "localhost," -c local

### Default trusted root certs
https://support.apple.com/en-us/HT202858
