# Election_Analysis

## Overview of Election Audit

As Data Analysts we are given raw data in many forms. For this project we are given the results of an election in .CSV(comma separated value) format. By utilizing Python code we can import the data from this file and sort this data into an easily readable format. In this project we were able to write code that allowed us to tabulate the results of an election for 3 counties in Colorado, then calculate and print the results of the election and export into a separate .txt file.

## Election-Audit Results

- **How many votes were cast in this congressional election?** 
    
    By utilizing the following code we were able to define a variable as an integer, and begin tracking this value at zero:
    
 ![Initializing Vote Count](https://github.com/MXV0921/Election_Analysis/blob/main/Resources/Initialize_Votes.png)

    
    After defining the variable we added more lines of code to help us to tabulate the total votes counted in the election:
  
  ![Adding Votes](https://github.com/MXV0921/Election_Analysis/blob/main/Resources/Adding_Total_Votes.png)
    
    Further down in our code we used an "F String code" below to print the total votes placed in the data we uploaded:
   ) 
![Printing Votes](https://github.com/MXV0921/Election_Analysis/blob/main/Resources/Election_Totals.png)

After running our full program, the total votes placed in the election was: 369,711
        
- **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**

For us to find this data we first defined a list and a dicionary to allow us to comb through the data and look for the vote totals for each county.  We then used a if statement within a for loop to add the counties to our list and calculate their vote totals.

![Defining County Data](https://github.com/MXV0921/Election_Analysis/blob/main/Resources/Defining_County_Data.png)

After running all the steps in our code, the output in our text file reported:

County Votes:

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

- **Which county had the largest number of votes?

The county with the largest number of votes was Denver County. We were able to produce this data through the following for loop. The image below also contains code to show how we arrived to the County Votes total that we show in the previous paragraph.

![County Images](https://github.com/MXV0921/Election_Analysis/blob/main/Resources/County_Totals_and_Export.png)


- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

As shown in the election_analysis.txt file that we created, our results for the candidates is:


Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)



- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Winner: Diana DeGette

Winning Vote Count: 272,892

Winning Percentage: 73.8%

## Election-Audit Summary

This code is a great format for tallying vote counts.  Voting districts across the entire country all submit the results from their polls and the voters in your state want **accurate results quickly**. Our program minimizes user error in tabulating voting data to produce a clear and concise file that will present a detailed report of an election. 

With some adjustments to our code, we would be able to calculate candidate results for each county.  These results would be beneficial to see a breakdown of how each candidate perfomed on a more local level.

This code would also be beneficial if edited to import a larger and more detailed data file.  Different states, counties, or towns would have different positions on a ballot that may vary, such as mayors, sheriffs or other officials. An actual election would have more items being voted on than just one candidate, but this code gives us a format to build on as we use it in a real world scenario.



