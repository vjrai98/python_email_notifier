import os,sys
import time
from gmail import Gmail #pull the git repository and run setup.py else you shall get importerror 


def init():
    print("hey buddy let me check your mailbox... \n establishing a connection..")
    g= Gmail()
    print("peeking into your inbox...")
    g.login("username","password")#for gmail login
    emails= g.inbox().mail(unread=True)
    newMail(emails)

def checkMail(new_mail):
    lst=["congratulations", "Congratulations","congrats", "kasa"]#a list of important words which you want to check in the incoming email.
    for i in lst:
        if i in new_mail:
            print("tadadada its the one and only dogg")
            os.system('omxplayer test.wav')#play some music and tell ma boy its your day

    
def newMail(emails):
    if len(emails)>0:
        for email in emails:
            email.fetch()#fetch the data of emails without this you will get response as None
            
            email.read()#mark your read mails as read ;) so that next time it knows if there is another new mail
            
            new_mail=email.body#read whats written inside that mail
            checkMail(new_mail)#check your conditions if this mail is from your boss or the desired one.
    else:
        print("no new mails bro")       
def main():
    init()
    try:
        while 1:
            time.sleep(10)
            init()
    except KeyboardInterrupt:
        exit(0)
main()
        
    

