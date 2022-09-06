d=int(input("Enter Date: ")) 
m=int(input("Enter Month: "))
y=int(input("Enter Year: "))
flag=False
if d==29:
    if(y%4==0 and y%100!=0 or y%400==0):
        flag=True
    else:
        print("Wrong Input")
elif d>0 and d<=31:
    if m>0 and m<=12:
        flag=True
else:
    print("Wrong Input")
def Previous_Date():
    if flag:
        print(f"Your Date is {d}:{m}:{y}")
    if flag and d==1 and m==1:
        return(f"31:12:{y-1}")
    elif flag and d==1:
        if m==3:
            if (y%4==0 and y%100!=0 or y%400==0):
                return(f"29:{m-1}:{y}")
            else:
                return(f"28:{m-1}:{y}")
        elif(m==8 or m==9 or m==11 or m==2 or m==4 or m==6):
            return(f"31:{m-1}:{y}")
        elif(m==5 or m==7 or m==10 or m==12):
            return(f"30:{m-1}:{y}")
    elif flag and d>0:
        return(f"{d-1}:{m}:{y}")
a=Previous_Date()
print(f"Previous Date is {a}")

def Next_Date():
    if flag and d==31 and m==12:
        return(f"1:1:{y+1}")
    elif flag and d==28 and m==2:
        return(f"1:{m+1}:{y}") 
    elif flag and d==29 and m==2:
        if (y%4==0 and y%100!=0 or y%400==0):
            return(f"1:{m+1}:{y}")
    elif flag and d==30 and (m==2 or m==4 or m==6 or m==9 or m==11):
        return(f"1:{m+1}:{y}")
    elif flag and d==31 and(m==1 or m==3 or m==5 or m==7 or m==8 or m==10):
        return(f"1:{m+1}:{y}")
    elif flag and d>0:
        return(f"{d+1}:{m}:{y}")
b=Next_Date()
print(f"Next Date is {b}")