import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    id = Column(Integer, primary_key=True)
    # Notice that each column is also a normal Python instance attribute.
    email = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey("user.id"))
    location_id = Column(Integer, ForeignKey("location.id"))
    description = Column(String(250), nullable=False)
    caption = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))


class Location(Base):
    __tablename__ = 'location'
    # Here we define columns for the table address.
    id = Column(Integer, primary_key=True)
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String(250), nullable=False)
    shortname = Column(String(250), nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    id = Column(Integer, primary_key=True)
    # Notice that each column is also a normal Python instance attribute.
    post_id = Column(Integer, ForeignKey("post.id"))
    photo_id = Column(Integer, nullable=False)
    emojis = Column(String(250))
    content = Column(String(250), nullable=False)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e