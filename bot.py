import getopt
import sys
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (ImportChatInviteRequest)

def startListener(opts):

    api_id = int(opts[0].__getitem__(1))
    api_hash = opts[1].__getitem__(1)
    channel = opts[2].__getitem__(1)

    shortURLRegex = r"https:\/\/t\.me\/\+(\S+)"

    user_input_channel = 'https://t.me/' + channel

    client = TelegramClient('auth', api_id, api_hash)
    client.start()

    @client.on(events.NewMessage(chats=user_input_channel))
    async def newMessageListener(event):
        messageFromEvent = event.message.message
        print("Received event with message:\n" + messageFromEvent)
        filteredMessage = re.findall(
            shortURLRegex, messageFromEvent, flags=re.IGNORECASE)
        if len(filteredMessage) != 0:
            for hash in filteredMessage:
                updates = await client(ImportChatInviteRequest(hash))
                print(updates)

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
        print("Starting the listener for channel: {channel}".format(channel=opts[2].__getitem__(1)))
        startListener(opts)

except getopt.GetoptError:
    print(usage)
    sys.exit(1)