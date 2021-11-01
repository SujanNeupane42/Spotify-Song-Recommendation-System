import streamlit as st
import pickle
import numpy as np
import requests
import base64

st.set_page_config(layout="wide")

# For getting the background image
# def get_base64(bin_file):
#    with open(bin_file, 'rb') as f:
#        data = f.read()
#    return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#    st.set_page_config(layout="wide")
#    bin_str = get_base64(png_file) 
#    page_bg_img = '''
#        <style>
#            .stApp {
#                background-image: url("data:image/png;base64,%s");
#                background-size: cover;
#                background-repeat: no-repeat;
#                background-attachment: scroll; 
#            }
#        </style>
#    ''' % bin_str
#    st.markdown(page_bg_img, unsafe_allow_html=True)
#    return
# set_png_as_page_bg('./images/images2.jpg')

'''
Created on friday oct 29, 2021 by Sujan Neupane
'''

if st.button('GitHub'):
    url = "https://github.com/SujanNeupane42/Spotify-Song-Recommendation-System"
    st.write("[GitHub](%s)" % url)

data_df = pickle.load(open('data_df.pkl', 'rb'))

st.title("Spotify Music Recommendation System")

input_song = st.text_input("Enter a Song you like with its correct name: ", value = 'Let me love you')

n_recommendations = st.slider('How many Songs do you want to be recommended? ', min_value=1, max_value=20, value=3, step=1)

artist_name = st.text_input("Enter the name of artist: ", value = 'Justin Bieber')

# For getting the artist name
def select_artist(song,artist):
  artist_names = [i.split(",") for i in list(data_df[data_df.name.str.lower() == song.lower()]['artists'])]

  for i in range(len(artist_names)): 
    for j in range(len(artist_names[i])):        
      if (artist_names[i][j].lower().strip() == artist.lower()):
        return i 

# For Recommending the songs
def get_songs(song, n_recommendations,data_df,artist_name):
    """
    Here, Manhattan Distance is calculated for all songs, and the songs with least Manhattan distance with the selected songs
    are used to recommend songs to the user.
    """
    distance = []
    artist_names_index = select_artist(song,artist_name)
    selected_song = data_df[(data_df['name'].str.lower() == song.lower())].values[artist_names_index]
    remaining_song = data_df[data_df.name.str.lower() != song.lower()]

    for songs in (remaining_song.values):
        d = 0
        for col in np.arange(len(remaining_song.columns)):
            # Indices of columns that will not be used
            if not col in [1,3,7,13,15,19,20]:
                d = d + np.absolute(float(selected_song[col]) - float(songs[col]))
        distance.append(d)
    remaining_song['distance'] = distance
    # Sorting our data to be ascending by 'distance' feature
    remaining_song = remaining_song.sort_values('distance')
    columns = ['id','artists', 'name','release_date']
    recommended_df = remaining_song[columns][:n_recommendations].reset_index()

    return recommended_df

# Using spotify api to access song details
def spotify_song_details(id):
    details = []
    api_url = 'https://open.spotify.com/oembed?url=spotify:track:' + id
    response = requests.get(api_url).json()

    song_thumbnail = response['thumbnail_url']
    details.append(song_thumbnail)

    title = response['title']
    details.append(title)
    
    song_url = 'https://open.spotify.com/track/' + id
    details.append(song_url)

    return details

# When the button is pressed, following code is executed
if st.button('Submit'):
    try:
        st.write("Please Know that the dataset used has limited songs from 1921 to 2020")
        st.write(" ")
        artist_names_index = select_artist(input_song,artist_name)
        Selected_Song = dict(data_df[data_df.name.str.lower() == input_song.lower()].iloc[artist_names_index])
        id = Selected_Song['id']
        artist = Selected_Song['artists']
        name = Selected_Song['name']
        release_date = Selected_Song['release_date']
        
        resultant = spotify_song_details(id)
        st.write("Selected Song: ",resultant[1], " by ",artist)
        image = "<img height = 400 width = 400 src = "+resultant[0]+">"
        st.markdown(image, unsafe_allow_html = True)
        st.write(" ")
        st.write("Released on: "," ",release_date)
        st.write("Spotify Url: ",resultant[2])
        st.write(" ")
        st.write(" ")

        st.header("Recommended Songs")
        st.write("Songs you may like:")
        st.write(" ")
        recommended_songs = get_songs(input_song,n_recommendations,data_df,artist_name)

        for i in range(0,n_recommendations):
            id = (recommended_songs['id'].values[i])
            artist = recommended_songs['artists'].values[i]
            release_date = recommended_songs['release_date'].values[i]
            resultant = spotify_song_details(id)

            st.write((i+1),". ",resultant[1], " by ",artist)
            image = "<img height = 400 width = 400 src = "+resultant[0]+">"
            st.markdown(image, unsafe_allow_html = True)
            st.write(" ")
            st.write("Released on: ",release_date)
            st.write("Spotify Url: ",resultant[2])
            st.write(" ")
            st.write(" ")
    except:
        st.write('Please check if the input values are absolutely correct or not.')
        st.write('If you have entered correct values, Sorry, The song \"',input_song,'\" is not in dataset used.')


#   Thank you
#   From Sujan Neupane (neupanesujan420@gmail.com)