# testJediXwingSimulator.py
# Created by: R. Givens
# Description: Tests the object and methods for Jedi and Xwing classes.  Also
# tests the flightBattle function in the simulator module.  
# Does not require any input.

from xwing import Xwing
from jedi import Jedi
from simulator import flightBattle

def main():
    # comment out until you are ready to test
    testJedi()
    testXwing()
    testSimulator()
    
    
def testJedi():
    print("************************")
    print("***** Testing Jedi *****")
    print("************************")
    print()
    
    # test constructor
    print("***** Constructor *****")
    jedi1 = Jedi("Yoda", False)
    jedi2 = Jedi("Luke Skywalker", True)
    jedi3 = Jedi("Mace Windu") # default
    jedi4 = Jedi("Obi-Wan Kenobi", True)
    print("Jedis created.  Default accepted.")
    print()
    
    # test getName
    print("***** getName *****")
    name1 = jedi1.getName()
    name2 = jedi2.getName()
    name3 = jedi3.getName()
    name4 = jedi4.getName()
    print('%-20s  %-20s' % ("Expected", "Actual"))
    print('%-20s  %-20s' % ("-"*20, "-"*20))
    print('%-20s  %-20s' % ('"Yoda"', '"'+name1+'"'))
    print('%-20s  %-20s' % ('"Luke Skywalker"', '"'+name2+'"'))
    print('%-20s  %-20s' % ('"Mace Windu"', '"'+name3+'"'))
    print('%-20s  %-20s' % ('"Obi-Wan Kenobi"', '"'+name4+'"'))
    print()
    
    # test hasLightsaber
    print("***** hasLightsaber *****")
    has1 = jedi1.hasLightsaber()
    has2 = jedi2.hasLightsaber()
    has3 = jedi3.hasLightsaber()
    has4 = jedi4.hasLightsaber()
    print('%-30s  %-30s' % ("Expected", "Actual"))
    print('%-30s  %-30s' % ("-"*30, "-"*30))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(has1), str(type(has1))))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(has2), str(type(has2))))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(has3), str(type(has3))))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(has4), str(type(has4))))
    print()
    
    # test ==    
    print("***** equals *****")
    equal1 = jedi1 == jedi2
    equal2 = jedi1 == jedi3
    equal3 = jedi1 == Jedi("Yoda", True)
    equal4 = jedi1 == Jedi("Yoda", False)
    equal5 = jedi2 == Jedi("Luke Skywalker", True)
    print('%-30s  %-30s' % ("Expected", "Actual"))
    print('%-30s  %-30s' % ("-"*30, "-"*30))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(equal1), str(type(equal1))))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(equal2), str(type(equal2))))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(equal3), str(type(equal3))))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(equal4), str(type(equal4))))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(equal5), str(type(equal5))))
    print()
    
    # test !=
    print("***** not equals *****")
    equal1 = jedi1 != jedi2
    equal2 = jedi1 != jedi3
    equal3 = jedi1 != Jedi("Yoda", True)
    equal4 = jedi1 != Jedi("Yoda", False)
    equal5 = jedi2 != Jedi("Luke Skywalker", True)
    print('%-30s  %-30s' % ("Expected", "Actual"))
    print('%-30s  %-30s' % ("-"*30, "-"*30))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(equal1), str(type(equal1))))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(equal2), str(type(equal2))))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(equal3), str(type(equal3))))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(equal4), str(type(equal4))))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(equal5), str(type(equal5))))
    print()
    
    # test str()/print()
    print("***** string representation *****")
    print("expected:  ", "Jedi Yoda.")
    print("actual:    ", jedi1)
    print("expected:  ", "Jedi Luke Skywalker with a lightsaber.")
    print("actual:    ", jedi2)
    print("expected:  ", "Jedi Mace Windu.")
    print("actual:    ", jedi3)
    print("expected:  ", "Jedi Obi-Wan Kenobi with a lightsaber.")
    print("actual:    ", jedi4)
    print()
    
    return

