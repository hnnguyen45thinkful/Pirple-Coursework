/*
Javascript Homework Assignment #6
Loops
By: Hieu Nguyen
*/

// Write a program that prints the numbers from 1 to 100.
// But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
// For numbers which are multiples of both three and five print "FizzBuzz".
// The one hint you'll likely need is: 
// There is a Javascript operator called "remainder" but often referred to as "modulus" or "modulo". It is represented by the percentage sign (%) and it gives you the remainder left over after division. So for example:
// 6 % 3 
// Equals zero. Because after dividing 6 by 3, there is zero leftover. Whereas:
// 6 % 4
// Equals 2. Because after dividing 6 by 4, there are 2 left over from the six.
// If that was confusing, don't worry. It will make more sense as you use it. The point is: the remainder operator is useful for finding out if X is a multiple of Y. If it is, then X % Y will yield zero. Knowing this should help you complete this assignment without any issue.

// Extra Credit:
// Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime". You should print this whenever you encounter a number that is prime (divisible only by itself and one). As you implement this, don't worry about the efficiency of the algorithm you use to check for primes. It's okay for it to be slow.

//I need to create a prime number checker start at 2 since 0 and 1 are prime to itself.
//Created a function and with a for loop statement
function primeNumberChecker(numbers) {
    for (let x = 2; x < numbers; x++)
        if (numbers % x === 0) //if the number is modulus to zero
        return false;// returns to false otherwise
    
    return numbers !== 0 &&  numbers !== 1; //if the numbers are not 0 and 1. Opposite 
}

//Since I created the function for checking prime numbers now I can add console.log for fizz, buzz and fizzbuzz and also showing which on is all the prime numbers from 1 to 100.
//I need to create a for loop statement for each case to see if they are modulus/multiple of 3 and 5 combination.
for (let x = 1; x <= 100; x++)    { //create a for loop up to 1 to 100
	if (primeNumberChecker(x))  { //function definition from above
		console.log(x + '--Prime');//Shows the prime number with the number and shows the word "Prime"
    } else if (x % 3 == 0 && x % 5 == 0) { //Reminder is equal to zero divisable to 3 and 5
        console.log(x + "--FizzBuzz"); // prints out numbers the word "fizzbuzz"
    } else if (x % 5 == 0) { // remainder is divisable to 5
        console.log(x + "--Buzz"); //same but prints out "buzz"
    } else if (x % 3 == 0) { // remainder is divisable to 5
        console.log(x + "--Fizz");//same but prints out "fizz"
    } else {
        console.log(x);// otherwise print the number out with a condition from above or not.
    }
}

//Output of all console.log for all prime numbers from 1 to 100
// 1
// 2--Prime
// 3--Prime
// 4
// 5--Prime
// 6--Fizz
// 7--Prime
// 8
// 9--Fizz
// 10--Buzz
// 11--Prime
// 12--Fizz
// 13--Prime
// 14
// 15--FizzBuzz
// 16
// 17--Prime
// 18--Fizz
// 19--Prime
// 20--Buzz
// 21--Fizz
// 22
// 23--Prime
// 24--Fizz
// 25--Buzz
// 26
// 27--Fizz
// 28
// 29--Prime
// 30--FizzBuzz
// 31--Prime
// 32
// 33--Fizz
// 34
// 35--Buzz
// 36--Fizz
// 37--Prime
// 38
// 39--Fizz
// 40--Buzz
// 41--Prime
// 42--Fizz
// 43--Prime
// 44
// 45--FizzBuzz
// 46
// 47--Prime
// 48--Fizz
// 49
// 50--Buzz
// 51--Fizz
// 52
// 53--Prime
// 54--Fizz
// 55--Buzz
// 56
// 57--Fizz
// 58
// 59--Prime
// 60--FizzBuzz
// 61--Prime
// 62
// 63--Fizz
// 64
// 65--Buzz
// 66--Fizz
// 67--Prime
// 68
// 69--Fizz
// 70--Buzz
// 71--Prime
// 72--Fizz
// 73--Prime
// 74
// 75--FizzBuzz
// 76
// 77
// 78--Fizz
// 79--Prime
// 80--Buzz
// 81--Fizz
// 82
// 83--Prime
// 84--Fizz
// 85--Buzz
// 86
// 87--Fizz
// 88
// 89--Prime
// 90--FizzBuzz
// 91
// 92
// 93--Fizz
// 94
// 95--Buzz
// 96--Fizz
// 97--Prime
// 98
// 99--Fizz
// 100--Buzz