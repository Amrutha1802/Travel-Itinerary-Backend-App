--Table: Users
CREATE TABLE Users (
   id int NOT NULL AUTO_INCREMENT,
   name varchar(200),
   email varchar(200),
   mobile_no bigint,
   status_id int,
   PRIMARY KEY (id),
   FOREIGN KEY(status_id) REFERENCES Status(id)
);

-- Table: States
CREATE TABLE States(
   id int NOT NULL AUTO_INCREMENT,
   name varchar(100) NOT NULL,
   image_url text,
   description text,
   state_type_id int,
   PRIMARY KEY (id),
   FOREIGN KEY(state_type_id) REFERENCES State_Types(id)
);

--Table: Statuses
CREATE TABLE Status(
    id int NOT NULL AUTO_INCREMENT,
    status varchar(200),
    PRIMARY KEY (id)
)

--Table: State_Types
CREATE TABLE State_Types (
   id int NOT NULL AUTO_INCREMENT,
   type varchar(200) NOT NULL,
   PRIMARY KEY (id)
);

-- Table: TouristPlaces
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
-- Table: Itineraries
CREATE TABLE Itineraries(
   id int NOT NULL AUTO_INCREMENT,
   state_id int,
   user_id int,
   start_date date,
   end_date date,
   notes text,
   budget double,
   PRIMARY KEY (id)
   FOREIGN KEY(state_id) REFERENCES States(id),
   FOREIGN KEY(user_id) REFERENCES Users(id)
)

-- Table: ItineraryPlaces
CREATE TABLE ItineraryPlaces(
   id int NOT NULL AUTO_INCREMENT,
   itinerary_id int,
   tourist_place_id int,
   start_time time,
   end_time time,
   visit_date date,
   PRIMARY KEY (id),
   FOREIGN KEY(itinerary_id) REFERENCES Itineraries(id),
   FOREIGN KEY(tourist_place_id) REFERENCES Tourist_Places(id)
)

-- Table: Favorites
CREATE TABLE Favorites(
    id int NOT NULL AUTO_INCREMENT,
    user_id int,
    tourist_place_id int,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES Users(id),
    FOREIGN KEY(tourist_place_id) REFERENCES Tourist_Places(id),
)
-- Table: Expenses
CREATE TABLE Expenses(
    id int NOT NULL AUTO_INCREMENT,
    category_id int NOT NULL,
    itinerary_id int NOT NULL,
    amount double,
    description varchar(200),
    PRIMARY KEY (id),
    FOREIGN KEY(itinerary_id) REFERENCES Itineraries(id),
    FOREIGN KEY(category_id) REFERENCES ExpenseCategories(id)
)

-- Table: ExpenseCategories
CREATE TABLE ExpenseCategories(
    id int NOT NULL AUTO_INCREMENT,
    category varchar(200),
    PRIMARY KEY (id)
)

-- Table: StatesTypes
CREATE TABLE StatesTypes(
    id int NOT NULL AUTO_INCREMENT,
    type varchar(200), 
    PRIMARY KEY (id)
)

--Table: Status
   CREATE TABLE Status(
      id int NOT NULL AUTO_INCREMENT,
      status varchar(200),
      PRIMARY KEY (id)
   )
