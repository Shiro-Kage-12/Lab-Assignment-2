# question 5
print ("Enter the first side of the triangle")
s1= (int)(input())
print ("Enter the second side of the triangle")
s2= (int)(input())
print ("Enter the third side of the triangle")
s3= (int)(input())
while (s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
    print("Triangle is valid")
    break
else:
    print("Triangle not valid")