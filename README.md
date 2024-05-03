# Download Driod Bot

This Telegram bot is designed to download videos from various platforms including YouTube, directly through Telegram. It uses the Telethon library to interact with the Telegram API and custom modules to handle video downloads.

## Online Bot

click [here](https://t.me/DD_Magic_bot) to use the bot online.

## Features

- Download videos by sending a direct URL.
- Currently supports downloading from YouTube.
- Easy to expand with more platforms like Instagram and Twitter in the future.

## Requirements

- Python 3.6+
- Telethon
- Requests
- A valid Telegram API ID, API Hash, and Bot Token

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bdr-pro/DownloadDriod.git
   cd DownloadDriod
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration:**
   - You will be prompted to enter your Telegram API ID, API Hash, and Bot Token when you run the bot. Make sure to have them ready.

## Running the Bot

To run the bot, execute the following command in the root directory of your project:

```bash
python main.py

```

Follow the prompts to enter your Telegram credentials.

## Usage

- Send `/start` to initiate the bot.
- Send `/help` for information on how to use the bot.
- To download a video, send a valid URL to the bot. It currently supports URLs from YouTube. Support for other platforms can be added as needed.

## Adding More Platforms

To add support for other platforms, define additional functions for handling downloads similar to the existing `download_youtube_video`, `get_thumbnail`, and `get_title` functions.

## Contributing

Contributions to expand the bot's capabilities are welcome. Please submit a pull request or create an issue if you have ideas or find bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
