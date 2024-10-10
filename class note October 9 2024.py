class pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name=name
        self.hp=hp
        self.typ=typ
        self.lvl=lvl
    
    def combat(self, other):
        if self.lvl > other.lvl:
            return f"{self.name} won!"
        elif self.lvl < other.lvl:
            return f"{other.name} won! You lost!!!"
        else:
            return f"Both of them passed out due to exhaustion you both lost."

    def __str__(self):
        return f"""
            name: {self.name}
            type: {self.typ}
            level: {self.lvl}
            HP: {self.hp}"""
    @classmethod
    def lvl_up(self):
        self.lvl +=1
        self.hp= int(self.hp*1.5)
    @classmethod
    def pikachu(self):
        return pokemon(input("Give me a name: "), 50, "eletric", 1)
    #static methods do no require self or cls
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5
    
eevee = pokemon("JayRod", 37, "normal", 2)
charizard = pokemon("Bob", 1, "fire", 36)
pika = pokemon.pikachu()
pika.hp = pokemon.hp_update(pika)
print(eevee)
print(eevee.combat(charizard))
print(eevee)
eevee.lvl= pokemon.lvl_up()
print(eevee)
print(pika)