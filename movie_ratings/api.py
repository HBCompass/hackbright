from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from datetime import datetime
from flask import Flask, render_template, redirect, request, flash
from flask import session as session
import judgement
import model
from model import session as dbsession

def get_user_from_db(id):
    return dbsession.query(model.User).filter_by(id=id).first()

def get_users_rating_by_movie_id(user_id, movie_id):
    return dbsession.query(model.Rating).filter_by(user_id=user_id).filter_by(movie_id=movie_id).first()

def get_user_by_email(email): 
    #email should be unique
    return dbsession.query(model.User).filter_by(email=email).first()

def get_movie_by_id(id):
    return dbsession.query(model.Movie).filter_by(id=id).first()

def check_login(email, password):
    #when a user a logs in: 
    #query the database for that email 
    user_record = get_user_by_email(email)
    if user_record:
    #check if email and password match
        if user_record.password == password:
            session["logged-in"] = True
            session["user_id"]= user_record.id
            return True
    else:
        return False

def logout():
    session["logged-in"] = False
    session["user_id"]= None


