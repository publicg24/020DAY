#POWERVIEW\
##To perform this we need at tool called powerview which is basically a powershell script\
download from here --->https://www.powershellgallery.com/packages/PowerSploit/3.0.0.0/Content/Recon%5CPowerView.ps1
Commands - powershell -ep bypass 
         Import-Module .\powerview.ps1 
    1. Get-NetUser
    2. Get-NetUser | select cn 
    3. Get-NetUser -UserName <any user name>
    4. Get-UserProperty  / Get-UserProperty -Properties pwdlastset
    5. Find-UserField 
        a. Find-UserField -SearchField Description -SearchTerm "pass"
        b. Find-UserField -SearchField Description -SearchTerm "built"
    6. Invoke-UserHunter / Invoke-UserHunter -CheckAccess
    7. Get-NetDomain / Get-NetDomain -domain "your domain.local"
    8. Get-NetDomainController / Get-NetDomainController -Domain yourdomain.local 
    9. Get-NetComputer /
        a. Get-NetComputer -Ping
        b. Get-NetComputer -FullData
        c. Get-NetComputer -Operatingsystem "Windows Server 2016 Standard Evaluation"
    10. Get-UserProperty
        a. Get-UserProperty -Properties badpwdcount 
        b. Get-UserProperty -Properties logoncount
    11. Get-NetForest / Get-NetForestCatalog  / Get-NetForestDomain
    12. Get-NetLoggedon
        a. Get-DomainComputer | Get-NetLoggedon 
        b. Get-NetLoggedon -ComputerName DC1
    13. Get-DomainPolicy
        a. (Get-DomainPolicy)."KerberosPolicy"
        b. (Get-DomainPolicy)."SystemAccess"
    14. Get-NetOU
    15. Get-NetGroup 
        a. Get-NetGroup *admin* 
        b. Get-NetGroup -UserName Tech01
        c. Get-NetGroup -Domain vd.local
        d. Get-NetGroup -FullData
        e. Get-NetGroup "Domain Admins" 
        f. Get-NetGroup "Domain Admins" -FullData
        g. Get-NetGroup -GroupName *admin* -Domain vd.local
    16. Get-NetGroup -GroupName *admin* -Domain ignite.local
        a. Get-NetGroupMember -GroupName "Domain Admins"
        b. Get-NetGroupMember -GroupName "Administrators" -Recurse
    17. Get-NetGPO 
    18. Get-NetGPO | select displayname
    19. Find-GPOLocation 
        a. Find-GPOLocation -UserName Tech01-verbose
    20. Invoke-EnumerateLocalAdmin
    21. Get-NetProcess 
    22. Invoke-ShareFinder
    23. Invoke-FileFinder 
    24. Invoke-ACLScanner 
        a. Invoke-ACLScanner -ResolveGUIDs
    25. Find-LocalAdminAccess
    26. Get-NetSession 






































































