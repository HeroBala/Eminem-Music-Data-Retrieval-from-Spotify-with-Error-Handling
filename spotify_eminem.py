# spotify_eminem.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Set up authentication credentials
CLIENT_ID = 'your_spotify_client_id'
CLIENT_SECRET = 'your_spotify_client_secret'

def authenticate_spotify(client_id, client_secret):
    try:
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        logger.info("Successfully authenticated with Spotify")
        return sp
    except Exception as e:
        logger.error(f"Failed to authenticate with Spotify: {e}")
        sys.exit(1)

def get_eminem_id(sp):
    try:
        results = sp.search(q='Eminem', type='artist')
        eminem_id = results['artists']['items'][0]['id']
        logger.info("Found Eminem's artist ID")
        return eminem_id
    except Exception as e:
        logger.error(f"Failed to find Eminem's artist ID: {e}")
        sys.exit(1)

def get_album_data(sp, artist_id):
    album_data = []
    try:
        albums = sp.artist_albums(artist_id, album_type='album,single')
        for album in albums['items']:
            album_info = {
                'album_name': album['name'],
                'release_date': album['release_date'],
                'album_type': album['album_type'],
                'tracks': []
            }
            
            # Get all tracks for the album
            tracks = sp.album_tracks(album['id'])
            for track in tracks['items']:
                track_info = {
                    'track_name': track['name'],
                    'duration_ms': track['duration_ms'],
                    'featured_artists': [artist['name'] for artist in track['artists'] if artist['id'] != artist_id]
                }
                album_info['tracks'].append(track_info)
            
            album_data.append(album_info)
        logger.info("Successfully retrieved album data")
    except Exception as e:
        logger.error(f"Failed to retrieve album data: {e}")
    return album_data

def save_data_to_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        logger.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logger.error(f"Failed to save data to {filename}: {e}")

def main():
    sp = authenticate_spotify(CLIENT_ID, CLIENT_SECRET)
    eminem_id = get_eminem_id(sp)
    album_data = get_album_data(sp, eminem_id)
    save_data_to_json(album_data, 'eminem_music_data.json')

if __name__ == '__main__':
    main()
