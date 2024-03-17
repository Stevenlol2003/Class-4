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
grader = otter.Notebook("p6.ipynb")

# + deletable=false editable=false
import p6_test

# + [markdown] deletable=false editable=false
# # Project 6: Airbnb

# + [markdown] deletable=false editable=false
# ## Learning Objectives:
#
# In this project, you will demonstrate how to:
#
# * access and utilize data in CSV files,
# * process real world datasets,
# * use string methods and sorting function / method to order data.
#
# Please go through [Lab-P6](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p6) before working on this project. The lab introduces some useful techniques related to this project.

# + [markdown] deletable=false editable=false
# ## Testing your code:
#
# Along with this notebook, you must have downloaded the file `p6_test.py`. If you are curious about how we test your code, you can explore this file, and specifically the value of the variable `expected_json`, to understand the expected answers to the questions.

# + [markdown] deletable=false editable=false
# ## Project Description:
#
# Data Science can help us understand user behavior on online platform services. This project is about the rooms listed on Airbnb. Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present a more unique, personalized way of experiencing the world. `airbnb.csv` has data of nearly 50,000 listings on Airbnb from New York City, NY from the year 2019. This file includes a lot of information about the hosts, geographical availability of the listings, and other necessary metrics to make predictions and draw conclusions. You will be using various string manipulation methods that come with Python as well as creating some of your own functions to solve the problems posed. Happy coding!

# + [markdown] deletable=false editable=false
# ## Dataset:
#
# A small portion of the dataset `airbnb.csv` you will be working with for this project is reproduced here:

# + [markdown] deletable=false editable=false
# room_id|name|host_id|host_name|neighborhood_group|neighborhood|latitude|longitude|room_type|price|minimum_nights|number_of_reviews|last_review|reviews_per_month|calculated_host_listings_count|availability_365
# ------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
# 2539|Clean & quiet apt home by the park|2787|John|Brooklyn|Kensington|40.64749000000001|-73.97237|Private room|149|1|9|2018-10-19|0.21|6|365
# 2595|Skylit Midtown Castle|2845|Jennifer|Manhattan|Midtown|40.75362|-73.98376999999998|Entire home/apt|225|1|45|2019-05-21|0.38|2|355
# 3647|THE VILLAGE OF HARLEM....NEW YORK !|4632|Elisabeth|Manhattan|Harlem|40.80902|-73.9419|Private room|150|3|0|||1|365
# 3831|Cozy Entire Floor of Brownstone|4869|LisaRoxanne|Brooklyn|Clinton Hill|40.68514|-73.95976|Entire home/apt|89|1|270|2019-07-05|4.64|1|194
# 5022|Entire Apt: Spacious Studio/Loft by central park|7192|Laura|Manhattan|East Harlem|40.79851|-73.94399|Entire home/apt|80|10|9|2018-11-19|0.1|1|0
# 5099|Large Cozy 1 BR Apartment In Midtown East|7322|Chris|Manhattan|Murray Hill|40.74767|-73.975|Entire home/apt|200|3|74|2019-06-22|0.59|1|129

# + [markdown] deletable=false editable=false
# You can find more details on the dataset in [Lab-P6](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p6).

# + [markdown] deletable=false editable=false
# ## Questions and Functions:
#
# Let us start by importing all the modules we will need for this project.

# + tags=[]
# it is considered a good coding practice to place all import statements at the top of the notebook
# please place all your import statements in this cell if you need to import any more modules for this project
import csv


# + [markdown] deletable=false editable=false
# #### Now, copy and paste the `process_csv` and `cell` functions from your Lab-P6 notebook to the cell below.
#
# You are expected to call the `process_csv` function correctly, and read the data on `airbnb.csv`. After reading the file, define the `csv_header`, and `csv_rows` variables as in Lab-P6, and define the `cell` function.
#
# **Important:** You **must** only use the `cell` function to extract data from the dataset. If you extract any data without explicitly using this function, you will **lose points** during manual review. It is recommended but **optional** that you use the `cell_v2` function defined in Lab-P6. However, you **must** rename the function to `cell` in this notebook. 

# + tags=[]
def process_csv(filename):
    example_file = open(filename, encoding="utf-8")
    example_reader = csv.reader(example_file)
    example_data = list(example_reader)
    example_file.close()
    return example_data

csv_data = process_csv("airbnb.csv")
csv_header = csv_data[0]
csv_rows = csv_data[1:]

def cell(row_idx, col_name):
    col_idx = csv_header.index(col_name)
    val = csv_rows[row_idx][col_idx]
    if val == "":
        return None
    elif col_name == 'price':
        val = int(val)
    elif col_name == 'reviews_per_month':
        val = float(val)
    return val


# + [markdown] deletable=false editable=false
# **Question 1:** What **unique** neighborhood groups (`neighborhood_group`) are included in the dataset?
#
# Your output **must** be a *list* which stores all the **unique** neighborhood groups (i.e., without any duplicates). The order **does not** matter.

# + tags=[]
# compute and store the answer in the variable 'neighborhood_groups', then display it
neighborhood_groups = []

for index in range(len(csv_rows)):
    if cell(index, "neighborhood_group") not in neighborhood_groups:
        neighborhood_groups.append(cell(index, "neighborhood_group"))  
        
neighborhood_groups

# + deletable=false editable=false
grader.check("q1")

# + [markdown] deletable=false editable=false
# **Question 2:** What is the **average** `price` of all rooms in the dataset?

# + tags=[]
# compute and store the answer in the variable 'avg_price', then display it
total_price = 0
count = 0

for index in range(len(csv_rows)):
    total_price += cell(index, "price")
    count += 1
    
avg_price = total_price / count            
avg_price

# + deletable=false editable=false
grader.check("q2")

# + [markdown] deletable=false editable=false
# **Question 3:** How many rooms are in the `neighborhood` of *SoHo*?

# + tags=[]
# compute and store the answer in the variable 'count_soho', then display it
count_soho = 0

for index in range(len(csv_rows)):
    if cell(index, "neighborhood") == "SoHo":
        count_soho += 1

count_soho

# + deletable=false editable=false
grader.check("q3")


# + [markdown] deletable=false editable=false
# ### Function 1: `find_room_names(phrase)`
#
# We require you to complete the below function and use it to answer question 4 to 6  
# (this is a **requirement**, and you will **lose points** if you do not implement this function). You can review string methods from the [lecture on Feb 24](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-lecture-material/-/blob/main/s23/Common_to_all_lectures/13_Strings/13_Strings.pdf)

# + tags=[]
def find_room_names(phrase):
    """
    find_room_names(phrase) returns a list of all the room names that CONTAINS the 
    substring (case insensitive match) `phrase`.
    """
    room_list = []
    for index in range(len(csv_rows)):
        if (cell(index, "name") == None):
            continue
        else:
            if cell(index, "name").lower().find(phrase) != -1:
                room_list.append(cell(index, "name"))
                
    return room_list
    # TODO: create an empty list
    # TODO: ignore rooms that do not have data entry for name, as indicated by a value of None
    # TODO: check if the room name string contains phrase (case insensitive match)
    # TODO: if so, add these room names to the list (the room names should be as in the dataset)
    # TODO: return your list of room names


# + [markdown] deletable=false editable=false
# **Question 4:** Find all room names that contain the string `"free wifi"`.
#     
# Your output **must** be a *list*. The order **does not** matter. You **must** call the `find_room_names` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'rooms_free_wifi', then display it
rooms_free_wifi = find_room_names("free wifi")

rooms_free_wifi

# + deletable=false editable=false
grader.check("q4")

