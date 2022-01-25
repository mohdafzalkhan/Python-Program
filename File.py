from sys import exit
while(True):
    ch=int(input("Menu\n1.write File\n2.Read file\n3.Read chunk file\n4.Read line file\n5.List file operation\n6.Add data to file\n7.Exit\nEnter your choice="))
    if ch==1:
        data=input("Enter the data to write a file=")
        fop=open('file.txt','wt')
        fop.write(data)
        fop.close()
    if ch==2:
        file=input("Enter the file name with extension .txt=")
        fop=open(file,'rt')
        data=fop.read()
        print(data)
        fop.close()
    if ch==3:
        data=""
        chunk=int(input("Enter the size of chunk="))
        fop=open('file.txt','rt')
        while(True):
            fragment=fop.read(chunk)
            if not fragment:
                break
            data+=fragment
        print(data)
        fop.close()
    if ch==4:
        data=''
        fop=open('file.txt','rt')
        while True:
            fr=fop.readline()
            if not fr:
                break
            data+=fr
        print(data)
        fop.close()
    if ch==5:
        data=''
        fop=open('file.txt','r')
        lines=fop.readlines()
        print("Read Line: %s"%(lines))
        fop.close()
    if ch==6:
        file=input("Enter the file name with extension .txt=")
        fop=open(file,'a+')
        data=input("Enter t write in the file=")
        fop.write(data)
        print(data)
        fop.close()
    if ch==7:
        raise SystemExit()
