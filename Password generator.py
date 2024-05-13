import random
import string
case=list(string.ascii_lowercase+string.ascii_uppercase)
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=['@','#','$','&','~']
print("Welcome to passsword generator")
l=int(input("How many letters would you like in your password?:"))
print(l)
sy=int(input("How many symbol would you like?:"))
print(sy)
num=int(input("How many numbers would you like?:"))
print(num)
password_list=""
for i in range(1,l+1):#1,2,3,4
    a=random.choice(case)
    password_list+=a
for i in range(1,sy+1):
    b=random.choice(symbols)
    password_list+=b
for i in range(1,num+1):
    c=random.choice(numbers)
    password_list+=str(c)

print(password_list)





