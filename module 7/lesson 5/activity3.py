def add(x, y):
    return x + y
# this function subracts two numbers
def subract(x, y):
    return x - y
 # this function multiplies two numbers
def multiply(x, y):
    return x * y

# this function divides two numbers
def divide(x, y):
    return x/y

num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))

print("sum:", add(num1, num2))
print("difference:", subract(num1, num2))
print("product:", multiply(num1, num2))
print("quotient:", divide(num1, num2))
    
