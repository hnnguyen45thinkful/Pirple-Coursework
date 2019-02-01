/*
Javascript Homework Assignment #4
Functions
By: Hieu Nguyen

*/
 
// Let's go back to your syllogism (logical argument) examples from Homework #3. Now it's time to turn those loose bits of logic into functions. Rather than having procedure that demonstrates that Socrates is mortal, you should create a function that accepts a name and returns a boolean (True or False) representing whether that name identifies a man who is mortal or not. Your function to gracefully handle unexpected inputs (such as an unrecognized name or a name that is a not a string at all) without throwing an exception.

// Extra Credit:

// If you did the extra credit on Homework #3, let's turn that example into a function as well. It should accept in 2 arguments:

// 1. An array of all cake possibilities (vanilla or chocolate)

// 2. A boolean representing whether or not the cake is chocolate.

// It should return a string indicating the actual flavor of the cake.

//Create an arrow function using const and also using name as a an array storing a few names and also using boolean true and false at return.

//Here is my array for const namesArr
const namesArr = ['Socrates', 'Plato', 'Aristotle', 'John Smith', 'Jane Smith', 'King James'];
//Here is my arrow function with name defined as a variable/constant with if statements and using === to check for the EXACT names using || (or).
const checkMortal = (names) => {
	if(names === ('Plato') || names === ('Socrates') || names === ('Aristotle')){
		return true;
	} else {
		return false;
	}
}

//create a nameArr.forEach((names) with an arrow function for each one in the array from above can test if all the names are true or false on console.log().
namesArr.forEach((names) => {
			console.log('This person named ' + names + ' a MORTAL? (True or False) ? ' + checkMortal(names)
			);
});
//Console.log results:
// This person named Socrates a MORTAL? (True or False) ? true
// This person named Plato a MORTAL? (True or False) ? true
// This person named Aristotle a MORTAL? (True or False) ? true
// This person named John Smith a MORTAL? (True or False) ? false
// This person named Jane Smith a MORTAL? (True or False) ? false
// This person named King James a MORTAL? (True or False) ? false