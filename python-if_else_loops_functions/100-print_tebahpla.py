 #!/usr/bin/python3

a=1
for x in list(range(ord('z'), ord('a') - 1, -1)):
    if(a==1):
        print(chr(x),end="")
        a=2
    elif(a==2):
        print(chr(ord(chr(x))-32),end="")
        a=1
