CREATE TABLE IF NOT EXISTS users (
    discord_id integer,
    username TEXT,
    PRIMARY KEY(discord_id, username)
);

CREATE TABLE IF NOT EXISTS questions (
    question_id unique integer,
    question_category integer,
    question_text text,
    answer_text text,
    FOREIGN KEY (question_category) REFERENCES categories (category_id)
);

CREATE TABLE IF NOT EXISTS categories (
    category_id integer PRIMARY KEY,
    category_title text
);

CREATE TABLE IF NOT EXISTS subcategory (
    category_id,
    subcategory_title  
);

CREATE TABLE IF NOT EXISTS user_question (
    discord_id integer,
    question_id integer,
    time_respawn integer
);

