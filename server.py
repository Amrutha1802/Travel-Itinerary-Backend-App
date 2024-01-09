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

    def DeleteUserItinerary(self, request, context):
        response = db_funcs.delete_user_itinerary(request)
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
