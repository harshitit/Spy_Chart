#Spy_Chart
from dictionaries import spy_details, spy_chat_history, spy_friend
from steganography.steganography import Steganography#Steganography package used to encrypt and Decrypyt the secret message
from datetime import datetime#datetime package used to deal with date and time
spy_list=['Harshit','Mayank','Dhawal']
#add the new status of a SPY
def status(spy_s):
    print "Your Current Status : "+str(spy_details[spy_s]['Status'])
    status_ask=int(raw_input("Select Status Type:\n1- Predefined\n2- Create your Own\n--> "))
    if status_ask==1:
        status_sel=int(raw_input("1- Online\n2- Offline\n--> "))
        if status_sel==1:
            spy_details[spy_s].update({'Status':'Online'})
            print "Now Your Current Status : " + str(spy_details[spy_s]['Status'])#change the current status with default status selected by spy in spy_details dictionary
        elif status_sel==2:
            spy_details[spy_s]['Status'].update({'Status':'Offline'})
            print "Now Your Current Status : " + str(spy_details[spy_s]['Status'])#change the current status with default status selected by spy in spy_details dictionary
    elif status_ask==2:
        status_cre=raw_input("Enter your status:\n-->")
        spy_details[spy_s].update({'Status':status_cre})
        print "Now Your Current Status : "+str(spy_details[spy_s]['Status'])#change the current status with spy defined status in spy_details dictionary
    return
#to add a new spy
def new_spy(spy_f):
    if len(spy_f) > 0:
        choice1 = True
        choice2 = True
        while choice1 == True:
            spy_sal = int(raw_input("New Spy Found**\nSalutation:\n1- Mr\n2- Ms\n--> "))
            if spy_sal == 1:
                print "Hello\nMr. " + spy_ask
                choice1 = False
            elif spy_sal == 2:
                print "Hello\nMs. " + spy_ask
                choice1 = False
            else:
                print "WRONG CHOICE"
        while choice2 == True:
            spy_age = int(raw_input("Enter Age b/w 12 to 50:\n--> "))
            if spy_age > 11 and spy_age < 51:
                choice1=True
                while choice1==True:
                    spy_rate = float(raw_input("Enter Ratings out of 5:\n--> "))
                    if spy_rate>-1 and spy_rate<5.1:
                        spy_list.append(spy_ask)
                        if spy_sal==1:#this condition is for ckeck and add the Salutation of new spy
                            x = {spy_f:{'Salutaion':'Mr','Status': 'Online', 'Rating': spy_rate, 'Age': spy_age,'Messagereceive':'-','Messagesend':{'Textsendto':'-','Textinformation':'-','Textsendtime':'-'}}}
                            print "WELCOME\n" + str(spy_f) + "\nSalutation : MR"+", Age : "+str(spy_age)+", Ratings : "+str(spy_rate)
                        elif spy_sal==2:
                            x = {spy_f: {'Salutaion': 'Ms', 'Status': 'Online', 'Rating': spy_rate, 'Age': spy_age,'Messagereceive': '-','Messagesend': {'Textsendto': '-', 'Textinformation': '-','Textsendtime': '-'}}}
                            print "WELCOME\n" + str(spy_f) + "\nSalutation : MS" + ", Age : " + str(spy_age) + ", Ratings : " + str(spy_rate)
                        spy_details.update(x)#the value stored in x is add in spy_details
                        spy_chat_history.update({spy_f:'-'})
                        spy_list.append(spy_f)
                        choice1=False
                        choice2=False
                    else:
                        print "Please Enter your Ratings out of 5*"
            else:
                print "Your age is not in Age limits*\nTry Again"
    else:
        print "INVALID NAME"
    return
#to add new friend of a spy
def addfriend(spy_s):
    spy_fri = raw_input("Enter your Friend's Name:\n--> ")
    if len(spy_fri) > 0:
        choice2 = True
        while choice2 == True:
            spy_age = int(raw_input("Enter Age b/w 12 to 50:\n--> "))
            if spy_age > 11 and spy_age < 51:
                choice1=True
                while choice1==True:
                    spy_friend_rate = float(raw_input("Enter Ratings out of 5 and equal or greater than your rating:\n--> "))
                    spy_rate=float(spy_details[spy_s]['Rating'])
                    if spy_friend_rate==spy_rate and spy_friend_rate<5.1:
                        spy_friend[spy_s]['friends'].update({spy_fri:{'Status': 'Online', 'Rating': spy_friend_rate, 'Age': spy_age}})#this line add a new spy's friend in spy_friend dictionary
                        choice1=False
                        choice2=False
                    else:
                        print "Ratings is not equal or greater than your rating*"
            else:
                print "Age is not in Age limits*\nTry Again"
    else:
        print "INVALID NAME"
    return
#to encode the message
def encodemsg(spy_a):
    path=raw_input("Enter the Name or Path of the image:\n-->")
    output_path=path
    text=raw_input("Enter the secret message:\n--> ")
    Steganography.encode(path,output_path,text)#this line encrypt your secret message in image
    select_a_friend=raw_input("Enter the name of the Receiver\nFriends List: "+str(spy_friend[spy_a]['friends'].keys())+":\n-->")#this line print the spy's friend list and then you have to enter the name of your friend
    spy_chat_history[spy_a]=str(spy_chat_history[spy_a])+str({'Sendto':select_a_friend,'Message':text,'Sendtime':str(datetime.today())})#here we add the send details to our spy_chat_history for future use/check
    return
#to read the message
def readmsg(spy_ab):
    get=raw_input("Enter the Name or Path of the image:\n-->")
    if len(get)>0:
        read=Steganography.decode(get)
        print read
    else:
        print "Donot Understand"
    return
#view spy chat history
def viewhist(spy_a):
    c=spy_chat_history[spy_a]
    if len(c)>0:
        print spy_chat_history[spy_a]
    else:
        print "No Message"
    return
def menu(spy_a):
    choice=True
    while choice==True:
        spy_men=int(raw_input("Operations:\n1- Add Status\n2- Add a friend\n3- Send An Encoded Message\n4- Read Message\n5- Read Previous History\n6- To quit\n--> "))
        if spy_men==1:
            status(spy_a)
        elif spy_men==2:
            addfriend(spy_a)
        elif spy_men==3:
            encodemsg(spy_a)
        elif spy_men==4:
            readmsg(spy_a)
        elif spy_men==5:
            viewhist(spy_a)
        elif spy_men==6:
            choice=False
    return
#program starts from here
choice=True
choice2=True
while choice2==True:
    spy_as=int(raw_input("Press 1 to continue with your default Name\nPress 2 to Create new Spy\nPress 3 for QUIT\n-->"))
    if spy_as==1:
        while choice==True:
            spy_ask = raw_input("-Welcome Spy-\nEnter your name:\n--> ")
            if spy_ask in spy_list:
                menu(spy_ask)
                choice=False
            else:
                print "Not Exist"
                choice = False
    elif spy_as==2:
        spy_ask = raw_input("Enter your name:\n--> ")
        new_spy(spy_ask)
    elif spy_as==3:
        print "Have A Nice Day Spy"
        choice2=False
    else:
        print "Wrong Choice"
