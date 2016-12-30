import requests
import configparser
import time

clientinfo = {}
streams = {}
streamids = []

def main():
    configfile = 'bot.ini'
    config = configparser.ConfigParser()
    config.read(configfile)

    clientinfo['baseurl'] = config['client']['baseurl']
    clientinfo['client-id'] = config['client']['client-id']
    clientinfo['usernames'] = [e.strip() for e in config['client']['usernames'].split(',')]
    clientinfo['webhook'] = config['client']['webhook']

    starttime = time.time()

    while True:
        mainloop()
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

def mainloop():
    print("running main loop")
    global streamids
    global streams
    update_flag = False

    streams_current = {}

    print("Current list of stream ids: {}".format(streamids))

#     for user in clientinfo['usernames']:
        # current_streams[user] = get_online_status(user)
        # if streams[user]['online'] and streams[user]['id'] not in streamids
            # announce_user(streams[user])
            # current_streamids.append(streams[user]['id'])
            # update_flag = True
    # if update_flag:
        # streamids = current_streamids

    ########

    streams_current = get_streams(clientinfo['usernames'])

    streamids_diff = compare_streams(streams, streams_current)

    # for streamid in streamids_diff:
    
def announce_stream(stream):
    announce = "{} has gone live! (Playing {})".format(stream['url'], stream['game'])

    print(announce)
    
    payload = {'text' : announce}

    p = requests.post(clientinfo['webhook'], json=payload)

def get_streams(usernames):
    streams = {}
    headers = {'Client-ID': clientinfo['client-id']}

    for user in usernames:
        print("Checking {}".format(user))
        r = requests.get(clientinfo['baseurl'] + user, headers=headers)
        res = r.json()

        print(res)

        if res['stream'] != None:
            stream_id = res['stream']['_id']
            streams[stream_id] = {}
            streams[stream_id]['username'] = user
            streams[stream_id]['game'] = res['stream']['game']
            streams[stream_id]['url']  = res['stream']['channel']['url']
            
    return streams

def compare_streams(streams_prev, streams_current):
    streamids_changed = {}
    streamids_changed['offline'] = []
    streamids_changed['online'] = []

    for key in streams_prev:
        if key not in streams_current:
            streamids_changed['offline'].append(key)

    for key in streams_current:
        if key not in streams_prev:
            streamids_changed['online'].append(key)
    
    return streamids_changed

def announce_streams(streamids_changed, streams):
    announce_offline = "{} stopped streaming. (Was playing {})"
    announce_online  = "{} has gone live! (Playing {})"
    announce_list = []

    # Streams that have gone offline since last check
    for streamid in streamids_changed['offline']:
        ann = announce_offline.format(streams[streamid]['url'], streams[streamid]['game'])
        announce_list.append(ann)

    # Streams that are new since last check
    for streamid in streamids_changed['online']:
        ann = announce_online.format(streams[streamid]['url'], streams[streamid]['game'])
        announce_list.append(ann)

    for item in announce_list:
        print(item)
        payload = {'text': item}
        p = requests.post(clientinfo['webhook'], json=payload)

if __name__ == "__main__":
    main()
