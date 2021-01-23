#Main Program

def mainProgram():
    #Initialise the variables
    Mode = ""       #Stores whether to encrypt or decrypt
    Message = ""    #Stores the message to convert
    Shift = 0       #Stores the value to shift the letters by that number
    newMessage = "" #Stores new message
    
    Message = InputMessage()                                #Stores input message in a variable
    Mode = InputEncryptOrDecrypt()                          #Stores input encrypt or decrypt in a variable
    Shift = InputShift()                                    #Stores input shift in a variable
    #MessageAsNumbers = convertLetters2Numbers()
    #NumbersShifted = applyShift()
    #newMessage = convertNumbers2Letters()
    newMessage = convertMessage(Message,Mode,Shift)         #Stores convert message in a variable
    outputMessage(newMessage)                               #Outputs new message

def InputEncryptOrDecrypt():                                #Function for EncryptOrDecrypt
    validResponse = False

    while validResponse == False:                           #While loop has been used to check Encrypt or Decrypt has been selected
        print("Do you want to Encrypt or Decrypt? :")       #Asks user to Encrypt or Decrypt
        Mode = input().lower()                              #User Input stored in variable Mode
        if Mode in "encrypt decrypt".split():               #Returns a list of all the words in the string, so it would return [Encrypt,Decrypt]
            print("You have chosen to, " + Mode + " , as your mode")
            return Mode                                     #Returns user input, whether to encrypt or decrypt
        else:
            print("Invalid Answer, enter whether you want to Encrypt or Decrypt.")         #Error message will come up if answer equals something else, other than encrypt or decrypt

def InputMessage():                                                                        #Function for Message
    validResponse = False

    while validResponse == False:   
        message = input("What is your message? ")                                          #Takes in the users input for message
        message = message.lower()                                                          #Converts the alphabetical characters in message to all lowercase form

        lengthOfMessage = len(message)                                                     #Checks length of message
        if lengthOfMessage > 0:                                                            #If message is less than that value 
            print("You have chosen, " + message + " ,as your message.")                    #Outputs message to show the user what message they have selected
            return message
        else:
            print("Message too short, pleast enter a message of at least 5 characters ")   #Error message, prompting the user to enter a longer message
            
            
def InputShift():
    validResponse = False

    while validResponse == False:
        shift = input ("What is the number you want to shift by? ")                            #Takes users input for shift
        if shift.isnumeric():                                                                  #Checks if shift is  a numerical value
            shift = int(shift)                                                                 #Converts the shift into an integer
            if shift >=0 and shift <=26:                                                             
                print("You have chosen, " + str(shift) + " , as your shift value")             #Shows user their chosen shift
                return shift
            else:
                print("Shift number out of 1-25 range.")                                       #Error Message, tells the user the value they have input is wrong
        else:
            print("Shift not a number")                                                        #Error Message is shown if shift contain invalid answer

        


def convertMessage(message, Mode, shift):   #Convert message contains three arguments for encrypting/decrypting your message
    newMessage = ""                         #Stores new message as a string since it has ("")
    if Mode == "encrypt":                   #If user input equal encrypt then this will happen . . . 
        for letter in message:              #For loop has been used, this generally can be refered to for every letter in message . . .
            num = ord(letter)               #Convert letter to number
            if letter.isalpha():            #Checks whether letter contains alphabetical charatcers
                if num + shift > ord("z"):  #If num + shift is greater than ord of z subtract 26 to make the number loop back around to a
                    newMessage += chr((num + shift)-26)
                else:                       #Else number plus shift does not exeeed 'z' so append string with just the shift added
                    newMessage += chr(num + shift)
            else:                           #Else if the character is non-alphabetic
                newMessage += chr(num)      #Appends the non-alphabetic character without applying a shift
               
    if Mode == "decrypt":                   #If user input equal decrypt then this will happen . . . 
        for letter in message:              #For loop has been used, this generally can be refered to for every letter in message . . .
            num = ord(letter)               #Convert letter to number
            if letter.isalpha():            #Checks whether letter contains alphabetical charatcers
                if num - shift < ord("a"):  #If num - shift is less than ord of a add 26 to make the number loop back around to a
                    newMessage += chr((num - shift)+26)
                else:                       #Else number plus shift does not exeeed 'a' so append string with just the shift added
                    newMessage += chr(num - shift)
            else:                           #Else if the character is non-alphabetic
                newMessage += chr(num)                       
    return newMessage          #Returns the new message

def outputMessage(newMessage):  #Output message takes in one argument which is the new message
    print("Your new message is: " + (newMessage)) #Displays new message after encryption/decryption           

mainProgram() #Calling the main program
