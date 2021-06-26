# put your python code here
words = list(input().split(' '))
print(words)
wordDict = dict() 
for word in words:
    word = word.lower()
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1

for k, v in wordDict.items():
    print(k, v)
