'''
the function of this program is to separate each list of tweets into their regions and bodies
the function then takes each region and body and calculates the sentiment score of each tweet, and
finally adds up all of the scores and finds the average happiness score for each region
Created by: William Zhang, CS1026A
SN: 251215208
'''
import string
#given coordinate values for latitude and longitude
p1 = (49.189787, -67.444574)
p2 = (24.660845, -67.444574)
p3 = (49.189787, -87.518395)
p4 = (24.660845, -87.518395)
p5 = (49.189787, -101.998892)
p6 = (24.660845, -101.998892)
p7 = (49.189787, -115.236428)
p8 = (24.660845, -115.236428)
p9 = (49.189787, -125.242264)
p10 = (24.660845, -125.242264)

#function checks to see if each latitude and longitude are within the specified regions
def TimeZone(latLongList):
    if latLongList[0] > p1[0] or latLongList[0] < p2[0] or latLongList[1] > p1[1] or latLongList[1] < p9[1]:
        zone = "Not within any timezone"
    elif latLongList[1] <= p1[1] and latLongList[1] >= p3[1]:
        zone = "Eastern"
    elif latLongList[1] < p3[1] and latLongList[1] >= p5[1]:
        zone = "Central"
    elif latLongList[1] < p5[1] and latLongList[1] >= p7[1]:
        zone = "Mountain"
    else:
        zone = "Pacific"
    return zone

#function splits each tweet into its latitude and longitude as well as the body of the tweet
def ChangedTweet(tweet):
    tweetSplit = tweet.split()
    tweetLatLong = (tweetSplit)[0:2]
    tweetText = (tweetSplit)[5:]
    #removes the punctuation from the latitude and longitude and puts it into a list
    newLatLong = [tweetLatLong[0].strip("[],"), tweetLatLong[1].strip("[],")]
    return newLatLong, tweetText

