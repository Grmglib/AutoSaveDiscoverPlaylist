import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
scope = 'playlist-read-private,playlist-read-collaborative,playlist-modify-private,playlist-modify-public'
os.environ['SPOTIPY_CLIENT_ID'] = 'YOUR CLIENT_ID'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'YOUR CLIENT_SECRET'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.com/callback'
username = 'YOUR SPOTIFY USERNAME'
playlist = 'YOUR PLAYLIST ID OF CHOICE'
discover = 'YOUR DISCOVER WEEKLY PLAYLIST ID'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
tracks = sp.user_playlist_tracks(user=username,playlist_id=discover)
items =[]
for track in tracks['items']:
    items.append(track['track']['uri'])
sp.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=items)