# + [markdown] deletable=false editable=false
# **Question 5:** Find all room names that contain **either** `"cinema"` **or** `"film"`.
#
# Your output **must** be a *list*. The order **does not** matter, but if a room's `name` contains **both** `"cinema"` and `"film"`, then the room must be included **only once** in your list. You **must** call the `find_room_names` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'rooms_contain_cinema_film', then display it
rooms_contain_cinema = find_room_names("cinema")
rooms_contain_film = find_room_names("film")

cinema_and_film = rooms_contain_cinema + rooms_contain_film

rooms_contain_cinema_film = []
for name in cinema_and_film:
    if name not in rooms_contain_cinema_film:
        rooms_contain_cinema_film.append(name)

rooms_contain_cinema_film

# + deletable=false editable=false
grader.check("q5")

# + [markdown] deletable=false editable=false
# **Question 6:** Find the **longest** room `name` that contains the word `"fun"`.
#
# There is a **unique** such room with the longest `name`, so you **do not** have to worry about breaking ties. You **must** call the `find_room_names` function to answer this question. You **must** initialize the variable `funnest_room` to be `None`.

# + tags=[]
# compute and store the answer in the variable 'funnest_room', then display it
funnest_room = None
possible_rooms = find_room_names("fun")
for i in range(len(possible_rooms)):
    if funnest_room == None:
        funnest_room = possible_rooms[i]
    else:
        if len(possible_rooms[i]) > len(funnest_room):
            funnest_room = possible_rooms[i]

funnest_room

# + deletable=false editable=false
grader.check("q6")

# + [markdown] deletable=false editable=false
# **Question 7:** Find the names (`name`) of all the rooms which have `price` *0* and have **more than** *90* reviews (`number_of_reviews`).
#
# Your output **must** be a *list*. The names **must** be sorted in **ascending (alphabetical) order**.

# + tags=[]
# compute and store the answer in the variable 'no_cost_rooms', then display it
no_cost_rooms = []

for index in range(len(csv_rows)):
    if cell(index, "price") == 0:
        if cell(index, "number_of_reviews") == None:
            continue
        else:  
            if int(cell(index, "number_of_reviews")) > 90:
                no_cost_rooms.append(cell(index, "name"))

no_cost_rooms.sort()
no_cost_rooms

# + deletable=false editable=false
grader.check("q7")

# + [markdown] deletable=false editable=false
# **Question 8:**  What neighborhoods (`neighborhood`) are the rooms that have `price` greater than *9999* located in?
#
# Your output **must** be a *list* of **unique** neighborhoods (i.e., without any duplicates). The names **must** be sorted in **descending (reverse-alphabetical) order**.

# + tags=[]
# compute and store the answer in the variable 'pricey_neighborhoods', then display it
pricey_neighborhoods_with_duplicates = []
pricey_neighborhoods = []

for index in range(len(csv_rows)):
    if cell(index, "price") > 9999:
        pricey_neighborhoods_with_duplicates.append(cell(index, "neighborhood"))
        
for name in pricey_neighborhoods_with_duplicates:
    if name not in pricey_neighborhoods:
        pricey_neighborhoods.append(name)
        
pricey_neighborhoods.sort(reverse=True)

# + deletable=false editable=false
grader.check("q8")

# + [markdown] deletable=false editable=false
# **Question 9:** How many rooms received their `last_review` **in or before** *2015*?
#
# You should **ignore** rooms for which the `last_review` data is missing.
#
# **Hint:** You can find the date of the last review in the `last_review` column.  
# You can review the get_year function from [lab-p5](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p5)

# + tags=[]
# compute and store the answer in the variable 'last_review_before_2015', then display it
last_review_before_2015 = 0

for index in range(len(csv_rows)):
    last_review = cell(index, "last_review")
    if last_review == None:
        continue
    elif int(last_review[:4]) <= 2015:
        last_review_before_2015 += 1

last_review_before_2015

# + deletable=false editable=false
grader.check("q9")


# + [markdown] deletable=false editable=false
# ### Function 2: `avg_price_per_room_type(room_type, neighborhood)`
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function).

