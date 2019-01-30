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

// Same from the above now calling it at the end reversing.
function greeting(name) {
    console.log('Hello, my name is ' + name + ".");
}
greeting('Hieu');
// 'Hello, my name is Hieu.'

//Variables
// In my words, variables can be used out of their scope in a function or deckaring them in the global scope or inside a function. For instance, "var" can declared inside the function which can make the entire function become the scope of var This is used a lot in ES5 before ES6 comes out with "let" and "const", but we will focus on "var". After using variables they can be used different and mutiple times by repeating or overwrittening them. Using var can be equal to declaring either empty value or assigning it to something.

//Here are some examples:
//Example 1:
var myName = "Hieu";// myName variable scope is global

function globalScope() { 
    console.log(myName);
}
globalScope(); //Hieu
//Example 2:
function functionScope() {
    //Now my var myName is a variable scope is global inside the function
    var myName = "Hieu";
    console.log(myName);
}    
functionScope(); //Hieu
//Example 3
function varName() {
    varName = "Hieu"; //declare my variable without "var"
    console.log(varName);
}
varName(); //Hieu

// Let and Constant
// Both "let" and "const" are both new features used in ES6 since ES5 uses more on "var" which is variables. They are both different from each other since one can be reassigned/modified and another can be used as a blocked scope variables. "Const" variable values cannot be changed, but only can be modified meaning it has to be an assigned value, for instance when declaring a variable with a local scope (block) it can be only used once and when assigning a new one it may cause an error. I like to think constant like in mathematics like Pi = 3.14 or e = 2.718 which are real number values. As for "let" are used on block scope variables and whereas they cannot be used out of the block when they are declared and used. Meaning the values you use "let" can be used many times and overwritten to assume different cases. I like to think the "let" variable as making more cases and assuming more assumptions using it in a block scopes just like "constant" but its similar to "var" in global scope function and assigning variables BUT REMEMBER let CANNOT BE "HOISTED" or "HOISTING". 

//Here is my let examples:

let myNameLet = "Hieu";

function globalScopeName() {
    // myNameLet is used as a variable scope is global
    console.log(myNameLet);
}
globalScopeName();//Hieu


function letBlockScope() {
    if(true) {
        // myNameBlockLet variable scope is if block specific
        // myNameLet variable scope is if block specific
        let myNameBlockLet = "Hieu";
        let myNameLet = "Hieu Ngoc Nguyen"
        console.log("myNameLet variable inside of this if block is my full name: " + myNameLet + '.');//Hieu Ngoc Nguyen.
    }
    // myNameLet testing cannot be accessed because of the outside and also the if block shows up as a - Gets 'ReferenceError: myNameBlockLet is not defined' if we uncomment the below line
    //console.log(myNameBlockLet);
    console.log("myNameLet variable value inside the function and so the outside the if block is my first name: " + myNameLet + '.');//Hieu.
}

letBlockScope();//Hieu.

//Here is my constant examples:

const myNameConstant = "Constant Hieu";
const myTestConstant = "Constant Test"

function constGlobalScope() {
    // myNameConstant variable scope is global used
    console.log(myNameConstant);
}


constGlobalScope();//Constant Hieu


function constantBlockScope() {
    // Gets 'TypeError: Assignment to constant variable' if we uncomment the below line
    // myConstName = "ConstModified";

    if(true) {
        // myConstNameIfBlock variable scope is if block specific
        // myConstName variable scope is if block specific
        const myNameConstantBlock = "Constant Hieu";
        const myNameConstant = "Constant Test"
        // Here I get 'TypeError: Assignment to constant variable' from the console log so now if I uncomment the below line
        // myTestConstant = "ModifyConstant";
        console.log("myNameContant variable inside the if block is: " + myNameConstant + '.');
    }
    // myNameConstant cannot be accessed outside the if block - Gets this 'ReferenceError: myNameConstant is not defined' if we uncomment the below line
    //console.log(myNameConstantBlock);
    console.log("myNameConstant value inside the function but outside the if block is: " + myNameConstant + '.');
}

constantBlockScope();//Constant Hieu