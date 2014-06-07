from fb import fb
import json
import pickle

print "downloading me"
myInfo = fb("me")
print "downloding my friends"
myInfo['friends'] = fb("me/friends")

people = [myInfo]
nfriends = len(myInfo['friends'])
i = 1
for friend in myInfo['friends']:
    print str(i) + ' / ' + str(nfriends)
    i = i + 1
    ref = friend['id']
    if 'name' in friend:
        ref = friend['name']
    elif 'username' in friend:
        ref = friend['username']
    print "downloading " + ref
    friendInfo = fb(friend['id'])
    print "downloading " + ref + " friends"
    friendInfo['friends'] = fb(friend['id']+'/mutualfriends')
    people.append(friendInfo)


with open('fb-friends.pickle', 'wb') as handle:
    pickle.dump(people, handle)

with open('fb-friends.json', 'wb') as handle:
    handle.write(json.dumps(people))
