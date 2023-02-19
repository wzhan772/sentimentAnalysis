'''
the function of the main program is to format and print the output of the files given
Created by: William Zhang, CS1026A
SN: 251215208
'''
from sentiment_analysis import compute_tweets

#get user input for file names
keywords = input("Please enter keyword file")
tweets = input("Please enter tweets file")

#grab the output from the files and store them
output = compute_tweets(tweets, keywords)

#format and print out each region's corresponding happiness score, keyword tweets, and total tweets
if output != []:
    print("Eastern Region: Happiness Score:", format(output[0][0], ".3f") + ",", output[0][1], "keyword tweets" + ",", output[0][2], "tweets in total for the region")
    print("Central Region: Happiness Score:", format(output[1][0], ".3f") + ",", output[1][1], "keyword tweets" + ",", output[1][2], "tweets in total for the region")
    print("Mountain Region: Happiness Score:", format(output[2][0], ".3f") + ",", output[2][1], "keyword tweets" + ",", output[2][2], "tweets in total for the region")
    print("Pacific Region: Happiness Score:", format(output[3][0], ".3f") + ",", output[3][1], "keyword tweets" + ",", output[3][2], "tweets in total for the region")
else:
    output = []
