USE salesDB;

-- Question 1
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

-- Question 2
INSERT INTO student (id, fullName, age) VALUES (1, 'Alice Johnson', 18);
INSERT INTO student (id, fullName, age) VALUES (2, 'Brian Otieno', 19);
INSERT INTO student (id, fullName, age) VALUES (3, 'Cynthia Mwangi', 21);

-- Question 3
UPDATE student
SET age = 20
WHERE id = 2;
