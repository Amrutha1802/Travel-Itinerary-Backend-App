import grpc

# import main_pb2 as pb2
# import main_pb2_grpc as pb2_grpc
# from datetime import datetime, timezone
# from datetime import datetime, timedelta
# from google.protobuf.timestamp_pb2 import Timestamp

# from t import create_time_stamp_from_datetime
# TODO: use pb2 and pb2_grpc for imports
from gen import main_pb2_grpc as pb2_grpc
from gen import main_pb2 as pb2


class ItineraryClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.ItineraryServicesStub(self.channel)

    def create_user(self, request):
        response = self.stub.CreateUser(request)
        return response

    def get_states(self, request):
        response = self.stub.GetAllStates(request)
        return response

    def get_states_by_filter(self, request):
        response = self.stub.GetStateByFilter(request)
        return response

    def get_tourist_places_by_filter(self, request):
        response = self.stub.GetTouristPlacesByFilter(request)
        return response

    def add_user_favorite_place(self, request):
        response = self.stub.AddUserFavoritePlace(request)
        return response

    def get_user_favorite_places(self, request):
        response = self.stub.GetUserFavoritePlaces(request)
        return response

    def create_user_itinerary(self, request):
        response = self.stub.CreateUserItinerary(request)
        return response

    def get_states_by_type(self, request):
        response = self.stub.GetStatesByType(request)
        return response

    def get_state_types(self, request):
        response = self.stub.GetStateTypes(request)
        return response

    def get_state_by_id(self, request):
        response = self.stub.GetStateById(request)
        return response

    def get_tourist_places_in_state(self, request):
        response = self.stub.GetTouristPlacesInState(request)
        return response

    def get_tourist_place_by_id(self, request):
        response = self.stub.GetTouristPlaceById(request)
        return response

    def add_to_favorites_of_user(self, request):
        response = self.stub.AddToFavoritesOfUser(request)
        return response

    def get_favorites_of_user(self, request):
        response = self.stub.GetFavoritesOfUser(request)
        return response

    def delete_user_favorite(self, request):
        response = self.stub.DeleteUserFavoritePlace(request)
        return response

    def create_user_itinerary(self, request):
        response = self.stub.CreateUserItinerary(request)
        return response

    def delete_user_itinerary(self, request):
        response = self.stub.DeleteUserItinerary(request)
        return response


