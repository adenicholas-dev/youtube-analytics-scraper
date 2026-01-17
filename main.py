import requests
from datetime import datetime
import json
import csv
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
search_url = "https://www.googleapis.com/youtube/v3/search"

channel_name = input("Enter channel name: ")


def get_channel_id(channel_name):
    from googleapiclient.discovery import build

    API_KEY = YOUTUBE_API_KEY
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        part='snippet',
        q=channel_name,
        type='channel',
        maxResults=1
    )

    response = request.execute()

    if response['items']:
        channel_id = response['items'][0]['snippet']['channelId']
        return channel_id
    else:
        return None

channel_id = get_channel_id(channel_name)
print(f"Channel ID: {channel_id}")

# Get channel statistics
channel_statistics_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&id={channel_id}&key={YOUTUBE_API_KEY}"
response = requests.get(channel_statistics_url)
response.raise_for_status()
channel_statistics = response.json()

channel = channel_statistics["items"][0]["statistics"]
subscribers_beast_total = int(channel.get('subscriberCount', 0))
views_beast_total = int(channel.get('viewCount', 0))
videos_beast_total = int(channel.get('videoCount', 0))
print(
    f"the chanel name {channel_name}, has {subscribers_beast_total} subscribers and {views_beast_total} views and {videos_beast_total} videos")

uploads_playlist_id = channel_statistics["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

next_page_token = None
video_count = 0
max_videos_to_fetch = 20

current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")

all_videos = []

while video_count < max_videos_to_fetch:
    # Build URL directly
    playlist_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&playlistId={uploads_playlist_id}&key={YOUTUBE_API_KEY}&maxResults=10"

    if next_page_token:
        playlist_url += f"&pageToken={next_page_token}"
        print(f"Fetching next page of videos...\n")

    response = requests.get(playlist_url)
    response.raise_for_status()
    search_data = response.json()

    # Extract video IDs
    video_ids = [item['contentDetails']['videoId'] for item in search_data['items']]
    if video_ids:
        videos_url = "https://www.googleapis.com/youtube/v3/videos"
        video_params = {
            "part": "snippet,statistics",
            "id": ",".join(video_ids),
            "key": YOUTUBE_API_KEY
        }

        response = requests.get(videos_url, params=video_params)
        response.raise_for_status()
        videos_data = response.json()

        for video in videos_data['items']:
            if video_count >= max_videos_to_fetch:
                break

            video_info = {
                "date_fetched": current_date,
                "title": video['snippet']['title'],
                "video_id": video['id'],
                "views": video['statistics'].get('viewCount', 'N/A'),
                "likes": video['statistics'].get('likeCount', 'N/A'),
                "comments": video['statistics'].get('commentCount', 'N/A')
            }
            all_videos.append(video_info)
            video_count += 1

            print(f"\nTitle: {video['snippet']['title']}")
            print(f"Views: {video['statistics'].get('viewCount', 'N/A')}")
            print(f"Likes: {video['statistics'].get('likeCount', 'N/A')}")
            print(f"Comments: {video['statistics'].get('commentCount', 'N/A')}")

    # Check if there's a next page
    if video_count < max_videos_to_fetch and "nextPageToken" in search_data:
        next_page_token = search_data["nextPageToken"]
        print(f"\n{'=' * 80}")
        print(f"There are more videos available. Next page token: {next_page_token[:20]}...")
        print(f"{'=' * 80}")
    else:
        print("\n" + "=" * 80)
        print(f"Fetched {video_count} videos. Stopping...")
        print("=" * 80)
        break

# Save all video details to JSON
videos_json_filename = f"videos_{current_date}.json"
with open(videos_json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(all_videos, json_file, indent=4)
print(f"\n Saved video details to: {videos_json_filename}")

# Save all video details to CSV
videos_csv_filename = f"videos_{current_date}.csv"
if all_videos:
    with open(videos_csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['date_fetched', 'title', 'video_id', 'views', 'likes', 'comments']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_videos)
    print(f" saved video details to: {videos_csv_filename}")