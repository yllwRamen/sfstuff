#needed shit
import os
import time

#useless ass splashscreen
print(" ________       _______       ________     ")
print("|\   ___  \    |\  ___ \     |\   ___ \    ")
print("\ \  \\ \   \   \ \   __/|     \ \  \_|\ \   ")
print(" \ \  \\ \   \   \ \  \_|/__    \ \  \ \\  \  ")
print("  \ \  \\ \   \   \ \  \_|\ \    \ \  \_\\  \ ")
print("   \ \__\\ \__ \   \ \_______\    \ \_______\ ")
print("    \|__| \|__|    \|_______|    \|_______|")
print("")
print("Made with <3 by 6ilent")
time.sleep(2)

#getting coords of the main overrworld portal
os.system('cls||clear')

print("+=================================================+")
print("| COORDINATES OF THE MAIN PORTAL IN THE OVERWORLD |")
print("+=================================================+")
print("")

main_over_X = int(input("X Coordinate: "))
main_over_Z = int(input("Z Coordinate: "))

#getting coords of the new overworld portal
os.system('cls||clear')

print("+================================================+")
print("| COORDINATES OF THE NEW PORTAL IN THE OVERWORLD |")
print("+================================================+")
print("")

new_over_X = int(input("X Coordinate: "))
new_over_Z = int(input("Z Coordinate: "))

#getting coords of the main portal in the nether
os.system('cls||clear')

print("+=================================================+")
print("| COORDINATES OF THE PORTAL THAT IS IN THE NETHER |")
print("+=================================================+")
print("")

main_nether_X = int(input("X Coordinate: "))
main_nether_Z = int(input("Z Coordinate: "))

#calculating the difference between the two x's and z's
tempX = new_over_X - main_over_X
tempZ = new_over_Z - main_over_Z

#finding the amount of travel blocks in nether distance
diffX = tempX / 8
diffZ = tempZ / 8

#we got'em
os.system('cls||clear')

print("+=====================================+")
print("| FROM YOUR MAIN PORTAL IN THE NETHER |")
print("+=====================================+")
print("")

print("Travel " + str(diffX) + " blocks in the X Coordinate!")
print("Travel " + str(diffZ) + " blocks in the Z Coordinate!")
print("")
print("XZ: " + str(main_nether_X + diffX) + " / " + str(main_nether_Z + diffZ))
print("")
input("Press any key to exit.")
