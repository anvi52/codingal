y = int(input("enter the value of y:"))
x = int(input("enter the value of x:"))
z = int(input("enter the value of z:"))

nums = [x , y , z]
nums.sort()

x, y, z = nums
print("values in ascending order")
print("x=", x)
print("y=", y)
print("z=", z)