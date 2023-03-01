use db;

CREATE TABLE planets(
    id int NOT NULL,
    name varchar(100) NOT NULL,
    climate varchar(100) NULL,
    terrain varchar(100) NULL,
    PRIMARY KEY (id)
);

CREATE TABLE films(
    id int NOT NULL,
    title varchar(100) NOT NULL,
    director varchar(100) NULL,
    release_date datetime NULL,
    PRIMARY KEY (id)
);

CREATE TABLE planets_films(
    id_planet int NOT NULL,
    id_film int NOT NULL,
    PRIMARY KEY (id_planet, id_film),  
    FOREIGN KEY (id_planet) REFERENCES planets(id),  
    FOREIGN KEY (id_film) REFERENCES films(id)
);
