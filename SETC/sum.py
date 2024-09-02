num=int(input("enter the number"))

sum=0
digit=0

while(num!=0):
    digit=num%10
    num=num//10

    if(digit%2!=0):
        sum=digit+sum
print(sum)        