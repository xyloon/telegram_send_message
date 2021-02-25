#!/usr/bin/env python

from telethon import TelegramClient, sync
import configparser
import argparse
import os


def make_check_if_print_message_print_help(parser):
    def method(cond, message):
        if cond:
            print(message)
            parser.print_help()
            exit(0)
    return method


def check_parameter():
    parser = argparse.ArgumentParser(
        description='Sending One message to someone')
    parser.add_argument('message', metavar='M', nargs='?',
                        type=str, help='message contents', default="test message")
    parser.add_argument('--message-window', nargs='?', type=str,
                        help='target message window name')
    parser.add_argument('--attach-file', nargs='?', type=str,
                        help='file path and contents')
    args = parser.parse_args()

    check_if_print_message_help = make_check_if_print_message_print_help(
        parser)

    check_if_print_message_help(args.attach_file and
                                not os.path.exists(args.attach_file),
                                "File does not exists")
    return args


def read_config(config_file: str = 'conf/config.ini'):
    config = configparser.ConfigParser()
    config.read('conf/config.ini')
    return {
        "id": config['TELEGRAM']['api_id'],
        "hash": config['TELEGRAM']['api_hash']
    }


def main():
    args = check_parameter()
    config = read_config()
    client = TelegramClient('telegram_client_test',
                            config["id"], config["hash"]).start()
    me = client.get_me()
    message_window_str = args.message_window if args.message_window else " ".join(
        (me.first_name, me.last_name))

    for dialog in filter(lambda x: x.name == message_window_str,
                         client.get_dialogs()):
        dialog.send_message(args.message, file=args.attach_file)


if __name__ == '__main__':
    main()
