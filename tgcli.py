import os
import sys

from telegram.ext import Updater, CommandHandler

import telegram
import argparse

"""
Requirements:-

Install python-telegram-bot package:-

python3 -mvenv . # create virtualenv in current directory
./bin/pip install python-telegram-bot

Usage:-

./bin/python tgsend.py <TOKEN> --send="test direct cli group" --chat_id=-<chat_id>
./bin/python tgsend.py <TOKEN> # listen for message
"""

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello World! The chat_id for this is %d' % update.message.chat_id)

def hello(bot, update):
    print(update)
    bot.sendMessage(update.message.chat_id,
                  text='Hello {}'.format(update.message.from_user.first_name))

def chat_id(bot, update):
    text='The chat_id for this is %d. Take note that chat_id for group is negative number' % update.message.chat_id
    bot.sendMessage(update.message.chat_id, text)

def main():
    parser = argparse.ArgumentParser(description='Run TG Bot')
    parser.add_argument('token', type=str)
    parser.add_argument('--send', dest='message')
    parser.add_argument('--chat_id', dest='chat_id')
    parser.add_argument('--webhook', dest='webhook')

    args = parser.parse_args()

    updater = Updater(args.token)

    if args.message is not None:
        if os.path.isfile(args.message):
            text = open(args.message).read()
        else:
            text = args.message

        # not all markdown supported
        # https://core.telegram.org/bots/api#formatting-options
        updater.bot.sendMessage(args.chat_id, text=text,
                                parse_mode=telegram.ParseMode.MARKDOWN)
        updater.stop()
        sys.exit()

    if args.webhook is not None:
        if args.webhook == 'info':
            print(updater.bot.get_webhook_info())
        else:
            updater.bot.setWebhook(args.webhook)

        updater.stop()
        sys.exit()

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('chat_id', chat_id))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
