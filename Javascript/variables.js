/*
Javascript Homework Assignment #2
Variables: Let(let), Constant(const), and Variable(var)
By: Hieu Nguyen

*/
// What are the differences between let, const and var? When would each be appropriate too use? In your own words, write 1 - 2 paragraphs explaining the different use-cases for each. If English is not your native language, feel free to write in whatever language you prefer. Just please note which language it is at the top of the assignment, so we know how to translate it.

// Create a file called variables.js and add your explanation as comments at the top of the page.

// Then, within the document write 3 code examples (1 for var, 1 for const and 1 for let) showcasing the use-cases you explained above.


// Extra Credit:

// To earn extra credit, add an explanation of "hoisting" to the top of your document. What is hoisting? What does the word mean, and how does hoisting work in Javascript?

// What are the differences between let, const and var? When would each be appropriate too use? In your own words, write 1 - 2 paragraphs explaining the different use-cases for each. If English is not your native language, feel free to write in whatever language you prefer. Just please note which language it is at the top of the assignment, so we know how to translate it.

// Hoisting

// What is hoisting?
// In Javascript, "hoisting", when a variable can be used and declared after it has been used, so in plain words a variable can be used before it has been declared in the Javascript file. This is still applied in ES5 not in ES6 because we are still using the "var" term call to declared variables only. Meaning ES6 calls for variables "let" or "const" are not elgible to use in hoisting only "var" call term. Remember that JavaScript only hoists declarations not initializations. Lastly, remember it declarations calling for a variable are hoisted to the top of their scope in var calling or function calling look example at the bottom for a clear picture. 

//Here are some examples:
var z; // DECLARING a VARIABLE
z = 100; // ASSIGNING a variable
console.log(z); // 100

//Another example: //lets reverse it
z = 100;
var z = 100;
console.log(z); //still the same and works // 100

//Same with functions calls
greeting('Hieu');
function greeting(name) {
    console.log('Hello, my name is ' + name+ ".");
}
// 'Hello, my name is Hieu.'

// Same from the above now calling it at the end.
function greeting(name) {
    console.log('Hello, my name is ' + name + ".");
}
greeting('Hieu');
// 'Hello, my name is Hieu.'

