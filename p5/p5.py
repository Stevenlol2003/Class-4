# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [code] deletable=false editable=false
# import and initialize otter
import otter
grader = otter.Notebook("p5.ipynb")

# + deletable=false editable=false
import p5_test

# +
# PLEASE FILL IN THE DETAILS
# enter none if you don't have a project partner

# project: p5
# submitter: skren
# partner: NETID2
# hours: 2

# + [markdown] deletable=false editable=false
# # Project 5: Investigating Hurricane Data

# + [markdown] deletable=false editable=false
# ## Learning Objectives:
#
# In this project you will demonstrate how to:
# - Write fundamental loop structures,
# - Perform basic string manipulations,
# - Create your own helper functions as outlined in lab-p5.

# + [markdown] deletable=false editable=false
# ## Testing your code:
#
# Along with this notebook, you must have downloaded the file `p5_test.py`. If you are curious about how we test your code, you can explore this file, and specifically the value of the variable `expected_json`, to understand the expected answers to the questions. You can have a look at [p2](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/p2) if you have forgotten how to read the outputs of the `grader.check` function calls.

# + [markdown] deletable=false editable=false
# **Please go through [lab-p5](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p5) before starting this project.** The lab introduces some useful techniques necessary for this project.

# + [markdown] deletable=false editable=false
# ## Project Description:
#
# Hurricanes often count among the worst natural disasters, both in terms of monetary costs, and more importantly, human life. Data Science can help us better understand these storms. For example, take a quick look at this FiveThirtyEight analysis by Maggie Koerth-Baker: [Why We're Stuck With An Inadequate Hurricane Rating System](https://fivethirtyeight.com/features/why-were-stuck-with-an-inadequate-hurricane-rating-system/)
#
# For this project, you'll be analyzing data in the `hurricanes.csv` file. We generated this data file by writing a Python program to extract data from several lists of hurricanes over the Atlantic Ocean on Wikipedia (here is an [example](https://en.wikipedia.org/wiki/2022_Atlantic_hurricane_season)). You can take a look at the script `gen_csv.ipynb` yourself. At the end of the semester, you will be able to write it yourself. 
#
# Start by downloading `project.py`, `p5_test.py`, and `hurricanes.csv` if you haven't already downloaded them. Double check that these files don't get renamed by your browser (by running `ls` in the terminal from your `p5` project directory). 
#
#
# We won't explain how to use the `project` module here (the code in the `project.py` file). Refer to [lab-p5](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p5) to understand how the module works. If necessary, use the `help` function to learn about the various functions inside `project.py`. Feel free to take a look at the `project.py` code, if you are curious about how it works.
#
# This project consists of writing code to answer 20 questions.

# + [markdown] deletable=false editable=false
# ## Dataset:
#
# The dataset you will be working with in this project is linked here [hurricanes](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/p5/hurricanes.csv). Be sure to look at this csv to see what it contains, and specifically what the names of the columns are.
#
# If needed, you can open the `hurricanes.csv` file, to verify answers to simple questions, but you must still have the correct code in your submission!

# + [markdown] deletable=false editable=false
# ## Project Requirements:
#
# You **may not** hardcode indices in your code unless specified in the question. If you hardcode the value of `project.count()`, we'll **manually deduct** points from your autograder score on Gradescope during code review. If you are not sure what hardcoding is, here is a simple test you can use to determine whether you have hardcoded:
#
# *If we were to change the data (e.g. add more hurricanes, or switch the columns or rows) would your code still find the correct answer to the question as it is asked?*
#
# If your answer to that question is *No*, then you have likely hardcoded something. Please reach out to TAs/PMs during office hours to find out how you can **avoid hardcoding**.
#
# **Store** your final answer for each question in the **variable specified for each question**. This step is important because Otter grades your work by comparing the value of this variable against the correct answer.
#
# For some of the questions, we'll ask you to write (then use) a function to compute the answer.  If you compute the answer **without** creating the function we ask you to write, we'll **manually deduct** points from your autograder score on Gradescope, even if the way you did it produced the correct answer. 
#
# Required Functions:
# - `get_month`
# - `get_day`
# - `get_year`
# - `format_damage`
# - `deadliest_in_range`
# - `get_year_total`
#     
# Students are only allowed to use Python commands and concepts that have been taught in the course prior to the release of p5. Therefore, **you should not use concepts/modules such as lists, dictionaries, or the pandas module, to name a few examples**.  We will **manually deduct** points from your autograder score on Gradescope otherwise.
#
# For more details on what will cause you to lose points during code review and specific requirements, please take a look at the [Grading rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/blob/main/p5/rubric.md).

