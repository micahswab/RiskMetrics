This license scanner python script works only on Window environment 

1/ Install Scancode from NexB on Github :

  Firstly, download this file and extract : https://github.com/nexB/scancode-toolkit/releases/download/v1.6.0/scancode-toolkit-1.6.0.zip
  Next step is to extract this file at your C drive. 
  
  Next step is open your command prompt and type this command line :
  cd C:\scancode-toolkit-1.6.0 
  
  (The purpose of this step is to change directory in order to install scancode and the license scanner works only on this directory  
  C:\scancode-toolkit-1.6.0)
  Next, type 
  scancode --help
  
  The purpose of this step is to set up scancode.
  Nextly, type
  scancode --format json samples name.json
  The purpose of this step is to scan the folder you want and output the file "name.json" This file will contain all the license it found 
  in the samples folder. You can change the name of the file samples into any folder you want to scan and you can also scan the output file 
  into the name you like with .json. Again, this license scanner python script file works on this C:\scancode-toolkit-1.6.0 and json result from scanner nexB
  If you need to scan a file, move the file to that directory and replace the name with samples with the file you want to scan
  
2/ Install Python 2 and 3

  Install python 2 and 3 in order to use scanner nexB and license scanner python script file
  
3/ How to use it :

  Double click it and a console will pop up and ask you to enter the json file you just entered from above. Also, it will ask you to enter
  the name to output. After a few second, there will be a json file appear right at where the license scanner python script is located.
  That is the shorter version of json file above. 
  
  
  
