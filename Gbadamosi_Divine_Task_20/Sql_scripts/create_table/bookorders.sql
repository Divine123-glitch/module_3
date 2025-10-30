CREATE TYPE fulfilment_status as ENUM('processing','pending','fulfilled');
CREATE TABLE BookOrders(
order_id int PRIMARY KEY,
order_date date,
book_id int REFERENCES Books(book_id),
cost decimal,
quantity int,
supply_date date,
fulfilment_status fulfilment_status DEFAULT 'processing',
supplier_name varchar not null
)
