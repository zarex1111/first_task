from flask import Flask, render_template
from data.db_session import global_init, create_session
from data.__all_models import *
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init("db/blogs.db")
    data = (
        ["Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org"],
        ["Luke", "Skywalker", 17, "master-jedi", "lasersaber fighter", "module_2", "iamnotyourson@endor.org"],
        ["9000", "HAL", 5, "navigator", "artificial intelligense", "the whole ship", "iamsmart@mars.org"],
        ["Pirx", "anonymous", 22, "pilot", "luck master", "module_4", "lemisthegoat@solaris.org"]
    )
    for elem in data:
        session = create_session()
        user = User()
        user.surname, user.name, user.age, user.position, user.speciality, user.address, user.email = elem
        session.add(user)
        session.commit()
    jobs = (1, "deployment of residential modules 1 and 2", 15, "2, 3", False)
    job = Job()
    job.team_leader, job.job, job.work_size, job.collaborators, job.is_finished = jobs
    session = create_session()
    session.add(job)
    session.commit()
    app.run(host='127.0.0.1', port='5000')


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<string:prof>')
def courses(prof):
    return render_template('courses.html', prof=prof, title="Подготовительные пунткты")


@app.route('/list_prof/<string:list_type>')
def duties(list_type):
    with open("static/json/duties.json", encoding="utf-8") as file:
        p = json.load(file)
    return render_template("professions_list.html", list_type=list_type, duties=p, title="Список профессий")


@app.route('/answer')
@app.route('/answer_auto')
def answer():
    with open("static/json/anketa.json", encoding="utf-8") as file:
        p = json.load(file)
    with open("static/json/keys.json", encoding="utf-8") as file:
        n = json.load(file)
    return render_template("auto_answer.html", form=p, keys=n)


@app.route('/')
def works_journal():
    all_jobs = create_session().query(Job).all()
    return render_template('works_journal.html', jobs=all_jobs, create_session=create_session, user_class=User)


if __name__ == '__main__':
    main()