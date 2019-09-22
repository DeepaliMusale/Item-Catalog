from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from catalogDb_setup import Sport, Base, SportItem
 
engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Menu for Soccer
sport1 = Sport(name = "Soccer")

session.add(sport1)
session.commit()

sportItem1 = SportItem(name = "Shoes", description = "Stealth cleats are built with your comfort in mind. These cleats feature a synthetic upper constructed from extremely durable, stretch-resistant materials that are designed to last.", sport = sport1)
sportItem2 = SportItem(name = "Jacket", description = "Whether you're looking for a lightweight soccer training jacket for early morning drills or a heavy-weight stadium jacket that offers full protection.", sport = sport1)
sportItem3 = SportItem(name = "Pant", description = "Our pants are designed to keep you comfortable and meet all exercise needs. Feel covered.", sport = sport1)

session.add(sportItem1)
session.add(sportItem2)
session.add(sportItem3)
session.commit()


#Menu for Basketball
sport2 = Sport(name = "Basketball")

session.add(sport2)
session.commit()

sportItem1 = SportItem(name = "Net", description = "description1", sport = sport2)
sportItem2 = SportItem(name = "Backboard", description = "description2", sport = sport2)
sportItem3 = SportItem(name = "Basketball", description = "description3", sport = sport2)

session.add(sportItem1)
session.add(sportItem2)
session.add(sportItem3)
session.commit()


#Menu for Baseball
sport3 = Sport(name = "Baseball")

session.add(sport3)
session.commit()

sportItem1 = SportItem(name = "Bat", description = "description1", sport = sport3)
sportItem2 = SportItem(name = "Glove", description = "description2", sport = sport3)

session.add(sportItem1)
session.add(sportItem2)
session.commit()


#Menu for Frisbee
sport4 = Sport(name = "Frisbee")

session.add(sport4)
session.commit()

sportItem1 = SportItem(name = "Disc", description = "description1", sport = sport4)

session.add(sportItem1)
session.commit()


#Menu for Snowboarding
sport5 = Sport(name = "Snowboarding")

session.add(sport5)
session.commit()

sportItem1 = SportItem(name = "Boots", description = "description1", sport = sport5)
sportItem2 = SportItem(name = "Helmet", description = "description2", sport = sport5)

session.add(sportItem1)
session.add(sportItem2)
session.commit()


#Menu for Rock Climbing
sport6 = Sport(name = "Rock Climbing")

session.add(sport6)
session.commit()

sportItem1 = SportItem(name = "Harness", description = "description1", sport = sport6)
sportItem2 = SportItem(name = "Ropes", description = "description2", sport = sport6)

session.add(sportItem1)
session.add(sportItem2)
session.commit()


#Menu for Foosball
sport7 = Sport(name = "Foosball")

session.add(sport7)
session.commit()

sportItem1 = SportItem(name = "Foosball Equipment", description = "description1", sport = sport7)

session.add(sportItem1)
session.commit()


#Menu for Skating
sport8 = Sport(name = "Skating")

session.add(sport8)
session.commit()

sportItem1 = SportItem(name = "Elbow Pads", description = "description1", sport = sport8)
sportItem2 = SportItem(name = "Wrist guards", description = "description2", sport = sport8)

session.add(sportItem1)
session.add(sportItem2)
session.commit()

#Menu for Hockey
sport9 = Sport(name = "Hockey")

session.add(sport9)
session.commit()

sportItem1 = SportItem(name = "Hockey Stick", description = "description1", sport = sport9)
sportItem2 = SportItem(name = "Hockey Puck", description = "description2", sport = sport9)

session.add(sportItem1)
session.add(sportItem2)
session.commit()

#Menu for Swimming
sport10 = Sport(name = "Swimming")

session.add(sport10)
session.commit()

sportItem1 = SportItem(name = "Swimwear", description = "description1", sport = sport10)
sportItem2 = SportItem(name = "Goggle", description = "description2", sport = sport10)

session.add(sportItem1)
session.add(sportItem2)
session.commit()

print "added menu items!"