# + [markdown] deletable=false editable=false
# ## Incremental Coding and Testing:
#
# You should always strive to do incremental coding. Incremental coding enables you to avoid challenging bugs. Always write a few lines of code and then test those lines of code, before proceeding to write further code. You can call the `print` function to test intermediate step outputs.
#
# We also recommend you do incremental testing: make sure to run the local tests as soon as you are done with a question. This will ensure that you haven't made a big mistake that might potentially impact the rest of your project solution. Please refrain from making multiple submissions on Gradescope for testing individual questions' answers. Instead use the local tests, to test your solution on your laptop.
#
# That said, it is **important** that you check the Gradescope test results as soon as you submit your project on Gradescope. Test results on Gradescope are typically available somewhere between 2 to 10 minutes after the submission.
#
# Also, remember to check with the [p5 rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/blob/main/p5/rubric.md) to verify that you will not be losing any points during manual review.

# + [markdown] deletable=false editable=false
# ## Project Questions and Functions:

# + tags=[]
# it is considered a good coding practice to place all import statements at the top of the notebook
# please place all your import statements in this cell if you need to import any more modules for this project
import project
# -

# For the first three questions, you do not have to define any of your own functions. Use the `project` module by calling the specific function needed to solve a certain question.
#
# *Please Note*, indexing in python starts from **0**. Therefore, if a question asks you to use a certain value's **index**, do not be confused that with the **location** of the value in the dataset. In our dataset here,
#
# ![table.PNG](attachment:table.PNG)
#
# the **index** for `1804 New England Hurricane` is 0, but the **location** is 1, and the **row number** is 2. Be sure to keep this concept in mind for *all* questions asking for the value at a particular **index**.

# + [markdown] deletable=false editable=false
# **Question 1:** How many hurricanes does the dataset have?

# + tags=[]
# compute and store the answer in the variable 'num_hurricanes'
num_hurricanes = project.count()
# display the variable 'num_hurricanes' here
num_hurricanes

# + deletable=false editable=false
grader.check("q1")

# + [markdown] deletable=false editable=false
# **Question 2:** How many `deaths` were caused by the hurricane at index `315`?

# + tags=[]
# compute and store the answer in the variable 'deaths_315'
deaths_315 = project.get_deaths(315)
# display the variable 'deaths_315' here
deaths_315

# + deletable=false editable=false
grader.check("q2")

# + [markdown] deletable=false editable=false
# **Question 3:** What is the `name` of the hurricane at the `end` of the dataset?
#
# **Hint**: Your code should work even if the number of hurricanes in the dataset were to change. You **must not hardcode** the index of the last hurricane.

# + tags=[]
# compute and store the answer in the variable 'name_last_index'
index = project.count()
name_last_index = project.get_name(index - 1)
# display the variable 'name_last_index' here
name_last_index

# + deletable=false editable=false
grader.check("q3")

# + [markdown] deletable=false editable=false
# **Question 4:** How many hurricanes in the dataset didn't cause any deaths?
#
# **Hint:** Loop through *all* hurricanes and count the hurricanes that has *0* `deaths`.

# + tags=[]
# compute and store the answer in the variable 'zero_death_hurrs'
zero_death_hurrs = 0
indexes = project.count()
for x in range(indexes):
    if project.get_deaths(x) == 0:
        zero_death_hurrs += 1
# display the variable 'zero_death_hurrs' here
zero_death_hurrs

# + deletable=false editable=false
grader.check("q4")

# + [markdown] deletable=false editable=false
# **Question 5:** What is the **fastest** speed (in `mph`) of a hurricane in the dataset?
#
# **Hint**: Look at the q17 and q18 in lab-p5 on finding the maximum/minimum. Here you will have to find the function value of the function `project.get_mph`.

# + tags=[]
# compute and store the answer in the variable 'max_speed'
max_speed = project.get_mph(0)
indexes = project.count()
for x in range(indexes):
    if project.get_mph(x) > max_speed:
        max_speed = project.get_mph(x)
# display the variable 'max_speed' here
max_speed

# + deletable=false editable=false
grader.check("q5")


