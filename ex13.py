from sys import argv

script, tea, drink, rice = argv

tea = raw_input("How much?")
drink = int(raw_input("How good?"))
rice = raw_input("How many?")

print "The script is called:", script
print "Your first variable is:", tea
print "Your second variable is:", drink
print "Your third variable is:", rice