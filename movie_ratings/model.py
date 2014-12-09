from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from datetime import datetime
from correlation import pearson


### Code for creating the database
# python -i model.py
# engine = create_engine("sqlite:///ratings.db", echo=True)
# Base.metadata.create_all(engine)


engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    """ from u.user info """  
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True, unique=True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)
    gender = Column(String(10), nullable = True)

    def form_user(self, form_dict):
        self.email = form_dict.get("email")
        self.password = form_dict.get("password")
        self.age = form_dict.get("age")
        self.gender = form_dict.get("gender")
        self.zipcode = form_dict.get("zipcode")

        #sample usage:
        #my_user = model.User()
        #my_user.form_user(request.form)

    def similarity(self, other):
        u_ratings = {}
        paired_ratings = []
        for r in self.ratings:
            u_ratings[r.movie_id] = r

        for r in other.ratings:
            u_r = u_ratings.get(r.movie_id)
            if u_r:
                paired_ratings.append( (u_r.rating, r.rating) )

        if paired_ratings:
            return pearson(paired_ratings)
        else:
            return 0.0

    def predict_rating(self, movie):
        ratings = self.ratings
        other_ratings = movie.ratings
        similarities = [ (self.similarity(r.user), r) for r in other_ratings ]
        similarities.sort(reverse = True)
        similarities = [ sim for sim in similarities if sim[0] > 0 ]
        if not similarities:
            return None
        numerator = sum([ r.rating * similarity for similarity, r in similarities ])
        denominator = sum([ similarity[0] for similarity in similarities ])
        return numerator/denominator

    # def predict_rating_by_movie(self, movie):
    #     ratings = self.ratings
    #     other_ratings = movie.ratings
    #     similarities = [ (movie.similarity(r.movie), r) for r in other_ratings ]
    #     similarities.sort(reverse = True)
    #     similarities = [ sim for sim in similarities if sim[0] > 0 ]
    #     if not similarities:
    #         return None
    #     numerator = sum([ r.rating * similarity for similarity, r in similarities ])
    #     denominator = sum([ similarity[0] for similarity in similarities ])
    #     return numerator/denominator
        

    def __repr__(self):
        return "Email: %s\n\
Password: %s\n\
Age: %s\n\
Zipcode: %s\n\
Gender: %s" % (self.email, self.password, self.age, self.zipcode, self.gender)

class Movie(Base):
    """ from u.items info """
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    movie_title = Column(String(120))
    release_date = Column(DateTime)
    IMDB = Column(String(140), nullable = True)

    # def similarity(self, other):
    #     u_ratings = {}
    #     paired_ratings = []
    #     for r in self.ratings:
    #         u_ratings[r.user_id] = r

    #     for r in other.ratings:
    #         u_r = u_ratings.get(r.user_id)
    #         if u_r:
    #             paired_ratings.append( (u_r.rating, r.rating) )

    #     if paired_ratings:
    #         return pearson(paired_ratings)
    #     else:
    #         return 0.0

    def __repr__(self):
        date_string = None
        try:
            date_string = datetime.strftime(self.release_date, "%d-%b-%Y")
        except: TypeError 
        return "ID: %s\n\
Movie Title: %s\n\
Release Date: %s\n\
IMDB: %s" % (self.id, self.movie_title, date_string,
             self.IMDB)

class Rating(Base):
    """ from u.data info """
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Integer)

    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=rating))

    def __repr__(self):
        return "Rating ID: %s\n\
User ID: %s\n\
Movie ID: %s\n\
%s Stars" % (self.id, self.user_id, self.movie_id, self.rating) 

### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()

