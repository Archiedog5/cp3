import random
p1hp=50
p1dp=10
p2dp=15
p2hp=75
herohp=50
herodp=5
pieces=0
ifkey="No"
def damagep1():
        global herohp
        global herodp
        global p1dp
        dmg=random.randint(1,10)
        dmgr=int(input("Guess a number 1-10 for thier dmg: "))
        given = abs(dmg-dmgr)
        herohp-=given
        print("Your stats are now Health:",herohp,"Damage:",herodp)
def fightp1():
    global p1hp
    global herodp
    global p1dp
    dmg=random.randint(1,herodp)
    dmgr=int(input("Guess a number 1-5 for your dmg: "))
    given = abs(dmg-dmgr)
    p1hp-=given
    print("Enimies stats are now Health:",p1hp,"Damage:",p1dp)
def damagep2():
        global herohp
        global herodp
        global p2dp
        dmg=random.randint(1,10)
        dmgr=int(input("Guess a number 1-15 for thier dmg: "))
        given = abs(dmg-dmgr)
        herohp-=given
        print("Your stats are now Health:",herohp,"Damage:",herodp)
def fightp2():
    global p2hp
    global herodp
    global p2dp
    dmg=random.randint(1,herodp)
    dmgr=int(input("Guess a number 1-10 for your dmg: "))
    given = abs(dmg-dmgr)
    p2hp-=given
    print("Enimies stats are now Health:",p2hp,"Damage:",p2dp)

p1LetGo=random.randint(1,5)
p2LetGo=random.randint(1,10)
def comabtP1():
    global herohp
    global herodp
    global p1hp
    global p1dp
    fightP1= input("Fight or take your chance to run. If you want to run press 1, if you want to fight press 2.: ")
    if fightP1 == "1":
        guess=int(input("Ok guess a number 1-5.(If you get it right you can scoot right pass him.): "))
        if guess != p1LetGo:
            print("He stopped you in your tracks it's now time to fight.")
            while herohp>0 and p1hp>0:
                damagep1()
                fightp1()  
            if herohp<=0:
                print("Game over; the gaurd deafeted you.")

            elif p1hp<=0:
                print("You deafected the guard.")
        else:
            print("You distracted him and got pass the door with piece 2.")
    if fightP1 == "2":
        print ("Then square up because the guard is bout to throw the first hand.")
        while herohp>0 and p1hp>0:
                damagep1()
                fightp1()  
        if herohp<=0:
                print("Game over; the gaurd deafeted you.")

        elif p1hp<=0:
            print("You deafected the guard.")
def combatP2():
    global herohp
    global herodp
    global p2hp
    global p2dp
    fightP2= input("Fight or take your chance to run. If you want to run press 1, if you want to fight press 2.: ")
    if fightP2 == "1":
        guess=int(input("Ok guess a number 1-10.(If you get it right you can scoot right pass him.): "))
        if guess != p2LetGo:
            print("He stopped you in your tracks it's now time to fight.")
            while herohp>0 and p2hp>0:
                damagep2()
                fightp2()  
            if herohp<=0:
                print("Game over; the gaurd deafeted you.")

            elif p2hp<=0:
                print("You deafected the guard.")
        else:
            print("You distracted him and got pass the door with piece 2.")
    if fightP2 == "2":
        print ("Well you better throw the first punch because that might be the only chance of deafting him.")
        while herohp>0 and p1hp>0:
                fightp2()
                damagep2()  
        if herohp<=0:
            print("Game over; the gaurd deafeted you.")

        elif p2hp<=0:
             print("You deafected the guard.")
def damagep1():
        global herohp
        global herodp
        global p1dp
        dmg=random.randint(1,10)
        dmgr=int(input("Guess a number 1-10 for thier dmg: "))
        given = abs(dmg-dmgr)
        herohp-=given
        print("Your stats are now Health:",herohp,"Damage:",herodp)
def fightp1():
    global p1hp
    global herodp
    global p1dp
    dmg=random.randint(1,herodp)
    dmgr=int(input("Guess a number 1-5 for your dmg: "))
    given = abs(dmg-dmgr)
    p1hp-=given
    print("Enimies stats are now Health:",p1hp,"Damage:",p1dp)
