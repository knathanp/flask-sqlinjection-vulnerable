from random import randint

from db import connection_context
from models import Contest, User

CREATE_TABLE_USER = """
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    ssn varchar(16) UNIQUE NOT NULL,
    email varchar(100) UNIQUE NOT NULL,
    birth_date varchar(12) NOT NULL,
    phone_number varchar(20) NOT NULL
);
"""


CREATE_TABLE_CONTEST = """
CREATE TABLE IF NOT EXISTS contest (
    id integer PRIMARY KEY,
    title varchar(100),
    score integer NOT NULL,
    user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);
"""

CLEAR_TABLE_CONTEST = "DELETE FROM contest"

USER_DATA = [
    User(
        1,
        email="any@email.com",
        ssn="999-99-9999",
        birth_date="06-01-2012",
        phone_number="(208) 555-5555"),
    User(2, email="another@email.com", ssn="111-22-3333"),
    User(3, email="yetanother@email.com", ssn="222-33-4444"),
    User(
        4,
        email="bob@example.com",
        ssn="123-45-6789",
        birth_date="12-15-2015",
        phone_number="(801) 555-5555"),
    User(
        5,
        email="sue@example.com",
        ssn="456-78-6789",
        birth_date="09-02-2013",
        phone_number="(123) 456-7890"),

]

MIN_CHALLENGES_PER_USER = 2
MAX_CHALLENGES_PER_USER = 6


def start_database():
    with connection_context() as cur:
        cur.execute(CREATE_TABLE_USER)
        cur.execute(CREATE_TABLE_CONTEST)
        cur.execute(CLEAR_TABLE_CONTEST)

        for user in USER_DATA:
            insert_cmd = f"""
                INSERT INTO users (id, email, ssn, birth_date, phone_number)
                VALUES (
                    {user.id},
                    '{user.email}',
                    '{user.ssn}',
                    '{user.birth_date}',
                    '{user.phone_number}'
                )
                ON CONFLICT DO NOTHING
            """
            cur.execute(insert_cmd)

            challenges_count = randint(
                MIN_CHALLENGES_PER_USER,
                MAX_CHALLENGES_PER_USER,
            )
            CHAR_A_OFFSET = 65
            for i in range(CHAR_A_OFFSET, challenges_count + CHAR_A_OFFSET):
                contest = Contest(user.id, f"Contest {chr(i)}")
                insert_cmd = f"""
                    INSERT INTO contest (title, score, user_id)
                    VALUES (
                        '{contest.title}',
                        {contest.score},
                        {contest.user_id}
                    )
                    ON CONFLICT DO NOTHING
                """
                cur.execute(insert_cmd)