# + [markdown] deletable=false editable=false
# ### Function 1: `format_damage(damage)`
#
# You will notice if you look at the dataset that the damages caused by the hurricanes are not stored directly as numbers. Instead the damages have a suffix (`"K"`, `"M"`, or `"B"`) attached at the very end. You will have to convert these 'numbers' into integers before you can perform any mathematical operations on them. 
#
# Since you will need to format damages for multiple hurricanes, you **must** create a general helper function that handles the `"K"`, `"M"`, and `"B"` suffixes. Remember that `"K"` stands for thousand, `"M"` stands for million, and `"B"` stands for billion. For example, your function should convert the string `"13.5M"` to `13500000`, `"6.9K"` to `6900` and so on. Note that for **some** hurricanes, the `damage` does **not** have **any** suffixes. For instance, the hurricane `Florence` at index `308` did damage `'0'`. Your function **must** also deal with such inputs, by directly typecasting them to ints. 
#
# This function should take in the strings from the `damage` column as input, and return an **int**. Refer to Task 3.2 in [lab-p5](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p5) to understand how to slice and calculate damage.
#
# **Warning:** Your function `format_damage` must take in the damage as a **string**, and **not** an index. If you code your function to take in the index of a hurricane, and return the damage caused as an int, it will be useful only for this project. To make your function more useful, you must make it accept the damage itself (i.e., a string like `"13.5M"` or `"6.9K"`) as input.

# + tags=[]
def format_damage(damage):
    pass # TODO: replace this with your code
    #TODO: use relevant intermediary variables to simplify your code
    #TODO: check the last character of the string `damage`
    #TODO: type cast the string (except for last character - use appropriate slicing) into a float
    #TODO: use the last character of string to determine what factor to multiply the float with
    #TODO: type cast the final computation to int
    length = len(damage)
    last_char = damage[length - 1]
    if last_char != "K" and last_char != "M" and last_char != "B":
        return int(damage)
    number = float(damage[0:length - 1])
    if last_char == "K":
        return int(number * 1000)
    elif last_char == "M":
        return int(number * 1000000)
    elif last_char == "B":
        return int(number * 1000000000)
    else:
        return int(number)


# + [markdown] deletable=false editable=false
# **Question 6:** What is the `damage` (in dollars) caused by the hurricane named *Igor*?
#
# There is **exactly one** hurricane in this dataset named *Igor*. You **must** exit the loop, and **stop** iterating as soon as you find the hurricane named *Igor*.
#
# You **must** use the `format_damage` function to answer this question. Your answer **must** be an `int`. 

# + tags=[]
# compute and store the answer in the variable 'damage_igor'
index = 0
indexes = project.count()
for x in range(indexes):
    if project.get_name(x) == "Igor":
        index = x
        break
damage_igor = format_damage(project.get_damage(x))
# display the variable 'damage_igor' here
damage_igor

# + deletable=false editable=false
grader.check("q6")

# + [markdown] deletable=false editable=false
# **Question 7:** What is the **total** `damage` (in dollars) caused by all hurricanes named *Karen* in the dataset? 
#
# There are **multiple** hurricanes in this dataset named *Karen*. You must add up the damages caused by all of them. You **must** use the `format_damage` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'total_damage_karen'
total_damage_karen = 0
indexes = project.count()
for x in range(indexes):
    if project.get_name(x) == "Karen":
        total_damage_karen += format_damage(project.get_damage(x))
# display the variable 'total_damage_karen' here
total_damage_karen

# + deletable=false editable=false
grader.check("q7")

# + [markdown] deletable=false editable=false
# **Question 8:** What is the **average** `damage` caused by hurricanes with names starting with the letter *G*?
#
# You should only consider hurricanes whose **first character** is `"G"`. Remember to search for `"G"` and not `"g"`. 

# + tags=[]
# compute and store the answer in the variable 'average_damage_starts_g'
# use relevant intermediary variables to simplify your code
total_damage = 0
count = 0
indexes = project.count()
for x in range(indexes):
    if project.get_name(x)[0] == "G":
        total_damage += format_damage(project.get_damage(x))
        count += 1
average_damage_starts_g = total_damage / count
# display the variable 'average_damage_starts_g' here
average_damage_starts_g

# + deletable=false editable=false
grader.check("q8")

# + [markdown] deletable=false editable=false
# **Question 9:** What is the `name` of the **fastest** hurricane in the dataset?
#
# To break ties (if there are multiple hurricanes with the same speed), you **must** consider the **last** one you find. 
#
# **Hint:** If you find the **index** of the fastest hurricane in `Q9` instead of just the **name** of the hurricane, you can solve `Q10` very easily using the appropriate function from the project module (i.e., without writing a new loop).

