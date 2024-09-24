import random
import webbrowser
import argparse
from pytubefix import Channel

def get_random_video_url(channel_url):
    # Initialize the Channel object from pytube
    channel = Channel(channel_url)
    # Fetch all video URLs from the channel
    video_urls = [video.watch_url for video in channel.videos]
    # Select a random video URL
    random_video_url = random.choice(video_urls)
    return random_video_url

def open_video_in_browser(video_url):
    # Open the video URL using the default web browser
    webbrowser.open(video_url)

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Get a random video from a YouTube channel and open it in the default web browser.')
    parser.add_argument('channel_name', type=str, help='The name of the YouTube channel, e.g., @KillTony')
    args = parser.parse_args()

    # Construct the channel URL
    channel_url = f'https://www.youtube.com/c/{args.channel_name}'

    # Fetch and open a random video
    video_url = get_random_video_url(channel_url)
    if video_url:
        open_video_in_browser(video_url)
    else:
        print("No videos found for the specified channel.")