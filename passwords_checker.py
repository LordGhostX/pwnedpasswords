#a password checker!!!!!!!
#checks if your password has every been hacked, how cool is this?

import requests #manually requesting for data from a browser
import hashlib
import sys
#hash your passwords (there are online hash generators,depends on your API)
#k anonimity: ensures your passwords aren't linked to your identity online

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'There\'s an error fetching: {response.status_code}, check your API and try again')
    return response
def get_password_hacks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for x,count in hashes:
        #print(x,count)
        if x == hash_to_check:
            return count
    return 0
def api_check(password):
    #print(hashlib.sha1(password.encod('utf-8').hexdigest().upper()))
    hashd_password = hashlib.sha1(password.encode('utf-8').upper()).hexdigest()
    #print(hashd_password)
    first5, tail = hashd_password[0:5], hashd_password[5:]
    password_response = request_api_data(first5)
    #print(password_response)
    return get_password_hacks(password_response,tail)

def omar(args):
    for password in args:
        count = api_check(password)
        if count:
            print(f'The password was found {count} times')
        else:
            print('Way to go')

if __name__ == '__main__':
    sys.exit(omar(sys.argv[1:]))