# Sprint 1
-------------
1. There are multiple users in this machine
![alt text](sprintimages/image.png)
![alt text](sprintimages/image-1.png)
2. Now trying user Derek  with Username - Derek Password - Derek001
3. After logged in checking version observed that the os is Ubuntu 18.04.5  LTS
   ![alt text](sprintimages/image-2.png)
    4. Method 1:
I transferred my kali exploit file through scp command  in victim machine and runed exploit it given me the access
 and observed multiple exploit scripts are able to perform and can able to access the root privilege 
![alt text](sprintimages/image-3.png)
Method 2:Using Find method
![alt text](sprintimages/image-4.png)
Another user 
Username : Axel
 password: Axel003
![alt text](sprintimages/image-5.png)
![alt text](sprintimages/image-7.png)
![alt text](sprintimages/image-6.png)

Another user 
Username : Chrono
 password: Chrono004
![alt text](sprintimages/image-8.png)
![alt text](sprintimages/image-9.png)
To exit press esc button then type :wq! And enter. Type sudo su enter
![alt text](sprintimages/image-10.png)
Another user 
Username : Tyler
 password: Tyler002

Using nano and sudo 
![alt text](sprintimages/image-11.png)
![alt text](sprintimages/image-12.png)
Here press control R
![alt text](sprintimages/image-13.png)
Press control X
![alt text](sprintimages/image-14.png)
At the execute  type : reset; sh 1 >&0 2>&0 press enter
![alt text](sprintimages/image-15.png)
To get # in the command line. Now type root@ubuntu:~#
![alt text](sprintimages/image-16.png)
![alt text](sprintimages/image-17.png)
![alt text](sprintimages/image-18.png)
Another user 
Username : Cassidy
 password: Cassidy005

1. Making changes in cleanup.py file we can get root access as follows
2. Edit the cleanup.py file as follows and run /tmp/rootbash -p
![alt text](sprintimages/image-19.png)
Another method
3. Find SUID files enter into previous privilage with cmd: /bin/bash -p 
![alt text](sprintimages/image-21.png)
Then create a file called test
![alt text](sprintimages/image-22.png)
Using that command  and find try to get root access as below
![alt text](sprintimages/image-23.png)