#We start classes with keyword class and we name them using PascalCase

class Animal:
    #We start with the constructor (defines all the attributes of the object being created) 
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity 

        #Makes a more readable string when printed
    def fight(self, other):
        if len(self.name)>len(other.name):
            other.losses +=1
            return self.name
        elif len(self.name)<len(other.name):
            self.losses +=1
            return other.name
        else:
            other.losses +=1
            self.losses +=1
            return "tie"
            
    #Makes a more readable string when printed
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nGender: {self.gender}\nRarirty: {self.rarity}"
# geanraly store objects in vairables (indivudually or in a list) so we find them later    
cat = Animal("Tom", "cat", 21, "Male", "Common")
frog= Animal("Jarod", "Poision Dark Frog", 500, "Female", "Rare")
#To call a method you put the name of the boject.name of the the method (needs arguments)
cat.losses = 0
frog.losses = 0
print(cat.fight(frog))

cat.name="Thomas"
print(cat.losses)

print(cat.fight(frog))
print(cat.losses)
print(frog.losses)
cat = None
print(cat)