# + tags=[]
def avg_price_per_room_type(room_type, neighborhood):
    '''
    avg_price_per_room_type(room_type, neighborhood) returns the average price of 
    rooms of the type `room_type` in the given `neighborhood`; if there are no
    rooms of the type `room_type` in the given `neighborhood`, it returns `None`
    '''
    total_price = 0
    count = 0
    
    for index in range(len(csv_rows)):
        if cell(index, "room_type") == room_type and cell(index, "neighborhood") == neighborhood:
            total_price += cell(index, "price")
            count += 1
    
    avg_price = total_price / count
    return avg_price


# + [markdown] deletable=false editable=false
# **Question 10:** What is the  **average** `price` of a *Private room* (`room_type`) in the`neighborhood` *Little Neck*?
#
# You **must** call the `avg_price_per_room_type` function to answer this question.
#
# **Hint:** To help you debug your code in case you run into any bugs, we have reproduced in the cell below, **all** the rows in the dataset from the `neighborhood` *Little Neck*. If you run into bugs with `avg_price_per_room_type`, it is recommended that you go through your code and verify that it does what it is supposed to, for this tiny dataset.

# + [markdown] deletable=false editable=false
# room_id|name|host_id|host_name|neighborhood_group|neighborhood|latitude|longitude|room_type|price|minimum_nights|number_of_reviews|last_review|reviews_per_month|calculated_host_listings_count|availability_365
# ------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
# 20227428|Douglaston Apartment Room A|18996093|Leonard|Queens|Little Neck|40.75794000000001|-73.72955999999998|Private room|45|1|12|2019-06-22|0.55|5|133
# 21025083|Douglaston (apt 2) Room one\n(Largest room)|18996093|Leonard|Queens|Little Neck|40.75777|-73.72949|Private room|50|1|6|2018-12-16|0.31|5|94
# 30325639|Cozy shared studio in a safe neighborhood|21495656|Ramy|Queens|Little Neck|40.76212|-73.71928|Shared room|32|3|1|2018-12-04|0.14|1|88
# 31553066|Near major transportation|41090359|Abi|Queens|Little Neck|40.77122|-73.738|Private room|100|1|0|||1|88
# 35515780|30-min to Manhattan Quiet Big House in Great Neck|31859704|Vincent|Queens|Little Neck|40.77444000000001|-73.73373000000002|Entire home/apt|149|3|0|||1|3

# + tags=[]
# compute and store the answer in the variable 'pvt_room_little_neck', then display it
pvt_room_little_neck = avg_price_per_room_type("Private room", "Little Neck")

pvt_room_little_neck

# + deletable=false editable=false
grader.check("q10")

# + [markdown] deletable=false editable=false
# **Question 11:** On average, how much **more** expensive (`price`) is a *Entire home/apt* (`room_type`) than a *Private room* (`room_type`) in the `neighborhood` *Astoria*?
#
# You **must** call the `avg_price_per_room_type` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'home_pvt_room_astoria_diff', then display it
home_pvt_room_astoria_diff = avg_price_per_room_type("Entire home/apt", "Astoria") - avg_price_per_room_type("Private room", "Astoria")

home_pvt_room_astoria_diff

# + deletable=false editable=false
grader.check("q11")


# + [markdown] deletable=false editable=false
# ### Function 3: `find_prices_within(lat_min, lat_max, long_min, long_max)` 
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function).

# + tags=[]
def find_prices_within(lat_min, lat_max, long_min, long_max):
    """
    find_prices_within(lat_min, lat_max, long_min, long_max) returns an unordered 
    list of prices of all the rooms within the geographical location between and including
    the latitudes lat_min and lat_max and longitudes long_min and long_max.
    """
    prices = []
    
    for index in range(len(csv_rows)):
        if lat_min <= float(cell(index, "latitude")) and float(cell(index, "latitude")) <= lat_max and long_min <= float(cell(index, "longitude")) and float(cell(index, "longitude")) <= long_max:
            prices.append(cell(index, "price"))
    
    return prices


