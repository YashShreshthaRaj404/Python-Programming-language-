"""
       This is a Calucator.
In the Calucator, there are Simple Calucator And Calculator Converter.In the simple 
Calucator, you can calucate a simple value. And in the Calucator Converter you can 
convert any of the following values:
"""

# function for background image:
"""
from tkinter import *

root = Tk()
root.title('Bg setting')
img = PhotoImage(file = "white_blank_wallpaper_background.png")
Label (root, image = img).pack()
mainloop()
"""
# exit

real_poster = "CALUCATOR"
print(real_poster.center(45)
    
                             )

choos1i = print(" \n1.Simple Calucator \n2.Calucator Converter")
choos1 = input(" ")
            

if(choos1 == "1"):
  main_poster1 = " Simple Calucator"
  print(main_poster1.center(45)
      
       )
  
# Simple Calculator Program in python...

# Functions: Addition, Subtraction, Multiplication, and Division...

# Function for Addition:

  def addition(n1, n2):
    return n1 + n2

# Function for Subtraction:

  def subtraction(n1, n2):
    return n1 - n2

# Function for Multiplication:

  def multiplication(n1, n2):
    return n1 * n2

# Function for Division:

  def division(n1, n2):
      return n1 / n2


  print("Select Operations")
  print(
    "1. Addition\n"
       "2. Subtraction\n"
          "3. Multiplication\n"
      "4. Division\n")

# ...Giving the option to the user to choose the operation...

  operation = int(input("Enter Choice Of Operation:- \n1:"
                        "\n2:"
                           "\n3:"
                     "\n4:")   
                 )

#Taking Input from the Users....

  n1 = float(input("Enter the First Number: ")
            
            )
  
  n2 = float(input("Enter the Second Number: ")
            
                   )
  
#.....Apply Conditional Statements: To make operation as-per-user choices.....

  if operation == 1:
     print (n1, "+", n2, "=", addition(n1, n2)         
           )
    
  elif operation == 2:
     print (n1, "-", n2, "=", subtraction(n1, n2)
                    ) 
    
  elif operation == 3:
     print (n1, "*", n2, "=", multiplication(n1, n2)
           ) 
    
  elif operation == 4:
     print (n1, "/", n2, "=", division(n1, n2)
           )
    
  else:
     print("Invalid Input")

# Simple Calculator function has been Exited:

if(choos1 == "2"):
  main_title_poster = " CALUCATOR CONVERTER"
  print(main_title_poster.center(47)
      
       )
  
# This function below is unit_converter, in which the unit is converted which you say...
unit_converteri = print("Choose A Unit Converter:-\n1.Length \n"
      "2.Temperature \n3.Data \n"
            "4.Time")
unit_converter = input(" ")
                    

#This function below is length_converter,in which the length is converted which you say.

if(unit_converter == "Length" or unit_converter == "1"):
  r2i = print("What Do You Call Converting: \n1.meter(m)  \n"
             "2.kilometers(km) \n" 
        "3.centimere(cm)")
  r2 = input("Enter The Value: \n"
                    " NOTE: [AS IT IS WRITTEN, IT HAS TO IN WRITTEN THE SAME WAY ]  \n"
                "1/2/3:-")
           
  r3i = print("What Do You Call Converting To: \n1.meter(m) \n2.kilometer(km) \n"
          "3.centimetre(cm)")
  r3 = input(" Enter The Value: \n"
                    " NOTE: [AS IT IS WRITTEN, IT HAS TO IN WRITTEN THE SAME WAY ]  \n"
                "1/2/3" )
            
#....This is entering_number function in which is the number put in it which you say....
  
  entering_number = float(input("Enter The Value: ")
       
         )

#.....Apply Conditional Statements: To make operation as-per-user choices.....

  # Function will starts when unit_converter = length
  if (r2 == "meter(m)" and r3 == "kilometer(km)" ):
    print(entering_number / 1000 , "km")
  elif (r2 == "meter(m)" and r3 == "centimetre(cm)" ):
    print(entering_number * 100 , "cm")

  if (r2 == "meter(m)" and r3 == "meter(m)" ):
    print(entering_number* 1 , "m")
  elif(r2 == "kilometer(km)" and r3 == "meter(m)"):
    print(entering_number * 1000 , "m")
  if(r2 == "kilometer(km)" and r3 == "centimetre(cm)"):
    print(entering_number * 100000 , "cm")
  elif(r2 == "kilometer(km)" and r3 == "kilomete(km)"):
    print(entering_number * 1 , "km")
  if(r2 == "centimetre(cm)" and r3 == "meter(m)"):
    print(entering_number / 100 , "m")
  elif(r2 == "centimetre(cm)" and r3 == "kilometer(km)" ):
    print(entering_number / 100000 , "km")
  if(r2 == "centimetre(cm)" and r3 == "centimetre(cm)"):
       print(entering_number * 1 , "cm")

