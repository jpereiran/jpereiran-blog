import requests
import pandas as pd

def get_release_group_from_artist(release_group_id):

    releases_url = f'https://musicbrainz.org/ws/2/release-group?artist={artist_id}&fmt=json'
    release_response = requests.get(releases_url)
    release_data = release_response.json()

    release_groups = []

    if 'release-groups' in release_data:
        for release_group in release_data['release-groups']:
            release_type = release_group['primary-type']
            secondary_type = release_group['secondary-types']

            # Only print albums (primary_type = "Album", secondary_type = [])
            if release_type == "Album" and secondary_type == []:
                release_groups.append({
                    'title': release_group['title'],
                    'release_date': release_group['first-release-date'],
                    'release_group_mbid': release_group['id']
                })

    
    return release_groups

def get_releases_from_group(release_group_id):
    url = f"https://musicbrainz.org/ws/2/release-group/{release_group_id}?inc=releases&fmt=json"
    response = requests.get(url)
    data = response.json()

    releases = []
    for release in data['releases']:
        releases.append({
                'title': release['title'],
                'mbid': release['id']
            })
    
    return releases


def get_tracks_from_release(release_id):
    url = f"https://musicbrainz.org/ws/2/release/{release_id}?inc=recordings&fmt=json"
    response = requests.get(url)
    data = response.json()
    
    tracks = []
    for track_entry in data['media'][0]['tracks']:
        tracks.append({
                    'title': track_entry['title'],
                    'position': track_entry['position'],
                    'length': track_entry['length']
                })
    
    return tracks


def get_lyrics_from_track(artist, track):
    url = f"https://api.lyrics.ovh/v1/{artist}/{track}"
    response = requests.get(url)
    if response.status_code == 200:
        lyrics = response.json().get("lyrics")
        if lyrics is not None:
            lyrics = lyrics.replace('\n\n','\n')
    else:
        lyrics = ''
    return lyrics


df_lyrics = pd.DataFrame(columns=['Artist', 'Artist ID', 'Release Group', 'Release Group Date', 'Release Group ID', 'Release', 'Release ID', 
                                    'Track', 'Track Position', 'Length', 'Lyrics'])

list_lyrics = []

artist = "Manic Street Preachers"
artist_id = '32efea44-6cb5-4b4f-bdaa-c8b8f6cef981'

release_groups = get_release_group_from_artist(artist_id)



for release_group in release_groups:
    release_group_mbid =  release_group['release_group_mbid']
    releases = get_releases_from_group(release_group_mbid)
    release_id = releases[0]['mbid']
    tracks = get_tracks_from_release(release_id)
    for track in tracks:
        track_lyrics = get_lyrics_from_track(artist, track['title'])

        list_lyrics.append([artist, artist_id,release_group['title'], release_group['release_date'], release_group_mbid, releases[0]['title'], release_id, 
                            track['title'], track['position'], track['length'], track_lyrics])


df_lyrics = pd.DataFrame(list_lyrics, columns=df_lyrics.columns)
df_lyrics.to_excel("DF Artist Lyrics.xlsx", sheet_name='Lyrics', index=False)