# + [markdown] deletable=false editable=false
# **Question 12:** What is the **lowest** `price` room near *NYU* (`40.729 <= latitude <= 40.73, -74.01 <= longitude <= -74.00`)?
#
# You **must** call the `find_prices_within` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'min_price_nyu', then display it
all_prices_nyu = find_prices_within(40.729, 40.73, -74.01, -74.00)
min_price_nyu = min(all_prices_nyu)

min_price_nyu

# + deletable=false editable=false
grader.check("q12")


# + [markdown] deletable=false editable=false
# ### Function 4: `median(items)` 
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function).
# You may copy/paste this function from your Lab-P6 notebook.

# + tags=[]
def median(items):
    """
    median(items) returns the median of the list `items`
    """
    items.sort()
    length = len(items)
    median = 0;
    if length % 2 == 1:
        median = items[int(length / 2)]
    else: 
        median = (items[length / 2] + items[length / 2 - 1]) / 2
        
    return median
    # you may copy/paste this function from your Lab-P6 notebook


# + [markdown] deletable=false editable=false
# **Question 13:** What is the **median** `price` of the rooms near *Columbia University* (`40.79 <= latitude <= 40.80, -73.96 <= longitude <= -73.95`)?
#
# You **must** call the `find_prices_within` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'median_price_columbia', then display it
price_columbia = find_prices_within(40.79, 40.80, -73.96, -73.95)
price_columbia
median_price_columbia = median(price_columbia)

median_price_columbia

# + deletable=false editable=false
grader.check("q13")

# + [markdown] deletable=false editable=false
# **Question 14:** What **percentage** of rooms near *Rockefeller Center* (`40.749 <= latitude <= 40.75, -73.98 <= longitude <= -73.97`) have a `price` **more than** *100*?
#
# Your answer **must** be a *float* value between *0* and *100*. You **must** call the `find_prices_within` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'pct_price_over_hundred', then display it
price_rockefeller = find_prices_within(40.749, 40.75, -73.98, -73.97)

total = len(price_rockefeller)
count = 0;

for index in range(total):
    if price_rockefeller[index] > 100:
        count += 1
        
pct_price_over_hundred = float(count / total * 100)

pct_price_over_hundred

# + deletable=false editable=false
grader.check("q14")


# + [markdown] deletable=false editable=false
# ### Function 5: `avg_review_avail_ratio(neighborhood)` 
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function).  
#
# $$\text{Ratio of number of reviews and availability =} \frac{\texttt{number_of_reviews}}{\texttt{availability_365}}$$
#   
# In this function, we want to compute the **average ratio** of `number_of_reviews` and `availability_365` in a `neighborhood`.
#
# You **must** **ignore** rooms that have `availability_365` data of 0.  
# You **must** also **ignore** rooms for which the ratio cannot be computed due to **missing data** (i.e., either the numerator or denominator is **missing**).
#
# **For example**, Let's consider a sample dataset which only has two rooms, and we want to compute the average ratio of `number_of_reviews` and `availability_365` in *Jamaica*
#
# `name`|`number_of_reviews`| `availability_365`|`neighborhood`
# ------|------|------|------|
# room_one| 4 | 200| Jamaica
# room_two| 200| 20 |Jamaica
#
#
# 1. Compute the ratio for each of the room in the `neighborhood` *Jamaica*: 
#
#     review-availability ratio for room_one = 4 / 200 = 0.02.
#     
#     review-availability ratio for room_two = 200 / 20 = 10. 
#     
# 2. Calculate the average between the two ratios:
#    $$\texttt{average_review_availability} \text{ in Jamaica} = \frac{0.02 + 10}{2} = 5.01.$$
#    
# **Hints:**
# 1.  The denominator is the availability of a room (`availability_365`). The numerator is the number of reviews of a room (`number_of_reviews column`). 
# 2.  Be careful! You need to compute the ratio for each room in the given neighborhood, then take the average of those ratios. Simply dividing the sum of reviews by the sum of availability will calculate the wrong answer.

