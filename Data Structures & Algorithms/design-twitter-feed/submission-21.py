import heapq
from collections import deque 

class Twitter:

    def __init__(self):
        self.tweets = dict(deque())
        self.followings = dict(set()) # map of follower -> following for each acc
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = deque()
            self.followings[userId] = set()
        self.tweets[userId].appendleft((-self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if len(self.tweets[userId]) > 0:
            heapq.heappush(heap, (self.tweets[userId][0], userId, 0))

        for f in self.followings[userId]:
            if f != userId:
                heapq.heappush(heap, (self.tweets[f][0], f, 0))

        c = 0
        rt = []
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
        if followerId not in self.followings:
            self.tweets[followerId] = deque()
            self.followings[followerId] = set()
        self.followings[followerId].add(followeeId)
        if followerId not in self.tweets:
            self.tweets[followerId] = deque()
            self.followings[followerId] = set()

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)