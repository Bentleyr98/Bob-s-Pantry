# Overview

I've always liked database, so I was very interested in how cloud databases work and how I can implement it into my programs. I decided to learn by writing a program for a fictional "Bob's Diner". This program will hold information for their food pantry by showing restock reports, adding new items, using items, and updating quantity. I created a class that's just solely for the database so Bob's Diner will know exactly how much of each item they have and when they need to reorder more.

Writing this program took away some of my nerves of working with cloud databases and learning more about how they can positively impact my future programs I write.

[Software Demo Video](https://www.youtube.com/watch?v=qE_IZszlwkA)

# Cloud Database
I'm using the Google Firestore Database to hold the information for this program.
I'm using each individual collection (table) for each food category to keep it organized. Each document (row) will hold a single food item and each document has specific fields (columns) to keep information on name and quantity.

# Development Environment
Tools
* Google Firestore Database
* Visual Studio Code

Language
* Python

Libraries
* Firestore libraries

# Useful Websites
* [Firestore Tutorial](https://firebase.google.com/docs/firestore)
* [Replit Example Code](https://replit.com/@cmacbeth/CSE310CloudDBWorkshopSolution)

# Future Work
* Make it more flexible and let the user access adding quantity when trying to add a new item.
* Make a loop that'll let the user go back and look at different food category.
* Clean up the menu to make it more consistent with the code and other parts of the program.