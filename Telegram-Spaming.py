from telethon import TelegramClient
from telethon.errors import rpcerrorlist, FloodWaitError
import time
import os


if os.path.isfile('spamer.txt'):
    with open('spamer.txt', 'r') as r:
        data = r.readlines()
    api_id = int(data[0])
    api_hash = data[1]

else:
    api_id = input('Enter api_id: ')
    api_hash = input('Enter api_hash: ')
    with open('spamer.txt', 'w') as a:
        a.write(api_id + '\n' + api_hash)

client = TelegramClient('spamer', api_id, api_hash)


async def main():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    global target
    print(''' _____    _      _____                       
|_   _|  | |    /  ___|                      
  | | ___| | ___\ `--. _ __   __ _ _ __ ___  
  | |/ _ \ |/ _ \`--. \ '_ \ / _` | '_ ` _ \ 
  | |  __/ |  __/\__/ / |_) | (_| | | | | | |
  \_/\___|_|\___\____/| .__/ \__,_|_| |_| |_|
                      | |                    
                      |_| by Deleted-accounts''')
    print('\n\nhere is your chats, Please choose a target...')
    i = 0
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(i, ':', dialog.name, 'has ID', dialog.id)
        i = i + 1

    confirm = False
    max = len(dialogs) - 1

    while confirm == False:
        target_index = -1

        # Get target chat
        while target_index < 0 or target_index > max:
            print('Please insert target between 0 and', max)
            target_index = int(input())
            if target_index < 0 | target_index > max:
                print('target out of range')

        target = dialogs[target_index]
        print('target is', target.name, 'with ID', target.id)

        # Wait for confirm
        print('Correct? Y/N')
        reply = input()[0]
        if reply == 'Y' or reply == 'y':
            confirm = True

    message = input("Enter the message to send here: ")
    treads = int(input("How many messages do you want to send?\n"))

    print("If you made some mistake with target, this is the last time you can Ctrl-Z")
    print('Start spaming in 3 sec...')
    time.sleep(3)
    print("[+] The spam started")
    try:
        for i in range(int(treads)):
            await client.send_message(target.id, message)
        print("[+] spam successful")
    except rpcerrorlist.ChatAdminRequiredError:
        print("[!] You do not have permission to post messages in this chat!")
    except FloodWaitError:
        print("[!] try again after one hour")


with client:
    client.loop.run_until_complete(main())
