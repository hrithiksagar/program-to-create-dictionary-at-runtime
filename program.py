n=int(input("enter size: "))
d={}
for i in range(n):
     keys=input("enter keys: ")
     values=input("enter values: ")
     d.update({keys:values})
print(d)  