# + tags=[]
# compute and store the answer in the variable 'fastest_hurricane'
index_of_fastest_hurricane = 0
indexes = project.count()
for x in range(indexes):
    if project.get_mph(x) >= project.get_mph(index_of_fastest_hurricane):
        index_of_fastest_hurricane = x
fastest_hurricane = project.get_name(index_of_fastest_hurricane)        
# display the variable 'fastest_hurricane' here
fastest_hurricane

# + deletable=false editable=false
grader.check("q9")

# + [markdown] deletable=false editable=false
# **Question 10:** What is the `damage` (in dollars) caused by the **fastest** hurricane (found in `Q9`)?

# + tags=[]
# compute and store the answer in the variable 'fastest_hurricane_damage'
fastest_hurricane_damage = format_damage(project.get_damage(index_of_fastest_hurricane))
# display the variable 'fastest_hurricane_damage' here
fastest_hurricane_damage

# + deletable=false editable=false
grader.check("q10")


# + [markdown] deletable=false editable=false
# ### Functions 2, 3, 4: `get_year(date)`, `get_month(date)`, and `get_day(date)`
#
# Now would be a good time to copy the `get_year`, `get_month`, and `get_day` functions you created in lab-p5 to your project notebook. You will need these functions for the upcoming questions.

# + tags=[]
# copy/paste the get_year, get_month, and get_day functions here from your lab-p5 practice notebook
def get_month(date):
    """get_month(date) returns the month when the date is the in the 'mm/dd/yyyy' format"""
    return int(date[:2])

def get_day(date):
    """get_day(date) returns the dat when the date is the in the 'mm/dd/yyyy' format"""
    return int(date[3:5])

def get_year(date):
    """get_year(date) returns the year when the date is the in the 'mm/dd/yyyy' format"""
    return int(date[6:10])


# + [markdown] deletable=false editable=false
# **Question 11:** What is the `name` of the **earliest** hurricane which caused over *1 billion* dollars in `damages`?
#
# You **must** use the `year` of formation of the hurricane to identify the earliest hurricane. There are **no** other hurricanes in that year which caused over 1 billion dollars in damages, so you do not have to worry about breaking ties.
#
# You need to find the hurricane with the earliest year of formation among those hurricanes with more than 1 billion dollars in damages. You **must not** initialize your variable to be some hurricane which caused less than 1 billion dollars in damages, such as the hurricane at index `0` for example. If you do so, you will find that you are finding the hurricane with the earliest year of formation among the hurricanes with **either** more than 1 billion dollars in damages **or** have index `0`. This is **not** what you are supposed to do.
#
# **Hint:** Take a look at the [lecture notes for February 20](https://canvas.wisc.edu/courses/343490/files/folder/Mikes_Lecture_Notes/lec12_iteration_practice) if you do not remember how to find the maximum/minimum with `None` initialization. You can use `continue` statement to skip top next index in a loop. 

# + tags=[]
# compute and store the answer in the variable 'earliest_billion_dollar_hurr'
earliest_year = None
earliest_billion_dollar_hurr = None
indexes = project.count()
for x in range(indexes):
    if format_damage(project.get_damage(x)) >= 1000000000:
        if earliest_year == None or get_year(project.get_formed(x)) < earliest_year:
            earliest_billion_dollar_hurr = project.get_name(x)
            earliest_year = get_year(project.get_formed(x))
# display the variable 'earliest_billion_dollar_hurr' here
earliest_billion_dollar_hurr

# + deletable=false editable=false
grader.check("q11")

# + [markdown] deletable=false editable=false
# **Question 12:** What is the `name` of the **most recent** hurricane which caused over *100 billion* dollars in `damages`?
#
# You **must** use the `year` of formation of the hurricane to identify the most recent hurricane. There are **no** other hurricanes in that year which caused over 100 billion dollars in damages, so you do not have to worry about breaking ties. You **must not** only use the indices of the hurricanes to determine the most recent hurricane.

# + tags=[]
# compute and store the answer in the variable 'most_recent_100_billion_hurr'
most_recent_year = None
most_recent_100_billion_hurr = None
indexes = project.count()
for x in range(indexes):
    if format_damage(project.get_damage(x)) >= 100000000000:
        if most_recent_year == None or get_year(project.get_formed(x)) > most_recent_year:
            most_recent_100_billion_hurr = project.get_name(x)
            most_recent_year = get_year(project.get_formed(x))
