# twitch slack notification bot

This is a simple bot that notifies your Slack and Discord channel(s) when people start
streaming on Twitch. 

# Requirements & Configuration

It's written in Python 3 and the only external dependency is the 'requests'
library. 

Copy 'bot.ini.example' to 'bot.ini' and modify as necessary. You'll need to
setup Slack and Discord incoming webhooks, as well as obtain a Twitch client-ID.  (Twitch
no longer allows API access without a client ID.)

Note for Discord: make sure you use the Slack-compatible webhook URL.

# Usage

Run main.py, preferably within a screen or tmux instance.  It will poll your
chosen list of users every 60 seconds looking for changes. To exit simply hit
ctrl-C.

# To Do

Currently I'm using this in both Slack and Discord so it assumes both webhooks exist. I need to add checking to see if one or the other webhook config items are blank and send messages accordingly.

# Author 

James Curbo <james@curbo.org>


