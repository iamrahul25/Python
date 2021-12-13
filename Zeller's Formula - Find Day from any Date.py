#Zeller's Formula for calculating Day from any Date

d=int(input("Enter date (dd):"))
m=int(input("Enter month (mm):"))
y=input("Enter year (yyyy):")

y1=int(y[0:2])
y2=int(y[2:4])

#Because March(1) is first month and February(12) is last month.
if m==1 or m==2:
    m=m+10
    y2=y2-1

elif m>2:
    m=m-2

#Main Formula
F=d+(((13*m)-1)//5)+y2+(y2//4)+(y1//4)-(y1*2)
#print("F:",F)

# d - date
# m - month
# y1 - first two digit of year
# y2 - last two digit of year

#Case 1:
if F>=0 and F<=6:
    D=F

#Case 2:
elif F>=7:
    D=F%7

#Case 3:
elif F<0:

    if F>=-6:
        D=F+7
   
    elif F<=-7:
        x=(-F)%7
        D=7-x

#print("D",D)

dict={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}

Day=dict[D]
print("Day is:",Day)
