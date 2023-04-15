# pands-problem-sheet

Week 1
1: Hello World
2: Project Description
- This project seems to be the first project for newbies into Programming World.
- This project simply outputs the phrase "Hello Word!"

Week 2
1: Bank.py
2: Project Description
- This program convert integer numbers into a decimal number. 
- So first I realized I need to create an input. So I difened the imput as float number.  
- Then I divided the float number per 100, trasforming it to cents, and in the sequence simply added the numbers.
- I tried to find other ways to convert the integer number into decimal, but this way had more sense for me at this moment, but I feel it can be done in another way. 
- The code finishing with the output "Your amount total is " + the value added before. 


Week 3
1: Accounts.py
2: Project Description
- This program read a account of any length and replace the characters with Xs, except the last four digits.
- The first part of the program the user give the input, which will following be divided in two parts. The first part will contain all number, except the last 4 digits. The second part will contain only the last for digits. To do it I used the slicing function in both cases. 
- After the input and slicing, I created a loop o make able that any length of input could be sliced and replaced with Xs.
- The ogic behind this program was on my mind all the time, but at the start I had no idea how to make it actually happen. I took me few hours to find this way, but I got it. 
3: References - Course "python for beginners" at Cork Collee of Comerce (teacher Liam De La Cour) - Which was really helfull, the drive provided by the teacher was used here the most of time, especially for the loop and replacement / https://www.w3schools.com/python/python_strings_slicing.asp  /  https://www.simplilearn.com/tutorials/python-tutorial/python-slicing


Week 4
1: Collatz.py
2: Project Description
- This task asks the user to input any positive integer
- At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
- But if it is odd, multiply it by three and add one. 
- This program has input, loop and output. 
- This task was the easiest one on my opinion, as the loop was able to do the math. 
- If the input is divided by 2 and the result is zero, the program output the loop of all number divided and divided till zero. But is the number is odd, the loop added one and kept diving till it is zero. 
- tho get all output at the same line, searated with space, the function end=" " was used. 
3: References - Course "python for beginners" at Cork Collee of Comerce (teacher Liam De La Cour) / https://www.freecodecamp.org/news/python-do-while-loop-example/#:~:text=What%20is%20a%20while%20loop%20in%20Python%3F&text=A%20while%20loop%20will%20run,check%20the%20condition%20before%20running.


Week 5
1: Weekday.py
2: Project Description
- This project tells which day of the week is. 
- I´ve done this project in one of my classes with teacher Liam. The code import the data from datetime and print which day is today. The output changes if is weekday or weekend using the function while.  
3: References -  Course "python for beginners" at Cork Collee of Comerce (teacher Liam De La Cour)  https://www.datacamp.com/tutorial/python-datetime?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720818&utm_adgroupid=143216588777&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=652967469589&utm_targetid=aud-392016246653:dsa-1947282172981&utm_loc_interest_ms=&utm_loc_physical_ms=1007835&utm_content=dsa~page~community-tuto&utm_campaign=230119_1-sea~dsa~tutorials_2-b2c_3-n-eu_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na&gclid=Cj0KCQjwlumhBhClARIsABO6p-zQLj7JtqLP7jFprmlVOG7bHvKQ0Pqoyekno5eptxMmJOVufKXfR6MaAmSkEALw_wcB 
https://www.programiz.com/python-programming/datetime    
https://docs.python.org/3/library/datetime.html


Week 6
1: Squareroot.py
2: Project Description
- This programm takes a positive floating-point number as input and outputs an approximation of its square root
- This programm takes a number from the input and calculate its square root in a while function.
- The Newton method starts with an initial guess for the square root, and then iteratively improve the guess until it's close enough to the actual value. So each iteration, a new guess is computed by taking the average of the previous guess and the quotient of x divided by the previous guess. 
3: References - Course "python for beginners" at Cork Collee of Comerce (teacher Liam De La Cour)
https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method?utm_content=cmp-true /  https://www.angela1c.com/projects/problem_set_links/problem7/  


Week 7
1: es.py
2: Project Description
- This program reads in a text file and outputs the number of e's it contains.
- To do it, I created an text file "mytext". 
- The program opens this file and reads it. I created a count which start in 0, but using the loop and while function, each time the program reads the letter e in the tex, it adds 1 to the counter. It output the total of the couter. 
3: References - Course "python for beginners" at Cork Collee of Comerce (teacher Liam De La Cour)
https://www.pythontutorial.net/python-basics/python-read-text-file/
https://www.w3schools.com/python/python_file_open.asp



Week 8
1: Plottask.py
2: Project Description
- This program generates a histogram of 1000 values from a normal distribution with a mean of 5 and a standard deviation of 2, and a plot of the function h(x) = x^3 in the range [0, 10]. 
-To do it, first I had to import the numpy and matplotlib.pyplot to generate data and the plot. Then the numpy.random.normal() function is used to generate 1000 values and distribute with a mean of 5 and standard deviation of 2, and stores them in an array called values.
- The histogram is created with the data of the values array using the matplotlib.pyplot.hist() function, which shows the distribution of the data. 
- The program sets the title labels using the matplotlib.pyplot.title(), matplotlib.pyplot.xlabel(), and matplotlib.pyplot.ylabel() functions.
- The program displays the histogram and plot on the same set of axes using the matplotlib.pyplot.show() function.
- This progrmm was hard to myself and I had to do a lot of research and ask few friends for a help, I[m glad it worked out
6: References - https://matplotlib.org/stable/plot_types/index
https://www.w3schools.com/python/matplotlib_pyplot.asp
https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
https://rpubs.com/nishantsbi/Probability_Distribution
https://www.mathworks.com/help/stats/normal-distribution.html
