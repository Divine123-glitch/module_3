CREATE TABLE Borrowed_History(
borrowed_id int PRIMARY KEY,
book_id int REFERENCES Books(book_id),
member_id int REFERENCES Members(member_id),
borrow_date date,
return_date date
)