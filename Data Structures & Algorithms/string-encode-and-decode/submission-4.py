class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += "#"
            encoded += string
        return encoded

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            char = s[i]
            # print(f"processing {char}")
            if char.isdigit():
                number = ""
                k = 0
                while char.isdigit():
                    number += char
                    k += 1
                    char = s[i+k]
                num = int(number)
                # print(f"collected {num}")
                # skip the next hashtag and then iterate for 
                string = ""
                for j in range(1+k, num+k+1):
                    # print(f"in inner loop, processing {s[i+j]}")
                    string += s[i+j]
                i += num + 2
                output.append(string)
            else:
                i += 1
        
        return output