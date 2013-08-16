import feedparser
import sqlite3
from simpleflake import * 
import re


# Define parameters for document
RSS_link_list = '/home/ty/code/data/feeds_list.txt'

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


def get_tablenames(RSS_link_list):
    ''' Table names are cleaned for SQL queries'''
    # Start up db
    database = "FeedMe.db"
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # List of tables to query
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # List of tables names that can be queried
    list_tables = c.fetchall()
    # Create a revised list for insert query
    revised_list = \
    [str(list_tables[t_name]).strip('(')\
    .strip(')').strip(',').strip('u').strip("'") 
    for t_name in range(len(list_tables))]
    return revised_list


def insert_query(RSS_link_list):
    '''
    Create a list of queries to run that
    include the name of each table 
    '''
    insert_queries = \
    ["INSERT INTO " + table_name + " VALUES (?,?,?,?,?)" 
     for table_name in get_tablenames(RSS_link_list)]
    return insert_queries


def get_RSS_link(RSS_link_list):
    '''RSS links used to pull feeds'''
    f = open(RSS_link_list, 'r').readlines()
    return f[0:len(f)-1] #Removes last \n to match len(cleaned_list)


def strip_garbage(description):
    '''
    Article descriptions were returning some garbage
    '''
    sep = '<img'
    rest = description.split(sep, 1)[0]
    return rest


def articles(RSS_link_list, number):
    '''
    This should give me a list of tuples containing
    information on the articles for a given RSS feed
    '''
    links = get_RSS_link(RSS_link_list)
    d = feedparser.parse(links[number])
    new_list = []
    for article in range(len(d)):
        # Hack simpleflake for sqlite3
        primary_key = str(simpleflake()) 
        # Remaining columns are iterated from feed parse
        title = d.entries[article].title
        description_junk = str(d.entries[article].description)
        description = strip_garbage(description_junk)
        link = d.entries[article].link
        published = d.entries[article].published
        new_list.append((primary_key,title,description,link,published))
    return new_list

def table(RSS_link_list):
    '''
    This should be a list of tables where each table
    consists of a list of tuples. 
    '''
    table_list = []
    for number in range(len(get_tablenames(RSS_link_list))):
        for table in get_tablenames(RSS_link_list):
            table = articles(RSS_link_list, number)
            table_list.append(table)
    return table_list


def populate_db(RSS_link_list):
    #Initialize sqlite3 
    database = "FeedMe.db"
    conn = sqlite3.connect(database)
    c = conn.cursor()
    # Insert queries across multiple tables
    for table in len(range(table(RSS_link_list))):
       c.executemany(insert_query(RSS_link_list)[table],\
                     table(RSS_link_list)[table])
       conn.commit()
    return True # Test
    

# test
#initial_db(RSS_link_list)
a = table(RSS_link_list) 
print a[0][1]

