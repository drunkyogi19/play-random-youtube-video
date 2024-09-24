# Random YouTube Video Selector

This script selects a random video from a specified YouTube channel and opens it in the default web browser. The channel name is provided as a command-line argument.

## Features

- Fetches all video URLs from the specified YouTube channel.
- Randomly selects one of the videos.
- Opens the selected video in the default web browser.

## Requirements

- Python 3.x
- `pytube` package

## Setup

1. **Clone the repository**

    ```sh
    git clone https://github.com/yourusername/random-youtube-video-selector.git
    cd random-youtube-video-selector
    ```

2. **Create a virtual environment and install dependencies**

    The provided batch file `setup_and_run.bat` handles creating a virtual environment and installing the necessary packages. It will also run the script with the default channel name `@KillTony`.

    **To run the batch file:**

    ```sh
    setup_and_run.bat
    ```

## Usage

To use the script with a different YouTube channel, you can modify the batch file or run the script directly with the desired channel name.

### Running the Python Script Directly

1. **Activate the virtual environment**

    On Windows:

    ```sh
    .venv\Scripts\activate
    ```

    On macOS and Linux:

    ```sh
    source .venv/bin/activate
    ```

2. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

3. **Run the script**

    ```sh
    python random_kt_episode.py @YourChannelName
    ```

### Batch File Usage

The batch file automates the setup and execution process:

```bat
@echo off

If Not Exist "%~dp0%\.venv\Scripts\activate.bat" (
    python -m venv .venv
    call "%~dp0%\.venv\Scripts\activate"
    pip install -r requirements.txt
)

call "%~dp0%\.venv\Scripts\activate"
python random_kt_episode.py @KillTony
pause
```

- The batch file checks if the virtual environment exists, creates it if it doesn't, and installs the requirements.
- It then activates the virtual environment and runs the random_kt_episode.py script using @KillTony as the default channel name.

To use a different channel, modify the batch file's last line to:

```bat
python random_kt_episode.py @YourChannelName
```
