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
import otter
# nb_name should be the name of your notebook without the .ipynb extension
nb_name = "p8"
py_filename = nb_name + ".py"
grader = otter.Notebook(nb_name + ".ipynb")

# + deletable=false
import p8_test

# +
# PLEASE FILL IN THE DETAILS
# Enter none if you don't have a project partner
# You will have to add your partner as a group member on Gradescope even after you fill this

# project: p8
# submitter: skren
# partner: none

# + [markdown] deletable=false editable=false
# # Project 8: Going to the Movies

# + [markdown] deletable=false editable=false
# ## Learning Objectives:
#
# In this project, you will demonstrate how to:
#
# * integrate relevant information from various sources (e.g. multiple csv files),
# * build appropriate data structures for organized and informative presentation (e.g. list of dictionaries),
# * practice good coding style.
#
# Please go through [Lab-P8](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p8) before working on this project. The lab introduces some useful techniques related to this project.

# + [markdown] deletable=false editable=false
# <h2 style="color:red">Warning (Note on Academic Misconduct):</h2>
#
# **IMPORTANT**: P8 and P9 are two parts of the same data analysis. You **cannot** switch project partners between these two projects. That is if you partner up with someone for P8, you have to sustain that partnership until the end of P9. Now may be a good time to review [our course policies](https://cs220.cs.wisc.edu/s23/syllabus.html).

# + [markdown] deletable=false editable=false
# ## Testing your code:
#
# Along with this notebook, you must have downloaded the file `p8_test.py`. If you are curious about how we test your code, you can explore this file, and specifically the value of the variable `expected_json`, to understand the expected answers to the questions.

# + [markdown] deletable=false editable=false
# ## Introduction:
#
# In this project and the next, we will be working on the [IMDb Movies Dataset](https://www.imdb.com/interfaces/). We will use Python to discover some cool facts about our favorite movies, cast, and directors.
#
# In this project, you will combine the data from the movie and mapping files into a more useful format.
# Start by downloading the following files: `p8_test.py`, `small_mapping.csv`, `small_movies.csv`, `mapping.csv`, and `movies.csv`.

# + [markdown] deletable=false editable=false
# ## The Data:
#
# Open `movies.csv` and `mapping.csv` in any spreadsheet viewer, and see what the data looks like.
# `movies.csv` has ~200,000 rows and `mapping.csv` has ~610,000 rows. These files store information about **every** movie on the IMDb dataset which was released in the US. These datasets are **very** large when compared to `small_movies.csv` and `small_mapping.csv` from [Lab-P8](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p8), but the data is stored in the **same format**. For a description of the datasets, please refer back to [Lab-P8](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/tree/main/lab-p8).
#
# Before we start working with these very large datasets, let us start with the much smaller datasets, `small_movies.csv` and `small_mapping.csv` from Lab-P8. In the latter half of P8 and in P9, you will be working with `movies.csv` and `mapping.csv`. Since the files `movies.csv` and `mapping.csv` are large, some of the functions you write in P8 and P9 **may take a while to execute**. You do not have to panic if a single cell takes between 5 to 10 seconds to run. If any cell takes significantly longer, follow the recommendations below:
#
# - **Do not** call **slow functions** multiple times within a loop.
# - **Do not** call functions that **iterate over the entire dataset within a loop**; instead, call the function before the loop and store the result in a variable.
# - **Do not** compute quantities **inside a loop** if it can be computed outside the loop; for example, if you want to calculate the average of a list, you should use the loop to find the numerator and denominator but divide **once** after the loop ends instead of inside the loop.

