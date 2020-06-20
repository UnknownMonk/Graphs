import random


class User:
    def __init__(self, name):
        self.name = name


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"User {i}")
        # Create friendships
        possibleFriendships = []

        for userId in self.users:
            print(self.lastID)
            for friendID in range(userId + 1, self.lastID + 1):
                possibleFriendships.append((userId, friendID))
        random.shuffle(possibleFriendships)

        for friendship_index in range(0, avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

        print(possibleFriendships)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.


        """
        visited = {}
        # Note that this is a dictionary, not a set
        q = Queue()
        q.enqueue([userID])
        # !!!! IMPLEMENT ME

        while q.size() > 0:
            path = q.dequeue()
            newUserID = path[-1]
            if newUserID not in visited:
                visited[newUserID] = path
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)

    print(connections)


# $ python social.py
# [(2, 4), (1, 5), (2, 10), (9, 10), (5, 7), (6, 8), (5, 10), (4, 7), (1, 6), (2, 8), (4, 8), (6, 9), (1, 7), (2, 5), (7, 9), (3, 5), (4, 5), (4, 10), (4, 6), (2, 3), (3, 8), (5, 6), (2, 7), (3, 6), (1, 8), (5, 8), (8, 10), (7,
# 10), (1, 2), (2, 6), (3, 7), (2, 9), (5, 9), (8, 9), (1, 10), (1, 3), (7, 8), (3, 10), (4, 9), (1, 9), (3, 9), (1, 4), (6, 7), (3, 4), (6, 10)]
# {1: {5, 6}, 2: {8, 10, 4}, 3: set(), 4: {2, 7}, 5: {1, 10, 7}, 6: {8, 1}, 7: {4, 5}, 8: {2, 6}, 9: {10}, 10: {9,
# 2, 5}}
# {1: [1], 5: [1, 5], 6: [1, 6], 10: [1, 5, 10], 7: [1, 5, 7], 8: [1, 6, 8], 9: [1, 5, 10, 9], 2: [1, 5, 10, 2], 4: [1, 5, 7, 4]}

# JOE@JOE-PC MINGW32 /d/Documents/Lambda_CS/Graphs/projects/social (jonas-walden)
# $ python social.py
# [(5, 8), (4, 6), (4, 5), (9, 10), (1, 2), (1, 8), (2, 7), (2, 3), (4, 9), (7, 10), (8, 9), (2, 10), (2, 9), (2, 4), (7, 9), (1, 4), (3, 8), (2, 8), (3, 10), (2, 6), (5, 9), (1, 7), (4, 7), (4, 10), (4, 8), (1, 5), (7, 8), (6,
# 10), (5, 10), (3, 6), (6, 7), (6, 8), (8, 10), (1, 6), (2, 5), (5, 6), (1, 10), (3, 9), (3, 5), (3, 7), (6, 9), (5, 7), (1, 9), (3, 4), (1, 3)]
# {1: {8, 2}, 2: {1, 3, 7}, 3: {2}, 4: {9, 5, 6}, 5: {8, 4}, 6: {4}, 7: {2, 10}, 8: {1, 5}, 9: {10, 4}, 10: {9, 7}}
# {1: [1], 8: [1, 8], 2: [1, 2], 5: [1, 8, 5], 3: [1, 2, 3], 7: [1, 2, 7], 4: [1, 8, 5, 4], 10: [1, 2, 7, 10], 9: [1, 8, 5, 4, 9], 6: [1, 8, 5, 4, 6]}
