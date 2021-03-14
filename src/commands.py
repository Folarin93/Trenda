from main import db, bcrypt
from flask import Blueprint
from faker import Faker
import random

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_db():
    from models.User import Users
    from models.Language import Languages
    from models.Watchlist import Watchlist




    faker = Faker()
    users = []
    languages = []
    watchlists = []
    colours = ['Red','White','Yellow','Green','Gold','Silver','Purple','Teal']
    list_FNames = ['Adam','Eve','Jada','Ryan','Alex','Myra','Amar','Jason','Frankie']
    list_LNames = ['Gold','Silver','Richardson','Teller','Rickers','Sarr','Farah','Reed','Port']
    list_languages = [{"python": {"2020-09-27": 2270.5, "2020-09-28": 2271.0, "2020-09-29": 2315.0, "2020-09-30": 2282.5, "2020-10-01": 2345.0, "2020-10-02": 2323.5, "2021-03-14": 3352.0}, "javascript": {"2020-09-27": 1907.0, "2020-09-28": 1896.0, "2020-09-29": 1947.5, "2020-09-30": 1918.0, "2020-10-01": 1969.0, "2020-10-02": 1942.0, "2021-03-14": 2867.5}, "html": {"2020-09-27": 1134.0, "2020-09-28": 1152.5, "2020-09-29": 1202.0, "2020-09-30": 1172.5, "2020-10-01": 1209.5, "2020-10-02": 1196.0, "2021-03-14": 1730.5}, "css": {"2020-09-27": 899.5, "2020-09-28": 906.0, "2020-09-29": 928.5, "2020-09-30": 923.0, "2020-10-01": 952.0, "2020-10-02": 947.0, "2021-03-14": 1260.5}, "java": {"2020-09-27": 2356.0, "2020-09-28": 2346.0, "2020-09-29": 2393.5, "2020-09-30": 2365.0, "2020-10-01": 2434.0, "2020-10-02": 2400.5, "2021-03-14": 3465.5}, "swift": {"2020-09-27": 212.0, "2020-09-28": 218.5, "2020-09-29": 213.5, "2020-09-30": 213.5, "2020-10-01": 215.5, "2020-10-02": 211.5, "2021-03-14": 357.5}}]

    for i in range(9):
        user = Users()
        user.first_name = random.choice(list_FNames)
        user.last_name = random.choice(list_LNames)
        user.username = f"{user.first_name}{i}"
        user.email =  f"{user.first_name}{i}@test.com"
        user.password = bcrypt.generate_password_hash(f"password{i}").decode("utf-8")
        user.phone = f"043226447{i}"

        db.session.add(user)
        users.append(user)
    
    db.session.commit()

    for lang in list_languages:
        for i in lang:
            language = Languages()
            language.name = i
            language.details = lang[i]
            db.session.add(language)
            languages.append(language)
    
    db.session.commit()

    for person in users:
        for lang in languages:
            user_watchlist = Watchlist()
            user_watchlist.user_id = person.id
            user_watchlist.language_id = lang.id
            db.session.add(user_watchlist)
    db.session.commit()

    print("Tables seeded")
    
    # watchlist_1 = Watchlist()
    # watchlist_1.user_id = 1
    # watchlist_1.language_id = 3

    # db.session.add(watchlist_1)

    # watchlist_2 = Watchlist()
    # watchlist_2.user_id = 1
    # watchlist_2.language_id = 4

    # db.session.add(watchlist_2)
    
    # db.session.commit()

    # watchlist_3 = Watchlist()
    # watchlist_3.user_id = 2
    # watchlist_3.language_id = 1

    # db.session.add(watchlist_3)

    # watchlist_4 = Watchlist()
    # watchlist_4.user_id = 2
    # watchlist_4.language_id = 5

    # db.session.add(watchlist_4)
    
    # db.session.commit()