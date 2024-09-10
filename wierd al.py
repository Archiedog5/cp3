import random
p1hp=50
p1dp=10
p2dp=15
p2hp=75
herohp=50
herodp=5
print("Welcome to Wierd Al Yankovic The Game.")
doYouWantToPlay = input(" Do you want to play? If so press 1. (Anything else is the wrong answer):")
while doYouWantToPlay !="1":
    print("Wrong answer. If you don't chose right we will be stuck in this loop forever. So Let me ask again.")
    doYouWantToPlay = input(" Do you want to play? If so press 1. (Anything else is the wrong answer):")
name = input("Good. Now what's your name?:")
print("The setting starts at your friends house, name benard.")
print("Benard: Hey",name,+", did you know wierd al is having a concert tonight?")
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
     print("You literaly commited breaking and enterning to get your song back. But it's ok you can just ingnorat you little menis.")
elif room1 == "Y":
     print("Okay you collected your first piece of paper it says ' ")
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