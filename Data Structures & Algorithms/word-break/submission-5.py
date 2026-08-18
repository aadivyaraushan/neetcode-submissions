class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # what choices at any step?
        # 1. continue current word tracking
        # 2. a word is found, so add word to found set, restart -> this requires resetting starting point
        # 3. if we reach end of s, then exit the recursive function

        # what's minimum info needed to make this work?
        # 1. current substr being tracked -> given by start, len of substr actly
        # with that state,
        # base case: start == len(s) -> return
        # recursive case:
        # 1. if start:start+len_of_substr in wordDict word is found so add word to found set and recursively
        # call recurse(start+length, 1)
        # 2. if it isn't, recurse(start, len+1) i.e. move length processing forward

        # check w input
        # neetcode, words = neet, code
        # initial call recurse(0, 1)
        # n -> not, recurse(start, 2)
        # ne -> not, recurse(start, 3)
        # nee -> not, recurse(start, 4)
        # neet. neet found so found = (neet). caling recurse(start+length, 1)
        # c -> not, recurse(5, 2)
        # co
        # cod
        # code -> found = (neet, code), calling recurse(8, 1)
        # start >= len -> exit
        c = 0
        memo = []
        for i in range(len(s)+2):
            row = []
            for j in range(len(s)+2):
                row.append(-1)
            memo.append(row)

        found = False

        def recurse(start, length):
            # stores whether its possible to break down
            # a string from 'start' onwards into 
            # space-separated seq of dictionary words
            nonlocal s
            nonlocal found
            print(f"calling w/ length: {length}")
            
            if start >= len(s):
                memo[start][length] = True
                return True
            if start+length > len(s):
                memo[start][length] = False
                return False
            if memo[start][length] != -1:
                return memo[start][length]
            # print(f"{s[start:start+length]}")
            memo[start][length] = recurse(start, length+1)
            if s[start:start+length] in wordDict:
                # print(f"word is in wordDict")
                memo[start][length] = memo[start][length] or recurse(start+length, 1)
            return memo[start][length]
        
        # print(f"post loop, c = {c}")

        return recurse(0, 1)


        # at end, return len found == len word dict