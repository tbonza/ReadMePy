import feedparser
import sqlite3
from simpleflake import * 
import re


# Define parameters for document
RSS_link_list = '/home/ty/code/data/feeds_list.txt'

def get_RSS_link(RSS_link_list):
    '''RSS links used to pull feeds'''
    f = open(RSS_link_list, 'r').readlines()
    return f[0:len(f)-1] #Removes last \n to match len(cleaned_list)


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


def strip_garbage(description):
    '''
    Article descriptions were returning some garbage
    '''
    sep = '<img'
    rest = description.split(sep, 1)[0]
    return rest


def strip_title(feed_titles):
    ''' Table names are cleaned for SQL queries'''
    revised_list = []
    for t_name in range(len(feed_titles)):
        str_name = str(feed_titles[t_name])
        title = \
        str_name.strip('(').strip(')').strip(',').strip('u').strip("'")
        revised_list.append(title)
    return revised_list


def populate_row(RSS_link_list, d):
    '''
    Populates a row entry for a given table, the returned tuple matches 
    the column names in each table. 
    '''
    article_list = []
    for article in range(len(d)):
        # Hack simpleflake for sqlite3
        primary_key = str(simpleflake()) 
        # Remaining columns are iterated from feed parse
        title = d.entries[article].title
        description_junk = str(d.entries[article].description)
        description = strip_garbage(description_junk)
        print description # test
        link = d.entries[article].link
        published = d.entries[article].published
        article_list.append((primary_key, title, description, 
                             link, published))
    return article_list
    

def news_source(RSS_link_list, number):
    '''
    Gets articles from one news source to put in db
    '''
    # Create list for tuples to enter all at once
    new_articles = []
    #Get data for each feed in the table 
    links = get_RSS_link(RSS_link_list)
    numbers =  range(len(links))
    d = feedparser.parse(links[link])
    print links[link] # test
    new_articles.append(populate_row(RSS_link_list, d))
    return new_articles


def info_for_db(RSS_link_list):
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
    for table in cleaned_titles:
        if len(table) != 1:
            # Create string for insert query
            insert_query = "INSERT INTO " + table + " VALUES (?,?,?,?,?)"
            # Get new articles for table
            new_articles = news_sources(RSS_link_list)
            c.executemany(insert_query, new_articles)
        elif len(table) == 1:
            # Save (commit) the changes
            conn.commit()
            # We can also close the connection if we are done with it.
            conn.close()

               



# creating a query
# pulling articles from online
