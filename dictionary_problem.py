# Creating a dictionary using an input

my_dic={}

while True:
    key=input("Enter keys ")
    value=input("Enter values ")
    my_dic[key]=value

    other=input("yes or no")
    if other !="yes":
        break

print(my_dic)
