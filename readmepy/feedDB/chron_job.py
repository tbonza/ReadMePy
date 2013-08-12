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


def populate_row(d, number):
    '''Row entry for a given table'''
    # # # # # # # # # # # # # # # # # # # 
    #These are the columns in each table #
    # # # # # # # # # # # # # # # # # # #
    # Hack simpleflake for sqlite3
    primary_key = str(simpleflake()) 
    # Remaining columns are iterated from feed parse
    title = d.entries[number].title
    description_junk = str(d.entries[number].description))
    description = strip_garbage(description_junk)
    link = d.entries[number].link
    published = d.entries[number].published
    return primary_key, title, description, link, published # Can this be returned as a tuple? 

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
    #Get data for each feed in the table 
    links = get_RSS_link(RSS_link_list)
    # We want to do a for loop based on which tables are in the db
    for table in range(len(cleaned_tables)):
        # Here I'm assuming that the number of tables in the db
        # match the number of links in RSS_link_list. Clean this
        # up later. 
        if len(table) != 1:
            d = feedparser.parse(links[table])
            print links[table] # test
            # Create list for tuples to enter all at once
            new_articles = []
            # Each article needs to be entered from the RSS feed
            for article in range(len(feedparser.parse(links[table]))):
                if len(article) != 1:
                    # Creating a list of tuples to insert all articles
                    new_articles.append((populate_row(d, article)))
                elif len(article) == 1:
                    # Create string for insert query
                    insert_query = "INSERT INTO " + cleaned_tables[table] \
                                   + " VALUES (?,?,?,?,?)"
                    # Populating each table with values
                    c.executemany(insert_query, new_articles)
        elif len(table) == 1:
            # Save (commit) the changes
            conn.commit()
            # We can also close the connection if we are done with it.
            conn.close()

               





