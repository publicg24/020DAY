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
    } Password Spraying 
    } Enumerating Domain Users 
    } Foothold
    } Privilege Escalation 


Namp
--------------------------------------------------------------------------------
#nmap -sV -Pn 10.10.11.35

Findings  -    Kerberos (port 88)
        LDAP/S (ports 389, 636, 3268, 3269)
        Domain: cicada.htb
        Host: CICADA-DC
        
Note: As there is no web interface, the first thing we can check is the SMB shares.

SMB shares
-----------------------------------------------------------------------------------------------------------------
#crackmapexec - a popular tool to automate enumerating domains (including users, files/ directories, and shares