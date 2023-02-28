use db;

CREATE TABLE planets(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    climate varchar(100) NULL,
    terrain varchar(100) NULL,
    PRIMARY KEY (id)
);

INSERT INTO planets(name)
VALUES ("Ronaldo"), ("Rivaldo")