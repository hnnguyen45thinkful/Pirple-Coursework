/*
Javascript Homework Assignment #7
The DOM
By: Hieu Nguyen

*/
 
// Create a very simple webpage, displaying some of your favorite colors. Use HTML, CSS and Javascript.
// 1. The top of the page should include a header <h1> tag, with a name for your page, and then an <h2> tag with a description of what's on the page.
// 2. Further down the page you should draw 10 rectangles, of any size you wish, and give them each a unique hex-code so they all appear as different colors. Here's a color-picker that might help.
// 3. Below each rectangles, list the hex code (in plain text).
// 4. Give all of the rectangles the same class, but make sure each rectangle has a unique ID.
// 5. Wrap all of the rectangles in an containing element ( a <div> ) and give that element the id "rectangleWrapper". Now give that element 50 pixels of padding on its top, right and left sides. But add zero padding to the bottom.
// 6. When the page loads, console.log the messages "Here are the rectangle IDs" and then console.log all the rectangles' IDs, one at a time.
// 7. In the <head> of the document, add a <title> tag that matches the text in the <h1> you added in step 1.
const rectangles = document.querySelectorAll(".rectangleDisplay");//using document.querySelectorAll() to get all rectangles information
const title = document.querySelector(".heading-title"); //same from above just only the specific one and only the first one.
const head = document.querySelector("head");//same but diffrent property from above
console.log("Here are the rectangles IDs:");
    let x = 1 ;
    for( const  prop  of rectangles){
        if (x <= rectangles.length) {
            console.log("rectangle " + x +" id : #" + prop.id);
            x += 1;
        }
    }
    const newElement = document.createElement("title");
    newElement.innerText = title.textContent;
    head.appendChild(newElement);

    //Overall test works!!!! on console.log
// Here are the my rectangles with IDs:
//  rectangle 1 id : #rectangle-color-1
//  rectangle 2 id : #rectangle-color-2
//  rectangle 3 id : #rectangle-color-3
//  rectangle 4 id : #rectangle-color-4
//  rectangle 5 id : #rectangle-color-5
//  rectangle 6 id : #rectangle-color-6
//  rectangle 7 id : #rectangle-color-7
//  rectangle 8 id : #rectangle-color-8
//  rectangle 9 id : #rectangle-color-9
//  rectangle 10 id : #rectangle-color-10