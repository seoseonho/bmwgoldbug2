# -*- coding: utf-8 -*-
from flask import Flask
import pandas as pd
from sqlalchemy import create_engine

## DB 연결 Local
def db_create()
    #로컬
    engine= create_engine("postgresql://postgres:12232305@localhost:5432/postgres",echo=False)
    #postgresql://username:password@localhost:5432/Maintenance database
    #Heroku
    engine= create_engine("postgresql://izqesmsjoczkzz:dded6e1737ec332ef2bb0a898d23101b70406d9e25cb44fd472079b9a2aab111@ec2-54-225-234-165.compute-1.amazonaws.com:5432/dbqh4fnj6la4kq",echo=False)

    engine.connect()
    engine.execute("""
        CREATE TABLEIF NOT EXISTS iris(
            sepal_length FLOAT NOT NULL,
            sepal_width FLOAT NOT NULL,
            pepal_length FLOAT NOT NULL,
            pepal_width FLOAT NOT NULL,
            species VARCHAR(100) NOT NULL
        );"""
    )

    data=pd.read_csv('data/iris.csv')
    print(data)
    data.to_sql(name='iris',con=engine, schema='public',if_exists='replace',index=False)

app =Flask(__name__)

@app.route("/")
def index():
    #db_create()
    return "Hello World!"

if__name__ == "__main__":
    db_create()
    app.run()