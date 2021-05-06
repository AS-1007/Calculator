def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(
    x,y):
    return x*y
def div(x,y):
    return x/y

print("1) Add")
print("2) sub")
print("3) mul")
print("4) div")


one=float(input("enter the number:"))
one1=float(input("enter the sec number:"))
select=int(input("enter the operaation you want to perfom"))
if select==1:
    print(one,"+",one1,"=",add(one,one1))
elif select==2:
    print(one,"-",one1,"=",sub(one,one1))
elif select==3:
    print(one,"*",one1,"=",mul(one,one1))
elif select==4:
    print(one,"/",one1,"=",div(one,one1))
else:
    print("invalid input")