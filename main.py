
def prime_checker(number):
    istrue = True
    for i in range(2,number):
        if number % i == 0:
            istrue = False
    if istrue == False:
        print("It's not a prime number.")
    elif istrue == True:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
