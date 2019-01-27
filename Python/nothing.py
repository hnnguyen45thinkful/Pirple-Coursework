for num in range(101):
    # special case for prime
    if num == 3 or num == 5:
        print( num, "is prime")
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")    
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3 != 0:
        print(number,"Buzz")
    else:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0 :
                    print(num)
                    break
            else:
                print(num, "is prime")

                FizzBuzz
2 is prime
3 is prime
Fizz
4
5 is prime
Buzz
Fizz
7 is prime
8
Fizz
Buzz
11 is prime
Fizz
13 is prime
14
FizzBuzz
16
17 is prime
Fizz
19 is prime
Buzz
Fizz
22
23 is prime
Fizz
Buzz
26
Fizz
28
29 is prime
FizzBuzz
31 is prime
32
Fizz
34
Buzz
Fizz
37 is prime
38
Fizz
Buzz
41 is prime
Fizz
43 is prime
44
FizzBuzz
46
47 is prime
Fizz
49
Buzz
Fizz
52
53 is prime
Fizz
Buzz
56
Fizz
58
59 is prime
FizzBuzz
61 is prime
62
Fizz
64
Buzz
Fizz
67 is prime
68
Fizz
Buzz
71 is prime
Fizz
73 is prime
74
FizzBuzz
76
77
Fizz
79 is prime
Buzz
Fizz
82
83 is prime
Fizz
Buzz
86
Fizz
88
89 is prime
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97 is prime
98
Fizz
Buzz
[Finished in 0.7s]