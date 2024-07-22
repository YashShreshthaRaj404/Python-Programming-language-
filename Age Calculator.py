"""
        This is an age calculator which will tell you your current age,
by entering your date of birth.
"""

print("AGE CALCULATOR".center(45) + '\n' + '\n')

# Function for years....
import datetime

current_year = datetime.datetime.now().year

# Function for months....

import datetime

current_month = datetime.datetime.now().month

# Function for days....

from datetime import date
today = date.today()

from datetime import datetime

""""
current_time = datetime.now()
print(current_time.strftime("%H:%M:%S")
    )
"""

print("Enter Your Date Of Birth".upper() + '\n'
     )
d1 = int(input("date:".upper()
              )
        )
m1 = int(input("month:".upper()
              )
        )
y1 = int(input("year:".upper() 
              )
        )
print('\n' "Age".upper() , "=" ,  current_year - y1, "Years", current_month - m1, 
      "Months",
      today.day - d1, "Days" + '\n'
     )
