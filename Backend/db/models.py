#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii
import datetime
import time 
import string
import random
import enum
import logging
import os
from _operator import and_
from builtins import getattr
from urllib.parse import urljoin

import falcon
from passlib.handlers.cisco import cisco_type7
from passlib.hash import pbkdf2_sha256
from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, Unicode, \
    UnicodeText, Table, type_coerce, case, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy_i18n import make_translatable

import messages
from db.json_model import JSONModel
import settings

mylogger = logging.getLogger(__name__)

SQLAlchemyBase = declarative_base()
make_translatable(options={"locales": settings.get_accepted_languages()})


def _generate_media_url(class_instance, class_attibute_name, default_image=False):
    class_base_url = urljoin(urljoin(urljoin("http://{}".format(settings.STATIC_HOSTNAME), settings.STATIC_URL),
                                     settings.MEDIA_PREFIX),
                             class_instance.__tablename__ + "/")
    class_attribute = getattr(class_instance, class_attibute_name)
    if class_attribute is not None:
        return urljoin(urljoin(urljoin(urljoin(class_base_url, class_attribute), str(class_instance.id) + "/"),
                               class_attibute_name + "/"), class_attribute)
    else:
        if default_image:
            return urljoin(urljoin(class_base_url, class_attibute_name + "/"), settings.DEFAULT_IMAGE_NAME)
        else:
            return class_attribute


def _generate_media_path(class_instance, class_attibute_name):
    class_path = "/{0}{1}{2}/{3}/{4}/".format(settings.STATIC_URL, settings.MEDIA_PREFIX, class_instance.__tablename__,
                                              str(class_instance.id), class_attibute_name)
    return class_path



class GameStatusEnum(enum.Enum):
    Closed = "C"
    Open = "O"
    Finished = "F"

class PlayerStatusEnum(enum.Enum):
    Playing = "P"
    Waiting = "W"



class CategoryEnum(enum.Enum):
    db = "db"
    os = "os"
    net = "net"
    patterns = "patterns"



class AnswerQuestionAssiation(SQLAlchemyBase, JSONModel):
        __tablename__ = "answer-question-association"

        id_question = Column(Integer, ForeignKey("questions.id",
                                             onupdate="CASCADE", ondelete="CASCADE"),
                         nullable=False, primary_key=True)
        id_answer = Column(Integer, ForeignKey("answers.id",
                                                   onupdate="CASCADE", ondelete="CASCADE"),
                               nullable=False, primary_key=True)
        is_correct = Column(Boolean, nullable=False)

        answers = relationship("Answer")


class Answer(SQLAlchemyBase, JSONModel):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    answer = Column(UnicodeText)

    @hybrid_property
    def json_model(self):
        return {
            "id": self.id,
            "answer": self.answer,
        }


class Question(SQLAlchemyBase, JSONModel):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(UnicodeText)
    category = Column(Enum(CategoryEnum))
    answers = relationship("AnswerQuestionAssiation")

    @hybrid_property
    def json_model(self):
        return {
            "id": self.id,
            "question": self.question,
            "category": self.category.value,
        }

class Player(SQLAlchemyBase, JSONModel):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(50), nullable=False, unique=True)
    rating = Column(Integer, default=0)

    @hybrid_property
    def json_model(self):
        return {
            "username": self.username,
            "rating": self.rating
        }

class Game(SQLAlchemyBase, JSONModel):
    __tablename__ = "games"


    id = Column(Integer, primary_key=True)
    start= Column(DateTime, default=datetime.datetime.now, nullable=False)
    end = Column(DateTime, nullable=True)
    code = Column(Unicode(6),
    nullable=False, unique=True)
    max_players = Column(Integer, default=2)
    players = relationship("PlayersGamesAssiation")
    status = Column(Enum(GameStatusEnum), default=GameStatusEnum.Open, nullable=False)


    @hybrid_property
    def json_model(self):
        return {
            "username": self.username,
            "code": self.code
        }  

class PlayersGamesAssiation(SQLAlchemyBase, JSONModel):
        __tablename__ = "participations"

        id_game = Column(Integer, ForeignKey("games.id",
                                             onupdate="CASCADE", ondelete="CASCADE"),
                         nullable=False, primary_key=True)
        id_player = Column(Integer, ForeignKey("players.id",
                                                   onupdate="CASCADE", ondelete="CASCADE"),
                               nullable=False, primary_key=True)

        score = Column(Integer, default=0)
        status = Column(Enum(PlayerStatusEnum), default=PlayerStatusEnum.Waiting, nullable=False)

        
        players = relationship("Player")    


      
class Turn(SQLAlchemyBase, JSONModel):
        __tablename__ = "turns"

        id = Column(Integer, primary_key=True)
        got_it_right  = Column(Boolean, nullable=True)
 
