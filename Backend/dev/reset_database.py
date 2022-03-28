#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import logging
import os
import random
import string
import numpy as np

from sqlalchemy.sql import text

import db
import settings
from db.models import GameStatusEnum, SQLAlchemyBase, Player,Game,PlayersGamesAssiation, Question, Answer, \
    AnswerQuestionAssiation
from settings import DEFAULT_LANGUAGE

# LOGGING
mylogger = logging.getLogger(__name__)
settings.configure_logging()


def execute_sql_file(sql_file):
    sql_folder_path = os.path.join(os.path.dirname(__file__), "sql")
    sql_file_path = open(os.path.join(sql_folder_path, sql_file), encoding="utf-8")
    sql_command = text(sql_file_path.read())
    db_session.execute(sql_command)
    db_session.commit()
    sql_file_path.close()


if __name__ == "__main__":
    settings.configure_logging()

    db_session = db.create_db_session()

    # -------------------- REMOVE AND CREATE TABLES --------------------
    mylogger.info("Removing database...")
    SQLAlchemyBase.metadata.drop_all(db.DB_ENGINE)
    mylogger.info("Creating database...")
    SQLAlchemyBase.metadata.create_all(db.DB_ENGINE)

    # -------------------- CREATE QUESTIONS --------------------
    mylogger.info("Creating default questions from file...")
    filepath = '/app/dev/questions'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        q = None
        while line:
            l = line.split(":")
            if l[0]=="C":
                q = Question()
                q.category=str.strip(l[1])
            elif l[0]=="Q":
                q.question=str.strip(l[1])
            elif l[0] == "AF" or l[0] == "AT":
                db_session.add(q)
                db_session.commit()
                a = Answer()
                a.answer = str.strip(l[1])
                db_session.add(a)
                db_session.commit()

                s = AnswerQuestionAssiation()
                s.id_question = q.id
                s.id_answer = a.id
                if l[0] == "AT":
                    s.is_correct = True
                else:
                    s.is_correct = False
                db_session.add(s)
                db_session.commit()

            cnt += 1
            line = fp.readline()

    db_session.close()

    # -------------------- CREATE PLAYERS --------------------
    mylogger.info("Creating default players...")


    names = ["Aatrox", "Ahri", "Anivia", "Ani", "Charmander", "Tyrion", "Sheldon", "Jax", "Jack", "Luffy", "Ace"
             "Kaido", "BigMom", "Sabo", "Goku", "Naruto", "Sasuke", "Tsunade", "Ichigo", "Amazeratu", "Genki", "KameHouse", "Bulma","Pikachu", "Thunder", "Fire", "Pro", "Shinigami", "Demon", "Devil", "Angel"]

    players = []
    index =0
    for p in range(20):
        name = random.choice(names)
        surname = random.choice(names)
        username= name + surname + str(index)
        player = Player(
            username=username,
        )
        players.append(player)
        db_session.add(player)
        index+=1
    db_session.commit()

       # -------------------- CREATE PLAYERS --------------------
    mylogger.info("Creating default players...")
    games = []
    index =0
    for p in range(5):
        np.random.seed(seed=int(p))
        game = Game(
            code=''.join(random.choices(string.ascii_letters+string.digits,k=6))
        )
        games.append(game)
        db_session.add(game)
        db_session.commit()

        s = PlayersGamesAssiation()
        s.id_game = game.id
        s.id_player= players[0].id
        db_session.add(s)
        db_session.commit()
        
        # Tirem una moneda per veure si completem la partida
        if (bool(random.getrandbits(1))):
            s = PlayersGamesAssiation()
            s.id_game = game.id
            s.id_player=players[random.randrange(1,19)].id
            game.status = GameStatusEnum.Finished
            db_session.add(s)
            db_session.commit()
        
        
        index+=1
    db_session.commit()



