from flask import Flask
from data.db_session import global_init, create_session
from data.__all_models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init("db/blogs.db")
    app.run()
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

if __name__ == '__main__':
    main()