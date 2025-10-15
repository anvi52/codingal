num = int(input("enter a number:"))

order = len(str(num))

temp = num
sum_num = 0
while temp > 0:
 digit =temp % 10
 sum_num += digit ** order
 temp //= 10

 if sum_num == num:
  print(num, "is an armstrong number")
 else:
  print(num,"is NOT an armstrong number")