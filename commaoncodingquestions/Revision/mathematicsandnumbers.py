# 3. Mathematics and Numbers

# Check if a number is prime.

def check_prime(num):
    if num ==1 or num == 2:
        print("Prime ")
        return
    for i in range(2,(num // 2)+2):
        print(i, num)
        if num % i == 0:
            print("not prime")
            return
    print("prime")
check_prime(13)    

# Generate the Fibonacci sequence up to n terms.

def fibbonacci(n):
    fib_list = [0,1]

    if n == 1:
        print("[0]")
        return
    for i in range(0,n-2):
        value = fib_list[i] + fib_list[i+1]
        fib_list.append(value)
    print(fib_list)    

# fibbonacci(10)
    

# Write a function to calculate the factorial of a number.
def factorial(num):
    n_factorial = 1
    for i in range(1,num + 1):
        n_factorial = n_factorial * i
    print(n_factorial)

# factorial(4)    

# Check if a number is an Armstrong number.
# input = number, 
# count = nu of digit,
# sum = list[0]^count + list[1]^count..........list[count]^count
def armstrong(dig):
    strg = str(dig)
    count = len(strg)
    str_list = []
    for element in strg:
        str_list.append(int(element))    
    summ = 0
    
    for i in range(0,count):
        summ = summ + str_list[i]**count

    print(summ)    

# armstrong(123)




