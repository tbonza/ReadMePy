import feedparser
import sqlite3
from simpleflake import * 
import re

# Define parameters for document
RSS_link_list = '/home/ty/code/data/feeds_list.txt'

def insert_query(RSS_link_list):
    '''
    yeah...
    '''
    tables = get_RSS_link(RSS_link_list)
    for table in tables:
        '''
        create a query for the table
        '''
        for article in table:
            '''
            populate the query with articles
            from the table.
            '''
            if article == len(table):
                '''
                execute the query in sqlite
                '''
            
    return True



        cleaned_titles = strip_title(feed_titles)
        query_list = create_query(RSS_link_list)
        info = info_for_db(RSS_link_list)
        init = init_sqlite3(call)
        garbage = strip_garbage(description)
        rows = populate_row(RSS_link_list, d)
        news = news_source(RSS_link_list)

def create_table(RSS_link_list):
    '''
    Reworking initial_db
    '''