# display the variable 'most_recent_100_billion_hurr' here
most_recent_100_billion_hurr

# + deletable=false editable=false
grader.check("q12")


# + [markdown] deletable=false editable=false
# ### Function 5: `deadliest_in_range(year1, year2)`
#
# This function should take in two years, `year1` and `year2` as its inputs and return the **index** of the hurricane which formed **or** dissipated between `year1` and `year2` and caused the **most** `deaths`. In case of any ties, you must return the index of the **first** hurricane in the dataset with the most deaths.
#
# As in `Q11` and `Q12`, you **must** initialize the variable you use to store the index of the deadliest hurricane as `None`, and update it for the first time only when you come across the first hurricane in the dataset within the year range.

# + tags=[]
def deadliest_in_range(year1, year2):
    """
    deadliest_in_range(year1, year2) gets the index of the deadliest (most deaths) hurricane 
    formed or dissipated within the given year range.
    year1 and year2 are inclusive bounds.

    deadliest_in_range(year1, year2) returns the index of the worst hurricane within the year range.
    """
    index = None
    deaths = None
    indexes = project.count()
    for x in range(indexes):
        if get_year(project.get_formed(x)) >= year1 and get_year(project.get_formed(x)) <= year2:
            if deaths == None or project.get_deaths(x) > deaths:
                index = x
                deaths = project.get_deaths(x)
    return index
        


# + [markdown] deletable=false editable=false
# **Question 13:** How much `damage` (in dollars) was done by the **deadliest** hurricane this century thus far (*2001 to 2023*, both inclusive)?
#
# Your answer **must** be an `int`. 

# + tags=[]
# compute and store the answer in the variable 'damage_by_deadliest_21st_century'
index_of_hurricane = deadliest_in_range(2001, 2023)
damage_by_deadliest_21st_century = format_damage(project.get_damage(index_of_hurricane))
# display the variable 'damage_by_deadliest_21st_century' here
damage_by_deadliest_21st_century

# + deletable=false editable=false
grader.check("q13")

# + [markdown] deletable=false editable=false
# **Question 14:** What was the speed (in `mph`) of the **deadliest** hurricane of the 20th century (*1901 to 2000*, both inclusive)?

# + tags=[]
# compute and store the answer in the variable 'speed_of_deadliest_20th_century'
index_of_hurricane = deadliest_in_range(1901, 2000)
speed_of_deadliest_20th_century = project.get_mph(index_of_hurricane)
# display the variable 'speed_of_deadliest_20th_century' here
speed_of_deadliest_20th_century

# + deletable=false editable=false
grader.check("q14")

# + [markdown] deletable=false editable=false
# **Question 15:** In this century (*2001 to 2022*, both inclusive) how many hurricanes formed on **average**, in the `month` of *October*?
#
# We will leave out the year *2023* since *October* hasn't yet come to pass. Your answer must be a  **float**. You can hardcode month and the range of years for average calculation

# + tags=[]
# compute and store the answer in the variable 'avg_hurricanes_in_oct'
years = 2022 - 2001 + 1
count = 0
indexes = project.count()
for x in range(indexes):
    if get_year(project.get_formed(x)) >= 2001 and get_year(project.get_formed(x)) <= 2022 and get_month(project.get_formed(x)) == 10:
        count +=1
avg_hurricanes_in_oct = float(count / years)       
# display the variable 'avg_hurricanes_in_oct' here
avg_hurricanes_in_oct

# + deletable=false editable=false
grader.check("q15")


# + [markdown] deletable=false editable=false
# ### Function 6: `get_year_total(year)`
#
# This function should take in `year` as its input and return the number of hurricanes that were **formed** in the given `year`.

# + tags=[]
# define the function `get_year_total` here
def get_year_total(year):
    count = 0
    indexes = project.count()
    for x in range(indexes):
        if get_year(project.get_formed(x)) == year:
            count += 1
    return count        


# + [markdown] deletable=false editable=false
# **Question 16:** How many hurricanes were formed in the `year` *2016*?
#
# You **must** answer this question by calling `get_year_total`.

# + tags=[]
# compute and store the answer in the variable 'total_hurricanes_2016'
total_hurricanes_2016 = get_year_total(2016)
# display the variable 'total_hurricanes_2016' here
total_hurricanes_2016

