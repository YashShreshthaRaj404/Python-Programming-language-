# virtual clock:

a1 = "TIME CLOCK"
print(a1.center(45)
    
        )
import time
timestamp = time.strftime('%H : %M : %S')
print(timestamp.center(46)

        )
# alarm clock:
b3 = " alarm clock"
print(b3.upper()
     )
#print(b3.center(46))
b1 = int(time.strftime('%H')
        )
tm1 = input("Enter Your Time:")
#if (tm1 > '11:59:59 PM  ' and tm1 <= '11:59:59 AM'):
    #print("Good Morning")
print(tm1.center(46))

if (tm1 > '11:59:59 AM' and tm1 <= '16:59:59 PM'):
    print("Good Afternoon")

elif (tm1 > '16:59:59 PM' and tm1 <= '18:59:59 PM'):
    print("Good Evening")

elif (tm1 > '18:59:59 PM' and tm1 <= '23:59:59 PM'):
    print("Good Night")
    
#if  (tm1 > '11:59:59 PM' and tm1 <= '11:59:59 AM'):
    #print("GoodMorning")

else:
    print("Good Morning")
    
#         xxxxxxxxxxxxx end xxxxxxxxxxxxxxxx