# Function will starts when unit_converter = Temperature 

if (unit_converter == "Temperature" or unit_converter == "2"):
  r2ei = print("What Do You Call Converting:-  \n1.Celsius(C) \n"
              "2.Fahrenheit(F) \n3.Kelvin(K)")
  r2e = input(" Enter The Value: \n1/2/3")
           
  r3ei = print("What Do You Call Converting To:- \n1.Celsius(C) \n2.Fahrenheit(F) \n"
              "3.Kelvin(K)")
  r3e = input("  Enter The Value: \n1/2/3 ")
           
  r4e = float(input("Enter The Value:")
          
           )
  
  if (r2e == "Celsius(C)" and r3e == "Fahrenheit(F)"):
    print(r4e * 9/5 + 32 , "F")
  elif (r2e == "Celsius(C)" and r3e == "Kelvin(K)"):
      print(r4e + 273.15 , "K")
  if (r2e == "Celsius(C)" and r3e == "Celsius(C)"):
    print(r4e * 1 , "C")
    
  elif(r2e == "Fahrenheit(F)" and r3e == "Celsius(C)"):
    print((r4e - 32) * 5/9 , "C")
  if(r2e == "Fahrenheit(F)" and r3e == "Kelvin(K)"):
    print((r4e - 32) * 5/9 + 273.15 , "K")
  elif(r2e == "Fahrenheit(F)" and r3e == "Fahrenheit(F)"):
    print(r4e * 1 , "F")

  if(r2e == "Kelvin(K)" and r3e == "Celsius(C)"):
    print(r4e - 273.15 , "C")
  elif(r2e == "Kelvi(K)" and r3e == "Fahrenheit(F)"):
    print(r4e * 9/5 - 459.67 , "F")
  if(r2e == "Kelvin(K)" and r3e == "Kelvin(K)"):
    print(r4e * 1 , "K")

# Function will starts when unit_converter = Data...

if (unit_converter == "Data" or unit_converter == "3"):
  
    d1i = print("What Do You Call Converting:-\n1.Bits(Bit)\n2.Bytes(B)\n3.Kilobytes(KB)"
             "\n4.Megabytes(MB)\n5.Gigabytes(GB)\n6.Terabytes(TB)\n"
             "7.Petabytes(PB)")
    d1 = input("  Enter The Value: \n1/2/3/4/5/6/7")
            
    d2i = print("What Do You Call Converting To:- \n1.Bits(Bit)\n2.Bytes(B)\n"
               "3.Kilobytes(KB)\n"
               "4.Megabytes(MB)\n5.Gigabytes(GB)\n6.Terabytes(TB)\n"
               "7.Petabytes(PB)")
    d2 = input("  Enter The Value: \n1/2/3/4/5/67 ")
              
    d3 = float(input(" Enter The Value:")
            )
  
    if (d1 == "Bit" and d2 == "(B)"):
      print(d3 / 8 , "B")
    elif (d1 == "Bit" and d2 == "KB"):
      print(d3 / 8000 , "KB")
    elif (d1 == "Bit" and d2 == "MB"):
      print(d3 / 8000000 , "MB")
    elif (d1 == "Bit" and d2 == "GB"):
      print(d3 / 8000000000 , "GB")
    elif (d1 == "Bit" and d2 == "TB"):
      print(d3 / 8000000000000 , "TB")
    elif (d1 == "Bit" and d2 == "PB"):
      print(d3 / 8000000000000000 , "PB")
  # Bit function has started!
    if (d1 == "B" and d2 == "Bit"):
      print(d3 * 8 , "Bit")
    elif (d1 == "B" and d2 == "KB"):
      print(d3 / 1000 , "KB")
    elif(d1 == "B" and d2 == "MB"):
      print(d3 / 1000000 , "MB")
    elif (d1 == "B" and d2 == "GB"):
      print(d3 / 1000000000 , "GB")
    elif (d1 == "B" and d2 == "TB"):
      print(d3 / 1000000000000 , "TB")
    elif (d1 == "B" and d2 == "PB"):
      print(d3 / 1000000000000000 , "PB")     
  # Kilobytes (KB) function has started!
    if (d1 == "KB" and d2 == "Bit"):
      print(d3 * 8000 , "Bit")
    elif(d1 == "KB" and d2 == "B"):
      print(d3 * 1000 , "B")
    elif(d1 == "KB" and d2 == "MB"):
      print(d3 / 1000 , "MB")
    elif(d1 == "KB" and d2 == "GB"):
      print(d3 / 1000000 , "GB")
    elif(d1 == "KB" and d2 == " TB"):
      print(d3 / 1000000000 , "TB")
    elif(d1 == "KB" and d2 == "PB"):
     print(d3 / 1000000000000 , "PB")
