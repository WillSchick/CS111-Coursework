#petTester.py
#will
#5/4/2018
#
#A module to create and test instances of the class Pet.

# import the class
from classPet import Pet

def main():
    doggy = Pet("Pup", "Dog",1)
    kitty = Pet("Chip", "Cat", 1)
    
    print(doggy.getName())
    print(kitty.getSpecies())
    doggy.setName("Old-Yeller")
    print(doggy.getName())

    print()
    print(doggy)
    print(kitty)
    
main()