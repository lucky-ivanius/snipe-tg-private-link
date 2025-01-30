import getopt
import sys
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (ImportChatInviteRequest)

def start_listener(opts):

    api_id = int(opts[0].__getitem__(1))
    api_hash = opts[1].__getitem__(1)
    channel = opts[2].__getitem__(1).lstrip('@')

    url_regex = r"https:\/\/t\.me\/\+(\S+)"

    user_input_channel = 'https://t.me/' + channel

    client = TelegramClient('auth', api_id, api_hash)
    client.start()

    @client.on(events.NewMessage(chats=user_input_channel))
    async def new_message_listener(event):
        event_message = event.message.message
        filtered_message = re.findall(
            url_regex, event_message, flags=re.IGNORECASE)
        if len(filtered_message) != 0:
            for hash in filtered_message:
                try:
                    update = await client(ImportChatInviteRequest(hash))
                    print(update)
                except Exception as e:
                    print(f"Error joining channel with hash {hash}: {str(e)}")

    with client:
        client.run_until_disconnected()


argv = sys.argv[1:]
usage = "usage: bot.py --api_id=<api_id> --api_hash=<api_hash> --channel=<channel>"
try:

    opts, args = getopt.getopt(
        argv, 'a:b:c:', ['api_id=', 'api_hash=', 'channel='])
    # Check if the options' length is 4 (can be enhanced)
    if len(opts) == 0 or len(opts) > 3:
        print(usage)
    else:
        # Start the listener
        print("Starting the listener for channel: {channel}".format(channel=opts[2].__getitem__(1).lstrip('@')))
        start_listener(opts)

except getopt.GetoptError:
    print(usage)
    sys.exit(1)