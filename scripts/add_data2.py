# import the module
import pandas as pd
from sqlalchemy import create_engine
import os 
import sys
sys.path.append(os.path.abspath(os.path.join('../scripts')))

# def dbconnect():
# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                    .format(user="root",
                            pw="sam123",
                            db="telcom"))

# def add_data_db():
data = pd.read_csv(r'C:\Users\sam\Desktop\Telecommunication_data_analysis\data\scores.csv')
# Insert whole DataFrame into MySQL
data.to_sql('score_table', con = engine, if_exists = 'append', chunksize = 1000)

# if __name__ == "__main__":
#     createDB(dbName='tweets')
#     emojiDB(dbName='tweets')
#     createTables(dbName='tweets')

#     df = pd.read_csv('processed_tweet_data.csv')

#     insert_to_tweet_table(dbName='tweets', df=df, table_name='TweetInformation')