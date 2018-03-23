import string as string

# set up some important global variables
wordList = {}
mString = ''
stopwordList = []

# read the stopwords
with open("C:\\Users\\twanv\\Desktop\\WordCloud\\stopwords", "r", encoding="utf8") as r:
        stopwordData = r.readlines()

        # remove /n newlines and save the stopwords in a global list
        for line in stopwordData:
            cleanedNewLineWord = line.replace('\n', '')
            stopwordList.append(cleanedNewLineWord)

# read the text that needs to be analysed and concatenate the lines to one string
with open("C:\\Users\\twanv\\Desktop\\WordCloud\\98-0.txt", "r", encoding="utf8") as f:
    data = f.readlines()

    for line in data:
       mString += line

 # clean the string up and split the string up into words       
cleanLines = mString.translate(str.maketrans('', '', string.punctuation + string.digits + '“”'))
cleanLines = cleanLines.lower()
splitWords = cleanLines.split()

# add words to dictionary with their occurence if they are not stopwords
for word in splitWords:
    if word not in stopwordList:
        if wordList.get(word) != None:
            wordList[(word)] += 1 
        else:
            wordList[(word)] = 1 

# give back sorted list of the dictionary as key-value pairs in reverse order     
sortedWordList = sorted(wordList.items(), key=lambda t:t[1], reverse=True)

# print the 10 most common words
for i in range(0, 11):
    print('{} : {}'.format(sortedWordList[i][0], sortedWordList[i][1]))



