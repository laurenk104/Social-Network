class User:

    def __init__(self, name):
        self.name = name
        self.id = 0
        self.connections = []

    def addFriend(self, connection):
        self.connections.append(connection)

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def printFriends(self):
        for friends in self.connections:
            print(friends.getName())

class Network:

    def __init__(self):
        self.users = []

    def addUser(self, name):
        self.users.append(name)

    def printUsers(self):
        for user in self.users:
            print(user.getName())

    def addConnection(self, user1, user2):
        user1.addFriend(user2)
        user2.addFriend(user1)

        #print("Would you like to create a user (c), add a friend (f), see your friends (p), or quit (q)?")

def main():
    myNetwork = Network()
    print("Would you like to create a user (c) or quit (q)?")
    answer = input()
    if answer == "c":
        print("Choose a username")
        username = input()
        user1 = User(username)
        myNetwork.addUser(user1)
        print("Would you like to create a user (c) or quit (q)?")
        answer = input()
        if answer == "c":
            print("Choose a username")
            username = input()
            user2 = User(username)
            myNetwork.addUser(user2)
            print("Would you like to create a user (c), add a friend (f), or quit (q)?")
            answer = input()
            if answer == "c":
                print("Choose a username")
                username = input()
                user3 = User(username)
                myNetwork.addUser(user3)
            elif answer == "f":
                print("Choose the user requesting to be friends")
                friendMaker = input()
                print("Choose the user who recieved the request")
                friendAccepter = input()
                print("Does this person accept the request?")
                answer = input()
                if answer == "no":
                    print("Sorry, your request was denied")
                elif answer == "yes":
                    myNetwork.addConnection(User(friendMaker), User(friendAccepter))
                    print(friendMaker + " and " + friendAccepter + " are friends!")
        else:
            exit()
    else:
        exit()

main()
