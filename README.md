# workorderManagementSystem

<h3>What?</h3>

This program was developed to be used in a building maintenance setting. The user can create and track repair workorders. Future updates can include 
cost forecasting, flagging repeat units (potential trouble tennants), or track/remind of yearly maintenance. 


<h3>Why?</h3>

This project was written as a final assignment for semester 4 of computer programming and analysis for George Brown College (GBC). It is for
the open source course (look at this public repo WOW!) and is written entirely using Python.

<h3>The Design</h3>

For this assignment I decided to use model-view-controller(MVC) for organizing the files and how they work with each other. I use Object Orientated Programming (OOP) and have a database using the sqlite3 library within python to save all of the changes locally. It is a simple program that takes user input through a GUI form (using the tkinter library) and then I take those fields and insert them into the database. Originally I started writing the program to just be a console app, but figured I need more GUI projects for my portfolio so ended up deleting some console-specific classes. To my suprise, using sqlite3 was very pain free. First time using it outsite of a lab. 

<h1>SET UP</h1>

This program requires an external library called tkcalendar. So, there is a requirements.txt to help with installing the package

To set up:<br>
1. Clone this repository.<br>
2. Navigate to the project directory. With bash for example. <br>
3. Run the command 'pip install -r requirements.txt'.<br>
4. Run the program from the main.py file.<br>
5. Enjoy the program 🙃<br>
