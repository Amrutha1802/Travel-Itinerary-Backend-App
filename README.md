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

`rpc CreateUser(CreateUserRequest) returns (User) {}`

##### GetUserStatuses

List all User statuses.

`rpc GetUserStatuses(EmptyRequest) returns (Statuses) {}`

#### GetAllStates

Lists all existing states information.

`rpc GetAllStates(EmptyRequest) returns (States) {}`

#### GetStatesByType

Lists all States based on given type.

`rpc GetStatesByType(StateTypeId) returns (States) {}`

#### GetStateById

Get Information about a state with given id

`rpc GetStateById(StateId) returns (State) {}`

#### GetTouristPlacesInState

Get Information about a tourist places in a state with given id

`rpc GetTouristPlacesInState(StateId) returns (TouristPlaces) {}`

#### GetTouristPlaceById

Get Information about a tourist place with given id

`rpc GetTouristPlaceById(TouristPlaceId) returns (TouristPlace) {}`

#### GetFavoritesOfUser

Get list of places that are added to favorites of given user with given id

`rpc GetFavoritesOfUser(UserId) returns (Favorites) {}`

#### AddToFavoritesOfUser

Add a place to user favorites

`rpc AddToFavoritesOfUser(AddFavoriteRequest) returns (Favorite) {}`

#### DeleteFromFavoritesOfUser

Remove a place from user favorites

`rpc DeleteFromFavoritesOfUser(FavoriteId) returns (Favorite) {}`

#### GetItinerariesOfUser

Get Information about itineraries created by a given user

`rpc GetItinerariesOfUser(UserId) returns (Itineraries) {}`

#### CreateItinerary

Create a new itinerary

`rpc CreateItinerary(AddItineraryRequest) returns (Itinerary) {}`

#### DeleteItinerary

Delete an itinerary with given id

`rpc DeleteItinerary(ItineraryId) returns (Itinerary) {}`

#### UpdateItinerary

Update Information of itinerary with given id

`rpc UpdateItinerary(UpdateItineraryRequest) returns (Itinerary) {}`

#### GetItinerary

Get Information about a itinerary with given id

`rpc GetItinerary(ItineraryId) returns (Itinerary) {}`

#### AddPlaceToItinerary

Add a place of visit to an itinerary

`rpc AddPlaceToItinerary(AddItineraryPlaceRequest) returns (ItineraryPlace) {}`

#### UpdatePlaceInItinerary

Update visit timings of a place in itinerary

`rpc UpdatePlaceInItinerary(UpdateItineraryPlaceRequest) returns (ItineraryPlace) {}`

#### GetItineraryPlacesByDateAndId

Get Information about a place and visit timings in an itinerary

`rpc GetItineraryPlacesByDateAndId(GetItineraryPlacesRequest returns (ItineraryPlaces) {}`

#### DeletePlaceInItinerary

Remove a place of visit from an itinerary

`rpc DeletePlaceInItinerary(ItineraryPlaceId) returns (EmptyResponse) {}`

#### GetExpensesOfItinerary

Get Information about expenses added to an itinerary with given id

`rpc GetExpensesOfItinerary(ItineraryId) returns (Expenses) {}`

#### AddExpenseToItinerary

Add a new expense to an itineray

`rpc AddExpenseToItinerary(AddExpenseRequest) returns (Expense) {}`

#### GetRemainingBudget

Get remaining budget of an itinerary with given id i.e total budget - total expenses

`rpc GetRemainingBudget(ItineraryId) returns (RemainingBudget) {}`

#### GetExpenseCategories

Get Information about all expense categories

`rpc GetExpenseCategories(EmptyRequest) returns (ExpenseCategories) {}`

### Project Structure

- server.py: Implementation of the gRPC server.
- client.py: Example client to interact with the gRPC server.
- Protos/main.proto: Protocol Buffers definition file.
- config.py: MySQL database setup.
- main_pb2.py and main_pb2_grpc.py: Generated files from the Protocol Buffers definition.
- sql-docs/db.sql: ddl queries for creating required tables in the MySQL database
- itinerarylib.py: helper functions for implementing the methods of the server
- timestamplib.py : helper functions for converting time stamp objects to mysql objects and vice versa
