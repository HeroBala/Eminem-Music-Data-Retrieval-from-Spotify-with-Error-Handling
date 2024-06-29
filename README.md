# Spotify Data Retrieval for Eminem

## Description
This project retrieves data related to Eminem's music from Spotify using the Spotify Web API. The data includes track names, album names, release dates, durations, type of music (single or album), and featured artists. It also includes error handling and logging.

## Setup

1. Clone this repository or download the files.
2. Install dependencies using `pip install -r requirements.txt`.
3. Obtain your Spotify API credentials (Client ID and Client Secret) from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
4. Replace `'your_spotify_client_id'` and `'your_spotify_client_secret'` in `spotify_eminem.py` with your actual Spotify API credentials.
5. Run `spotify_eminem.py` to execute the script and retrieve the data.

## Usage

```sh
python spotify_eminem.py
```

The script will save the data to a file named `eminem_music_data.json`.

## Notes
- Ensure you have access to the Spotify API by registering an application on the Spotify Developer Dashboard.
- Customize the script as needed for additional data processing or analysis.
