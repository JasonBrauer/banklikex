# Bank Like X
## Problem
Many questions within the commercial lending space take the form “What is X for a bank like us?”  
For example:  
- “What is the average loan-to-value ratio on a typical owner-occupied real estate loan, for banks
like us?”
- “What is the average rate on a typical 5-year term, owner-occupied real estate loan, for banks
like us?”  

To answer these questions, we need to be able to identify a group of banks that are “like” a given
bank. We use a combination of our own data and publicly available data (such FDIC data found
[here](https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx)). We would like to see your solution to
this problem. We would like you to solve the “banks like this one” problem.

## Questions
1. Where would you start? What information do you wish you had? In the absence of perfect
knowledge and access to perfect data, what can you do to make a first attempt?  
<span style="color:orange">
I would start by getting familiar with the data set. Understanding the dataset provides a lot of insight into the scope of the project. You can immediately get an idea of how much effort it will take to import can clean the data set. You can also being to formulate some ideas on how you will break it down into some sort of model allowing for easy interaction and analysis.  
&nbsp;  
I wish I had more information and knowledge about many of the parameters in the data set. The data set referenced in the problem has a lot of detail about bank activities and standings. However, not being familiar with the banking industry means many of those parameters aren't meaningful to me personally. As a first pass and to create a reasonable scope for the project, I focused in a a few paremters from common sources such as the balance sheet and income statement. That way I was either more familiar with the parameters or I could easily look up their meaning.  
</span>

2. Now do it. Build a model that classifies banks. Explain the steps you took and the decisions you
made along the way, as if you were leaving notes for the next person who might tackle this problem.  
<span style="color:orange">
I first started by importing and cleaning up the data set. It was important to get the data set into a model that I could quickly use regardless of how I was going to analyze it. First I focused on making sure to include any useful bank identifiers in the model. That is why I included unique identifers such is idrssd as well as the bank name and address. 
</span> 

    ```
    class CallData():
    """
    Structure to hold data from FFEIC call data summaries
    """

    def __init__(self):
        self.period = None
        self.idrssd = None
        self.fdic = None
        self.bank_name = None
        self.address = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.field_dict = None
    ```
    <span style="color:orange">
    Aside from the unique bank identifiers, I wanted to make sure the parameters used to compare banks was flexible within the program. That way if I discovered better paremeters after interacting with the data for a longer period of time, I could quickly include them in the analysis. Therefore, I included a dictionary of fields in the data model so new fields could easily be added. The call data field dict variable within the model determines which fields should be used in the bank comparison.  
    </span>   
    
    ```
    call_data_field_dict = {
    "RCON2170" : "TOTAL ASSETS",
    "RCON2948" : "TOTAL LIABILITIES",
    "RIAD4010" : "INTEREST AND FEES ON LOANS"
    }
    ```
    <span style="color:orange">
    Next, I needed to figure out how I was going to analyze the various parameters for each bank to determine if one was like another. An idea that popped into my mind early on was to create a probability density function for each parameter across all the banks. I could then determine a which percentile a specific parameter fell in for a specified bank. From there, I could compare the same parameter for all the other banks to understand whether the parameter's value was around the same location in the distribution as the specified bank. I could then repeat that process for however many parameters I wanted to compare. Finally, I could determine which banks had all their parameter values similar to the specified bank. 
    </span>

    &nbsp;
    
    INSERT PROB DIST IMAGE HERE

    <span style="color:orange">
    Unfortunately, with so many different parameters and the desire to be flexible in which parameters were used, I couldn't be tied to any few probability distribution shapes. I would also have to implement complicated logic to figure out which shape applied to a certain parameter. Being time consuming both for implementation computation, I started searching for another method. After a bit of searching I found that a cumulative distribution function (cdf) could also easily provide a percentile associated with a certain parameter value. There was also the option to build an empirically defined cdf. Therefore, needing to understand the shape of a distribution was no longer as critical and the logic could be significantly simplified. 
    </span>
    
    &nbsp;
    
    INSERT CUML DIST IMAGE HERE

3. Now that you’re done, suppose a co-worker is eager to use your results & ideas in our business,
starting immediately. What would you advise and why?  
<span style="color:orange">
I would advise against using the results in the business immediately. First, the system built to perform the analysis wasn't built with production intent. Unit and integration tests need to be added to validate functions and the program as a whole. Second, the results ideally would be validated by another expert and against a different dataset to sure they are not biased or skewed in any way. 
</span>

4. When should your solution NOT be used?  
<span style="color:orange">
The solution should not be used before its written with production intent and validated.
</span>

5. If you had more time and resources, what would you do next, to improve or refine your work?  
<span style="color:orange">
First, I would take more time to understand a larger number of the parameters in the dataset. Ideally I would find an independent group that tend to not take the same distribution shape. Therefore, each parameter would represent a distinct aspect of the bank and be relatively indepenent of other bank characteristics. Second, I would research a wider variety of methods to solve the bank like x problem. Given the short timeline to complete this assignement, I found it more useful to produce something with reasonable results than diving deep into finding the ideal solution to the problem.  
</span>

6. Tell us what you think of this homework assignment. What would you do differently, if you were
designing it?  
<span style="color:orange">
I felt the assignment was meaningful and interesting. At first it was overwhelming to be working with such a vast data set I knew little about. However, that is a realistic scenario for a lot of data analysis work. It also forced me to scope my work so that I could both produce something meaningful, while meeting a relatively short timeline. 
&nbsp;  
If I were designing the problem, I might provide a dataset that would be easier to interact with. On one hand, data ingestion is part of the problem and is a necessary skill. On the other hand, I spent a lot of time working the data into a model that I could easliy use to run an analysis. That said, I'm sure there are better libraries and simpler ways to accomplish the data ingestion and cleanup task. 
</span>

    