from telethon import TelegramClient
from telethon.errors import FloodWaitError
import time

# Use your own values from my.telegram.org
api_id = int(input("enter your app id: "))
api_hash = input("enter your app hash: ")

client = TelegramClient('spamer', api_id=api_id, api_hash=api_hash)


async def main():
    global destination, target
    print('Here are your opened chat:')

    i = 0
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(i, ':', dialog.name, 'has ID', dialog.id)
        i = i + 1

    confirm = False
    max = len(dialogs) - 1

    while (confirm == False):
        destination_index = -1

        # Get destination chat
        while destination_index < 0 or destination_index > max:
            print('Please insert destination between 0 and', max)
            destination_index = int(input())
            if destination_index < 0 | destination_index > max:
                print('Destination out of range')

        destination = dialogs[destination_index]
        print('Destination is', destination.name, 'with ID', destination.id)

        # Wait for confirm
        print('Correct? Y/N')
        reply = input()[0]
        if reply == 'Y' or reply == 'y':
            confirm = True

    message = input("Enter the message to send here: ")
    treads = int(input("How many messages do you want to send?\n"))

    print("If you made some mistake with destination, this is the last time you can Ctrl-Z")
    print('Start spaming in 5 sec...')
    time.sleep(5)
    try:
        for i in range(int(treads)):
            await client.send_message(destination.id, message)
        print("[+] spam successful")
    except FloodWaitError:
        print("stoping...")


with client:
    client.loop.run_until_complete(main())
