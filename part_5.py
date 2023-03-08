# Please copy the completed function from above into this active code window. 
# Now write a function called get_movie_rating.
# It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. 
# For example, if given the OMDB dictionary for “Black Panther”, it would return 97.
# If there is no Rotten Tomatoes rating, return 0.




# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
import requests_with_caching
import json 

def get_movie_data(title_of_movie):
    endpoint = "http://www.omdbapi.com/"
    parameter = {}
    parameter["t"] = title_of_movie
    parameter["r"] = "json"
    this_page_cache = requests_with_caching.get(endpoint, params=parameter)
    return json.loads(this_page_cache.text)
    


def get_movie_rating(Dict):
    #print(Dict) #return from get_movie_data()
    #print(Dict.keys()) #find out the rating key
    print(Dict['Ratings']) #of rating key, it is a list of dictionaries
    #print(Dict['Ratings'][0]) #first element of above list,it is a dictonary,with two keys,source and value
    for item in Dict['Ratings']:
        if item['Source'] == 'Rotten Tomatoes' :
            return int((item['Value'][:-1]))
    return 0    
    
            
print(get_movie_rating(get_movie_data("Deadpool 2")))

#line N0. 32 : (Explaination) -> item['Value'] = '83%' -> item['Value'][:-1] = '83' -> int(item['Value'][:-1]) = 83(integer)
