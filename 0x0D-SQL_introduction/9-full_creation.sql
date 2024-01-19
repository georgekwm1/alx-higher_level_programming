--Create a 2nd table in the database
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` INT ,
    `name` VARCHAR(250) NOT NULL,
    `score` INT
);
#Insert data into the second table
INSERT INTO `second_table` (`id`, `name`, `score`) 
VALUES (1, 'John', 10),(2,'Alex', 3),
(3,'Bob', 14),(4,'George', 8);