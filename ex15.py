from sys import argv # get filename

script, filename = argv # last lesson

txt = open(filename) # open the file

print "Here's your file %r:" % filename # print name
print txt.read() # print content

txt.close()

print "Type the filename again:" # interact
file_again = raw_input(">") # input name again

txt_again = open(file_again) # open the file again

print txt_again.read() # print the content again