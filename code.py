print("Hey, I am a chatbot that will answer all your doubts!!!:)\n")
print("But first please tell me what should I call you?\n")
print("Hey user please enter your name-: ")
name = input()
print("Hey "+name+", welcome to this chatbot,we have the following options available for you-:\n")

email=""
address=""
gender=""
mobile=""
choice = 0
while(choice!=5):
    print("1. Contact customer care\n2. Load Information about your account\n3. Update Information About your account\n4. Ask another question\n5. Exit")
    
    updatedChoice = int(input())
    
    choice = updatedChoice
    if(choice==1):
        print("Please enter your mobile number and we will contact you shortly\n")
        print("Mobile Number-: ")
        mobileNum = input()
        mobile=mobileNum
        print("You entered the following number, "+mobile+" we will contact you shortly,is there anything else we can help you with? [Y/N]")
        yn = input()
        if(yn=="Y"):
            choice=1
        if(yn=="N"):
            choice=0
    if(choice==2):
        print("Here are the details we could fetch-:\n")
        print("Name-: "+name+"\n")
        
        if(len(mobile)>0):
            print("Mobile-: "+mobile+"\n")
        if(len(email)>0):
            print("Email-: "+email+"\n")
        if(len(address)>0):
            print("Address-: "+address+"\n")
        if(len(gender)>0):
            print("Address-: "+gender+"\n")
            
    if(choice==3):
        print("What would you like to update?\n1.Name\n2.Email\n3.Address\n4.Gender\n5.Mobile Number\n6.Back to main menu")
        updationChoice = int(input())
        if(updationChoice==1):
            newName = input()
            if(newName==name):
                print("New name can't be same as old name")
            else:
                name=newName
                
        if(updationChoice==2):
            newEmail = input()
            if(newEmail==email):
                print("New email can't be same as old email")
            else:
                email=newEmail
        
        if(updationChoice==3):
            newAddress = input()
            if(newAddress==address):
                print("New address can't be same as old address")
            else:
                address=newAddress
                
                
        if(updationChoice==4):
            newGender = input()
            if(newGender==gender):
                print("New gender can't be same as old gender")
            else:
                gender=newGender
                
        if(updationChoice==5):
            newMobile = input()
            if(newMobile==mobile):
                print("New mobile number can't be same as old mobile number")
            else:
                mobile=newMobile
                
        if(updationChoice==6):
            choice=0
        
    if(choice==4):
        print("Please type your question-: ")
        question = input()
        
        if(len(mobile)>0):
            print("Please enter your mobile number and we will contact you shortly\n")
        print("Mobile Number-: ")
        mobileNum = input()
        mobile=mobileNum
        print("Your question was,'"+question+".' You entered the following number, "+mobile+" we will contact you shortly,is there anything else we can help you with? [Y/N]")
        yn = input()
        if(yn=="Y"):
            choice=1
        if(yn=="N"):
            choice=0
    
        
    if(choice==5):
        print("Thankyou for using this bot,see you soon!!!")
        
