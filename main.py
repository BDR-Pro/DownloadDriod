from telethon import TelegramClient, events
import os
from dd import download_youtube_video, get_thumbnail, get_title

# Ensure these are the correct credentials from your Telegram application

api_id = input("Enter your API ID: ")
api_hash = input("Enter your API Hash: ")
bot_token = input("Enter your bot token: ")


client = TelegramClient('bot', api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! How can I help you today?')
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond('Download any video from YouTube, Instagram, or Twitter by sending me the link.')
    raise events.StopPropagation

@client.on(events.NewMessage)
async def download(event):
    if not event.message.message.startswith("http"):
        await event.respond("Please send a valid URL.")
        return

    url = event.message.message.strip()
    file_path = None  # Initialize file_path to ensure it's defined for later cleanup

    try:
        await event.respond('Downloading the video...')
        if 'instagram' in url:
            #file_path = insta(url)
            await event.respond('Instagram download is not supported yet. Please try again later.')
        elif 'x.com' in url:
            await event.respond('Twitter download is not supported yet. Please try again later.')
        elif 'youtube' in url:
            title = get_title(url.split('v=')[-1])
            await event.respond(title)
            thumbnail_path = get_thumbnail(url.split('v=')[-1])
            await client.send_file(event.sender_id, thumbnail_path, caption='Thumbnail')
            file_path = download_youtube_video(url.split('v=')[-1])
            # Send the video if download was successful
            if file_path:
                await event.respond('Download successful, now sending the video...')
                await client.send_file(event.sender_id, file_path, caption='Here is your video')
        else:
            await event.respond('Failed to download the video. Please check the URL.')

    except Exception as e:
        await event.respond(f'An error occurred: {str(e)}')

    # Clean up the downloaded file and thumbnail
    if file_path and os.path.exists(file_path):
        os.remove(file_path)
    if 'youtube' in url and thumbnail_path and os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)

async def main():
    await client.start(bot_token=bot_token)
    await client.run_until_disconnected()

if __name__ == '__main__':
    print('Starting the bot...')
    client.loop.run_until_complete(main())
