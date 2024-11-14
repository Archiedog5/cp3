class Monster:
    def __init__(self, name, place_of_orgin, method_of_attack):
        self.name=name
        self.place_of_orgin=place_of_orgin
        self.method_of_attack=method_of_attack

class Vampire(Monster):
    def __init__(self, name, place_of_orgin, method_of_attack, flight_speed, max_distance_of_flight):
        super.__init__(name, place_of_orgin, method_of_attack,)
        self.flight_speed=flight_speed
        self.max_distance_of_flight=max_distance_of_flight

class Zombie(Monster):
    def __init__(self, name, place_of_orgin, method_of_attack, bite_force, type_of_zombie, travle_speed):
        super().__init__(name, place_of_orgin, method_of_attack)
        self.bite_force=bite_force
        self.type_of_zombie=type_of_zombie
        self.travle_speed=travle_speed

class Ghost(Monster):
    def __init__(self, name, place_of_orgin, method_of_attack, danger_level):
        super().__init__(name, place_of_orgin, method_of_attack)
        self.danger_level=danger_level

class Frankienstine(Monster):
    pass
