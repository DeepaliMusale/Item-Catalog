import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Sport(Base):
    __tablename__ = 'sport'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class SportItem(Base):
    __tablename__ = 'sport_item'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    sport_id = Column(Integer,ForeignKey('sport.id'))
    sport = relationship(Sport) 

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
       }
 

engine = create_engine('sqlite:///catalog.db')
 

Base.metadata.create_all(engine)