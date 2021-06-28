
import pandas as pd
cleanTweet = pd.read_pickle('./pickles/data_clean.pkl')

x = list(cleanTweet.polarity)
y = list(cleanTweet.subjectivity)

data = {
    "sentiment_plot_X": x,
    "sentiment_plot_Y": y
}

data_two = [1, 2, 3, 4]