# + tags=[]
def avg_review_avail_ratio(neighborhood):
    """
    avg_review_avail_ratio(neighborhood) returns the average of the ratios of 
    number of reviews to availability of all rooms in the `neighborhood`;
    If there are no rooms in the `neighborhood` for which the ratio can
    be computed, then the function returns `None`
    """
    total_ratio = 0
    count = None
    for index in range(len(csv_rows)):
        if cell(index, "neighborhood") == neighborhood:
            if int(cell(index, "availability_365")) == 0:
                continue
            if cell(index, "number_of_reviews") == None or cell(index, "availability_365") == None:
                continue
            else:     
                total_ratio += float(int(cell(index, "number_of_reviews")) / int(cell(index, "availability_365")))
                if count == None:
                    count = 1
                else:    
                    count += 1
                
    if count == None:
        return None
    
    return total_ratio / count

    # TODO: you should **ignore** rooms that have `availability_365` data of 0
    # TODO: you should **ignore** rooms for which the ratio cannot be computed due to missing data
    # Hint: the numerator is the number of reviews of a room (`number_of_reviews column`)
    # Hint: the denominator is the availability of a room (`availability_365` column)
    # Hint: note that you need to compute the average of the ratios, **not** the ratio of the averages.
    #       you must compute the ratio for each room in the `neighborhood`, then take the average of those ratios.
    #       simply dividing the sum of reviews by the sum of availability will calculate the wrong answer.


# + [markdown] deletable=false editable=false
# **Question 15:** What is the **average of the ratios** of the `number_of_reviews` to `availability_365` in the `neighborhood` *Bushwick*?
#
# You **must** call the `avg_review_avail_ratio` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'bushwick_avg_ratio', then display it
bushwick_avg_ratio = avg_review_avail_ratio("Bushwick")

bushwick_avg_ratio

# + deletable=false editable=false
grader.check("q15")

# + [markdown] deletable=false editable=false
# **Question 16:** What is the **average of the ratios** of the `number_of_reviews` to `availability_365` in the `neighborhood` *Manhattan Beach*?
#
# You **must** call the `avg_review_avail_ratio` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'manhattan_beach_avg_ratio', then display it
manhattan_beach_avg_ratio = avg_review_avail_ratio("Manhattan Beach")

manhattan_beach_avg_ratio

# + deletable=false editable=false
grader.check("q16")

# + [markdown] deletable=false editable=false
# **Question 17:** Which `neighborhood` in the `neighborhood_group` *Staten Island* has the **highest average of ratios** of the `number_of_reviews` to `availability_365`?
#
# You **must** **ignore** any `neighborhood` for which the average ratio **cannot be computed**.
#
# **Clarification:** Don't worry about it if this cell takes around 10 seconds to run, that is expected. If it takes much longer (i.e., more than 30 seconds), you **must** optimize your code. Attend office hours if you are unable to get your code to run faster.
#
# **Hint:** You do not need to compute the average of ratios for the **same** `neighborhood` more than once. Make a list of the **unique** neighborhoods in *Staten Island* first, and then find the **highest average of ratios** among those `neighborhoods`.

# + tags=[]
# compute and store the answer in the variable 'max_nbhd_staten_island', then display it
neighborhoods_with_duplicates = []
neighborhoods = []

for index in range(len(csv_rows)):
    if cell(index, "neighborhood_group") == "Staten Island":
        neighborhoods_with_duplicates.append(cell(index, "neighborhood"))
        
for name in neighborhoods_with_duplicates:
    if name not in neighborhoods:
        neighborhoods.append(name)
        
max_nbhd_staten_island = None
highest_avg_ratio = None
for index in range(len(neighborhoods)):
    avg_ratio = avg_review_avail_ratio(neighborhoods[index])
    if avg_ratio == None:
        continue
    else:
        if max_nbhd_staten_island == None and highest_avg_ratio == None:
            max_nbhd_staten_island = neighborhoods[index]
            highest_avg_ratio = avg_ratio
        else: 
            if avg_ratio > highest_avg_ratio:
                highest_avg_ratio = avg_ratio
                max_nbhd_staten_island = neighborhoods[index]
    
