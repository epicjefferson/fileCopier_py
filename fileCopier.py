#!/usr/bin/python

#open text files, one is the original, the other
#will save the translated version
original = open("something.txt", "r")
copy = open("copy_" + original.name, "w")



#copy the contents of the original to a
#temporary variable, then write it in the new file
temp = original.read()
copy.write(temp)

#close the copy, then re-open as readable
#gotta find a better way to do this
copy.close()
copy = open("copy_" + original.name, "r")

#for verification, we'll print the contents
#of the original and the copy
checkCopy = copy.read()
print "Original file name: ", original.name, "\n", temp
print "This is the copy:", copy.name, "\n", checkCopy

#close it up
copy.close()
original.close()
