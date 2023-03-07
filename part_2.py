# Please copy the completed function from above into this active code window.
# Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. 
# Call it extract_movie_titles.


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
    return this_page_cache.json() # retun a dictionary


def extract_movie_titles(Dict):
    print(Dict) # dictonary
    #print(Dict['Similar']) #dictionary
    #print(Dict['Similar'].keys()) # two keys : info and result
    #print(Dict['Similar']['Results'])   #list 
    #print(Dict['Similar']['Results'][0]) # above list 1st element(dictionary)
    list_of_movie_title = []
    for d in Dict['Similar']['Results']:
        list_of_movie_title.append(d['Name'])
    return list_of_movie_title
        
    
  
print(extract_movie_titles(get_movies_from_tastedive("Tony Bennett")))
print(extract_movie_titles(get_movies_from_tastedive("Black Panther")))
