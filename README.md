# YouTube Transcript and Title Fetcher

## Overview

The **YouTube Transcript and Title Fetcher** is a Python application that retrieves subtitles (transcripts) for YouTube videos and saves them to a CSV file. Additionally, it fetches the video title using web scraping and includes it in the CSV file. This tool is useful for collecting and organizing video subtitles for further analysis or archival purposes.

## Features

- **Fetch Video Title**: Extracts the title of a YouTube video using web scraping techniques.
- **Retrieve Subtitles**: Retrieves the subtitles (transcripts) for a given YouTube video ID using the YouTube Transcript API.
- **Save to CSV**: Saves the video title and corresponding subtitles to a CSV file. Appends data to an existing file or creates a new file if it does not exist.

## How It Works

1. **Video Title Extraction**:
   - The application uses web scraping to fetch the video title from YouTube's video page. It parses the HTML content to extract the title from the `<meta name="title">` tag.

2. **Transcript Retrieval**:
   - Utilizes the YouTube Transcript API to get the subtitles for the specified video ID. It collects the subtitle text and formats it into a structured format.

3. **Data Storage**:
   - Creates a CSV file with two columns: `VideoTitle` and `Text`. The video title is repeated for each subtitle entry, and each subtitle text is stored in its own row. Data is appended to the CSV file if it already exists or written to a new file if it does not.

## Requirements

- Python 3.x
- `requests` library for making HTTP requests
- `BeautifulSoup` library for web scraping
- `pandas` library for data manipulation
- `youtube_transcript_api` library for retrieving YouTube subtitles

## Installation

1. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 pandas youtube-transcript-api
