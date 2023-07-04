import os
from flask import Flask, render_template, request, redirect, jsonify
from py2neo import Graph
from aiml import Kernel
from datetime import datetime, date
from web_part import get_Query
import nlp_part

app = Flask("Mohi's Bot", template_folder='templates')
graph = Graph("bolt://localhost:7689", auth=("neo4j", "12345678"))

check_siginday = False
total_days = 0
user = ''

@app.route('/')
def login():
    return render_template("mohi's_home.html")

@app.route('/getlogin')
def sigin():
    return render_template('login.html')

@app.route('/registration')
def signup():
    return render_template('registration.html')

@app.route("/home")
def home():
    message = f"Hey! {user} welcome to Mohi's Bot. Tell me How I can assist you today."
    return render_template("home.html", msg=message)


def get_totaldays(cr_date):
    global total_days
    joining_date = date.fromisoformat(cr_date)
    current_date = date.today()
    total_days = (current_date - joining_date).days
    print(total_days, "days")


@app.route("/signup", methods=['POST'])
def getvalue():
    username = request.form.get('username')
    email = request.form.get('email')
    pass1 = request.form.get('pass1')
    my_bot.setPredicate('name', username)
    created_at = str(datetime.now())[0:16]
    gender = nlp_part.predict_gender(username)
    username = username.split(" ")
    graph.run(
        f"MERGE(n:OWNER{{name: \"{username[0]}\", email: \"{email}\", password: \"{pass1}\",gender: \"{gender}\" , accout_creation_time: \"{created_at}\"}})")
    return redirect("/getlogin")

@app.route("/login", methods=['POST'])
def login_user():
    try:
        global check_siginday, user
        email = request.form.get('email')
        pass1 = request.form.get('password')
        print(email,pass1)
        ipAdrres = nlp_part.getIpAdrress()
        signedin_date = str(date.today())
        cr_date = graph.run(
            f"MATCH (n:OWNER{{email: \"{email}\", password: \"{pass1}\"}}) return n.accout_creation_time")
        print(cr_date)
        cr_date = list(cr_date)
        cr_date = cr_date[0][0]
        print(cr_date)
        get_totaldays(cr_date[:10])
        last_date = graph.run(
            f"MATCH (n:OWNER{{email: \"{email}\", password: \"{pass1}\"}}) return n.signedin_at")
        last_date = list(last_date)
        last_signedin = last_date[0][0]
        print("last_signedin", last_signedin)
        if last_signedin == signedin_date:
            check_siginday = True
            print("Same day")
        email_ver0 = graph.run(
            f"MATCH (n:OWNER{{email: \"{email}\", password: \"{pass1}\"}}) set n.Ip= \"{ipAdrres}\" set n.signedin_at= \"{signedin_date}\" return n.email")
        usr_name = graph.run(
            f"MATCH (n:OWNER{{email: \"{email}\", password: \"{pass1}\"}}) return n.name")
        email_ver_list = list(email_ver0)
        email_ver = email_ver_list[0][0]
        usr_name = list(usr_name)
        username = usr_name[0][0]
        print(ipAdrres, "ipAdrres")
        my_bot.setPredicate('email', email_ver)
        my_bot.setPredicate('myip', ipAdrres)
        my_bot.setPredicate('name', username)
        print(my_bot.getPredicate('myip'))
        user = username
        print(email_ver,email)
        if email == email_ver:
            return redirect("/home")
    except:
        return render_template("login.html", msg='User not found or password or email are wrongs')

my_bot = Kernel()

def load_aiml_files():
    aiml_directory = "data1"
    aiml_files = [os.path.join(aiml_directory, file) for file in os.listdir(
        aiml_directory) if file.endswith(".aiml")]
    for aiml_file in aiml_files:
        my_bot.learn(aiml_file)

load_aiml_files()

def chat_bot_reply(message):
    try:
        response = my_bot.respond(message)
        return response
    except:
        return None
def def_relative_person(user):
    ipAdrres = nlp_part.getIpAdrress()
    try:
        relative_person = graph.run(
            f"MATCH (n:OWNER{{Ip: \"{ipAdrres}\"}}) where n.name <> \"{user}\" return n.name")
        relative_person = list(relative_person)
        relative_person = relative_person[0][0]
        if relative_person:
            try:
                query = f"MATCH (person1:OWNER {{name: '{user}'}})-[r]-(person2:OWNER {{name: '{relative_person}'}})RETURN r"
                result = graph.run(query)
                result = str(result)
                if result == "(No data)":
                    my_bot.setPredicate('relative_person', relative_person)
            except:
                None
    except:
        None
@app.route("/get")
def get_bot_response():
    global user
    query = request.args.get('msg')
    query = nlp_part.autospell(query)
    sents = nlp_part.sentence(query)
    values = nlp_part.chart(query)
    response = ''
    bot_response = ''
    def_relative_person(user)
    prev_response = ""
    for query in sents:
        query = nlp_part.autospell(query)
        nlp_part.NER(query, user)
        print("query", query)
        bot_response = chat_bot_reply(query)
        response = response + '' + bot_response
        # web scrapping and wordnet
        if response == '' or "xfind" in response or "unknown" in response or "I have never been asked that before." in response or "tried searching the web?" in response or "no answer for that" in response or "do not know" in response or "deeper algorithm" in response or "My brain contains more than 22,000 patterns, but not one that matches your last input." in response or "do not recognize" in response or "I need time to formulate the reply." in response:
            response = ''
            web_resonse = get_Query(query)
            if web_resonse:
                prev_response = prev_response + ''+web_resonse
                response = response + "" + prev_response
            else:
                r = nlp_part.sent_tokenize(response)[0]
                Postags = nlp_part.pos_tag(nlp_part.word_tokenize(r))
                for tag in Postags:
                    if tag[1].startswith('N') or tag[1].startswith('V'):
                        prev_response = prev_response + "" + \
                            nlp_part.get_definition(tag[0])
                        response = response + "" + prev_response
        else:
            prev_response += response
            response = prev_response
        prev_response = response

    if check_siginday:
        filename = f"episode_{total_days}.txt"
        with open(f'chatting/{filename}', 'a') as chat:
            chat.write(f"{user} : {query}\n")
            chat.write(f"Bot : {response}\n")
    else:
        filename = f"episode_{total_days}.txt"
        with open(f'chatting/{filename}', 'a') as chat:
            chat.write(f"{user} : {query}\n")
            chat.write(f"Bot : {response}\n")
    reply = []
    if response:
        reply.append(response)
        reply.append(values)
        return jsonify(reply)
    else:
        reply.append(" : )")
        reply.append(values)
        return jsonify(reply)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8000')