# + [markdown] deletable=false editable=false
# ## Project Requirements:
#
# You **may not** hardcode indices in your code, unless the question explicitly asks you to do so. If you open your `.csv` files with Excel, manually count through the rows and use this number to loop through the dataset, this is also considered as hardcoding. If any instances of hardcoding are found during code review, the Gradescope autograder will **deduct** points from your public score.
#
# **Store** your final answer for each question in the **variable specified for each question**. This step is important because Otter grades your work by comparing the value of this variable against the correct answer.
#
# For some of the questions, we'll ask you to write (then use) a function to compute the answer. If you compute the answer **without** creating the function we ask you to write, the Gradescope autograder will **deduct** points from your public score, even if the way you did it produced the correct answer.
#
# Required Functions:
# - `get_mapping`
# - `get_raw_movies`
# - `get_movies`
# - `find_specific_movies`
# - `bucketize_by_genre`
#
# In this project, you will also be required to define certain **data structures**. If you do not create these data structures exactly as specified, the Gradescope autograder will **deduct** points from your public score, even if the way you did it produced the correct answer.
#
# Required Data Structures:
# - `small_movies`
# - `movies`
# - `genre_dict`
#
# You are only allowed to define these data structures **once** and the Gradescope autograder will **deduct** points from your public score if you redefine the values of these variables.
#
# In this project (and the next), you will be asked to create **lists** of movies. For all such questions, **unless it is explicitly mentioned otherwise**, the movies should be in the **same order** as in the `movies.csv` (or `small_movies.csv`) file. Similarly, for each movie, the **list** of `genres`, `directors`, and `cast` members should always be in the **same order** as in the `movies.csv` (or `small_movies.csv`) file.
#
# Students are only allowed to use Python commands and concepts that have been taught in the course prior to the release of P8. Therefore, you should not use the pandas module.  the Gradescope autograder will **deduct** points from your public score otherwise.
#
# In addition, you are also **required** to follow the requirements below:
# - **Do not use the method `csv.DictReader` for P8**. Although the required output can be obtained using this method, one of the learning outcomes of this project is to demonstrate your ability to build dictionaries with your own code.  
# - Additional import statements beyond those that are stated in the directions are not allowed. For this project, we allow you to use `csv` and `copy` packages (that is, you can use the `import csv` and `import copy` statements in your submission). You should not use concepts / modules that are yet to be covered in this course; for example: you should not use modules like `pandas`.
#
# The Gradescope autograder will **deduct** points accordingly, if you don't follow the provided directions.
#
# For more details on what will cause you to lose points during code review and specific requirements, please take a look at the [Grading rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-s23-projects/-/blob/main/p8/rubric.md).

# + [markdown] deletable=false editable=false
# ## Questions and Functions:
#
# Let us start by importing all the modules we will need for this project.
#
#

# + tags=[]
# it is considered a good coding practice to place all import statements at the top of the notebook
# please place all your import statements in this cell if you need to import any more modules for this project
import csv
import copy


# + [markdown] deletable=false editable=false
# ### Function 1: `get_mapping(path)`
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function). You may copy/paste code from your lab-p8 notebook to finish this function.

# + tags=[]
def get_mapping(path):
    """
    get_mapping(path) converts a mapping csv in 'path' 
    into a dict with keys as IDs and values as names
    """
    csv_file = open(path, encoding="utf-8")
    csv_reader = csv.reader(csv_file)
    csv_data = list(csv_reader)
    csv_file.close()
    data = dict()
    for mapping in csv_data:
        key = mapping[0]
        value = mapping[1]
        data[key] = value
    return data

#     TODO: process path
#     TODO: create a dictionary  
#     TODO: iterate through each row of processed path
#     TODO: map value in first column (ID) to value in second column (name/title)


# + [markdown] deletable=false editable=false
# **Question 1:** What is returned by `get_mapping("small_mapping.csv")`?
#
# Your output **must** be a **dictionary** which maps the *IDs* in `small_mapping.csv` to *names*.

# + tags=[]
# compute and store the answer in the variable 'small_mapping', then display it
small_mapping = get_mapping("small_mapping.csv")

small_mapping

# + deletable=false editable=false
grader.check("q1")

