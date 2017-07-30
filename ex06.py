x = "There are %d types of people." % 10
# define the x and use d type
binary = "binary"
# define the binary
do_not = "don't"
# define the do_not
y = "Those who know %s and those who %s." % (binary, do_not)
# define the y and use s type

print x
# print the x 
print y
# print the y 

print "I said: %r." % x 
# print the x with r type
print "I also said: '%s'." % y 
# print the y with the s type 

hilarious = False
# define the hilarious
world = True
joke_evaluation = "Isn't that joke so funny?! %r"
# define joke_evaluation

print joke_evaluation % world
# print with %

w = "This is the left side of..."
# define w 
e = "a string with a right side."
# define e 

print w + e
# print them