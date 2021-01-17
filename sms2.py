import urllib
import time,os
print(   "\033[1;33mPrivate Messaging!! \n Message Anyone without showing your number as a service massage!! \n   ->[Lasiya]<-   ")
print("\033[1;31m<<<_____________________________>>>\n")
while True:
    num=int(input("\033[1;36mNumber:"))
    if str(num)[0:2] not in ("77","76","71","78","70","72","75"):
        print("Number incorrect !")
        continue 
    if len(str(num)) !=9:
        print(len(str(num)))
        continue 
    msg=input(" Type Message :")
    url="https://sv2.ideamarthosting.dialog.lk/lakpriya1016Apps/wapp/otp2.php"
    body={"id":num,"apphash":msg}

    print("\033[1;31m<------waiting------>")
    try:
      import requests
    except ImportError:
      print( '%s Requests isn\ t installed, installing now.' )
      os.system('pkg install pip3' )
      os.system( 'pip3 install requests')
      print( '%s Requests has been installed.' )
      os.system('clear' )
      import requests
    r=requests.post(url,json=body)
    print ("\033[1;32m[ ..Successfully sent.. ]")
    c=input("\033[1;90mDo you want send message again? -")
    if c.lower()=="y":
        continue 
    else:
        print("\033[1;37m_GOOD BYE_")
        break
