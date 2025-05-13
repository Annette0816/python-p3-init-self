#!/usr/bin/env python3

class Dog:
    def __init__ (self, name, breed="Mutt",favorite_toy="Any"):
        self.name = name
        self.favorite_toy= favorite_toy
        self.breed = breed
        

    def bark(self):
        print("Woof!")

    
fido = Dog("Fido","Dalmatian")
fido.favorite_toy


fido.owner = "Sophie"



snoopy = Dog("Snoopy","Tennis Ball")
snoopy.favorite_toy
   