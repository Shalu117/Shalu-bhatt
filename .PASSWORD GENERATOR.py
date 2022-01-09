import random
import string
print("THE PASSWORD GENERATOR")
len=int(input("\n Enter the length of your password: \n"))
l=string.ascii_letters
s="!#$&%?@*"
d=string.digits
a=l+d+s
print(" Here is a collection of passwords for you:")
for i in range(0,10):
    j="".join(random.sample(a,len))
    print("\n",j)