def damagep2():
        global herohp
        global herodp
        global p2dp
        dmg=random.randint(1,10)
        dmgr=int(input("Guess a number 1-15 for thier dmg: "))
        given = abs(dmg-dmgr)
        herohp-=given
        print("Your stats are now Health:",herohp,"Damage:",herodp)
def fightp2():
    global p2hp
    global herodp
    global p2dp
    dmg=random.randint(1,herodp)
    dmgr=int(input("Guess a number 1-5 for your dmg: "))
    given = abs(dmg-dmgr)
    p2hp-=given
    print("Enimies stats are now Health:",p2hp,"Damage:",p2dp)

p1LetGo=random.randint(1,5)
p2LetGo=random.randint(1,10)
def comabtP1():
    global herohp
    global herodp
    global p1hp
    global p1dp
    fightP1= input("Fight or take your chance to run. If you want to run press 1, if you want to fight press 2.: ")
    if fightP1 == "1":
        guess=int(input("Ok guess a number 1-5.(If you get it right you can scoot right pass him.): "))
        if guess != p1LetGo:
            print("He stopped you in your tracks it's now time to fight.")
            while herohp>0 and p1hp>0:
                damagep1()
                fightp1()  
            if herohp<=0:
                print("Game over; the gaurd deafeted you.")

            elif p1hp<=0:
                print("You deafected the guard.")
        else:
            print("You distracted him and got pass the door with piece 2.")
    if fightP1 == "2":
        print ("Then square up because the guard is bout to throw the first hand.")
        while herohp>0 and p1hp>0:
                damagep1()
                fightp1()  
        if herohp<=0:
                print("Game over; the gaurd deafeted you.")

        elif p2hp<=0:
            print("You deafected the guard.")
def combatP2():
    global herohp
    global herodp
    global p2hp
    global p2dp
    fightP2= input("Fight or take your chance to run. If you want to run press 1, if you want to fight press 2.: ")
    if fightP2 == "1":
        guess=int(input("Ok guess a number 1-10.(If you get it right you can scoot right pass him.): "))
        if guess != p2LetGo:
            print("He stopped you in your tracks it's now time to fight.")
            while herohp>0 and p2hp>0:
                damagep2()
                fightp2()  
            if herohp<=0:
                print("Game over; the gaurd deafeted you.")

            elif p2hp<=0:
                print("You deafected the guard.")
        else:
            print("You distracted him and got pass the door with piece 2.")
    if fightP2 == "2":
        print ("Well you better throw the first punch because that might be the only chance of deafting him.")
        while herohp>0 and p1hp>0:
                fightp2()
                damagep2()  
        if herohp<=0:
            print("Game over; the gaurd deafeted you.")

        elif p2hp<=0:
             print("You deafected the guard.")
print("Welcome to Wierd Al Yankovic The Game.")
doYouWantToPlay = input(" Do you want to play? If so press 1. (Anything else is the wrong answer):")
while doYouWantToPlay !="1":
    print("Wrong answer. If you don't chose right we will be stuck in this loop forever. So Let me ask again.")
    doYouWantToPlay = input(" Do you want to play? If so press 1. (Anything else is the wrong answer):")
