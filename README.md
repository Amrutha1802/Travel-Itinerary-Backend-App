# Travel Itinerary Backend Application with gRPC, Protocol Buffers, and MySQL

This is a Travel Itinerary Application implemented using gRPC, Protocol Buffers, and MySQL in Python.
The application allows users

- to view tourist place in different states
- add tourist places to their favorites
- view their favorites
- user can create itinerary for a trip to a state
- view the itineraries created by the user,
- in the itinerary
  - user can add notes
  - add places to visit
  - visit timings on a particular date
  - add budget
  - add expenses to an itinerary
  - user can update the notes
  - update the budget
  - remove places in the itinerary

## Prerequisites

Before running the application, install following dependencies:

- Python 3.8.10
- MySQL 8.0.35

`pip install -r requirements.txt`

Create a database in MySQL- ItineraryDataBase

### To generate pb2 and pb2_grpc files

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. main.proto`

### To run grpc server

`python server.py`

The server will start at localhost:50051

### gRPC Client

You can use the provided gRPC client to interact with the server. Refer to the `client.py` file for examples on how to use the client.

`python client.py`

#### gRPC Service Methods

##### CreateUser

Create a new User.

`rpc CreateUser(User) returns (User) {}`

#### GetAllStates

Lists all existing states information.

`rpc GetAllStates(EmptyRequest) returns (StatesList) {}`

#### GetStateByFilter

List states based on the given filter type(id or state_type)

`rpc GetStateByFilter(StateFilterRequest) returns (StatesFilterResponse) {}`

#### GetTouristPlacesByFilter

List Tourist Places based on the given filter type(id or state_id)

`rpc GetTouristPlacesByFilter(TouristPlacesFilterRequest)returns (TouristPlacesFilterResponse) {}`

#### GetUserFavoritePlaces

Lists Tourist Places added to Favorites of a user

`rpc GetUserFavoritePlaces(User) returns (FavoritePlacesList) {}`

#### AddUserFavoritePlace

Add a tourist place to user Favorites

`rpc AddUserFavoritePlace(AddFavoritePlaceRequest) returns (AddFavoritePlaceResponse) {}`

#### DeleteUserFavoritePlace

Delete a tourist place from User Favorites

`rpc DeleteUserFavoritePlace(FavoritePlace) returns (EmptyResponse) {}`

#### GetUserItineraries

`rpc GetUserItineraries(User) returns (ItinerariesList) {}`

#### CreateUserItinerary

`rpc CreateUserItinerary(CreateUserItineraryRequest returns (CreateUserItineraryResponse) {}`

#### DeleteUserItinerary

`rpc DeleteUserItinerary(Itinerary) returns (EmptyResponse) {}`

#### UpdateUserItinerary

`rpc UpdateUserItinerary(Itinerary) returns (Itinerary) {}`

### Project Structure

- server.py: Implementation of the gRPC server.
- client.py: Example client to interact with the gRPC server.
- protos/main.proto: Protocol Buffers definition file.

gen/

- main_pb2.py and main_pb2_grpc.py: Generated files from the Protocol Buffers definition.

itinerary/

- db_config.py: MySQL database setup.
- db_funcs.py: helper functions for performing queries in database
- time_funcs: helper functions for converting datetime objects to timestamps and vice versa

- sql-docs/db.sql: ddl queries for creating required tables in the MySQL database

-scripts/db_seed.py: contains functions for populating data into tables in database
-db.json: json file with data of states and union territories
