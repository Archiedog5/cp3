import random
p1hp=50
p1dp=10
p2dp=15
p2hp=50
wierdaldp=20
wierdalhp=50
herohp=50
herodp=5
pieces=0
ifkey="No"
ifkeywierdal="no"
chestcode=0
first_boss="no"
second_boss="no"
if2roombeen = "no"
if4roombeen="no"
if5roombeen="no"
if6roombeen="no"
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
def damageweirdal():
    global herohp
    global herodp
    global wierdaldp
    dmg=random.randint(1,20)
    dmgr=int(input("Guess a number 1-20 for thier dmg: "))
    given = abs(dmg-dmgr)
    herohp-=given
    print("Your stats are now Health:",herohp,"Damage:",herodp)
def fightweirdal():
    global wierdalhp
    global herodp
    global wierdaldp
    dmg=random.randint(1,wierdaldp)
    dmgr=int(input("Guess a number 1-10 for your dmg: "))
    given = abs(dmg-dmgr)
    p1hp-=given
    print("Enimies stats are now Health:",wierdalhp,"Damage:",wierdaldp)
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
                quit()
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
                quit()
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
                quit()
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
            quit()
        elif p2hp<=0:
             print("You deafected the guard.")
def combatweirdal():
    global herohp
    global herodp
    global wierdalhp
    global wierdaldp
    print ("There is no chance of escaping this and, well you better throw the first punch because that might be the only chance of deafting him.")
    while herohp>0 and wierdalhp>0:
        fightweirdal()
        damageweirdal()  
    if herohp<=0:
        print("Game over; Wierd al Yankovick deafeted you.")
        quit()
    elif wierdalhp<=0:
        print("You deafeated Wierd al Yankovick.")
        print("And he gave you the last piece of song to tape together. He looked it over parodied it and sang it for everybody encluding Bendard.")
        print("The end")
def room3():
    global pieces
    global first_boss
    if first_boss=="no":
        print( "You see a gaurd, fight!!!")
        print("Defence works by gussing how much thier going to damage you. Then it gets the absolute value of thier actul damage minus your guess.")
        print("Offence works the same but your gussing your dmg.")
        comabtP1()
        pieces+=1
        print("You scavange the nocked out gaurd and you find a code. And it says'941'. The same guard also has a piece of paper that says 'big iron on his hip/ Big iron on his hip/ In this town there lived an outlaw by the name of Texas Red/ Many men had tried to take him and that many men were dead/ He was vicious and a killer though a youth of 24/ And the notches'")
        first_boss = "yes"
    else: 
        print("You already defeated this guard.")
    room12=input("Now do you want to go to the left(1) room, right(2) room, or front room(3)?: ")
    if room12=="1":
        room1()
    elif room12 =="2":
        room2()
    elif room12=="3":
        front_room()
def room2():
    global pieces
    global if2roombeen
    if if2roombeen == "no":
        print("You found another piece of paper and it says 'hip/ Big iron on his hip/ It was early in the morning when he rode into the town/ He came riding from the south side slowly lookin' all around/ He's an outlaw loose and running, came the whisper from each lip/ And he's here to do some business with the' ")
        pieces+=1
        if2roombeen="yes"
    else:
        print("You have colected paper already.")
    room13=input("Now do you want to go to the center room(1), left room(2), or the front room(3)?: ")
    if room13 == "2":
        room1()
    elif room13== "1":
        room3()
    elif room13=="3":
        front_room()
def room1():
    global ifkey
    global chestcode
    if ifkey == "No":
        chestcode=input("You see a chest in the center of the room. And it asks you for a code to open. What's the code?: ")
        if chestcode!="941":
            leave="2"
            while chestcode!="941" and leave=="2" :
                print("wrong")
                leave=input("Do you want to leave or try again. 1 for leave and 2 to try agian?: ")
                if leave == "2":
                    chestcode=input("Whats the code?: ")
                else:
                    print("Ok find the password and try another time.")
        if chestcode=="941":
            print("You find two things a key too the right hallway and a potion that increases your dmg by 10 points")
            wannpickup=input("You also find a piec of paper. Do you wanna pick it up?(y/n):")
            if wannpickup=="y":
                print("The piece of paper says 'deadly with the big iron on his hip/Big iron on his hip/It was over in a moment and the folks had gathered round/There before them lay the body of the outlaw on the ground/Oh, he might have went on living but he made one fatal slip'")

            ifkey="yes"
    else:
        print("You already been here and colected everything.")
    room23=input("Now do you want to go to the center room(1), right room(2), or to the front room(3)?: ")
    if room23=="2":
        room2()
    elif room23=="1":
        room3()
    elif room23=="3":
        front_room()
def room4():
    global pieces
    global if4roombeen
    global ifkeywierdal
    if if4roombeen == "no":
        wannapickup=input("Up on ladder that leads to chandelier you see another piece of paper, do you wanna pick it up? (y/n): ")
        if wannapickup=="y":
            pieces+=1
            print("This piece of papper says 'on his pistol numbered one and 19 more/One and 19 more/Now the stranger started talking, made it plain to folks around/Was an Arizona ranger, wouldn't be too long in town/He came here to take an outlaw back alive or maybe dead/And he said it didn't'")
            if4roombeen="yes"
        elif wannapickup=="n":
            print("It will always be here for you to pick up.")
    elif if4roombeen=="yes":
        print("There is nothing to collect.")
    room2345=input("Now do you want to go to the second room(1), third room(2), fourth room(3), front room(4), or backstage(5)?: ")
    if room2345=="1":
        room5()
    elif room2345=="2":
        room6()
    elif room2345=="3":
        room7()
    elif room2345=="4":
        front_room()
    elif room2345=="5" and ifkeywierdal == "yes":
        room8()
    elif room2345=="5" and ifkeywierdal == "no":
        print("That room needs a key.")
        room4()