max_nbhd_staten_island    

# + deletable=false editable=false
grader.check("q17")


# + [markdown] deletable=false editable=false
# ### Function 6: `find_good_rooms(room_type, neighborhood, number_of_reviews_threshold)`
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function).  
#
# Price, location, room type and number of reviews are metrics that people look into when they book a room in Airbnb. 
# In this function, we want to return a **list** of all the room names (`name`) of the given `room_type` from the given `neighborhood` who have received **at least** `number_of_reviews_threshold` many reviews (`number_of_reviews`), and are **cheaper** than the **average** priced (`price`) room of the given `room_type` from that `neighborhood`.
#
# The order of the **list** does **not** matter. You **must** **ignore** any rooms for which the `price`, `room_type`, `neighborhood`, or `number_of_reviews` data is **missing**. If the average `price` of rooms of the given `room_type` from the given `neighborhood` **cannot be computed** due to missing data, then the function **must** return `None`.
#
# **For example**, let's consider the following small dataset:  
#
# `name`| `price` |`number_of_reviews`|`room_type`|`neighborhood`
# ------|------|------|------|------|
# room_one| 65 | 165| Private room |Jamaica
# room_two| 50 |200| Private room |Jamaica
# room_three| 80| 120| Private room |Jamaica
# room_four| 300| 300| Private room |Jamaica
# room_five| 450| 240| Private room |Jamaica
# room_six| 180| 150| Private room |Jamaica
#
# In this small dataset, we want to find the list of all room names in *Jamaica* of `room_type` *Private room* with **at least** *150* reviews that have a price **lower** than the **average** price of `room_type` *Private room* in *Jamaica*. 
#     
# 1. The **average** `price` of a *Private room* in the `neighborhood` *Jamaica* is:
# $$\frac{65 + 50 + 80 + 300 + 450 + 180}{6} = 187.5.$$  
#
# 2. We can see that there are *4* rooms (`room_one`, `room_two`, `room_three`, and `room_six`) with a `price` **lower** than the **average**, *187.5*. Of these rooms, *3* of them (`room_one`, `room_two`, and `room_six`) also have `number_of_reviews` **at least** *150*.
#
# 3. So, the output should be the **list** `["room_one", "room_two", "room_six"]`.
#
# The `find_good_rooms` function definition **must** invoke the function `avg_price_per_room_type`. **We'll manually deduct points** if you don't use `avg_price_per_room_type`. 

# + tags=[]
def find_good_rooms(room_type, neighborhood, number_of_reviews_threshold=150):
    """
    find_good_rooms(room_type, neighborhood, number_of_reviews_threshold)
    returns a list of room `names` having at least the given `number_of_reviews` 
    that also have a price that is lower than the average price of rooms
    of the same `room_type` from the same `neighborhood`
    """    
    avg_price = avg_price_per_room_type(room_type, neighborhood)
    
    good_rooms = []
    
    for index in range(len(csv_rows)):
        if cell(index, "room_type") == room_type and cell(index, "neighborhood") == neighborhood and cell(index, "price") < avg_price and int(cell(index, "number_of_reviews")) >= number_of_reviews_threshold:
            good_rooms.append(cell(index, "name"))
            
    return good_rooms
    # TODO: use 'avg_price_per_room_type' to find the average `price` of rooms
    #       of the given `room_type` from the given `neighborhood`
    # TODO: create an empty list
    # TODO: add the names of all the rooms of the given `room_type` from the
    #       the given `neighborhood` with `price` lower than the average
    #       and `number_of_reviews` at least the threshold
    # TODO: return the list


