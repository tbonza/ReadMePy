import feedparser
import sqlite3
from simpleflake import * 
import re

# Define parameters for document
RSS_link_list = '/home/ty/code/data/feeds_list.txt'

def get_RSS_link(RSS_link_list):
    '''RSS links used to pull feeds'''
    f = open(RSS_link_list, 'r').readlines()
    return f


def initial_db(RSS_link_list):
    '''
    Sets up db tables where each RSS link feeds
    into a separate table because it's easier
    to aggregate then deaggregate.
    '''
    #Initialize sqlite3
    database = "FeedMe.db"
    conn = sqlite3.connect(database)
    c = conn.cursor()
    for RSS_link in get_RSS_link(RSS_link_list):
        if len(RSS_link) != 1:
            # Make table name match RSS feed name
            d = feedparser.parse(RSS_link)
            table_name = re.sub(r'\W+', '', d.feed.title)
            print table_name #test
            # Creating string separately makes multiple table 
            # creation easier
            table = "CREATE TABLE " +  table_name + \
                    "( primary_key text, title text , description text," \
                    "link text, published text)" 
            # Create table in sqlite3
            c.execute(table)
        elif len(RSS_link) == 1:
            # Save (commit) the changes
            conn.commit()
            # Close the connection to sqlite3
            conn.close()
    return True #test


def strip_garbage(object):
    '''
    try to work this function out
    '''
    pass
    sep = '<img'
    rest = text.split(sep, 1)[0]

def strip_title(feed_titles):
    ''' Table names are cleaned for SQL queries'''
    revised_list = []
    for t_name in range(len(feed_titles)):
        str_name = str(feed_titles[t_name])
        title = \
        str_name.strip('(').strip(')').strip(',').strip('u').strip("'")
        revised_list.append(title)
    return revised_list

def get_articles(RSS_link_list):
    '''Articles from each RSS feed to be put into DB'''
    pass

def info_for_db(RSS_links):
    ''' 
    Insert entries into their respective tables in
    feed.db
    '''
    #Initialize sqlite3
    database = "FeedMe.db"
    conn = sqlite3.connect(database)
    c = conn.cursor()
    #Selecting all tables for list
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    feed_titles = c.fetchall()
    cleaned_titles = strip_title(feed_titles)
    # We want to do a for loop based on which tables are in the db
    for table in range(len(cleaned_tables)):
        # Each article needs to be entered from the RSS feed
        for article in range(10):
            if len(article) != 1:
                # # # # # # # # # # # # # # # # # # # 
                #These are the columns in each table #
                # # # # # # # # # # # # # # # # # # #
                # Hack simpleflake for sqlite3
                primary_key = str(simpleflake()) 
                # Remaining columns are iterated from feed parse
                title = d.entries[article].title
                description = d.entries[article].description
                link = d.entries[article].link
                published = d.entries[article].published
                # Creating a string so we can insert rows for each table
                cleaned_titles[table]



    
d = feedparser.parse('http://feeds.reuters.com/reuters/businessNews')


d['feed']['title']

# These should be the fields
d.feed.title
d.feed.link
d.feed.description
d.feed.updated

d.entries[0].title
d.entries[0].link
d.entries[0].description
d.entries[0].published


text = d.entries[1].description