name = input("Good. Now what's your name?:")
print("The setting starts at your friends house, name benard.")
print("Benard: Hey",name+", did you know wierd al is having a concert tonight?")
print(name+": Really were is he playing?!")
print("Benard: He is playing at a venue 10 mins away from here lets go.")
print(name+": Okay, Okay! Let me get a song that I wan't him to play. It's in my room.")
print("Benard: Are you really bringing anoter song to concert. We all know that he won't play it then your going to throw a hissy fit and ruin the concert.")
print(name+": Nu Uh!")
print("Benard:",name+"!")
print(name+": Okay if I promise not to throw a hissy fit then will you let me bring it?")
print("Benard: Fine, I will let you if promise.")
print(name+": I promise.")
print("Benard: Ok lets go.")
print("10 minutes later....")
print("Guard 1: No, I am not going to force Wierd Al Yankoviv to play your song.")
print(name+(": Why not dude? Im just acting for a favor."))
print("Guard 1: You know whay give me that paper. (Contiues to grab it out of your hands and rip it to pices and disrubutes it across the building.)")
print(name+": Dude not cool.")
print("Guard 1: Cry about it.")
print("Benard: Please don't make a scene and try to colect all of the pices of paper.")
print(name+": Well that just what I'm going to do. (You continue to climb to the roof and jump through a sun light.)")
room1 = input("You find a the first piece of paper with the lyrics on it. Do you wan't to pick it up? Y or N?: ")
if room1 == "N":
    print("You literaly commited breaking and enterning to get your song back. But it's ok you can just ingnor it. You little menis. You know what, nvm. YOU TOOK THE PIECE OF PAPER.")
    pieces+=1    
elif room1 == "Y":
    print("You collected your first piece of paper it says 'To the town of Agua Fria rode a stranger one fine day/ Hardly spoke to folks around him, didn't have too much to say/ No one dared to ask his business, no one dared to make a slip/ For the stranger there among them had a big iron on his' ")
    print("Good job. Only 8 more pieces to go.") 
    pieces+=1
hallwayLorR = input("Now you are here do you want to go to left or right?(1 for left, 2 for right): ")
if hallwayLorR ==  "2" and ifkey == "Yes":
     pass 
elif hallwayLorR == "2" and ifkey == "No":
    print("This door is locked, try the other one.")
elif hallwayLorR == "1":
    room123 = input("You see three rooms, left right and center wich one do you want to go to?(1,2 and 3,): ")
    if room123 == "3":
        print( "You see a gaurd, fight!!!")
        print("Defence works by gussing how much thier going to damage you. Then it gets the absolute value of thier actul damage minus your guess.")
        print("Offence works the same but your gussing your dmg.")
        comabtP1()
        pieces+=1
        print("You scavange the nocked out gaurd and you find your secound piece of paper. And it says'941'. The same guard also has a piece of paper that says 'big iron on his hip/ Big iron on his hip/ In this town there lived an outlaw by the name of Texas Red/ Many men had tried to take him and that many men were dead/ He was vicious and a killer though a youth of 24/ And the notches")
    elif room123 == "2":
        print("You found another piece of paper and it says 'hip/ Big iron on his hip/ It was early in the morning when he rode into the town/ He came riding from the south side slowly lookin' all around/ He's an outlaw loose and running, came the whisper from each lip/ And he's here to do some business with the' ")
        pieces+=1
    elif room123 == "1":
        print("You see a chest in the center of the room. But it requires a code. What is the code?;")
        chestcode=int(input("Whats the code to the chest?: "))
        if chestcode==941:
            print("You find two things a key too the right hallway and a potion that increases your dmg by 10 points")
            ifkey="yes"
        else:
            leave=0
            while chestcode!=941 and leave=="1" :
                print("wrong")
                leave=input("Do you want to leave or try again. 1 for leave and 2 to try agian.")
            room23=input("Now do you want to go to the center room or right room?: ")
        if room23=="2":
            print("You found another piece of paper and it says 'hip/ Big iron on his hip/ It was early in the morning when he rode into the town/ He came riding from the south side slowly lookin' all around/ He's an outlaw loose and running, came the whisper from each lip/ And he's here to do some business with the' ")
            pieces+=1
        elif room23=="3":
                    print( "You see a gaurd, fight!!!")
        print("Defence works by gussing how much thier going to damage you. Then it gets the absolute value of thier actul damage minus your guess.")
        print("Offence works the same but your gussing your dmg.")
        comabtP1()
        pieces+=1
        print("You scavange the nocked out gaurd and you find your secound piece of paper. And it says'941'. The same guard also has a piece of paper that says 'big iron on his hip/ Big iron on his hip/ In this town there lived an outlaw by the name of Texas Red/ Many men had tried to take him and that many men were dead/ He was vicious and a killer though a youth of 24/ And the notches")
        


        


            
    