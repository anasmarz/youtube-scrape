import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_video_title(video_id):
    """Fetch the video title using web scraping."""
    url = f'https://www.youtube.com/watch?v={video_id}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('meta', {'name': 'title'})
        if title_tag:
            return title_tag.get('content')
        else:
            return "Title not found"
    else:
        return f"Error: {response.status_code}"

def append_transcript_to_csv(video_id, file_path):
    """Fetch transcript and append to CSV."""
    from youtube_transcript_api import YouTubeTranscriptApi

    # Get video title
    video_title = get_video_title(video_id)

    # Get the transcript for the given video ID
    srt = YouTubeTranscriptApi.get_transcript(video_id)

    # Create a DataFrame from the transcript data including the video title
    df = pd.DataFrame({
        'VideoTitle': [video_title] * len(srt),  # Repeat the video title for each subtitle entry
        'Text': [entry["text"] for entry in srt]  # Extract the text from each subtitle entry
    })

    # Check if the file exists
    if os.path.isfile(file_path):
        # If the file exists, append the data without the header
        df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8')
    else:
        # If the file does not exist, create it and write the data with the header
        df.to_csv(file_path, mode='w', header=True, index=False, encoding='utf-8')

# Example usage
file_path = "subtitles1.csv"
video_id = "T2gi8MKaTQo" #example of video id<video_id>

# Append the first video's transcript
append_transcript_to_csv("T2gi8MKaTQo", file_path)