# + [markdown] deletable=false editable=false
# **Question 2:** What is the **value** associated with the **key** *nm0503567*?
#
# Your output **must** be a **string**. You **must** use the variable `small_mapping` defined above to answer this question. You **must** not call the function `get_mapping` again on this dataset.

# + tags=[]
# access and store the answer in the variable 'nm0503567_value', then display it
nm0503567_value = small_mapping['nm0503567']

nm0503567_value

# + deletable=false editable=false
grader.check("q2")

# + [markdown] deletable=false editable=false
# **Question 3:** What are the **values** associated with **keys** that **begin** with *nm*?
#
# Your output **must** be a **list** of **strings**. You **must** find **only** the values of the keys that **begin** with *nm*, and **not** the keys that contain *nm*.

# + tags=[]
# compute and store the answer in the variable 'nm_values', then display it
nm_values = []

for key in small_mapping:
    if key[0:2] == 'nm':
        nm_values.append(small_mapping[key])

nm_values

# + deletable=false editable=false
grader.check("q3")

# + [markdown] deletable=false editable=false
# **Question 4:** Find the **keys** of the people (keys **beginning** with *nm*) whose **last name** is *Jones*.
#
# Your output **must** be a **list** of **string(s)**.
#
# **Requirements:** Your **code** must be robust and satisfy all the requirements, even if you were to run this on a larger dataset (such as `mapping.csv`). In particular:
# 1. You will **lose points** if your code would find people whose **first** name or **middle** name is *Jones* (e.g. *Jones Leanardo*, *Carson Jones Daly*).
# 2. You will **lose points** if your code would find people whose **last** name contains *Jones* as a **substring** (e.g. *Catherine Zeta-Jones*). The name should be **exactly** *Jones*. 
# 3. You will **lose points** if your code would find any **movie titles** (e.g. *Jasper Jones*).

# + tags=[]
# compute and store the answer in the variable 'nm_jones', then display it
nm_jones = []

for key in small_mapping:
    if small_mapping[key][-5:] == 'Jones':
        nm_jones.append(key)
        
nm_jones

# + deletable=false editable=false
grader.check("q4")


# + [markdown] deletable=false editable=false
# #### Now, let's move on to reading the movie files!

# + [markdown] deletable=false editable=false
# ### Function 2: `get_raw_movies(path)`
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function).
#
# This function **must** return a **list** of **dictionaries**, where each **dictionary** is of the following format:
#
# ```python
#    {
#         'title': <title-id>,
#         'year': <the year as an integer>,
#         'duration': <the duration as an integer>,
#         'genres': [<genre1>, <genre2>, ...],
#         'rating': <the rating as a float>,
#         'directors': [<director-id1>, <director-id2>, ...],
#         'cast': [<actor-id1>, <actor-id2>, ....]
#     }
# ```
#
# Here is an example:
#
# ```python
#     {
#         'title': 'tt0033313',
#         'year': 1941,
#         'duration': 59,
#         'genres': ['Western'],
#         'rating': 5.2,
#         'directors': ['nm0496505'],
#         'cast': ['nm0193318', 'nm0254381', 'nm0279961', 'nm0910294', 'nm0852305']
#     }
# ```
#
# You may copy/paste code from your lab-p8 notebook to finish this function.

# + tags=[]
def get_raw_movies(path):
    """
    get_raw_movies(path) converts a movies csv in 'path' 
    into a list of dicts with column names as keys and
    the corresponding type converted values as the values
    """
    csv_file = open(path, encoding="utf-8")
    csv_reader = csv.reader(csv_file)
    csv_data = list(csv_reader)
    csv_file.close()
    csv_header = csv_data[0]
    csv_rows = csv_data[1:]
    list_data = []
 
    for index in range(len(csv_rows)):
        movie_data = {}
        movie_data["title"] = csv_rows[index][csv_header.index("title")]
        movie_data["year"] = int(csv_rows[index][csv_header.index("year")])
        movie_data["duration"] = int(csv_rows[index][csv_header.index("duration")])
        genres = csv_rows[index][csv_header.index("genres")]
        movie_data["genres"] = genres.split(", ")
        movie_data["rating"] = float(csv_rows[index][csv_header.index("rating")])
        directors = csv_rows[index][csv_header.index("directors")]
        movie_data["directors"] = directors.split(", ")
        cast = csv_rows[index][csv_header.index("cast")]
        movie_data["cast"] = cast.split(", ")
        list_data.append(movie_data)

    return list_data