# Megabytes (MB) function has started!
    if (d1 == "MB" and d2 == "Bit"):
      print(d3 * 8000000 , "Bit")
    elif(d1 == "MB" and d2 == "B"):
      print(d3 * 1000000, "B")
    elif(d1 == "MB" and d2 == "KB"):
      print(d3 * 1000 , "KB")
    elif(d1 == "MB" and d2 == "GB"):
      print(d3 / 1000 , "GB")
    elif(d1 == "MB" and d2 == "TB"):
      print(d3 / 1000000 , "TB")
    elif(d1 == "MB" and d2 == "PB"):
      print(d3 / 1000000000 , "PB")
# Gigabytes (GB) function has started!
    if(d1 == "GB" and d2 == "Bit"):
      print(d3 * 8000000000 , "Bit")
    elif(d1 == "GB" and d2 == "B"):
      print(d3 * 1000000000 , "B")
    elif(d1 == "GB" and d2 == "KB"):
      print(d3 * 1000000 , "KB")
    elif(d1 == "GB" and d2 == "MB"):
      print(d3 * 1000 , "MB")
    elif(d1 == "GB" and d2 == "TB"):
      print(d3 / 1000 ,"TB")
    elif(d1 == "GB" and d2 == "PB"):
      print(d3 / 1000000 , "PB")
# Terabytes (TB) function has started!
    if(d1 == "TB" and d2 == "Bit"):
      print(d3 * 8000000000000 , "Bit")
    elif(d1 == "TB" and d2 == "B"):
      print(d3 * 1000000000000 , "B")
    elif(d1 == "TB" and d2 == "KB"):
      print(d3 * 1000000000 , "KB")
    elif(d1 == "TB" and d2 == "MB"):
      print(d3 * 1000000 ,"MB")
    elif(d1 == "TB" and d2 == "GB"):
      print(d3 * 1000 , "GB")
    elif(d1 == "TB" and d2 == "PB"):
      print(d3 / 1000 , "PB")
  # Petabytes (PB) function has started!!
    if(d1 == "PB" and d2 == "Bit"):
      print(d3 * 8000000000000000 , "Bit")
    elif(d1 == "PB" and d2 == "B"):
      print(d3 * 1000000000000000 , "B")
    elif(d1 == "PB" and d2 == "KB"):
      print(d3 * 1000000000000 , "KB")
    elif(d1 == "PB" and d2 == "MB"):
      print(d3 * 1000000000 , "MB")
    elif(d1 == "PB" and d2 == "GB"):
      print(d3 * 1000000 , "GB")
    elif(d1 == "PB" and d2 == "TB"):
      print(d3 * 1000 , "TB")
      
    # In the following function BITS(bit)/BYTES(B)/KILOBYTES(KB)/MEGABYTES(MB)/GIGABYTES
  #(GB)/PEGABYTES(PB) = 1
  
    elif(d1 == "Bit" and d2 == "Bit" or d1 == "B" and d2 == "B" or d1 == "KB" and d2 == 
                        "KB" or d1 == "MB" and d2 == "MB" or d1 == "GB" and d2 =="GB" or
                      d1 == "TB" and d2 == "TB" or d1 == "PB" and d2 == "PB"):
      print(d3 * 1 )

# Function will starts when unit_converter = Time

if(unit_converter == "Time" or unit_converter == "4"):
  t1i = print(" What Do You Call Converting:- \n1.Hours(H) \n2.Minutes(M) \n"            
                 "3.Secounds(S)")
  t1 = input("  Enter The Value: \n1/2/3 ")
          
  t2i = print( "What Do You Call Converting To:- \n1.Hours(H) \n2.Minutes(M) \n"
                   "3.Secounds(S)")
  t2 = input("  Enter The Value: \n1/2/3")
          
  t3 = float(input("Enter The Value:")
            )
  if(t1 == "H" and t2 == "M"):
    print(t3 * 60 , "M")
  elif(t1 == "H" and t2 == "S"):
    print(t3 * 3600 , "S")
  elif(t1 == "M" and t2 == "H"):
    print(t3 / 60 , "H")
  elif(t1 == "M" and t2 == "S"):
    print(t3 * 60 , "S")
  elif(t1 == "S" and t2 == "H"):
    print(t3 / 3600 , "H")
  elif(t1 == "S" and t2 == "M"):
    print(t3 / 60 , "M")
    
  # In the following function H/M/S = 1
  elif(t1 == "H" and t2 == "H" or t1 == "M" and t2 == "M" or 
                           t1 == "S" and t2 == "S"):
    print(t3 * 1)
  else:
    print("Invalid Input")