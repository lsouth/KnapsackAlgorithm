# KnapsackAlgorithm

September 9:  KIRA 

After finally understanding the ins and outs of the knapsack algorithm, I began coding the actual algorithm. 
I went through the process of all the possible options and wrote out psuedo code, which allowed me to work out
some things with the creation of the table and how to format the algorithm to backtrack through it. Because I 
understood the process, the biggest problem that I had to overcome was learning the python code that
would support the algorithm. In a language I was more comfortable with, I could probably have finished it 
considerably faster, as I was forgetting how to do simple things like for loops. 

September 12: KIRA

I've submitted the final knapsack algorithm code. Overall, I've been testing the speed and it is not as good as
I would prefer, especially since I am currently only testing it with a smaller file size, when I would like it 
to be optimized enough to handle data sizes of up to around 1000. However, with the big O complexity, I am unsure 
of how you would go about creating a matrix at less than n^2 complexity, since a matrix in it's very definition
is n by n. I will continue to work on optimizing the structure. 

October 3: KIRA

After working on the generator for a bit, I've submitted a rough version of a generator that we can use to create 
bigger probelem sets so that our complexity can be tested at a higher and more strenous level to test the limits 
of our program. Unfortuantely, I was unable to find a solution that correctly used the newline character as a 
way to actually create a new line, instead of just prining out /n. I will continue to work on this.

October 14: Laura

Today I fixed the Generator file so that it produces a .json file with the traditional formatting. I tested it with our knapsack.py and it runs successfully! I will try to get the timing done today as well, now that the generator can be used to create large files.

After looking at the timing data, I think we have a bug somewhere in our backtracking algorithm. The program is spending virtually no time in that method, compared to the time spent constructing the table. Additionally, the program isn't returning accurate solutions to the larger problems (the value of the selected items is not equal to the optimum calculated when building the table), so we will have to look into that this week. 

I also made a slight alteration to our expected JSON format. Before we were using the format 

[{"capacity": maxWeight} , {"value_i": "weight_i", "value_i+1": "weight_i+1", ... }] which was fine on small problems but caused issues with big problems. Dicts cannot have duplicate keys so when we were creating the random problems it would create override any duplicate "value_i"s so the end result would have fewer pairs that expected. To fix this, I changed to using this format:

[{"capacity": maxWeight} , {1 : [value_1 , weight_1] , 2 : [value_2 , weight_2] , ... }] which ensures that there will be no duplicate keys. 

October 20: Laura

I found the bug that was preventing us from properly backtracking in larger files! We were one off on the indexing in the backtracking function. I also updated times.txt with the new data!

October 22: Kira

I went through the knapsack algorithm code, and added in comments to better explain the code to someone who might
not be as familiar with it. This also helped me further my understanding of the code, since the one that I initially wrote
had a bit of a different structure than Laura's. I also created more test files (2000, 3000, 4000, and 100000 pairs) to use
to plot the complexity of our code. The graph I constructed then went into the report to help the visualization of the
effect that increasing the number of pairs has on our code.

November 1: Laura

I made quite a bit of progress tonight on the recursive space-efficient implementation of the Knapsack algorithm. I wrote code to build the small tables, select the proper cut points, and recurse accordingly. I'm still having some trouble getting the algorithm to actually select the right element, but I think that I completed a lot of the necessary helper functions. 

November 13: Kira
I updated the report to include how I worked to best understand the algorithm before I starting coding by including my process. I also expanded on an explanation of the graph provided from the dynamic programming approach, and added in another section to explain how we both felt about how the honors option expirience, and what worked well and what could be improved. We still need to measure the memory of both implementations to prove that the new algorithm is improved. 