# + [markdown] deletable=false editable=false
# **Question 5:** What is returned by `get_raw_movies("small_movies.csv")`?
#
# Your output **must** be a **list** of **dictionaries** where each dictionary contains information about a movie.

# + tags=[]
# compute and store the answer in the variable 'raw_small_movies', then display it
raw_small_movies = get_raw_movies("small_movies.csv")

get_raw_movies("small_movies.csv")

# + deletable=false editable=false
grader.check("q5")

# + [markdown] deletable=false editable=false
# If your answer looks correct, but does not pass `grader.check`, make sure that the **datatypes** are all correct. Also make sure that the **directors** and **cast**  are in the **same order** as in `small_movies.csv`.

# + [markdown] deletable=false editable=false
# **Question 6:** How **many** cast members does the **first** movie have?
#
# Your output **must** be an **int**. You **must** use the variable `raw_small_movies` defined above to answer this question. You **must** not call the function `get_raw_movies` again on this dataset.

# + tags=[]
# compute and store the answer in the variable 'num_cast_first_movie', then display it
num_cast_first_movie = len(raw_small_movies[0]['cast'])

num_cast_first_movie

# + deletable=false editable=false
grader.check("q6")

# + [markdown] deletable=false editable=false
# **Question 7:** What is the *ID* of the **first** cast member listed for the **first** movie of the dataset?
#
# Your output **must** be a **string**.

# + tags=[]
# compute and store the answer in the variable 'first_actor_id_first_movie', then display it
first_actor_id_first_movie = raw_small_movies[0]['cast'][0]

first_actor_id_first_movie

# + deletable=false editable=false
grader.check("q7")


# + [markdown] deletable=false editable=false
# ### Function 3: `get_movies(movies_path, mapping_path)`
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function).
#
#
# This function **must** return a **list** of **dictionaries**, where each **dictionary** is of the following format:
#
# ```python
#    {
#         'title': "the movie name",
#         'year': <the year as an integer>,
#         'duration': <the duration as an integer>,
#         'genres': [<genre1>, <genre2>, ...],
#         'rating': <the rating as a float>,
#         'directors': ["director-name1", "director-name2", ...],
#         'cast': ["actor-name1", "actor-name2", ....]
#     }
# ```
#
# Here is an example:
#
# ```python
#     {
#         'title': 'Across the Sierras',
#         'year': 1941,
#         'duration': 59,
#         'genres': ['Western'],
#         'rating': 5.2,
#         'directors': ['D. Ross Lederman'],
#         'cast': ['Dick Curtis', 'Bill Elliott', 'Richard Fiske', 'Luana Walters', 'Dub Taylor']
#     }
# ```
#
# You may copy/paste code from your lab-p8 notebook to finish this function.

# + tags=[]
def get_movies(movies_path, mapping_path):
    """
    get_movies(movies_path, mapping_path) converts a movies csv in 'movies_path' 
    into a list of dicts with column names as keys and the corresponding 
    type converted values as the values; then uses the mapping csv in 'mapping_path'
    to replace the IDs of the titles, cast, and directors into actual names
    """
    movies = get_raw_movies(movies_path)
    mapping = get_mapping(mapping_path)
    
    for movie in movies:
        movie['title'] = mapping.get(movie['title'], movie['title'])
        movie['directors'] = [mapping.get(director, director) for director in movie['directors']]
        movie['cast'] = [mapping.get(actor, actor) for actor in movie['cast']]
        
    return movies
    # you are allowed to call get_mapping and get_raw_movies
    # on movies_path and mapping_path


