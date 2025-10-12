total_days = int(input("enter total numbe of working days:"))
absent_days = int(input("enter total number of days absent:"))

present_day = total_days - absent_days
attendence_percentage = present_day/total_days * 100
print(f"\nTotal working days:", total_days)

print(f"days present:", present_day)

print(f"attendence percentage:", attendence_percentage)

if attendence_percentage < 75:
    print("you are not allowed to sit in the exam")
else: 
   print("you are allowed to sit in the exam")