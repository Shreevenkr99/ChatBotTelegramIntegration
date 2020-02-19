#api_ID=333963
#api_secret=76a1fe909f584e0625c3a3f3ddb115f1

import time
from modelTrain import msgInteract
from telethon import TelegramClient, events

# Use your own values from my.telegram.org
api_id = 333963
api_hash = '76a1fe909f584e0625c3a3f3ddb115f1'

client = TelegramClient('anon', api_id, api_hash, sequential_updates=True)


@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if event.is_private:  # only auto-reply to private chats
        from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
        if not from_.bot:  # don't auto-reply to bots
            #print(time.asctime(), '-', event.message)  # optionally log time and message
            respond = msgInteract(event.message.message)
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            await event.respond(respond)


print(time.asctime(), '-', 'Auto-replying...')
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Stopped!')
    