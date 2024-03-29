-- DROP DATABASE ItineraryDataBase;
-- CREATE DATABASE ItineraryDataBase;
-- USE ItineraryDataBase;


CREATE TABLE States(
   id int NOT NULL AUTO_INCREMENT,
   name varchar(100) NOT NULL,
   image_url text,
   description text,
   type varchar(200),
   PRIMARY KEY (id)
);


CREATE TABLE Users (
   id int NOT NULL AUTO_INCREMENT,
   name varchar(200),
   email varchar(200),
   status varchar(50),
   PRIMARY KEY (id)
);


CREATE TABLE Tourist_Places(
   id int NOT NULL AUTO_INCREMENT,
   name varchar(100) NOT NULL,
   state_id int,
   image_url text,
   description text,
   review double,
   PRIMARY KEY (id),
   FOREIGN KEY(state_id) REFERENCES States(id)
);

CREATE TABLE Itineraries(
   id int NOT NULL AUTO_INCREMENT,
   state_id int,
   user_id int,
   start_date date,
   end_date date,
   notes text,
   budget double,
   PRIMARY KEY (id),
   FOREIGN KEY(state_id) REFERENCES States(id),
   FOREIGN KEY(user_id) REFERENCES Users(id)
);

CREATE TABLE Itinerary_Places(
   id int NOT NULL AUTO_INCREMENT,
   itinerary_id int,
   tourist_place_id int,
   visit_date date,
   start_time time,
   end_time time,
   PRIMARY KEY (id),
   FOREIGN KEY(itinerary_id) REFERENCES Itineraries(id),
   FOREIGN KEY(tourist_place_id) REFERENCES Tourist_Places(id)
);

CREATE TABLE Favorites(
    id int NOT NULL AUTO_INCREMENT,
    user_id int,
    tourist_place_id int,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES Users(id),
    FOREIGN KEY(tourist_place_id) REFERENCES Tourist_Places(id)
);

CREATE TABLE Expenses(
    id int NOT NULL AUTO_INCREMENT,
    category varchar(200),
    itinerary_id int NOT NULL,
    amount double,
    description varchar(200),
    PRIMARY KEY (id),
    FOREIGN KEY(itinerary_id) REFERENCES Itineraries(id)
    );

--INSERTION QUERIES

INSERT INTO Users(name,email,status) values("Amrutha","amrutha.mothajigari@gmail.com","ACTIVE");
INSERT INTO Users(name,email,status) values("Varsha","varsha.mothajigari@gmail.com","ACTIVE");

INSERT INTO Favorites(user_id,tourist_place_id) VALUES(1,2);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(1,12);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(1,32);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(1,52);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(1,23);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(1,28);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(2,4);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(2,5);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(2,6);
INSERT INTO Favorites(user_id,tourist_place_id) VALUES(2,27);


