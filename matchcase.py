
variable = int(input("pick a number (1-7):"))

match variable:
 case 1:
     print("monday")
 case 2:
     print("tuesday")
 case 3:
     print("wednesday")
 case 4:
     print("thursday")
 case 5:
     print("friday")
 case 6:
     print("saturday")
 case 7:
     print("sunday")
    
 case _:  print("invalid number")
