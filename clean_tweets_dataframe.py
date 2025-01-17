import pandas as pd
class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df = df.drop_duplicates()
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        df['created_at'] = pd.to_datetime(df['created_at'], format='%d%b%Y:%H:%M:%S.%f')
        
        df = df[df['created_at'] >= '2020-12-31' ]
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        # df['polarity'] = pd.----
        
        
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        self.df = df[df['lang']=='en']
        
        return df
    def add_id(self, df:pd.DataFrame)->pd.DataFrame:
        df.insert(0, 'id', range(0, 0 + len(df)))
        return df

if __name__ == "__main__":
    df = pd.read_csv("./processed_tweet_data.csv")
    clean_tweets = Clean_Tweets(df=df)
    clean_tweets.add_id(df=df)
    print(df.dtypes)
    df.to_csv('processed_tweet_data.csv', index=False)
    # print(clean_tweets.drop_duplicate(df).head())
    # df = clean_tweets.drop_duplicate(df)
    # print(df.shape[0])
    # df = clean_tweets.remove_non_english_tweets(df)
    # print(df.shape[0])