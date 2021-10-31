# Spotify Music Recommendation System
![Python](https://img.shields.io/badge/Python-3.9.2-blueviolet)
![Scikit learn](https://img.shields.io/badge/sklearn-0.24.2-red)
![Numpy](https://img.shields.io/badge/Numpy-1.19.5-green)
![Pandas](https://img.shields.io/badge/Pandas-1.3.3-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.1.0-red)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3.4-white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11.1-pink)

This is a simple song recommendation system. I have used following python libraries: numpy, matplotlib, seaborn, and sklearn. 


The dataset contains various features lke valence, year,	acousticness,	artists,	danceability,	duration_ms,	energy,	explicit,	id,	instrumentalness,	key,	liveness,	loudness,	mode,	name,	popularity,	release_date,	speechiness, and	tempo.

The dataset can also be found in `Kaggle`. However, I have added the csv files in the respository. The link to Kaggle dataset is https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify.

I have performed the following steps in the jupyter notebook:
  1. Loading the data- I have used pandas library to load all the csv files.
 
  2. Gathering Insights Into the Data - I have performed a short analysis on the datasets and came to the conclusion that there are no null values present.
 
  3. Exploratory Data Analysis and Visualization - I have used matplotlib and seaborn to visualize data using various histograms, heatmap, bar-diagrams, and lineplots.
   
  4. Data Preprocessing and Feature Engineering
   
      4.1 Preprocessing - Performed preprocessing by converting datatime columns into a datatime object, sorted the dataframes based on year, removed unnecessary characters from                              different features, removed duplicates etc.
      
      4.2 Selecting Features - Selected the necessary features to make recommendations
      
      4.3 Feature Engineering - Converted and Engineered few selected columns like scaling the features using MinMax Scaler, used KMeans Clustering to create cluster feature 

   5. Building the System - Used and created column transformer, pipeline, and a function that calculates manhattan distance to make recommendations.


# Heroku
Then, I used streamlit to create a proper and appealing GUI ,which I deployed using Heroku Platform.

# Spotify API
In the streamlit/python file, I have used Spotify Spotify `API` to get thumbnail, url, and title of the song.
