#check even odd and store even odd numbers in the list

num=int(input())
if num%2==0:
    print("EVEN")
else:
    print("ODD")

odd=[]
even=[]

for i in range (1, 1001):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    
print(odd)
print(even)