# + deletable=false editable=false
grader.check("q16")

# + [markdown] deletable=false editable=false
# **Question 17:** How many hurricanes were formed in the last `decade` (*2011 to 2020*, both inclusive)?
#
# You **must** answer this question by looping across the years in this decade, and calling the function `get_year_total`.

# + tags=[]
# compute and store the answer in the variable 'total_hurricanes_in_last_decade'
total_hurricanes_in_last_decade = 0
for x in range(2011, 2021):
    total_hurricanes_in_last_decade += get_year_total(x)
# display the variable 'total_hurricanes_in_last_decade' here
total_hurricanes_in_last_decade

# + deletable=false editable=false
grader.check("q17")

# + [markdown] deletable=false editable=false
# **Question 18:** Which `year` in the 20th century (*1901 to 2000*, both inclusive) suffered the **most** number of hurricanes?
#
# You **must** answer this question by calling the function `get_year_total`. You **must** break ties in favor of the most recent year.

# + tags=[]
# compute and store the answer in the variable 'year_with_most_hurricanes'
year_with_most_hurricanes = 1901
num_hurricanes = get_year_total(1901)
for x in range(1901, 2001):
    if get_year_total(x) >= num_hurricanes:
        year_with_most_hurricanes = x
        num_hurricanes = get_year_total(x)
# display the variable 'year_with_most_hurricanes' here
year_with_most_hurricanes

# + deletable=false editable=false
grader.check("q18")

# + [markdown] deletable=false editable=false
# **Question 19:** How many hurricanes lasted across at least 2 *different* `months`?
#
# **Hint:** You can determine if a hurricane lasted across two different months by comparing the month of formation and the month of dissipation of the hurricane. Note that there may be hurricanes which formed late in the year, and dissipated early in the next year.

# + tags=[]
# compute and store the answer in the variable 'multiple_months_hurrs'
multiple_months_hurrs = 0
indexes = project.count()
for x in range(indexes):
    if (get_month(project.get_dissipated(x)) - get_month(project.get_formed(x))) >= 1 or (get_year(project.get_dissipated(x)) - get_year(project.get_formed(x))) >= 1:
        multiple_months_hurrs += 1
# display the variable 'multiple_months_hurrs' here
multiple_months_hurrs

# + deletable=false editable=false
grader.check("q19")

# + [markdown] deletable=false editable=false
# **Question 20:** What is the **average** `damage` caused by the **deadliest** hurricane of each year from *2001 - 2023*, both inclusive?
#
# You **must** use the `deadliest_in_range` function to identify the deadliest hurricane of each year, and you **must** use `format_damage` to convert the `damages` into an `int`. If two hurricanes in a year have the **same** deaths, you must break ties in favor of the hurricane that appears **first** in the dataset.
#
# While calculating the average you **must** only consider the years that had a deadliest hurricane. You **must** **ignore** any years which had no hurricanes in them. 
#
# Your answer must be a  **float**.

# + tags=[]
# compute and store the answer in the variable 'average_damage_deadliest'
total_damage_deadliest = 0
years = 2023 - 2001 + 1
for x in range(2001, 2024):
    index_of_hurricane = deadliest_in_range(x, x)
    if index_of_hurricane == None:
        years -= 1
        continue
    total_damage_deadliest += format_damage(project.get_damage(index_of_hurricane))

average_damage_deadliest = total_damage_deadliest / years
# display the variable 'average_damage_deadliest' here
average_damage_deadliest

# + deletable=false editable=false
grader.check("q20")

# + [markdown] deletable=false editable=false
# ## Submission
# It is recommended that at this stage, you Restart and Run all Cells in your notebook.
# That will automatically save your work and generate a zip file for you to submit.
#
# **SUBMISSION INSTRUCTIONS**:
# 1. **Upload** the zipfile to Gradescope.
# 2. Check **Gradescope otter** results as soon as the auto-grader execution gets completed. Don't worry about the score showing up as -/100.0. You only need to check that the test cases passed.

# + [code]
# running this cell will create a new save checkpoint for your notebook
from IPython.display import display, Javascript
display(Javascript('IPython.notebook.save_checkpoint();'))

# + [code] deletable=false editable=false
# !jupytext --to py p5.ipynb

# + [code] deletable=false editable=false
p5_test.check_file_size("p5.ipynb")
grader.export(pdf=False, run_tests=True, files=["p5.py"])

# + [markdown] deletable=false editable=false
#  
