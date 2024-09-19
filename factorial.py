def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
number=int(input("please enter your number: "))
print(f"factorial {number} is equal to:{factorial(number)}")