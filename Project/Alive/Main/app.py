# import necessary libraries
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
    
import pymysql
from config import remote_db_endpoint, remote_db_port
from config import remote_db_name, remote_db_user, remote_db_pwd
pymysql.install_as_MySQLdb()
from sqlalchemy import func, create_engine

app = Flask(__name__)

engine = create_engine(f"mysql://{remote_db_user}:{remote_db_pwd}@{remote_db_endpoint}:{remote_db_port}/{remote_db_name}")

# create route that renders index.html template
@app.route("/")
def home():    
    return render_template("index.html")

# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    conn = engine.connect()

    if request.method == "POST":
        Username = request.form["Username"]
        age = request.form["Age"]
        city = request.form["City"]
        state = request.form["State"]
        gender = request.form["Gender"]
        Discovery = request.form["Discovery"]

        game_df = pd.DataFrame({
            'Username': [Username],
            'Age': [age],
            'City': [city],
            'State': [state],
            'Gender': [gender],
            'Discovery': [Discovery]
        })

        game_df.to_sql('game', con=conn, if_exists='append', index=False)

        return redirect("/", code=302)

    conn.close()

    return render_template("RegisterForm.html")

@app.route("/survey", methods=["GET", "POST"])
def survey():
    conn = engine.connect()

    if request.method == "POST":
        Gaming = request.form["Gaming"]
        Hours = request.form["Hours"]
        Job_performance = request.form["Job performance"]
        Help = request.form["Help"]
        Community = request.form["Community"]
        Players = request.form["Players"]
        Ramifications = request.form["Ramifications"]
        Social_Life = request.form["Social Life"]
        Sleeping_Habits = request.form["Sleeping Habits"]
        Thoughts = request.form["Thoughts"]

        survey_df = pd.DataFrame({
            'Gaming': [Gaming],
            'Hours': [Hours],
            'Job performance': [Job_performance],
            'Help': [Help],
            'Community': [Community],
            'Players': [Players],
            'Ramifications': [Ramifications],
            'Social Life': [Social_Life],
            'Sleeping Habits': [Sleeping_Habits],
            'Thoughts': [Thoughts]
        })

        survey_df.to_sql('survey', con=conn, if_exists='append', index=False)

        return redirect("/", code=302)

    conn.close()

    return render_template("form.html")

@app.route("/info")
def info():
    conn = engine.connect()
    
    query = '''
        SELECT 
            *
        FROM
            game
    ''' 

    game_df = pd.read_sql(query, con=conn)

    game_json = game_df.to_json(orient='records')

    conn.close()

    return game_json

@app.route("/surveydata")
def surveydata():
    conn = engine.connect()
    
    query = '''
        SELECT 
            *
        FROM
            survey
    ''' 

    survey_df = pd.read_sql(query, con=conn)

    survey_json = survey_df.to_json(orient='records')

    conn.close()

    return survey_json

if __name__ == "__main__":
    app.run(debug=True)