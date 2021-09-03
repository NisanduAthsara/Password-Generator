x = str(input("Enter your first name : "))
y = int(input("Enter your age : "))
a = int(input("Enter your favourite number : "))
pwd = ["@","%","&","%","!","$","&*"]
pwd1 = ["bhk","kjh","typ","oll","qwy","kpo","qql"]
pwd2 = ["CoOL","DskG","HjoF","KoLL","LoL","UiP","vIP"]
pwd3 = [21, 46, 59, 33, 19, 81, 64]
x.lower()

length = len(pwd)
z = 1

print("Your password is : "+pwd2[0]+x+pwd[0]+str(y)+pwd1[0]+str(pwd3[0])+str(a)+"\n")

i = str(input("Press 'y' for genarate another password. Press 'n' for exit. : "))
i.lower()

if i=='n':
    exit()
    
while i=="y" and z<length:
    print("Your password is : "+pwd2[z]+x+pwd[z]+str(y)+pwd1[z]+str(pwd3[0])+str(a)+"\n")
    z+=1
    i = str(input("Press 'y' for genarate another password. Press 'n' for exit. : "))
    i.lower()
    if i=='n':
        exit()