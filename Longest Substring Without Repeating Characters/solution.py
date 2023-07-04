def lengthOfLongestSubstring(s: str) -> int:
        maxLength = 0
        dict = {}

        i,j = 0,0
        n = len(s)

        while(j < n):
            c = s[j]     
            
            dict[c] = 1 if not c in dict else dict[c] + 1
            print(dict)
            
            if dict[c] > 1:
                while(dict[c] > 1):
                    dict[s[i]] -= 1
                    i += 1
                    
            maxLength = max(maxLength, j - i + 1)
            j += 1
            print(dict)
            print(i,j,maxLength)

        return maxLength

print(lengthOfLongestSubstring('pwwkew'))