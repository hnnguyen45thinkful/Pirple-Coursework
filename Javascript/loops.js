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
    for (let i = 2; i < numbers; i++)
        if (num % i === 0) //if the number is modulus to zero
        return false;// returns to false otherwise
    
    return numbers !== 0 &&  numbers !== 1; //if the numbers are not 0 and 1. Opposite 
}