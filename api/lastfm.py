import requests


def get_lastfm_data(username: str, api_key: str) -> dict:
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={api_key}&format=json&limit=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return {"error": f"Last.fm API error: {data['message']}"}

        recent_tracks = data.get("recenttracks", {})
        track = recent_tracks.get("track", [{}])[0]

        song_name = track.get("name", "No song name found")
        artist_name = track.get("artist", {}).get("#text", "No artist found")

        images = track.get("image", [])
        album_art_url = ""
        if images:
            album_art_url = images[-1].get("#text", "")

        is_playing = track.get("@attr", {}).get("nowplaying", "false") == "true"

        return {
            "song": song_name,
            "artist": artist_name,
            "albumArt": album_art_url,
            "isPlaying": is_playing,
        }

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