# + [markdown] deletable=false editable=false
# **Question 8:** What is returned by `get_movies("small_movies.csv", "small_mapping.csv")`?
#
# Your output **must** be a **list** of **dictionaries** where each dictionary contains information about a movie.

# + tags=[]
# compute and store the answer in the variable 'small_movies_data', then display it
small_movies_data = get_movies("small_movies.csv", "small_mapping.csv")

small_movies_data

# + deletable=false editable=false
grader.check("q8")

# + [markdown] deletable=false editable=false
# **Question 9:** What is `title` of the **second** movie in `small_movies_data`?
#
# Your output **must** be a **string**. You **must** use the variable `small_movies_data` defined above to answer this question. You **must** not call the function `get_movies` again on this dataset.

# + tags=[]
# compute and store the answer in the variable 'second_movie_title_small_movies', then display it
second_movie_title_small_movies = small_movies_data[1]['title']

second_movie_title_small_movies

# + deletable=false editable=false
grader.check("q9")

# + [markdown] deletable=false editable=false
# **Question 10:** Who are the `cast` members of the **second** movie in `small_movies_data`?
#
# Your output **must** be a **list** of **string(s)**.

# + tags=[]
# compute and store the answer in the variable 'second_movie_cast_small_movies', then display it
second_movie_cast_small_movies = small_movies_data[1]['cast']

second_movie_cast_small_movies

# + deletable=false editable=false
grader.check("q10")

# + [markdown] deletable=false editable=false
# **Question 11:** Who are the `directors` of the **last** movie in `small_movies_data`?
#
# Your output **must** be a **list** of **string(s)**.

# + tags=[]
# compute and store the answer in the variable 'last_movie_directors_small_movies', then display it
last_movie_directors_small_movies = small_movies_data[len(small_movies_data) - 1]['directors']

last_movie_directors_small_movies

# + deletable=false editable=false
grader.check("q11")

# + [markdown] deletable=false editable=false
# #### Now that you’ve made it this far, your functions must be working pretty well with small datasets. Next, let's try a much bigger dataset!
#
# Run the following code to open the full dataset:
# -

movies = get_movies("movies.csv", "mapping.csv")
len(movies)

# + [markdown] deletable=false editable=false
# As the files are very large, this cell is expected to take around ten seconds to run. If it takes much longer (say, around a minute), then you will **need** to **optimize** your `get_movies` function so it runs faster.
#
# **Warning**: You are **not** allowed to call `get_movies` more than once on the full dataset (`movies.csv` and `mapping.csv`) in your notebook. Instead, reuse the `movies` variable, which is more efficient. You will **lose points** during manual review if you call `get_movies` again on these files.
#
# **Warning:** Do **not** display the value of the variable `movies` **anywhere** in your notebook. It will take up a **lot** of space, and your **Gradescope code will not be displayed** for grading. So, you will receive **zero points** for p8. Instead you should verify `movies` has the correct value by looking at a small *slice* of the **list** as in the question below. 

# + [markdown] deletable=false editable=false
# **Question 12:** What are the movies in `movies[20220:20230]`?
#
# Your answer should be a *list* of *dictionaries* that follows the format below:
#
# ```python
# [{'title': 'Dark Rider',
#   'year': 1991,
#   'duration': 94,
#   'genres': ['Action', 'Adventure', 'Crime'],
#   'rating': 5.6,
#   'directors': ['Bob Ivy'],
#   'cast': ['Joe Estevez', 'Doug Shanklin', 'Alicia Anne', 'Cloyde Howard']},
#  {'title': 'Izu no odoriko',
#   'year': 1967,
#   'duration': 85,
#   'genres': ['Drama'],
#   'rating': 8.4,
#   'directors': ['Hideo Onchi'],
#   'cast': ['Yôko Naitô',
#    'Toshio Kurosawa',
#    'Tatsuyoshi Ehara',
#    'Nobuko Otowa']},
#  {'title': 'Things Change',
#   'year': 1988,
#   'duration': 100,
#   'genres': ['Comedy', 'Crime', 'Drama'],
#   'rating': 7.0,
#   'directors': ['David Mamet'],
#   'cast': ['Don Ameche', 'Joe Mantegna', 'Robert Prosky', 'J.J. Johnston']},
#  ...]
# ```

