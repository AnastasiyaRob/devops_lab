"Monitor" package is used for making snapshot of resources value:
 - cpu
 - used memory in percent
 - used swap in percent

Steps to install:
  - Install psutil: 
         pip install psutil
  - Copy package "monitor" to the work directory 
  - Install package: 
         pip install .
  - Check install packages: 
         pip list
  - To execute "monitor" script use command: 
         monitor
  - To escape from execution enter CTRL+C
  
Arguments for "monitor" script:
  -i <value> - time interval for making snapshot (30 seconds are default)
  -t json - export information to JSON-file (Plain text is default)
  

