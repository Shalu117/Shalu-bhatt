import time
print(" The format will be in Hour:Minute:Second ")
print(' ')
print("Enter value of :")
Hr=int(input("hr:\t"))
Min=int(input("min:\t"))
Sec=int(input("sec:\t"))
print(' ')
print("             TIMER")
while(Sec>=0):
    t = '{:02d}:{:02d}:{:02d}'.format(Hr,Min, Sec)
    print(t,end="\r")
    if(Sec>0):
        time.sleep(1)
    Sec=Sec-1
if(Min>0):
    Sec=59
    Min=Min-1
elif(Hr>0):
    Hr=Hr-1
    Min=59
    Sec=59
else:
    print("\n ************Times Up!!*************")