# + tags=[]
# compute and store the answer in the variable 'movies_20220_20230', then display it
movies_20220_20230 = movies[20220:20230]

movies_20220_20230

# + deletable=false editable=false
grader.check("q12")

# + [markdown] deletable=false editable=false
# **Question 13:** What is the **number** of movies released so far in the `year` *2023*?
#
# Your outuput must be an **int**.

# + tags=[]
# compute and store the answer in the variable 'num_movies_2023', then display it
num_movies_2023 = 0

for movie in movies:
    if movie['year'] == 2023:
        num_movies_2023 += 1

num_movies_2023

# + deletable=false editable=false
grader.check("q13")


# + [markdown] deletable=false editable=false
# ### Function 4: `find_specific_movies(movies, keyword)`
#
# Now that we have created this data structure `movies`, we can start doing some fun things with the data!
# We will continue working on this data structure for the next project (P9) as well.
#
# Let us now use this data structure `movies` to create a **search bar** like the one in Netflix!
# **Do not change the below function in any way**.
# This function takes in a keyword like a substring of a title, a genre, or the name of a person, and returns a list of relevant movies with that title, genre, or cast member/director.
#
# **Warning:** As `movies` is very large, the function `find_specific_movies` may take five to ten seconds to run. This is normal and you should not panic if it takes a while to run.

# + deletable=false editable=false
# DO NOT EDIT OR REDEFINE THIS FUNCTION
def find_specific_movies(movies, keyword):
    """
    find_specific_movies(movies, keyword) takes a list of movie dictionaries 
    and a keyword; it returns a list of movies that contain the keyword
    in either its title, genre, cast or directors.
    """
    idx = 0
    while idx < len(movies):
        movie = movies[idx]
        # note: \ enables you split a long line of code into two lines
        if (keyword not in movie['title']) and (keyword not in movie["genres"]) \
        and (keyword not in movie["directors"]) and (keyword not in movie["cast"]):
            movies.pop(idx)
        else:
            idx += 1
    return movies


# + [markdown] deletable=false editable=false
# **Important:** While it might look as if we are making it easy for you by providing `find_specific_movies`, there is a catch! There is a subtle flaw with the way the function is defined, that will cause you issues in the next two questions. If you can spot this flaw by just observing the definition of `find_specific_movies`, congratulations! Since you are **not** allowed to modify the function definition, you will have to be a little clever with your function arguments to sidestep the flaw with the function definition.
#
# If you don't see anything wrong with the function just yet, don't worry about it. Solve Question 14 and Question 15 as you normally would, and see if you notice anything suspicious about your answers.

# + [markdown] deletable=false editable=false
# **Question 14:** List all the movies that were directed by *Stanley Kubrick*.
#
# Your answer **must** be a **list** of **dictionaries**.
#
# You **must** answer this question by calling `find_specific_movies` with the keyword `"Stanley Kubrick"`.
#
# The `find_specific_movies` function is expected to take around 5 seconds or more to run, so do not panic if it takes so long to run.
#
# Remember that you are **not** allowed to modify the definition of `find_specific_movies`. You will need to cleverly pass arguments to `find_specific_movies` (in both Question 14 and Question 15) to ensure that `movies` does not get modified by the function calls. Take a look at the Lecture Slides ([Mike](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-lecture-material/-/tree/main/s23/Michael_lecture_notes/21_Copying) and [Gurmail](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-lecture-material/-/tree/main/s23/Gurmail_lecture_notes/21_Copying)) from March 22 for more hints. You will have to Restart and Run all your cells to see the correct output after you fix your answer for Question 14 (and Question 15).

