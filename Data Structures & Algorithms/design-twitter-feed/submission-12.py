import heapq

class Twitter:

    def __init__(self):
        self.twitter = {}
        self.t = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.twitter:
            self.twitter[userId] = {"tweets": [], "followers": set(), "following": set()}
        self.twitter[userId]["tweets"].append((-self.t, tweetId))
        self.twitter[userId]["tweets"].sort()
        self.t += 1
        # print(f"after postTweet({userId}, {tweetId}): {self.twitter}")

    def getNewsFeed(self, userId: int) -> List[int]:
        c = 0
        rt = []
        tc = self.twitter

        heap = []

        if len(self.twitter[userId]["tweets"]) > 0:
            heapq.heappush(heap, (self.twitter[userId]["tweets"][0], userId, 0))
        for f in self.twitter[userId]["following"]:
            if f == userId:
                continue
            if len(self.twitter[f]["tweets"]) > 0:
                heapq.heappush(heap, (self.twitter[f]["tweets"][0], f, 0))
        # print(f"starting state: heap = {heap}")
    
        while c < 10 and heap:
            most_recent = heapq.heappop(heap)
            # print(f"most_recent: {most_recent}")
            # print(f"heap post pop: {heap}")
            time = most_recent[0][0]
            tweet = most_recent[0][1]
            userId = most_recent[1]
            index = most_recent[2]
            # print(f"index: {index}")
            # most_recent has shape ((time, tweet), userId)
            rt.append(tweet)
            if index + 1 < len(self.twitter[userId]["tweets"]):
                heapq.heappush(heap, (self.twitter[userId]["tweets"][index+1], userId, index+1))
            # print(f"heap post push: {heap}")
            c += 1
        
        return rt
           

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.twitter:
            self.twitter[followerId] = {"tweets": [], "followers": set(), "following": set()}
        self.twitter[followerId]["following"].add(followeeId)
        
        if followeeId not in self.twitter:
            self.twitter[followeeId] = {"tweets": [], "followers": set(), "following": set()}
        self.twitter[followeeId]["followers"].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.twitter[followerId]["following"].discard(followeeId)
        self.twitter[followeeId]["followers"].discard(followerId)
