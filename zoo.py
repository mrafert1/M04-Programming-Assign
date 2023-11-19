##Exercise 11.1
##Define function hours and save it as zoo.py
def hours ():
    print ('open 9-5 daily')

##use import zoo method to display 'open 9-5 daily'
import zoo
zoo.hours ()

##Exercise 11.2
##use menagerie method to display 'open 9-5 daily'
import zoo as menagerie
menagerie.hours ()

#---------------------------------------------------------------------------

##Exercise 16.8

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select

##Create engine that will connect to database
engine = create_engine('sqlite:///books.db')
metadata = MetaData()

##define books table
book = Table('book', metadata,
             Column('id', Integer, primary_key=True),
             Column('title', String),
             Column('author', String),
             Column('pub_year', Integer))

##connect to database with engine
with engine.connect() as connection:
    ##query selects title from the books table and does so in alphabetical order
    query = select([book.c.title]).order_by(book.c.title)
    ##Use query to search for and fetch the rows for result
    result = connection.execute(query)
    ##Print title column
    for row in result:
        print(row['title'])