# + tags=[]
# compute and store the answer in the variable 'kubrick_films', then display it
kubrick_films = find_specific_movies(copy.deepcopy(movies), "Stanley Kubrick")

kubrick_films

# + deletable=false editable=false
grader.check("q14")

# + [markdown] deletable=false editable=false
# **Question 15:** List all the movies that contain the string *Wisconsin* in their `title`.
#
# Your answer **must** be a **list** of **dictionaries**.
#
# You **must** answer this question by calling `find_specific_movies` with the keyword `"Wisconsin"`.
#
# **Important Hint:**  If you did not notice the flaw with the definition of `find_specific_movies` before, you are likely to have run into an issue with this question. It is likely that you will see that your output for this question is an empty list. To see why this happened, find the value of `len(movies)` and see if it is equal to the value you found earlier.
#

# + tags=[]
# compute and store the answer in the variable 'wisconsin_movies', then display it
wisconsin_movies = find_specific_movies(copy.deepcopy(movies), "Wisconsin")

wisconsin_movies

# + deletable=false editable=false
grader.check("q15")


# + [markdown] deletable=false editable=false
# ### Function 5: `bucketize_by_genre(movies)`
#
# We require you to complete the below function to answer the next several questions (this is a **requirement**, and you will **lose points** if you do not implement this function).

# + tags=[]
def bucketize_by_genre(movies):
    """bucketize_by_genre(movies) takes a list of movie dictionaries;
    it returns a dict in which each genre is a key and
    the value is a list of all movies that contain that genre"""
    genre_bucket = {}
    for movie in movies:
        for index in range(len(movie['genres'])):
            if not (movie['genres'][index]) in genre_bucket:
                genre_bucket[movie['genres'][index]] = []
                genre_bucket[movie['genres'][index]].append(movie)
            else: 
                genre_bucket[movie['genres'][index]].append(movie)
    
    return genre_bucket
    # TODO: initialize a dictionary
    # TODO: loop through all movies
    # TODO:     loop through all genres in this movie
    # TODO:         if this genre is not a key in our dictionary, set the value associated with this genre to an empty list
    # TODO:         add the movie to the list associated with this genre
    # TODO: return the dictionary


# + tags=[]
# call the function bucketize_by_genre on 'movies' and store it in the variable 'genre_dict'
# do NOT display the output directly

genre_dict = bucketize_by_genre(movies)

# + [markdown] deletable=false editable=false
# **Warning:** You are **not** allowed to call `bucketize_by_genre` more than once on the full list of movies (`movies`) in your notebook. You will **lose points** during manual review if you call `bucketize_by_genre` again on `movies`.

# + [markdown] deletable=false editable=false
# **Question 16:** How many **unique** movie `genres` are present in the dataset?

# + tags=[]
# compute and store the answer in the variable 'num_genres', then display it
num_genres = len(genre_dict)

num_genres

# + deletable=false editable=false
grader.check("q16")

# + [markdown] deletable=false editable=false
# **Question 17:** How many *Romance* movies (i.e. movies with *Romance* as one of their `genres`) do we have in the dataset released **after** the `year` *2017*?
#
# Your output **must** be an **int**. You **must** use the `genre_dict` data structure to answer this question.

# + tags=[]
# compute and store the answer in the variable 'romance_after_2017', then display it
romance_after_2017 = 0

for index in range(len(genre_dict["Romance"])):
    if genre_dict["Romance"][index]["year"] > 2017:
        romance_after_2017 += 1
        
romance_after_2017

# + deletable=false editable=false
grader.check("q17")

