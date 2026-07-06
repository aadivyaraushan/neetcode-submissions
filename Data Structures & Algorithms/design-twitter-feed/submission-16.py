import heapq
from collections import deque 

class Twitter:

    def __init__(self):
        self.tweets = dict(deque())
        self.followers = dict(set())
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque()
            self.followers[userId] = set()
        self.tweets[userId].appendleft((-self.t, tweetId))
        self.t += 1
        print(f"after postTweet({userId}, {tweetId}), tweets = {self.tweets} and followers = {self.followers}")

    def getNewsFeed(self, userId: int) -> List[int]:
        print(f"starting getNewsFeed({userId})")
        heap = []
        if len(self.tweets[userId]) > 0:
            heapq.heappush(heap, (self.tweets[userId][0], userId, 0))

        # add tweet IDs in similar structure from 
        following = []
        for followee, followers in self.followers.items():
            print(f"followee = {followee} and follower = {followers}")
            if userId in followers and followee != userId:
                following.append(followee)
        for f in following:
            heapq.heappush(heap, (self.tweets[f][0], f, 0))

        c = 0
        rt = []
        print(f"init heap state: {heap}")
        while heap and c < 10:
            most_recent = heapq.heappop(heap)
            # structure of a heap element: ((time, tweetId), userId, index)
            time = most_recent[0][0]
            tweetId = most_recent[0][1]
            userId = most_recent[1]
            index = most_recent[2]


            rt.append(tweetId)
            if index+1 < len(self.tweets[userId]):
                heapq.heappush(heap, (self.tweets[userId][index+1], userId, index+1))

            c += 1 
        return rt

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers:
            self.tweets[followeeId] = deque()
            self.followers[followeeId] = set()
        self.followers[followeeId].add(followerId)
        if followerId not in self.tweets:
            self.tweets[followerId] = deque()
            self.followers[followerId] = set()
        print(f"after follow({followerId}, {followeeId}),  followers = {self.followers}")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
        print(f"after unfollow({followerId}, {followeeId}),  followers = {self.followers}")