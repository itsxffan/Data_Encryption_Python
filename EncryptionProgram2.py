def mainProgram2():
    #Variables
    Message = ""
    Mode = ""
    KeyWord = ""
    newMessage = ""
    KeyWordAsNumbers = []
    MessageAsNumbers = []
    

    #Call Functions:
    Message = InputMessage()
    Mode = InputEncryptOrDecrypt()
    KeyWord = getKeyWord()
    #convertString2Numbers(Message)
    #convertKey2Numbers(KeyWord)
    newMessage = convertMessage(Message,Mode,KeyWord)
    outputMessage(newMessage)

def getKeyWord():                                   #Function for keyword
    KeyWord = ""                                    #Lets the programmer know its a string since it has "" 
    while True:                                     #This is a while loop with a boolean expression 'True'
        KeyWord = input("Please enter your selected key word: ") #takes in the users input for key
        KeyWord = KeyWord.upper()                   #Converts the keyword to upper case form
        lengthOfKeyWord = len(KeyWord)              #Checks the length of the keyword
        if lengthOfKeyWord > 0 and KeyWord.isalpha(): #Checks if keyword is contains alphabetical characters and the correct length
            print("You have chosen, " + KeyWord + " , as your key word")
            return KeyWord                          #Returns the users input
        else:
            print("Error Blank: Please enter your selected key word  ") #Error message is given



def InputMessage():                                 #Function for message
    validResponce = False

    while validResponce == False:                   
        message = input("What is your message: ")   #Takes users input for message and stores in variable as string
        message = message.lower()                   #The message that has been inputted by the user is given in lower case form
        lengthOfMessage = len(message)              #Checks the length of given message
        if lengthOfMessage > 0:
            print("You have chosen, " + message + " ,as your message")
            return message                          #Returns the users input
        else:
            print("Error: Your message is blank, please enter your message: ") #Else returns error message
    
    
def InputEncryptOrDecrypt():                                 #Function for Encrypt or Decrypt
    while True:                                             #While loop has been used
        print("Do you want to Encrypt or Decrypt? :")       #Ask for users input for mode
        Mode = input().lower()                              #Takes in users input for mode in lowercase form               
        if Mode in "encrypt decrypt".split():               #If mode is either encrypt or decrypt, [Encrypt,Decrypt](Split function will be used)
            print("You have chosen to, " + Mode + " , as your mode")
            return Mode                                     #Returns users input for mode, from either encrypt or decrypt
        else:           
            print("Invalid Answer, enter whether you want to encrypt or decrypt.")  #Else returns error message

                                          
def convertMessage(message, Mode, KeyWord): #Function for converting message with three arguments
    newMessage = ""                         #Stores new message is stored as string
    counter = 0
    if Mode == "encrypt":                   #If mode is encrypt set the program for encryption
        for letter in message:              #for loop has been used, this can be refered to for every letter in message
            letterAsNum = ord(letter)       #Converts letter to number in message
            keyAsNum = ord(KeyWord[counter % len(KeyWord)])          #Converts letter to number in keyword
            keyAsNum -= 64
            if letter.isalpha():        #Checks whether letter contains alphabetical characters
                if letterAsNum + keyAsNum > ord("z"):   #if new letter and new number added together is greater than ord z
                    newMessage += chr((letterAsNum + keyAsNum)-26)
                else: 
                    newMessage += chr((letterAsNum + keyAsNum))
            else:                   #Else of character is non-alphabetic
                newMessage += chr(letterAsNum) #Appends the non-alphabetic character without applying the keyword
            counter += 1
 

    if Mode == "decrypt":                    #If mode is decrypt set the program for decryption  
        for letter in message:              #for loop has been used, this can be refered to for every letter in message
            letterAsNum = ord(letter)       #Converts letter to number in message
            keyAsNum = ord(KeyWord[counter % len(KeyWord)]) #Converts letter to number in keyword
            keyAsNum -= 64
            if letter.isalpha():            #Checks whether letter contains alphabetical characters
                if letterAsNum - keyAsNum < ord("a"):       #if new letter and new number added together is less than ord a
                    newMessage += chr((letterAsNum - keyAsNum)+26)
                else: 
                    newMessage += chr((letterAsNum - keyAsNum))
            else:                           #Else of character is non-alphabetic
                newMessage += chr(letterAsNum) #Appends the non-alphabetic character without applying the keyword
            counter += 1
    return newMessage                       #New message will be returned
         

def outputMessage(newMessage):              #Output message takes in one argument which is the new message
    print("Your new message is: " + (newMessage)) #Displays new message after encryption/decryption  

mainProgram2() #Calling the main program for task 2 program
