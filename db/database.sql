CREATE TABLE Cabinet (
	id SERIAL PRIMARY KEY,
	position VARCHAR(50)
);

CREATE TABLE Type (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE Item (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	brand VARCHAR(50),
	expiry_date DATE,
	weight VARCHAR(15),
	type_id INT NOT NULL,
	FOREIGN KEY (type_id)
		REFERENCES type (id)
);

CREATE TABLE CabinetItem (
	cabinet_id INT NOT NULL,
	item_id INT NOT NULL,
	amount SMALLINT NOT NULL
);

