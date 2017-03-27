num = raw_input("Enter any Number: ")
Reverse = 0
while(num > 0):
    Reminder = num %10
    Reverse = (Reverse *10) + Reminder
    num = num //10
 
print("\n Reverse of entered word is: %d" %Reverse)