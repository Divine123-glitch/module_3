CREATE TABLE Books(
book_id int PRIMARY KEY,
title VARCHAR,
author_id int REFERENCES Authors(author_id),
genre VARCHAR,
date_of_publication DATE,
publisher varchar,
isbn varchar unique,
language_ varchar,
available_copies int,
age_rating varchar
)