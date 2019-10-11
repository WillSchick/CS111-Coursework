#functions101
#
#Will Schick
#3/19/2018
#
#Writing and testing simple functions

#Main function------------------------------------------------------------------------------
def main():
    pentagon1 = pentagonArea(2,2)
    pentagon2 = pentagonArea(5,3)
    print("A pentagon with a side of 2 and apothem of 2 has area", pentagon1)
    print("A pentagon with a side of 5 and apothem of 3 has area", pentagon2)

    cube1 = cubeVolume(2)
    cube2 = cubeVolume(5)
    print("A cube with sidelength of 2 has volume:",cube1)
    print("A cube with sidelength of 5 has volume:",cube2)
    

## Calculate the volume of a cube ----------------------------------------------------------
# Parameter: sideLength - The length of a cube
# Return: The volume of a cube
def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume

## Calculate the area of a pentagon --------------------------------------------------------
# Parameters: 
#             sideLength - the length of the side
#             apothem - Distance between the center and the side
#
# Returns: 
#          Area of the pentagon
def pentagonArea(sideLength, apothem):
    area = (5/2) * sideLength * apothem
    return area



#Call main
main()
