for num in range(101):
    # special case for prime
    if num == 3 or num == 5:
        print( num, "is prime")
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")    
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print("Buzz")
    else:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0 :
                    print(num)
                    break
            else:
                print(num, "is prime")