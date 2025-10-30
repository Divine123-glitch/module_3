CREATE TYPE gender as ENUM ('male','female');
CREATE TYPE type_of_membership as ENUM ('student', 'standard', 'premium');
CREATE TYPE status as ENUM ('active', 'suspended');
CREATE TABLE Members(
member_id int PRIMARY KEY,
member_name varchar not null,
gender gender not null,
email_address varchar not null,
phone_number varchar not null,
address varchar not null,
age int,
type_of_membership type_of_membership DEFAULT 'student',
date_of_membership date,
status status DEFAULT 'active'
)
