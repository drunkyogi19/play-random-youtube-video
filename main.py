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


def get_random_video_with_certain_guest(channel_url, guest_name):
    # Initialize the Channel object from pytube
    channel = Channel(channel_url)

    # Process guest_name : convert to upper, since titles are returned in upper case
    guest_name = guest_name.upper()
    # if a guest_name is provided, search in channel videos to find a video whose title has the guest_name in it
    videos = [video for video in channel.videos]

    # Shuffle the list to so we get different episodes each time
    random.shuffle(videos)
    for video in videos:
        if guest_name in video.title:
            print(f"Now playing: {video.title}")
            return video.watch_url


def open_video_in_browser(video_url):
    # Open the video URL using the default web browser
    webbrowser.open(video_url)


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description='Get a random video from a YouTube channel and open it in the default web browser.')
    parser.add_argument('--channel_name', type=str, help='The name of the YouTube channel, e.g., @KillTony',
                        required=True)
    parser.add_argument('--guest_name', type=str, help='Guest in an Episode, e.g., Adam_Ray', required=False)
    args = parser.parse_args()

    # Construct the channel URL
    channel_url = f'https://www.youtube.com/c/{args.channel_name}'

    # Fetch a video with a certain guest
    if args.guest_name is not None:
        video_url = get_random_video_with_certain_guest(channel_url, guest_name=args.guest_name)

    else:
        video_url = get_random_video_url(channel_url)

    if video_url:
        open_video_in_browser(video_url)
    else:
        print("No videos found for the specified channel.")