#function computes each tweet and calculates the happiness scores, keyword tweets, and total tweets for each region
def compute_tweets(tweets, keywords):
    try:
        #open and read each file
        tweetsFile = open(tweets, "r" , encoding="utf-8")
        keywordsFile = open(keywords, "r" , encoding="utf-8")
        #read the current tweet
        tweetCurrent = tweetsFile.readline()

        #values for calculations
        totalEast = 0
        totalCentral = 0
        totalMountain = 0
        totalPacific = 0

        hapScoreEast = 0
        hapScoreCentral = 0
        hapScoreMountain = 0
        hapScorePacific = 0

        keywordTweetsEast = 0
        keywordTweetsCentral = 0
        keywordTweetsMountain = 0
        keywordTweetsPacific = 0

        tweetsEast = 0
        tweetsCentral = 0
        tweetsMountain = 0
        tweetsPacific = 0

        keywordsList = []
        #creates a list for keywords and splits the file into keywords and their sentiment values
        for keywordsRow in keywordsFile:
            splitKeywords = keywordsRow.split(",")
            keywordsList.append(splitKeywords)

        #while the current tweet is not empty
        while tweetCurrent != "":
            #create a list for latitude and longitude by converting its values into floats and adding them to the list
            LatLongList = []
            for tweet in ChangedTweet(tweetCurrent)[0]:
                LatLongList.append(float(tweet))
            tweetText = ChangedTweet(tweetCurrent)[1]
            #if the timezone is Eastern, add one for the region and if the current word is a keyword, add it to the total
            if TimeZone(LatLongList) == "Eastern":
                tweetsEast += 1
                sentimentTotal = 0
                keywordTotal = 0
                for char in tweetText:
                    changedText = (char.strip(string.punctuation)).lower()
                    for keyword in keywordsList:
                        if changedText == keyword[0]:
                            sentimentTotal += int(keyword[1])
                            keywordTotal += 1
                #calculate the total eastern tweets
                try:
                    totalEastDivided = sentimentTotal / keywordTotal
                    if totalEastDivided != 0:
                        keywordTweetsEast += 1
                        totalEast += totalEastDivided
                except ZeroDivisionError:
                    totalEastDivided = 0
            #if the timezone is Central, add one for the region and if the current word is a keyword, add it to the total
            elif TimeZone(LatLongList) == "Central":
                tweetsCentral += 1
                sentimentTotal = 0
                keywordTotal = 0
                for char in tweetText:
                    changedText = (char.strip(string.punctuation)).lower()  # removes trailing/leading punctuation of each word and turns into lowercase
                    for keyword in keywordsList:  # for each pairing in my keywords list, compare to the current word being looked at
                        if changedText == keyword[0]:
                            sentimentTotal += int(keyword[1])
                            keywordTotal += 1
                #calculate the total Central tweets
                try:
                    totalCentralDivided = sentimentTotal / keywordTotal
                    if totalCentralDivided != 0:
                        keywordTweetsCentral += 1
                        totalCentral += totalCentralDivided
                except ZeroDivisionError:
                    totalCentralDivided = 0
            #if the timezone is Mountain, add one for the region and if the current word is a keyword, add it to the total
            elif TimeZone(LatLongList) == "Mountain":
                tweetsMountain += 1
                sentimentTotal = 0
                keywordTotal = 0
                for char in tweetText:
                    changedText = (char.strip(string.punctuation)).lower()  # removes trailing/leading punctuation of each word and turns into lowercase
                    for keyword in keywordsList:  # for each pairing in my keywords list, compare to the current word being looked at
                        if changedText == keyword[0]:
                            sentimentTotal += int(keyword[1])
                            keywordTotal += 1
                #calculate the total Mountain tweets
                try:
                    totalMountainDivided = sentimentTotal / keywordTotal
                    if totalMountainDivided != 0:
                        keywordTweetsMountain += 1
                        totalMountain += totalMountainDivided
                except ZeroDivisionError:
                    totalMountainDivided = 0
            #if the timezone is Pacific, add one for the region and if the current word is a keyword, add it to the total
            elif TimeZone(LatLongList) == "Pacific":
                tweetsPacific += 1
                sentimentTotal = 0
                keywordTotal = 0
                for char in tweetText:
                    changedText = (char.strip(string.punctuation)).lower()  # removes trailing/leading punctuation of each word and turns into lowercase
                    for keyword in keywordsList:  # for each pairing in my keywords list, compare to the current word being looked at
                        if changedText == keyword[0]:
                            sentimentTotal += int(keyword[1])
                            keywordTotal += 1
                #calculate the total Pacific tweets
                try:
                    totalPacificDivided = sentimentTotal / keywordTotal
                    if totalPacificDivided != 0:
                        keywordTweetsPacific += 1
                        totalPacific += totalPacificDivided
                except ZeroDivisionError:
                    totalPacificDivided = 0
            #read the next tweet in the file
            tweetCurrent = tweetsFile.readline()

        #calculate the happiness scores for each region
        if keywordTweetsEast != 0:
            hapScoreEast = totalEast / keywordTweetsEast
        else:
            hapScoreEast = 0
        if keywordTweetsCentral != 0:
            hapScoreCentral = totalCentral / keywordTweetsCentral
        else:
            hapScoreCentral = 0
        if keywordTweetsMountain != 0:
            hapScoreMountain = totalMountain / keywordTweetsMountain
        else:
            hapScoreMountain = 0
        if keywordTweetsPacific != 0:
            hapScorePacific = totalPacific / keywordTweetsPacific
        else:
            hapScorePacific = 0

        #update each region's tuple with the values
        return[(hapScoreEast, keywordTweetsEast, tweetsEast),
        (hapScoreCentral, keywordTweetsCentral, tweetsCentral),
        (hapScoreMountain, keywordTweetsMountain, tweetsMountain),
        (hapScorePacific, keywordTweetsPacific, tweetsPacific)]

    except IOError:
        print("Sorry, the file you entered does not exist")
        return []


