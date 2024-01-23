import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

movies_df = pd.read_csv("movies.csv")
credit_df = pd.read_csv("credits.csv")

movies_df = movies_df.merge(credit_df, on = 'title')
movies_df = movies_df[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies_df.dropna(inplace = True)

#create a method to convert the genres section and keyword section to a list of strings, get rid of useless
#words
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies_df['genres'] = movies_df['genres'].apply(convert)
movies_df['keywords'] = movies_df['keywords'].apply(convert)

def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter +=1
        else:
            break
    return L

movies_df['cast'] = movies_df['cast'].apply(convert3)

movies = movies_df


def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L

movies['crew'] = movies['crew'].apply(fetch_director)
movies.rename(columns={'crew':'Director'}, inplace = True)
movies['overview'] = movies['overview'].apply(lambda x:x.split())

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ", "") for i in x])
movies['Director'] = movies['Director'].apply(lambda x:[i.replace(" ", "") for i in x])

movies['tags'] = movies['overview'] + movies["genres"] +movies["keywords"] + movies["cast"] + movies["Director"]


new_df = movies[['movie_id', 'title', 'tags']]


new_df['tags'] = new_df['tags'].apply(lambda x:' '.join(x))

new_df["tags"] = new_df["tags"].apply(lambda X:X.lower())

#this function will allow me to use text as input in my ML model. it changes text to numerical values
cv = CountVectorizer(max_features = 5000, stop_words = 'english')

vectors = cv.fit_transform(new_df['tags']).toarray()



def stem(text):
    ps = PorterStemmer()
    y =[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

#tells us similarity between vecotors often used to find similarity between words
similarity = cosine_similarity(vectors)

sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x:x[1])[1:6]


def recommend(movie): 
    res = " "
    movie_index = new_df[new_df['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    for i in movies_list:
        res += new_df.iloc[i[0]].title + ", "
    return res

print(recommend("Avatar"))








