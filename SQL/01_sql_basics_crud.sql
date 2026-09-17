-- SQL Basics: Table Creation, CRUD Operations & Data Types
-- Author: Data Analytics Practice

-- 1. Create Employee Table
CREATE TABLE employee (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2) CHECK (salary > 0),
    joining_date DATE NOT NULL,
    age INT CHECK (age > 18)
);

-- 2. Insert Records (Correct Column-Value Alignment)
INSERT INTO employee (first_name, last_name, department, salary, joining_date, age) VALUES
('Amit', 'Sharma', 'IT', 65000.00, '2022-05-01', 29),
('Neha', 'Patel', 'HR', 55000.00, '2021-08-15', 32),
('Ravi', 'Kumar', 'IT', 65000.00, '2020-11-22', 28),
('Suresh', 'Reddy', 'Operations', 50000.00, '2023-01-10', 26);

-- 3. Retrieve First Name & Department
SELECT first_name, department FROM employee;

-- 4. Update Salary (+10% increment for IT Department)
UPDATE employee
SET salary = salary + (salary * 0.10)
WHERE department = 'IT';

-- 5. Delete Records (Employees older than 34)
DELETE FROM employee
WHERE age > 34;

-- 6. Schema Modification: Add Email Column
ALTER TABLE employee
ADD COLUMN email VARCHAR(100);

-- 7. Schema Modification: Rename Department Column
ALTER TABLE employee
RENAME COLUMN department TO dept_name;

-- 8. Filter Employees Joined After Jan 1, 2021
SELECT first_name, dept_name, joining_date 
FROM employee
WHERE joining_date > '2021-01-01';

-- 9. Change Data Type of Salary Column
ALTER TABLE employee
ALTER COLUMN salary TYPE INTEGER USING salary::INTEGER;

-- 10. List Employees Ordered by Salary Descending
SELECT first_name, age, salary 
FROM employee
ORDER BY salary DESC;

-- 11. Increment Age for All Employees
UPDATE employee
SET age = age + 1;

-- Verify final data
SELECT * FROM employee;
