# Lecture 2 - Securing Systems 

## Project: Secure Remore Access 

This demo showcases a secure remote login to a kali linux Vm using a "testuser" account, with ssh config, key-based authentication, and other hardening steps.
]
### Key Actions Taken:
- Created a non-root user named "testuser"
- Enabled SSH access
- Hardened ssh settings (/etc/ssh/sshd_config)
- Restricted Root Login
- Connected using: ssh testuser@<Ip>

### Importance of the Project:
- Demonstrates system hardening
- Real-world practice for remote secure access

NOTE: This project was a part of the cs50 Cybersecurity course in which i ran into a few issues with the key-based login but documented everything as i went.

Time spent: ~8 hours over 2 days 
Challenges: Troubleshooting public key authentication, configuring ssh, using port 2222, firewall and permission issues, I was able to resolve all those except the key-auth so i just skipped it, might check up on it later though. 
