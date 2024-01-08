import grpc
from concurrent import futures
import logging
from itinerary import db_funcs
from gen import main_pb2_grpc as pb2_grpc


class ItineraryAppServer(pb2_grpc.ItineraryServicesServicer):
    def CreateUser(self, request, context):
        response = db_funcs.create_user(request)
        return response

    def GetAllStates(self, request, context):
        response = db_funcs.get_all_states()
        return response

    def GetStateByFilter(self, request, context):
        response = db_funcs.get_states_by_filter(request)
        return response

    def GetTouristPlacesByFilter(self, request, context):
        response = db_funcs.get_tourist_places_by_filter(request)
        return response

    def AddUserFavoritePlace(self, request, context):
        response = db_funcs.add_user_favorite_place(request)
        return response

    def GetUserFavoritePlaces(self, request, context):
        response = db_funcs.get_user_favorite_places(request)
        return response

    def DeleteUserFavoritePlace(self, request, context):
        response = db_funcs.delete_user_favorite_place(request)
        return response

    def CreateUserItinerary(self, request, context):
        response = db_funcs.create_user_itinerary(request)
        return response

    def GetStateTypes(self, request, context):
        response = get_state_types()
        return response

    def GetStateById(self, request, context):
        response = get_state_by_id(request)
        return response

    def GetTouristPlacesInState(self, request, context):
        response = get_tourist_places_in_state(request)
        return response

    def GetTouristPlaceById(self, request, context):
        response = get_tourist_place_by_id(request)
        return response

    def AddToFavoritesOfUser(self, request, context):
        response = add_to_favorites_of_user(request)
        return response

    def GetFavoritesOfUser(self, request, context):
        response = get_favorites_of_user(request)
        return response

    def DeleteFromFavoritesOfUser(self, request, context):
        response = delete_from_favorites_of_user(request)
        return response

    def CreateItinerary(self, request, context):
        response = create_itinerary(request)
        return response

    def GetItinerariesOfUser(self, request, context):
        response = get_itineraries_of_user(request)
        return response

    def UpdateItinerary(self, request, context):
        response = update_itinerary(request)
        return response

    def DeleteItinerary(self, request, context):
        response = delete_itinerary(request)
        return response

    def GetItinerary(self, request, context):
        response = get_itinerary_by_id(request)
        return response

    def AddPlaceToItinerary(self, request, context):
        response = add_place_to_itinerary(request)
        return response

    def UpdatePlaceInItinerary(self, request, context):
        response = update_place_in_itinerary(request)
        return response

    def GetItineraryPlacesByDateAndId(self, request, context):
        response = get_itinerary_places_by_date_and_id(request)
        return response

    def DeletePlaceInItinerary(self, request, context):
        response = delete_place_in_itinerary(request)
        return response

    def AddExpenseToItinerary(self, request, context):
        response = add_expense_to_itinerary(request)
        return response

    def GetExpenseCategories(self, request, context):
        response = get_expense_categories(request)
        return response

    def GetExpensesOfItinerary(self, request, context):
        response = get_expenses_of_itinerary(request)
        return response

    def GetRemainingBudget(self, request, context):
        response = get_remaining_budget(request)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ItineraryServicesServicer_to_server(ItineraryAppServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Running the gRPC server at localhost:50051")
    logging.basicConfig()
    serve()
