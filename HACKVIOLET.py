#!/usr/bin/env python
# coding: utf-8

# In[3]:


from IPython.display import HTML, Javascript, Image

#--- Calling Toggle ----
# Hide or display code button definition
HideShowCodeButton = HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click to toggle on/off raw code"></form>''')

display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(), IPython.notebook.get_selected_index()+1)'))


import ipywidgets as widgets
testy = widgets.Dropdown(
    options=['Select mood' , 'Happy', 'Alright', 'Sad' , 'Angry', 'Alone'],
    value='Select mood',
    description='Mood:',
    disabled=False,
)


# Display Hide or display code button
HideShowCodeButton, testy


# In[5]:


f = open("C:\\Users\\tinai\\secret.txt", "r")
f.seek(0)
keys = f.readlines()

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
market = [ "CA" ]

CLIENT_ID = keys[0][:-1]
CLIENT_SECRET = keys[1]

credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

res = spotify.search(testy.value, type="playlist", market=market, limit=1)
f.close()

link = res['playlists']['items'][0]['external_urls']['spotify'] # link to playlist
track = res['playlists']['items'][0]['name'] # track name
cover = res['playlists']['items'][0]['images'][0]['url'] # track cover
owner = res['playlists']['items'][0]['owner']['display_name'] # track owner

import PIL
from PIL import Image
import requests
import io

response = requests.get(cover)
image_bytes = io.BytesIO(response.content)

img = PIL.Image.open(image_bytes)
# img = PIL.Image.open(response)

display(img)


# In[ ]:




