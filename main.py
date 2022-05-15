#find length of given string
a= "Python is a case sensitive language"
print ("Length of the string is ",len(a))
#reverse the given string
b= a [::-1]
print ("The reversed string is :-",b)
#slice the string
c= a [10:26]
print (c)
#replace "a case sensitive" with "object oriented"
a2 = a.replace("a case sensitive", "object oriented")
print (a2)
#find index of "a"
ind = a.index("a")
print ("The index of substring a is ", ind)
# remove whitespaces from the string
a3 = a.replace(" ", "")
print ("The string with no white spaces is :-",a3)