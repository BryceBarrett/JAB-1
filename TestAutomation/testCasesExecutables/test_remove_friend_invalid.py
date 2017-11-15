import sys
import warnings
from dbus.mainloop.glib import DBusGMainLoop
warnings.filterwarnings("ignore")

sys.path.append('../Project/src/jarabe/model')
from friends import *

def test_remove_friend_invalid():
    mainloop = DBusGMainLoop(set_as_default=True)
    arguments = sys.argv[1].split(",")
    test = "null"
    try:
        friend1 = FriendBuddyModel(arguments[0], arguments[1], arguments[2], arguments[3])
        friend2 = FriendBuddyModel(arguments[0], arguments[1], arguments[2], arguments[3])
        os.chdir('../reports')
        f = open("testOutput.html", "a+")
        myFriends = Friends()
        myFriends.make_friend(friend1)
        myFriends.remove(friend1)
        test = str((myFriends.has_buddy(friend2)))
    except Exception as exception:
        return("Test Failed!: Exception: " +str(exception))
        
    try:
        test == sys.argv[2]
        return "Test Passed!" 

    except:
        return "Test Failed! Expected: " + sys.argv[2] + " but was: " + str(test)


if __name__ == '__main__':
    test_remove_friend_invalid()
    print(test_remove_friend_invalid())
