import random

global codelist
codelist = []

def MainMenu():
    print('welkom bij MasterMind\nKies een GameMode\n1. PvP\n2. PvC\n3. CvC')
    GameMode = int(input("Selecteer een playstyle: "))#selecten the playing style
    while True:
        if GameMode == 1:
            PvP()
            break
        elif GameMode == 2:
            PvC()
            break
        elif GameMode == 3:
            CvC()
            break
        else:
            print("Geef een bruikbare playstyle op.")

            
def PvP():
    Player = True
    CodeGeneratie(Player)

    
def PvC():
    print('Welke Rol wil je nemen?\n1. CodeCracker\n2. CodeMaster')
    SpellerKeuze = int(input()) # Selecting what rol you want
    if SpellerKeuze == 1:
        Player = False
    elif SpellerKeuze == 2:
        Player = True
    else:
        print('Pleas pick between the given options')
        PvC()
    
    CodeGeneratie(Player)
    return Player


def CvC():
    Player = False
    CodeGeneratie(Player)

    
def CodeGeneratie(Player):
    if Player == False: # computer random generated code
        for i in range(0,4):
            code = random.randint(1,6)
            codelist.append(code)
        print('The secret Code is:', codelist)
    if Player == True: # player self made code
        while len(codelist) != 4:
            CodeInput = int(input('Maak een code van 4 lang tussen 1 en 6'))
            if CodeInput >= 7 or CodeInput <= 0:
                print('Tussen 1 en 6!')
            else:
                codelist.append(CodeInput)
        print('The secret Code is:', codelist)
    GetCode()

    
def GetCode():
    cl = []
    userCode = ""

    while len(userCode) != 4: # Ensures that the code is exactly four digits long
        print("The code consists of 4 integers.")
        userCode = input("Input 4-digit code: ")

    try:
        for i in range(len(userCode)):
            cl.append(int(userCode[i])) # Convert string number to int
    except:
        print("please don't use letters, only digits!")
        GetCode()
    CheckBlack(cl, codelist)

    
def CheckBlack(cl, codelist):
    copy1=cl
    copy2=codelist
    pinList=[]
    for i in range(len(copy2)):
        if copy2[i] == cl[i]: # Takes out the already given numbers with feedback
            copy2[i] = None
            copy1[i] = None
            pinList.append("B")
    print(pinList)
    CheckWhite(copy1,copy2, pinList)

    
def CheckWhite(cl, codelist, pinList):
    print(cl)
    print(codelist)
    for j in cl:# Still broken
        print(j)
        if j in codelist:
            cl[j] = None
            pinList.append("W")
        print(pinList)


MainMenu()
