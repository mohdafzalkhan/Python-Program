from sys import exit
def factorial():
    n=int(input("Enter the numebr="))
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial of ",n," numbers is ",f)
while True:
    ch=int(input("\n Menu\n1.Without using functions \n2.Using functions\n3.Exit\nEnter your choice="))
    if ch==1:
        n=int(input("Enter the numebr="))
        f=1
        for i in range(1,n+1):
            f=f*i
        print("Factorial of ",n," numbers is ",f)
    elif ch==2:
        factorial()
    elif ch==3:
        raise SystemExit()
    else:
        print("!!!Invalid choice!!!")
