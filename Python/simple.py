for i in range(10):
    print(i)
for i in range(18,35):
    print(i)
a=[]
sum=0
skaitlis=int(input('ievadi skaitli'))
lielakais=a[-1]
while skaitlis!=0:
    sum+=skaitlis
    a.append(skaitlis)
    skaitlis=int(input('ievadi skaitli'))
print(sum)

for i in range(len(a)):
  print(a[i], end=" ")
print()
    
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i], end=" ")
print()
for i in range(len(a)-1,-1,-1):
    print(a[i], end=" ")
print()
print(lielakais)




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    