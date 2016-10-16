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
    update_flag = False

    print("Current list of stream ids: {}".format(streamids))
    current_streamids = []
    for user in clientinfo['usernames']:
        streams[user] = get_online_status(user)
        if streams[user]['online'] and streams[user]['id'] not in streamids
            announce_user(streams[user])
            current_streamids.append(streams[user]['id'])
            update_flag = True
    if update_flag:
        streamids = current_streamids
    
def announce_user(streaminfo):
    announce = "{} has gone live! (Playing {})".format(streaminfo['url'], streaminfo['game'])

    print(announce)
    
    payload = {'text' : announce}

    p = requests.post(clientinfo['webhook'], json=payload)

def get_online_status(username):
    print("checking status of {}".format(username))

    streaminfo = {}
    baseurl = clientinfo['baseurl']
    headers = {'Client-ID': clientinfo['client-id']}

    r = requests.get(baseurl + username, headers=headers)

    res = r.json()

    if res['stream'] == None:
        streaminfo['online'] = False
    else:
        streaminfo['online'] = True
        streaminfo['url'] = res['stream']['channel']['url']
        streaminfo['game'] = res['stream']['game']
        streaminfo['id'] = res['stream']['_id']
        print(streaminfo)

    return streaminfo

if __name__ == "__main__":
    main()