# + [markdown] deletable=false editable=false
# **Question 18:** List the `title` of all *Film-Noir* movies (i.e. movies with *Film-Noir* as one of their `genres`) with `rating` **larger** than *8.0* in the dataset.
#
# Your output **must** be a **list** of **strings**. You **must** use the `genre_dict` data structure to answer this question.

# + tags=[]
# compute and store the answer in the variable 'film_noir_movies_above_8', then display it
film_noir_movies_above_8 = []

for index in range(len(genre_dict["Film-Noir"])):
    if genre_dict["Film-Noir"][index]["rating"] > 8.0:
        film_noir_movies_above_8.append(genre_dict["Film-Noir"][index]["title"])
        
film_noir_movies_above_8

# + deletable=false editable=false
grader.check("q18")

# + [markdown] deletable=false editable=false
# **Question 19:** Which movie `genre` does *Blake Lively* play the most?
#
# There is a **unique** `genre` that *Blake Lively* has played the most. You do **not** have to worry about breaking ties.
#
# **Hint:** You can combine the *two* functions above to bucketize the movies that *Blake Lively* has acted in by their `genres`. Then, you can loop through each genre to find the one with the most number of movies in it.

# + tags=[]
# compute and store the answer in the variable 'blake_lively_genre', then display it
blake_lively_genre = ''
most_count = 0
for genre in genre_dict:
    count = 0
    for index in range(len(genre_dict[genre])):
        for idx in range(len(genre_dict[genre][index]["cast"])):
            if genre_dict[genre][index]["cast"][idx] == "Blake Lively":
                count += 1
    if count > most_count:
        most_count = count
        blake_lively_genre = genre              
        
blake_lively_genre

# + deletable=false editable=false
grader.check("q19")

# + [markdown] deletable=false editable=false
# **Question 20:** Who are the `directors` of the *Comedy* movies with the **highest** `rating` in the movies dataset?
#
# There are **multiple** *Comedy* movies in the dataset with the joint highest rating. You **must** output a **list** of **strings** containing the **names** of **all** the `directors` of **all** these movies.
#
# **Hint:** If you are unsure how to efficiently add the elements of one list to another, please review any of the lecture notes from the February 27 lectures ([here](https://canvas.wisc.edu/courses/343490/files/folder/Mikes_Lecture_Notes/lec14_lists) and [here](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-lecture-material/-/tree/main/s23/Gurmail_lecture_notes/14_Lists)).

# + tags=[]
# compute and store the answer in the variable 'max_comedy_rating_directors', then display it
max_comedy_rating_directors = []
highest_rating = 0

for index in range(len(genre_dict["Comedy"])):
    directors = []
    if genre_dict["Comedy"][index]["rating"] > highest_rating:
        highest_rating = genre_dict["Comedy"][index]["rating"]
        for idx in range(len(genre_dict["Comedy"])):
            if genre_dict["Comedy"][idx]["rating"] == highest_rating:
                for i in range(len(genre_dict["Comedy"][idx]["directors"])):
                    directors.append(genre_dict["Comedy"][idx]["directors"][i])
                    max_comedy_rating_directors = directors

max_comedy_rating_directors

# + deletable=false editable=false
grader.check("q20")

# + [markdown] deletable=false editable=false
# ## Submission
# Make sure you have run all cells in your notebook in order before running the following cells, so that all images/graphs appear in the output. The following cells will generate a zip file for you to submit.
#
# **SUBMISSION INSTRUCTIONS**:
# 1. **Upload** the zipfile to Gradescope.
# 2. Check **Gradescope otter** results as soon as the auto-grader execution gets completed. Don't worry about the score showing up as -/100.0. You only need to check that the test cases passed.

# + [code] deletable=false editable=false
from IPython.display import display, Javascript
display(Javascript('IPython.notebook.save_checkpoint();'))

# + [code] deletable=false editable=false
# !jupytext --to py p8.ipynb

# + [code] deletable=false editable=false
grader.export(pdf=False, run_tests=True, files=[py_filename])

# + [markdown] deletable=false editable=false
#  
