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
    from models.Lang_watchlist import Lang_watchlist



    faker = Faker()
    users = []
    languages = []
    watchlists = []
    colours = ['Red','White','Yellow','Green','Gold','Silver','Purple','Teal']
    list_FNames = ['Adam','Eve','Jada','Ryan','Alex','Myra','Amar','Jason','Frankie']
    list_LNames = ['Gold','Silver','Richardson','Teller','Rickers','Sarr','Farah','Reed','Port']
    list_languages = [{"Python": {"2020-09-27": 2270.5, "2020-09-28": 2271.0, "2020-09-29": 2315.0, "2020-09-30": 2282.5, "2020-10-01": 1517.0}},{'Javascript': {"2020-09-27":1907.0, "2020-09-28":1896.0, "2020-09-29":1947.5, "2020-09-30":1918.0, "2020-10-01":1429.5}},{'HTML': {"2020-09-27": 1134.0, "2020-09-28": 1152.5, "2020-09-29": 1202.0, "2020-09-30": 1172.5, "2020-10-01": 1070.5}},{'CSS': {"2020-09-27": 899.5, "2020-09-28": 906.0, "2020-09-29": 928.5, "2020-09-30": 923.0, "2020-10-01": 925.0}},{'Swift': {"2020-09-27": 212.0, "2020-09-28": 218.5, "2020-09-29": 213.5, "2020-09-30": 213.5, "2020-10-01": 239.0}},{'Java': {"2020-09-27": 2356.0, "2020-09-28": 2346.0, "2020-09-29": 2393.5, "2020-09-30": 2365.0, "2020-10-01": 1275.0}}]

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

    for i in list_languages:
        language = Languages()
        language.name = str(i.keys())
        language.details = i.get(language.name)
        db.session.add(language)
        languages.append(language)
    
    db.session.commit()

    for i in colours:
        watchlist = Watchlist()
        watchlist.name = f"{i}_watchlist"
        watchlist.user_id = random.choice(users).id

        db.session.add(watchlist)
        watchlists.append(watchlist)
    
    db.session.commit()
    
    for i in range(20):
        lang_watchlist = Lang_watchlist()
        lang_watchlist.language_id = random.choice(languages).id
        lang_watchlist.watchlist_id = random.choice(watchlists).id

        db.session.add(lang_watchlist)
    
    db.session.commit()



    print("Tables seeded")
    
