# telegram_send_message


## Preparing to use

### creating ini file

You can find out your id and hash at this link
https://pypi.org/project/Telethon/0.9/#obtaining-your-telegram-api-id-and-hash

And then you have to create config.ini file in the conf directory

### Installing dependencies for this code

```bash
pip install -U -r requirements.txt
```

## Sending message

### Send one message to me

```bash
src/send_one_message.py "some message to me"
```

### Send message to windows

For example the window name is "Tony Jaa",
You can send a message to "Tony Jaa" windows (You have to create this messaging windows)

```bash
src/send_one_message.py --message-window "Tony Jaa" "message to Tony"
```
