/*
Javascript Homework Assignment #3
Statements and Operators
By: Hieu Nguyen

*/

// Details:

// Let's look at a popular logical argument (a syllogism)

// All men are mortal
// Socrates is a man.
// Therefore, socrates is mortal.

// Using "if statements" and any other logical operators and data-types you see fit, recreate this logical argument. Your code should make clear that "socrates" is part of a collection of items referred to as "men", and that all members of this collection are mortal. You should also then demonstrate that since Socrates is part of this collection, it follows that he is mortal as well.


// Extra Credit:

// Got the hang of creating a logical argument? Want to try another one? Try this one as well:

// This cake is either vanilla or chocolate.
// This cake is not chocolate.
// Therefore, this cake is vanilla.

//Create an array of mens names
const mensarrays = ["Mike", "Socrates", "Edison", "Albert", "Scot"];
const mensThatAreMortals = true;
//Create an if-statement to print out the console.log below to show the EXACT statements given and also give opposite (NOT). 
if (mensThatAreMortals) {
    console.log("All men are mortal");
} else {
    console.log("All men are not mortal");
}
//Same thing from above (if statments and logical operators && (AND)) but I used the includes the mensarrays with "Socrates" to complete the statements give from above. Also if the opposite case (NOT) with all the console.log()s.
if (mensarrays.includes("Socrates") && mensThatAreMortals) {
    console.log("Socrates is a men");
    console.log("Therefore, socrates is mortal.");
} else {
    console.log("Socrates is not a men");
}

//Results on console.log()s are PERFECT!!!.

// All men are mortal
// Socrates is a men
// Therefore, socrates is mortal.



// Extra Credit create an constant object cake with the properties name and  
const cakeFlavorName = {
    flavor: "Vanilla",
    name: "Vanilla cake"
};
if (cakeFlavorName.flavor === "Vanilla" || cakeFlavorName.flavor === "Chocolate") {
    console.log("This cake flavor is either Vanilla or Chocolate.");
    if (cakeFlavorName.flavor !== "Chocolate") {
        console.log("This cake flavor is NOT Chocolate.");
        console.log("Therefore, this cake flavor is Vanilla.");
    }
}
//Results check the same PERFECT!!! on the console.log()s.

// This cake flavor is either Vanilla or Chocolate.
// This cake flavor is NOT Chocolate.
// Therefore, this cake flavor is Vanilla.