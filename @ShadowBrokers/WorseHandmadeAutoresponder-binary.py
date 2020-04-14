b = int(input("enter your number to convert to binary: "))
#print("your answer is", bin(b)) this will give the 0b value in binary

def f(n):
  print('your answer is {:0b}'.format(n))
f(17)

b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)