# + [markdown] deletable=false editable=false
# **Question 18:** Find a **list** of all the *Entire home/apt* type rooms (`room_type`) in the *Chinatown* `neighborhood` with at least *100* reviews (`number_of_reviews`) that are cheaper than average.
#
# Your answer **must** be a **list**. The order does **not** matter. You **must** call the `find_good_rooms` function to answer this question.

# + tags=[]
# compute and store the answer in the variable 'good_chinatown_rooms', then display it
good_chinatown_rooms = find_good_rooms("Entire home/apt", "Chinatown", 100)

good_chinatown_rooms

# + deletable=false editable=false
grader.check("q18")

# + [markdown] deletable=false editable=false
# **Question 19:** Find a **list** of all the *Private room* type rooms (`room_type`) in the *Harlem* `neighborhood` with $\geq 300$ and $< 500$ reviews (`number_of_reviews`) that are cheaper than average.
#
# Your answer **must** be a **list**. The order does **not** matter. You **must** call the `find_good_rooms` function to answer this question.
#
# **Hint**: Call the `find_good_rooms` function twice with the two different `number_of_reviews_threshold` values, and use these two lists to compute the answer.

# + tags=[]
# compute and store the answer in the variable 'decent_harlem_rooms', then display it
decent_harlem_rooms_300 = find_good_rooms("Private room", "Harlem", 300)

decent_harlem_rooms_500 = find_good_rooms("Private room", "Harlem", 500)

contains_duplicated_names = decent_harlem_rooms_300 + decent_harlem_rooms_500

decent_harlem_rooms = []
    
for room in contains_duplicated_names:
    if contains_duplicated_names.count(room) == 1:
        decent_harlem_rooms.append(room)
        
decent_harlem_rooms

# + deletable=false editable=false
grader.check("q19")


# + [markdown] deletable=false editable=false
# **Question 20:** On a trip to NYC, you need to stay for *3* days in *Queens*, and then *4* days in *Brooklyn*. What is the **minimum** amount of money you need to spend on this trip?
#
# Note that:
# 1. The `price` of each room is for one day, and you'll only stay in one room at each location.
# 2. The total cost = (lowest price in *Queens*) * 3 + (lowest price in *Brooklyn*) * 4.
# 3. You'll need to **skip** those rooms that don't have enough availability, for example, you **must** ignore rooms in *Queens* whose availability is **less than** *3*.
# 4. You'll need to **skip** those rooms for which you don't meet the required number of `minimum_nights`, for example, you **must** ignore rooms in *Brooklyn* whose `minimum_nights` is **greater than** *4*.
# 5. You **must** skip all rooms with any of the relevant data missing.
#
#
# **Hint:** You might want to define a helper function to compute the **minimum** daily `price` of a room in a given `neighborhood_group` among rooms whose `availability_365` is at least the number of days one will be staying in that neighborhood group, and the `minimum_nights` is at most the number of the number of days one will be staying in that neighborhood group.

# + tags=[]
# compute and store the answer in the variable 'min_cost_trip', then display it
def minimum_daily_price(neighborhood_group, days):
    cheapest_per_day = None;
    for index in range(len(csv_rows)):
        if cell(index, "neighborhood_group") == neighborhood_group and int(cell(index, "availability_365")) >= days and int(cell(index, "minimum_nights")) < (days + 1):
            if cheapest_per_day == None:
                cheapest_per_day = cell(index, "price")
            else:
                if cell(index, "price") < cheapest_per_day:
                    cheapest_per_day = cell(index, "price")
    return cheapest_per_day

queens_cost = minimum_daily_price("Queens", 3) * 3

brooklyn_cost = minimum_daily_price("Brooklyn", 4) * 4

min_cost_trip = queens_cost + brooklyn_cost

min_cost_trip

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
# !jupytext --to py p6.ipynb

# + [code] deletable=false editable=false
p6_test.check_file_size("p6.ipynb")
grader.export(pdf=False, run_tests=True, files=["p6.py"])

# + [markdown] deletable=false editable=false
#  
# -




