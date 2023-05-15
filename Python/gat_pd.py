
#1 uzd
# x=int(input("ievadi skaitli"))
# y=int(input("ievadi skaitli"))
# if y>x:
#     print(y-x)
# elif y==x:
#     print(x-y)
# else:
#     print(x-y)

# 2 uzd
# x=int(input("ievadi skaitli"))
# if x%2==0:
#     print("skaitlis ir pāra")
# else:
#     print("nepāra")

# 3 uzd
# x=int(input("ievadi skaitli"))
# y=int(input("ievadi skaitli"))
# if x>0 and y>0:
#     print("1")
# elif x<0 and y>0:
#     print("2")
# elif x<0 and y<0:
#     print("3")
# elif x>0 and y<0:
#     print("4")
# else:
#     print("skaitlis ir uz ass")

# 4 uzd
# x=int(input("ievadi triscipara skaitli"))
# sum=0
# while x>0:
#     skaitlis=x%10
#     sum+=skaitlis
#     x//=10
# print("summa:", sum)

# 5 uzd
# x=int(input("ievadi skaitli"))
# y=int(input("ievadi skaitli"))
# z=int(input("ievadi skaitli"))
# if x>y and y>z:
#     print(z,y,x)
# elif x<y and y<z:
#     print(x,y,z)
# elif x<y and x>z:
#     print(z,x,y)
# elif x>y and x<z:
#     print(y,x,z)
# elif x>y and z>y and x>z:
#     print(y,z,x)
# elif x<y and x<z and y>z:
#     print(x,z,y)
# elif x==y and x==z and y==z:
#     print("skaitli ir vienadi")
# else:
#     print("es hz")

# 6 uzd
# diena=int(input("ievadi dienu"))
# menesis=int(input("ievadi menesi"))
# def check_menesis(diena,menesis):
#     dienas_menesi=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if menesis<1 or menesis>12:
#         return False
#     if diena<1 or diena>dienas_menesi[menesis-1]:
#         return False
# if check_menesis(diena,menesis):
#     print("menesis eksiste")
# else:
#     print("menesis neeksiste")

# 7 uzd 
# s1=int(input("ievadi skaitli"))
# s2=int(input("ievadi skaitli"))
# s3=int(input("ievadi skaitli"))
# sum=0
# if s1%2==0:
#     sum+=s1
# if s2%2==0:
#     sum+=s2
# if s3%2==0:
#     sum+=s3
# print(sum)

# 8 uzd
# a=int(input("ievadi skaitli"))
# b=int(input("ievadi skaitli"))
# if a<=0 or b<=0:
#     print("daunis")
# print(a*2+b*2)
# print(a*b)

# 9 uzd
# a=input("ievadi divciparu skaitli")
# a_reversed=a[::-1]
# print(int(a)+int(a_reversed))

# 10 uzd
# for i in range(10):
#     if i<10:
#         print(i)

# 11 uzd
# a=int(input("ievadi skaitli"))
# b=int(input("ievadi skaitli"))
# c=int(input("ievadi skaitli"))
# d=int(input("ievadi skaitli"))
# e=int(input("ievadi skaitli"))
# print(a+b+c+d+e)
# print((a+b+c+d+e)/5)

# 12 uzd


# 13 uzd
# for i in range(100):
#     if i%3==0 and i%8==0:
#         print(i)

# 14 uzd


# 15 uzd


# 16 uzd
# x=[]
# n=int(input("ievadi skaitli"))
# x.append(n)
# while n!=0:
#     n=int(input("ievadi skaitli"))
#     x.append(n)
#     if n==0:
#         print(sum(x))

# 17 uzd
# n=int(input("ievadi skaitli"))
# x=1
# while x<n:
#     x+=1
#     print(x-1)

# 18 uzd
# n=int(input("ievadi skaitli"))
# for i in range(n):
#     if i<n:
#         print(i**2)
#         i+=1

# 19 uzd
# n=int(input("ievadi skaitli"))
# for i in range(n):
#     if i**2<n:
#         print(i**2)
#         i+=1

# 20 uzd
# n=int(input("ievadi skaitli"))
# for i in range(n+1,2*n):
#     print(i)


# 21 uzd
# x=0
# for i in range(101):
#     x+=i
# print(x)

# 22 uzd
# for i in range(25,0,-1):
#     if i%2!=0:
#         print(i)

# 23 uzd
# x=[]
# j=0
# while j!=5:
#     a=int(input("ievadi skaitli"))
#     x.append(a)
#     j+=1
# print(sum(x))

# 24 uzd
# a=int(input("ievadi skaitli"))
# x=[]
# x.append(a)
# while a!=0:
#     a=int(input("ievadi skaitli"))
#     x.append(a)
# print(sum(x))

# 25 uzd
# x=int(input("ievadi skaitli"))
# sum=0
# while x>0:
#     skaitlis=x%10
#     sum+=skaitlis
#     x//=10
# print("summa:", sum)

# 26 uzd
# x=int(input("ievadi skaitli"))
# a=0
# for i in range(1,x+1):
#     if x%i==0:
#         a+=1
# if a==2:
#     print(a," (pirmskaitlis)")
# else:
#     print(a)

# 27 uzd
# x=int(input("ievadi skaitli"))
# while x!=0:
#     m=int(input("ievadi skaitli"))
#     if m>x:
#         print("lielaks")
#     else:
#         print("nav lielaks")
#     x=m

# 28 uzd
# m=[1,5,3,7,2,4,2,7,9,2,5,6]
# dic={}
# for num in m:
#     dic[num]=m.count(num)
# print(dic)

# 44 uzd
# a=[]
# x=[5,5,5,5,5,5,5,5,5,6,6,6,6,6,1]
# for i in range(len(x)):
#     if a.count(x[i])<1:
#         a.append(x[i])
# print(a)
# print(list(set(x)))

# 45 uzd
text = "The Serbian tennis star was detained in January over his refusal to be vaccinated against Covid. He was deported from the country 10 days later, despite mounting a successful legal challenge. At times dubbed Fortress Australia, the country had some of the strictest pandemic restrictions in the world. When Djokovic arrived in Australia in January, Covid cases were skyrocketing and government rules required anyone entering the country be vaccinated, unless they had a valid medication exemption."
text=text.lower()
text=text.replace(".","").replace("!","").replace(",","").replace(" ","")
d={}
import string
for char in string.ascii_lowercase:
    d[char]=round(text.count(char)/len(text)*100,2)
for key in d:
    print(key,d[key])
    
# 68 uzd
# arr = [[0 for _ in range(8)] for _ in range(8)]
# def printArray(m):
#     for row in m:
#         for elem in row:
#             print(elem, end=" ")
#         print()
# burts="abcdefgh"
# poz=input("pozicija: ") #e4 -> [0] = e, [1]=4
# x=burts.index(poz[0])
# y=8-int(poz[1])
# arr[x][y]=1
# printArray(arr)

# #69 uzd
# # tornis
# for i in range(8):
#     for j in range(8):
#         if i==x or j==x:
#             arr[i][j]+=1
# # laidnis
# # zirgs
# for i in range(8):
#     for j in range(8):
#         if (abs(x-i)==1 and abs(y-j)==2) or (abs(x-i)==2 and abs(y-j)==2):
#             arr[i][j]+=1