def room5():
    global pieces
    global if5roombeen
    global ifkeywierdal
    if if5roombeen == "no":
        wannapickup=input("You see another piece of paper in a mouth of a statue, do you wanna pick it up? (y/n): ")
        if wannapickup=="y":
            pieces+=1
            print("This piece of papper says 'matter he was after Texas Red/After Texas Red/Wasn't long before the story was relayed to Texas Red/But the outlaw didn't worry men that tried before were dead/20 men had tried to take him, 20 men had made a slip/21 would be the ranger with the'")
            if5roombeen="yes"
        elif wannapickup=="n":
            print("It will always be here for you to pick up.")
    elif if5roombeen=="yes":
        print("There is nothing to collect.")
    room1345=input("Now do you want to go to the first room(1), third room(2), fourth room(3), front room(4), or backstage(5)?: ")
    if room1345=="1":
        room4()
    elif room1345=="2":
        room6()
    elif room1345=="3":
        room7()
    elif room1345=="4":
        front_room()
    elif room1345=="5" and ifkeywierdal == "yes":
        room8()
    elif room1345=="5" and ifkeywierdal == "no":
        print("That room needs a key.")
        room5()
def room6():
    global pieces
    global if6roombeen
    global ifkeywierdal
    if if6roombeen == "no":
        wannapickup=input("You see a giant chess board and on top of a rook you see a pice of paper, do you wanna pick it up? (y/n): ")
        if wannapickup=="y":
            pieces+=1
            print("This piece of papper says 'big iron on his hip/Big iron on his hip/The morning passed so quickly, it was time for them to meet/It was 20 past 11 when they walked out in the street/Folks were watching from the windows, everybody held their breath/They knew this handsome ranger was'")
            if6roombeen="yes"
        elif wannapickup=="n":
            print("There is nothing to collect.")
    elif if6roombeen=="yes":
        print("You already have been here.")
    room1245=input("Now do you want to go to the first room(1), secound room(2), fourth room(3), front room(4), or backstage(5)?: ")
    if room1245=="1":
        room4()
    elif room1245=="2":
        room6()
    elif room1245=="3":
        room7()
    elif room1245=="4":
        front_room()
    elif room1245=="5" and ifkeywierdal == "yes":
        room8()
    elif room1245=="5" and ifkeywierdal == "no":
        print("That room needs a key.")
        room6()
def room7():
    global pieces
    global second_boss
    global ifkeywierdal
    if second_boss=="no":
        print( "You see a gaurd, fight!!!")
        combatP2()
        pieces+=1
        print("You scavange the nocked out gaurd and you find the key for the back stage. The same guard also has a piece of paper that says 'about to meet his death/About to meet his death/There was 40 feet between them when they stopped to make their play/And the swiftness of the ranger is still talked about today/Texas Red had not cleared leather 'fore a bullet fairly ripped/And the ranger's aim was'")
        second_boss = "yes"
        ifkeywierdal="yes"
    else: 
        print("You already defeated this guard.")
    room1235=input("Now do you want to go to the first room(1), secound room(2), third room(3), front room(4), or backstage(5)?: ")
    if room1235=="1":
        room4()
    elif room1235=="2":
        room6()
    elif room1235=="3":
        room7()
    elif room1235=="4":
        front_room()
    elif room1235=="5" and ifkeywierdal == "yes":
        room8()
    elif room1235=="5" and ifkeywierdal == "no":
        print("That room needs a key.")
        room7()
def room8():
    print("You unlocked the door to back stage and see Wierd al Yankovik sitting in a chair.")
    print("And he said that he has been expecting you. And said if you want him to parody your song you have to beat him in a round of combat.")
    combatweirdal()
    print("You did good boy ")
def front_room():
    global ifkey 
    global ifkeywierdal
    hallwayLorR = input("Now you are here in the front room do you want to go to left or right?(1 for left, 2 for right): ")
    if hallwayLorR ==  "2" and ifkey == "yes":
        two_room12345=input("You unlocked the door and see 5 rooms in a half circle. The first 4 rooms are unlocked but the last one isn't and the last one says back stage employs only. Now do you want to go to the first room(1), the second room(2), the tird room(3), the fourth room(4), or the locked room(5)?: ")
        if two_room12345=="5" and ifkeywierdal == "yes":
            room8()
        elif two_room12345=="4":
            room7()
        elif two_room12345=="3":
            room6()
        elif two_room12345=="2":
            room5()
        elif two_room12345=="1":
            room4()
    elif hallwayLorR == "2" and ifkey == "No":
        print("This door is locked, try the other one.")
        front_room()
    elif hallwayLorR == "1":
        room123 = input("You see three rooms, left(1) right(2) and center(3) wich one do you want to go to?: ")
        if room123 == "3":
            room3()
        elif room123 == "2":
            room2()
        elif room123 == "1":
            room1()

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
room1dy = input("You find a the first piece of paper with the lyrics on it. Do you wan't to pick it up? y or n?: ")
if room1dy == "n":
    print("You literaly commited breaking and enterning to get your song back. But it's ok you can just ingnor it. You little menis. You know what, nvm. YOU TOOK THE PIECE OF PAPER.")
    pieces+=1    
elif room1dy == "y":
    print("You collected your first piece of paper it says 'To the town of Agua Fria rode a stranger one fine day/ Hardly spoke to folks around him, didn't have too much to say/ No one dared to ask his business, no one dared to make a slip/ For the stranger there among them had a big iron on his' ")
    print("Good job. Only 8 more pieces to go.") 
    pieces+=1
front_room()