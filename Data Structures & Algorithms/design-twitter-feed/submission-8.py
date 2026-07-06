import heapq

class Twitter:

    def __init__(self):
        self.twitter = {}
        self.t = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.twitter:
            self.twitter[userId] = {"tweets": [], "followers": set(), "following": set()}
        heapq.heappush(self.twitter[userId]["tweets"], (-self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for account in self.twitter[userId]["following"]:
            tweets.extend(self.twitter[account]["tweets"])
        tweets.extend(self.twitter[userId]["tweets"])

        tweets = list(set(tweets))
        heapq.heapify(tweets)
        n = 0
        rt = []
        while n < 10:
            if len(tweets) == 0:
                break
            recent = heapq.heappop(tweets)
            rt.append(recent[1])
            n += 1
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
