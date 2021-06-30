from clean_tweets_dataframe import Clean_Tweets
import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))


df = pd.read_csv("./processed_tweet_data.csv")


class TestTweetDfCleaner(unittest.TestCase):
    """
                A class for unit-testing function in the clean_tweets_dataframe.py file

                Args:
        -----
                        unittest.TestCase this allows the new class to inherit
                        from the unittest module
        """

    def setUp(self) -> pd.DataFrame:
        self.df = df
        # tweet_df = self.df.get_tweet_df()

    def test_drop_duplicate(self):
        self.assertEqual(self.df.duplicated().sum(), 0)

    def test_convert_to_numbers(self):
        number_types = df[['polarity', 'subjectivity', 'followers_count',
                           'retweet_count', 'favorite_count', 'friends_count']]
        required_types = number_types.dtypes.tolist()
        self.assertEqual(required_types, [
                         "float64", "float64", "int64", "float64", "float64", "int64"])


if __name__ == '__main__':
    unittest.main()
