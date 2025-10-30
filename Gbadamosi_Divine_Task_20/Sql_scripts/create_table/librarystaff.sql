CREATE TABLE LibraryStaff(
staff_id int PRIMARY KEY,
staff_name varchar not null,
job_title varchar not null,
dept_id int REFERENCES Departments(dept_id),
gender gender,
address varchar not null,
phone_number varchar not null,
hire_date date,
manager_id int
)