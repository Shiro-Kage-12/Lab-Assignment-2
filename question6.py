# question 5
print ("Enter the first numnber")
a= (int)(input())
print ("Enter the second number")
b= (int)(input())
num = a ^ b
Count_flipped_bit = 0
while (num != 0):
    num = num & (num - 1)
    Count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is:", Count_flipped_bit)