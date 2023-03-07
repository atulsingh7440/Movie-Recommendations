# Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.

# Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

# invoking your function with the input “Black Panther”.
# HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache.
# If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. 
# Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

import requests_with_caching
import json


def get_movies_from_tastedive(movie_or_music_artist_name):
    end_points = "https://tastedive.com/api/similar"      # url according to condition
    Parameters = {} # parameter dictionary
    Parameters["q"] = movie_or_music_artist_name
    Parameters["type"] = "movies"
    Parameters["limit"] = 5
    this_page_cache = requests_with_caching.get(end_points, params = Parameters) # it return a object
    return this_page_cache.json()
  
print(get_movies_from_tastedive("Bridesmaids")) # it will be dictionary
print(get_movies_from_tastedive("Black Panther"))
    