if __name__ == "__main__":
    client = ItineraryClient()
    # create user
    # request = pb2.User(
    #     name="User456",
    #     email="user456@gmail.com",
    # )
    # response = client.create_user(request)
    # print(response)

    # get all states
    # request = pb2.EmptyRequest()
    # response = client.get_states(request)
    # for i in response.states:
    #     print(i)

    # get states by filter
    # type = pb2.StateType.Name(2)
    # print("type is", type)

    # get_states_by_filter (id)
    # request = pb2.StateFilterRequest(
    #     state_id=456, place_type_filter="FILTER_BY_STATE_ID", type="STATE"
    # )
    # response = client.get_states_by_filter(request)
    # for i in response.states:
    #     print(i)

    # get states by filter(type)
    # request = pb2.StateFilterRequest(
    #     place_type_filter="FILTER_BY_STATE_TYPE", type="STATE"
    # )
    # response = client.get_states_by_filter(request)
    # for i in response.states:
    #     print(i)

    # get tourist places by filter
    # request = pb2.TouristPlacesFilterRequest(
    #     tourist_place_id=889, place_type_filter=3, state_id=1
    # )
    # response = client.get_tourist_places_by_filter(request)
    # for i in response.tourist_places:
    #     print(i)

    # add to favorites of user
    # request = pb2.AddFavoritePlaceRequest(user_id=4, tourist_place_id=112)
    # response = client.add_user_favorite_place(request)
    # print("response is", response.place)

    # get user favorites
    request = pb2.User(id=4)
    response = client.get_user_favorite_places(request)
    for i in response.favorites:
        print(i)

    # delete from favorites
    # request = pb2.FavoritePlace(id=2)
    # response = client.delete_user_favorite(request)
    # print("res is ", response)

    # create user itinerary

    from google.protobuf.timestamp_pb2 import Timestamp

    request = pb2.CreateUserItineraryRequest(
        budget=26222,
        end_date=Timestamp(seconds=-1295020477, nanos=698),
        notes="sed dolor ad eiusmod exercitation",
        start_date=Timestamp(seconds=427304120, nanos=4103529),
        state_id=1,
        user_id=1,
        expenses=[
            {
                "amount": 986,
                "description": "laborum nisi voluptate",
                "expense_category": 0,
            },
            {
                "description": "in eiusmod in ipsum id",
                "expense_category": 3,
                "amount": 123,
            },
        ],
        itinerary_places=[
            {
                "tourist_place": {
                    "id": 24,
                },
                "end_time": Timestamp(seconds=99196, nanos=-7930543),
                "start_time": Timestamp(seconds=8678, nanos=2076311),
                "visit_date": Timestamp(seconds=33456, nanos=-112269279),
            },
            {
                "tourist_place": {
                    "id": 2,
                },
                "end_time": Timestamp(seconds=9169, nanos=-7058143),
                "start_time": Timestamp(seconds=71427, nanos=20728611),
                "visit_date": Timestamp(seconds=334567, nanos=-112269279),
            },
        ],
    )
    # for i in request.itinerary_places:
    #     print("hiiii", i.visit_date)
    # print("request is ", type(request.itinerary_places))
    response = client.create_user_itinerary(request)
    print("response is ", response)

    # delete user itinerary

    # request = pb2.Itinerary(id=1)
    # client.delete_user_itinerary(request)

    # # print("request is ", request.itinerary_places[1]["tourist_place"])
    # response = client.create_user_itinerary(request)
    # print(response)

    # get user statueses
    # request = pb2.EmptyRequest()
    # response = client.get_user_statuses(request)
    # for i in response.statuses:
    #     print(i)

    # get states by type
    # request = pb2.StateTypeId(id=2)
    # response = client.get_states_by_type(request)
    # for i in response.states:
    #     print(i)

    # get_state_types
    # request = pb2.EmptyRequest()
    # response = client.get_state_types(request)
    # for i in response.state_types:
    #     print(i)

    # get_state_by_id
    # request = pb2.StateId(id=8)
    # response = client.get_state_by_id(request)
    # print(response)

    # get_tourist_places_in_state
    # request = pb2.StateId(id=3)
    # response = client.get_tourist_places_in_state(request)
    # for i in response.tourist_places:
    #     print(i)

    # get_tourist_place_by_id
    # request = pb2.TouristPlaceId(id=56)
    # response = client.get_tourist_place_by_id(request)
    # print(response)

    # add_to_favorites_of_user
    # request = pb2.AddFavoriteRequest(user_id=75, tourist_place_id=10)
    # response = client.add_to_favorites_of_user(request)
    # print(response)

    # get favorites of user
    # request = pb2.UserId(id=75)
    # response = client.get_favorites_of_user(request)
    # for i in response.favorites:
    #     print(i)

    # delete_from_favorites_of_user
    # request = pb2.FavoriteId(id=9)
    # response = client.delete_from_favorites_of_user(request)

    # add itinerary
    # start_date = datetime(2024, 1, 1, 0, 0, 0)
    # end_date = datetime(2024, 1, 8, 0, 0, 0)
    # start_timestamp = create_time_stamp_from_datetime(start_date)
    # end_timestamp = create_time_stamp_from_datetime(end_date)
    # request = pb2.AddItineraryRequest(
    #     state_id=1,
    #     start_date=start_timestamp,
    #     end_date=end_timestamp,
    #     user_id=75,
    #     budget=456.78,
    #     notes="Your itinerary notes",
    # )
    # response = client.add_itinerary(request)
    # print(response)

    # get itineraries of user
    # request = pb2.UserId(id=75)
    # response = client.get_itineraries_of_user(request)
    # for i in response.itineraries:
    #     print(i)

    # update itinerary
    # request = pb2.UpdateItineraryRequest(
    #     id=7,
    #     budget=1234556,
    #     notes="updated itinerary notes",
    # )
    # response = client.update_itinerary(request)
    # print(response)

    # delete itinerary
    # request = pb2.ItineraryId(id=5)
    # client.delete_itinerary(request)

    # get itinerary by id
    # request = pb2.ItineraryId(id=7)
    # response = client.get_itinerary_by_id(request)
    # print(response)

    # add itinerary_place
    # start_time = datetime(1970, 1, 1, 17, 30)
    # start_timestamp = Timestamp()
    # start_timestamp.FromDatetime(start_time)
    # end_time = datetime(1970, 1, 1, 23, 30)
    # end_timestamp = Timestamp()
    # end_timestamp.FromDatetime(end_time)
    # visit_date = datetime(2024, 12, 31, 0, 0)
    # visit_timestamp = Timestamp()
    # visit_timestamp.FromDatetime(visit_date)
    # request = pb2.AddItineraryPlaceRequest(
    #     tourist_place_id=12,
    #     itinerary_id=5,
    #     start_time=start_timestamp,
    #     end_time=end_timestamp,
    #     visit_date=visit_timestamp,
    # )
    # response = client.add_itinerary_place(request)
    # print(response)

    # update place in itinerary
    # start_time = datetime(1970, 1, 1, 12, 30)
    # start_timestamp = Timestamp()
    # start_timestamp.FromDatetime(start_time)
    # end_time = datetime(1970, 1, 1, 14, 30)
    # end_timestamp = Timestamp()
    # end_timestamp.FromDatetime(end_time)
    # request = pb2.UpdateItineraryPlaceRequest(
    #     id=6,
    #     start_time=start_timestamp,
    #     end_time=end_timestamp,
    # )
    # response = client.update_itinerary_place(request)
    # print(response)

    # get_itinerary_places_by_id_and_date
    # visit_date = datetime(2024, 12, 31, 0, 0)
    # visit_timestamp = Timestamp()
    # visit_timestamp.FromDatetime(visit_date)
    # request = pb2.GetItineraryPlacesRequest(itinerary_id=5, visit_date=visit_timestamp)
    # response = client.get_itinerary_places_by_date_and_id(request)
    # for i in response.itinerary_places:
    #     print(i)

    # remove place in itinerary
    # request = pb2.ItineraryPlaceId(id=4)
    # response = client.delete_place_in_itinerary(request)

    # get expense categories
    # request = pb2.EmptyRequest()
    # response = client.get_expense_categories(request)
    # for i in response.expense_categories:
    #     print(i)

    # add expense
    # request = pb2.AddExpenseRequest(
    #     itinerary_id=7, category_id=2, amount=130.0, description="dinner"
    # )
    # response = client.add_expense_to_itinerary(request)
    # print(response)

    # get expenses of itinerary
    # request = pb2.ItineraryId(id=7)
    # response = client.get_expenses_of_itinerary(request)
    # for i in response.expenses:
    #     print(i)

    # get remaining budget
    # request = pb2.ItineraryId(id=10)
    # response = client.get_remaining_budget(request)
    # print(response)
