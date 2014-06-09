from multiprocessing import Pool
import json
import pickle
from fb import fb

print "downloading me"
myInfo = fb("me")
print "downloding my friends"
myInfo['friends'] = fb("me/friends")

def getFriendandFriends(friend):
    ref = friend['id']
    if 'name' in friend:
        ref = friend['name']
    elif 'username' in friend:
        ref = friend['username']
    print "downloading " + ref
    friendInfo = fb(friend['id'])
    print "downloading " + ref + " friends"
    friendInfo['friends'] = fb(friend['id']+'/mutualfriends')
    return friendInfo

if __name__ == '__main__':
    # 8 processors
    p = Pool(8)
    people = p.map(getFriendandFriends, myInfo['friends'])
    people.append(myInfo)

    # with open('fb-friends.pickle', 'wb') as handle:
    #     pickle.dump(people, handle)

    with open('fb-friends.json', 'wb') as handle:
        handle.write(json.dumps(people))
