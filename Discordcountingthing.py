import requests
import time

# Ask the user for input
mode = input("Do you want to send a message to a server or a DM? (s/d): ")
auth_token = input("Enter your authorization token: ")

# Set up the request headers and message data
auth = {
   'authorization': auth_token
}
msg = {
    'content': ''
}

if mode == 's':
    # Ask for server ID and channel ID, then send messages to it
    server_id = input("Enter the server ID: ")
    channel_id = input("Enter the channel ID: ")
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    
    # sending messages with numbers from 1 to 1000000
    for i in range(1, 1000001):
        msg['content'] = str(i)
        requests.post(url, headers=auth, data=msg)

        if i % 5 == 0:
            print("Rate Limit Bypass :)")
            time.sleep(5) # pause for 5 seconds after every 5 messages

        time.sleep(1) # delay for 1 second between messages

elif mode == 'd':
    # Ask for recipient ID, create a DM channel, and send messages to it
    recipient_id = input("Enter the recipient's ID: ")
    url = "https://discord.com/api/v9/users/@me/channels"
    data = {"recipient_id": recipient_id}
    r = requests.post(url, headers=auth, json=data)
    if r.status_code != 200:
        print(f"Error creating DM channel: {r.status_code}")
        exit()

    channel_id = r.json()['id']
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    # sending messages with numbers from 1 to 1000000
    for i in range(1, 1000001):
        msg['content'] = str(i)
        requests.post(url, headers=auth, data=msg)

        if i % 5 == 0:
            print("Rate Limit Bypass :)")
            time.sleep(5) # pause for 5 seconds after every 5 messages

        time.sleep(1) # delay for 1 second between messages

else:
    print("Invalid mode selected. Please enter 's' or 'd' as the mode.")