def testXwing():
    print("*************************")
    print("***** Testing Xwing *****")
    print("*************************")
    print()
    # test constructor
    print("***** Constructor *****")
    jedi1 = Jedi("Yoda", False)
    jedi2 = Jedi("Luke Skywalker", True)
    jedi3 = Jedi("Mace Windu") # default
    jedi4 = Jedi("Obi-Wan Kenobi", True)
    xwing1 = Xwing(jedi1)
    xwing2 = Xwing(jedi2)
    xwing3 = Xwing(jedi3)
    xwing4 = Xwing(jedi4)
    print("Xwings created.")
    print()
    
    # test getPilot
    print("***** getPilot *****")
    pilot1 = xwing1.getPilot()
    pilot2 = xwing2.getPilot()
    pilot3 = xwing3.getPilot()
    pilot4 = xwing4.getPilot()
    print(pilot1)
    print('%-20s  %-20s' % ("Expected", "Actual"))
    print('%-20s  %-20s' % ("-"*20, "-"*20))
    print('%-20s  %-20s' % ('"Yoda"', '"'+pilot1+'"'))
    print('%-20s  %-20s' % ('"Luke Skywalker"', '"'+pilot2+'"'))
    print('%-20s  %-20s' % ('"Mace Windu"', '"'+pilot3+'"'))
    print('%-20s  %-20s' % ('"Obi-Wan Kenobi"', '"'+pilot4+'"'))
    print()
    
    # test isArmed
    print("***** isArmed *****")
    armed1 = xwing1.isArmed()
    armed2 = xwing2.isArmed()
    armed3 = xwing3.isArmed()
    armed4 = xwing4.isArmed()
    print('%-30s  %-30s' % ("Expected", "Actual"))
    print('%-30s  %-30s' % ("-"*30, "-"*30))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(armed1), str(type(armed1))))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(armed2), str(type(armed2))))
    print('%-5s     %-20s  %-5s     %-20s' % ("False", "<class 'bool'>", str(armed3), str(type(armed3))))
    print('%-5s     %-20s  %-5s     %-20s' % ("True", "<class 'bool'>", str(armed4), str(type(armed4))))
    print()
    
    # test getSpeed
    print("***** getSpeed *****")
    speed1 = xwing1.getSpeed()
    speed2 = xwing2.getSpeed()
    speed3 = xwing3.getSpeed()
    speed4 = xwing4.getSpeed()
    print('%-10s  %-10s' % ("Expected", "Actual"))
    print('%-10s  %-10s' % ("-"*10, "-"*10))
    print('%-10s  %-10d' % ("200 - 500", speed1))
    print('%-10s  %-10d' % ("200 - 500", speed2))
    print('%-10s  %-10d' % ("200 - 500", speed3))
    print('%-10s  %-10d' % ("200 - 500", speed4))
    print()
    
    # test updateSpeed
    print("***** updateSpeed *****")
    xwing1.updateSpeed()
    xwing2.updateSpeed()
    xwing3.updateSpeed()
    xwing4.updateSpeed()    
    
    update1 = xwing1.getSpeed()
    update2 = xwing2.getSpeed()
    update3 = xwing3.getSpeed()
    update4 = xwing4.getSpeed()  
    print('%-10s < %-10s' % ("Initial", "Update (Random)"))
    print('%-10s   %-10s' % ("-"*10, "-"*10))
    print('%-10s < %-10s' % (speed1, update1))
    print('%-10s < %-10s' % (speed2, update2))
    print('%-10s < %-10s' % (speed3, update3))
    print('%-10s < %-10s' % (speed4, update4))
    print()  
    
    # force speed of 500
    for i in range(300):
        xwing1.updateSpeed()
    update1 = xwing1.getSpeed()
    print('%-10s  %-10s' % ("Expected", "Actual"))
    print('%-10s  %-10s' % ("-"*10, "-"*10))
    print('%-10d  %-10d' % (500, update1))
    print()
    
    # test str()/print()
    print("***** string representation *****")
    print("expected:  ", "X-wing with Jedi Yoda.")
    print("actual:    ", xwing1)
    print("expected:  ", "X-wing with Jedi Luke Skywalker with a lightsaber.")
    print("actual:    ", xwing2)
    print("expected:  ", "X-wing with Jedi Mace Windu.")
    print("actual:    ", xwing3)
    print("expected:  ", "X-wing with Jedi Obi-Wan Kenobi with a lightsaber.")
    print("actual:    ", xwing4)
    print()    
    
    return

def testSimulator():
    print("*****************************")
    print("***** Testing Simulator *****")
    print("*****************************")
    print()
    # test flightBattle
    jedi1 = Jedi("Yoda", False)
    jedi2 = Jedi("Luke Skywalker", True)
    jedi3 = Jedi("Mace Windu") # default
    jedi4 = Jedi("Obi-Wan Kenobi", True)
    xwing1 = Xwing(jedi1)
    xwing2 = Xwing(jedi2)
    xwing3 = Xwing(jedi3)
    xwing4 = Xwing(jedi4)
    
    
    print("-"*50)
    # Random winner, Random minutes
    print(">>>>> Expected: Winner - Random, Minutes - Random\n")
    winner = flightBattle(xwing1, xwing3, 1000)
    print("\n>>>>> End Simulation")
    print("Returned winner:", winner)
    print()
    
    print("-"*50)
    # Random winner, Random minutes
    print(">>>>> Expected: Winner - Random, Minutes - Random\n")
    winner = flightBattle(xwing2, xwing4, 1000) 
    print("\n>>>>> End Simulation")
    print("Returned winner:", winner)
    print()
    
    # force speed of 500
    for i in range(300):
        xwing1.updateSpeed() 
        xwing2.updateSpeed()  
        xwing3.updateSpeed()  
        xwing4.updateSpeed()  
    
    print("-"*50)    
    # Random winner, 2.5 minutes
    print(">>>>> Expected: Winner - Random, Minutes - 2.5\n")
    winner = flightBattle(xwing1, xwing3, 2500)
    print("\n>>>>> End Simulation")
    print("Returned winner:", winner)
    print()
    
    print("-"*50)
    # Random winner, 3.0 minutes
    print(">>>>> Expected: Winner - Random, Minutes - 3.0\n")
    winner = flightBattle(xwing2, xwing4, 3000)
    print("\n>>>>> End Simulation") 
    print("Returned winner:", winner)
    print()    
    
    print("-"*50)
    # Luke wins, 2.8 minutes
    print(">>>>> Expected: Winner - Luke Skywalker, Minutes - 2.8\n")
    winner = flightBattle(xwing2, xwing1, 2750)
    print("\n>>>>> End Simulation") 
    print("Returned winner:", winner)
    print()   
    
    print("-"*50)
    # Obi-Wan wins, 1.6 minutes
    print(">>>>> Expected: Winner - Obi-Wan Kenobi, Minutes - 1.6\n")
    winner = flightBattle(xwing3, xwing4, 1620) 
    print("\n>>>>> End Simulation")
    print("Returned winner:", winner)
    print()
    
    
    return


main()