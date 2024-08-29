import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__="User"
    id=Column(Integer, primary_key=True)
    userName=Column(String(255),nullable=False)
    firstName=Column(String(255),nullable=False)
    lastName=Column(String(255),nullable=False)
    email=Column(String(255),nullable=False)

class CharacterFavorites(Base):
    __tablename__='CharacterFavorites'
    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('User.id'))
    user=relationship(User)
    
    Characters_id=Column(Integer, ForeignKey('Characters.id'), nullable=False)

class PlanetFavorites(Base):
    __tablename__='PlanetFavorites'
    id=Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('User.id'))
    user=relationship(User)
    Planets_id=Column(Integer, ForeignKey('Planets.id'), nullable=False)
    


class Planets(Base):
    __tablename__='Planets'
    id=Column(Integer, primary_key=True)
   
    name=Column(String(255),nullable=False )
    size=Column(Integer,nullable=False )
    population=Column(Integer, nullable=False)
    

class Characters(Base):
    __tablename__='Characters'

    id=Column(Integer, primary_key=True)
    name=Column(String(255),nullable=False )
    movies=Column(String(255), nullable=False)
    
   
   

    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
