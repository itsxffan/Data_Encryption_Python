def mainProgram3():
    #Variables
    Message = ""
    Mode = ""
    KeyWord = ""
    KeyWord2 = ""
    newMessage = ""
    KeyWordAsNumbers = []
    MessageAsNumbers = []
    

    #Call Functions:
    Message = InputMessage()
    Mode = InputEncryptOrDecrypt()
    KeyWord = getKeyWord()
    KeyWord2 = getKeyWord2()
    newMessage = convertMessage(Message,Mode,KeyWord,KeyWord2)
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
        elif KeyWord.isnumeric():
            print("Error: Your second keyword contains numeric values ")
        else:
            print("Error: Please enter your selected key word  ") #Error message is given

def getKeyWord2():                                  #Function for the second keyword
    KeyWord2 = ""                                   #Stores the second keyword in a variable as a string
    while True:                                     #This is a while loop with a boolean expression 'True'
        KeyWord2 = input("Please enter another key word: ") #Takes in the users input for seocnd keyword
        KeyWord2 = KeyWord2.upper()                         #Converts the second keyword in upper case form
        lengthOfKeyWord2 = len(KeyWord2)                    #Checks the length of the second keyword
        if lengthOfKeyWord2 > 0 and KeyWord2.isalpha():     #Checks if seocnd keyword contains alphabetical characters and the correct length
            print("You have chosen, " + KeyWord2 + " , as your second key word") #Diplays the second keyword for the user
            return KeyWord2                                 #Returns the users input for the second keyword
        elif KeyWord2.isnumeric():                          #Checks if users second keyword contains any numeric values
            print("Error: Your second keyword contains numeric values ")
        else:
            print("Error: Please enter your selected key word ") #Error Message 



def InputMessage():                                     #Function for message
    import os.path
    message = ""                                        #Message is stored in a variable as string

    print("Is your selected message inside a Text File <txt>? (Text File: Output.txt)")
    user_input = input("[Yes or No]: ").lower()           #Takes in user input
    while True:                                         #While loop has been used
        if user_input == "yes":                         #If user input equals yes then this will happen . . . 
            while True:
                fileName = input("Please select a file you wish to translate: ")
                if os.path.isfile(fileName): 
                    file = open(fileName, "r+")                 #File is opened("InputMessage.txt", "r")
                    message = file.read()                       #Stores the string in file in a variable
                    message = message.lower()
                    print(file.read())                          #Prints the string inside the file(InputMessage.txt)
                    file.close()                                #Closes the file
                    print(message)                              #Displays message for the user to see
                    return message                              #Returns message
                else:                                           #Else statement has been used
                    print("Error: File does not exist")         #Displays error message
        elif user_input == "no":                                #If user input equals no
            message = input("Please enter your message: ")      #Takes in user input for message
            lengthOfMessage = len(message)                      #Checks the length of given message
            message = message.lower()
            if lengthOfMessage > 0:                             #Checks the length of the message
                print("Your message is: " + message)            #Displays the message for the user
                return message                                  #Returns the users input
            else:
                print("Error: Your message is blank, please enter your message: ") #Else returns error message
        else:
            print("Error: Invalid responce, please select either [Yes or No]")
    
def InputEncryptOrDecrypt():                                #Function for Encrypt or Decrypt
    while True:                                             #While loop has been used
        print("Do you want to Encrypt or Decrypt? :")       #Ask for users input for mode
        Mode = input().lower()                              #Takes in users input for mode in lowercase form               
        if Mode in "encrypt decrypt".split():               #If mode is either encrypt or decrypt, [Encrypt,Decrypt](Split function will be used)
            print("You have chosen to, " + Mode + " , as your mode")
            return Mode                                     #Returns users input for mode, from either encrypt or decrypt
        else:           
            print("Invalid Answer, enter whether you want to encrypt or decrypt.")  #Else returns error message

                                          
def convertMessage(message, Mode, KeyWord, KeyWord2): #Function for converting message with three arguments
    newMessage = ""                         #Stores new message is stored as string
    counter = 0
    if Mode == "encrypt":                   #If mode is encrypt set the program for encryption
        for letter in message:              #for loop has been used, this can be refered to for every letter in message
            letterAsNum = ord(letter)       #Converts letter to number in message
            keyAsNum = ord(KeyWord[counter % len(KeyWord)]) #Converts letter to number in keyword
            keyAsNum -= 64
            key2AsNum = ord(KeyWord2[counter % len(KeyWord2)]) #Converts letter to number in the second keyword
            key2AsNum -= 64
            if letter.isalpha():               #Checks whether letter contains alphabetical characters
                if letterAsNum + keyAsNum + key2AsNum > ord("z")+26:   #if new letter and new number added together is greater than ord z
                    newMessage += chr((letterAsNum + keyAsNum + key2AsNum)-52)
                elif letterAsNum + keyAsNum + key2AsNum > ord("z"):   #if new letter and new number added together is greater than ord z
                    newMessage += chr((letterAsNum + keyAsNum + key2AsNum)-26)
                else: 
                    newMessage += chr((letterAsNum + keyAsNum + key2AsNum))
            else:                              #Else of character is non-alphabetic
                newMessage += chr(letterAsNum) #Appends the non-alphabetic character without applying the keyword
            counter += 1
 

    if Mode == "decrypt":                   #If mode is decrypt set the program for decryption  
        for letter in message:              #for loop has been used, this can be refered to for every letter in message
            letterAsNum = ord(letter)       #Converts letter to number in message
            keyAsNum = ord(KeyWord[counter % len(KeyWord)]) #Converts letter to number in keyword also divides the counter by the length of the keyword
            keyAsNum -= 64
            key2AsNum = ord(KeyWord2[counter % len(KeyWord2)]) #Converts letter to number in the second keyword, also divides the counter by the length of the second keyword
            key2AsNum -= 64
            if letter.isalpha():               #Checks whether letter contains alphabetical characters
                if letterAsNum - keyAsNum - key2AsNum < ord("a")-26: #if new letter and new number added together is less than ord a
                    newMessage += chr((letterAsNum - keyAsNum - key2AsNum)+52)
                elif letterAsNum - keyAsNum - key2AsNum < ord("a"):
                    newMessage += chr((letterAsNum - keyAsNum - key2AsNum)+26)
            else:                              #Else of character is non-alphabetic
                newMessage += chr(letterAsNum) #Appends the non-alphabetic character without applying the keyword
            counter += 1
    return newMessage                       #New message will be returned
         

def outputMessage(newMessage):              #Output message takes in one argument which is the new message
    import os.path
    print("Your new message is: " + (newMessage)) #Displays new message after encryption/decryption
    while True:
        Write2File = input("Do you want to write to a file [Yes or No]? ") #Takes in users input for write to file
        if Write2File == "Yes":                 #If user input equals yes then this will happen  . . .
            if os.path.isfile(Write2File):
                file = open("Output.txt", "w")      #You are opening your file to write in
                file.write(newMessage)              #Writes in new message into the file
                file.close()                        #Closes the file
                print("You have successfully written to a file") 
        elif Write2File == "No":                         #If write to file equals no then this will happen . . .
            print("YOUR CONVERSION WILL NOT BE SAVED")   #Lets the user know the conversion will not be saved in file
            print("Your new message is: " +(newMessage)) #If write to file equals no then new message would be printed
        else:
            print("You did not select Yes or No")
            

mainProgram3() #Calling the main program for task 3 program
