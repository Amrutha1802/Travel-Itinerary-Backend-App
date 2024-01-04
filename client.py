import grpc

# import main_pb2 as pb2
# import main_pb2_grpc as pb2_grpc
# from datetime import datetime, timezone
# from datetime import datetime, timedelta
# from google.protobuf.timestamp_pb2 import Timestamp

# from t import create_time_stamp_from_datetime
# TODO: use pb2 and pb2_grpc for imports
import generated


class ItineraryClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = generated.ItineraryServicesStub(self.channel)

    def create_user(self, request):
        response = self.stub.CreateUser(request)
        return response

    def get_states(self, request):
        response = self.stub.GetAllStates(request)
        return response

    def get_user_statuses(self, request):
        response = self.stub.GetUserStatuses(request)
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

    def delete_from_favorites_of_user(self, request):
        response = self.stub.DeleteFromFavoritesOfUser(request)
        return response

    def add_itinerary(self, request):
        response = self.stub.CreateItinerary(request)
        return response

    def get_itineraries_of_user(self, request):
        response = self.stub.GetItinerariesOfUser(request)
        return response

    def update_itinerary(self, request):
        response = self.stub.UpdateItinerary(request)
        return response

    def delete_itinerary(self, request):
        response = self.stub.DeleteItinerary(request)
        return response

    def get_itinerary_by_id(self, request):
        response = self.stub.GetItinerary(request)
        return response

    def add_itinerary_place(self, request):
        response = self.stub.AddPlaceToItinerary(request)
        return response

    def update_itinerary_place(self, request):
        response = self.stub.UpdatePlaceInItinerary(request)
        return response

    def get_itinerary_places_by_date_and_id(self, request):
        response = self.stub.GetItineraryPlacesByDateAndId(request)
        return response

    def delete_place_in_itinerary(self, request):
        response = self.stub.DeletePlaceInItinerary(request)
        return response

    def get_expense_categories(self, request):
        response = self.stub.GetExpenseCategories(request)
        return response

    def add_expense_to_itinerary(self, request):
        response = self.stub.AddExpenseToItinerary(request)
        return response

    def get_expenses_of_itinerary(self, request):
        response = self.stub.GetExpensesOfItinerary(request)
        return response

    def get_remaining_budget(self, request):
        response = self.stub.GetRemainingBudget(request)
        return response


if __name__ == "__main__":
    client = ItineraryClient()
    # create user
    request = generated.User(
        name="Varsha",
        email="amothajigari@gmail.com",
        status="ACTIVE",
    )
    response = client.create_user(request)
    print(response)

    # get user statueses
    # request = pb2.EmptyRequest()
    # response = client.get_user_statuses(request)
    # for i in response.statuses:
    #     print(i)

    # get all states
    # request = pb2.EmptyRequest()
    # response = client.get_states(request)
    # for i in response.states:
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
