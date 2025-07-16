'''str="i am a coder."
print(str.endswith("er."))
print(str.capitalize())
print(str.replace("coder","programmer"))
print(str.find("coder"))#return first occurence of string 
print(str.count("o"))
'''
'''name=input("Enter first name:")
print(len(name))
print(name.count("$"))'''

'''num=int(input())
print("even" if num%2==0 else "odd")
'''

'''list_input=list(map(int,input("Enter num list:").split()))
print(max(list_input))'''

'''#ARMSTRONG NUMBER
n=int(input())
order=len(str(n))
sum=0
for i in str(n):
    sum+=int(i)**order
if n==sum:
    print("Armstrong number")
else:
    print("Not armstrong number")
    
#ARMSTRONG NUMBER IN AN INTERVAL
l=int(input())
u=int(input())
for num in range(l,u+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)'''

#PANGRAM STRING OR NOT
'''alphabet="abcdefghijklmnopqrstuvwxyz"
flag=True
inp_str=input("Enter a string:")
inp_str=inp_str.lower()
for i in alphabet:
    if i not in inp_str:
        flag=False
        break
if flag:
    print("pangram")
else:
    print("Not pangram")
    

#HARSHAD NUMBER
num=int(input())
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit
    temp//=10
if num%sum==0:
    print("harshad number")
else:
    print("Not harshad number")

#SUM OF NATURAL NUMBERS
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#powers of 2
n=int(input())
for i in range(0,n):
    r=2**i
    print(r)

#NUMBERS DIVISIBLE BY 13 ONLY
list1=list(map(int,input().split()))
result=list(filter(lambda i:(i%13==0),list1))
print(result)

#Fibonacci sequence 
n=int(input())
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
        
#ASCII VALUE
n=input()
print(ord(n))

#HCF OF TWO NUMBERS
x=int(input())
y=int(input())
if x<y:
    smaller=x
else:
    smaller=y
for i in range(1,smaller+1):
    if x%i==0 and y%i==0:
        hcf=i
print(hcf)

#LCM OF 2 NUMBERS  
x=int(input())
y=int(input())
if x>y:
    greater=x
else:
    greater=y
for i in range(greater,x*y+1):
    if i%x==0 and i%y==0:
        lcm=i
        break
print(lcm)        
        
#program to append all zeros at the end
l=[int(i) for i in input().split()]
nonzero=[x for x in l if x!=0]
zero_count=l.count(0)
res=nonzero+zero_count*[0]
print(res)

#program to print the missing number
n=int(input("Enter the input number:"))
l1=list(map(int,input("Enter list items:").split()))
l=[]
for i in range(1,n+1):
    if i not in l1:
        l.append(i)
print(l)'''

#NUMBER EXTRACTION
import re
sentence=input()
f=re.findall(r'\d+',sentence)
f=[int(i) for i in f]
print(f)


#STRING METHODS
#str.upper() - converts all characters to uppercase
#str.lower() - converts all characters to lowercase











        
        
        
