# twitch slack notification bot

This is a simple bot that notifies your Slack channel when people start
streaming on Twitch. 

# Requirements & Configuration

It's written in Python 3 and the only external dependency is the 'requests'
library. 

Copy 'bot.ini.example' to 'bot.ini' and modify as necessary. You'll need to
setup a Slack incoming webhook, as well as obtain a Twitch client-ID.  (Twitch
no longer allows API access without a client ID.)

# Usage

Run main.py, preferably within a screen or tmux instance.  It will poll your
chosen list of users every 60 seconds looking for changes. To exit simply hit
ctrl-C.

# Author James Curbo <james@curbo.org>


