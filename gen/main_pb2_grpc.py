# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import main_pb2 as main__pb2


class ItineraryServicesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
            "/ItineraryServices/CreateUser",
            request_serializer=main__pb2.User.SerializeToString,
            response_deserializer=main__pb2.User.FromString,
        )
        self.GetAllStates = channel.unary_unary(
            "/ItineraryServices/GetAllStates",
            request_serializer=main__pb2.EmptyRequest.SerializeToString,
            response_deserializer=main__pb2.StatesList.FromString,
        )
        self.GetStateByFilter = channel.unary_unary(
            "/ItineraryServices/GetStateByFilter",
            request_serializer=main__pb2.StateFilterRequest.SerializeToString,
            response_deserializer=main__pb2.StatesFilterResponse.FromString,
        )
        self.GetTouristPlacesByFilter = channel.unary_unary(
            "/ItineraryServices/GetTouristPlacesByFilter",
            request_serializer=main__pb2.TouristPlacesFilterRequest.SerializeToString,
            response_deserializer=main__pb2.TouristPlacesFilterResponse.FromString,
        )
        self.GetUserFavoritePlaces = channel.unary_unary(
            "/ItineraryServices/GetUserFavoritePlaces",
            request_serializer=main__pb2.User.SerializeToString,
            response_deserializer=main__pb2.FavoritePlacesList.FromString,
        )
        self.AddUserFavoritePlace = channel.unary_unary(
            "/ItineraryServices/AddUserFavoritePlace",
            request_serializer=main__pb2.AddFavoritePlaceRequest.SerializeToString,
            response_deserializer=main__pb2.AddFavoritePlaceResponse.FromString,
        )
        self.DeleteUserFavoritePlace = channel.unary_unary(
            "/ItineraryServices/DeleteUserFavoritePlace",
            request_serializer=main__pb2.FavoritePlace.SerializeToString,
            response_deserializer=main__pb2.EmptyResponse.FromString,
        )
        self.CreateUserItinerary = channel.unary_unary(
            "/ItineraryServices/CreateUserItinerary",
            request_serializer=main__pb2.CreateUserItineraryRequest.SerializeToString,
            response_deserializer=main__pb2.CreateUserItineraryResponse.FromString,
        )
        self.DeleteUserItinerary = channel.unary_unary(
            "/ItineraryServices/DeleteUserItinerary",
            request_serializer=main__pb2.Itinerary.SerializeToString,
            response_deserializer=main__pb2.EmptyResponse.FromString,
        )
        self.GetUserItineraries = channel.unary_unary(
            "/ItineraryServices/GetUserItineraries",
            request_serializer=main__pb2.User.SerializeToString,
            response_deserializer=main__pb2.ItinerariesList.FromString,
        )
        self.UpdateUserItinerary = channel.unary_unary(
            "/ItineraryServices/UpdateUserItinerary",
            request_serializer=main__pb2.Itinerary.SerializeToString,
            response_deserializer=main__pb2.Itinerary.FromString,
        )
        self.GetItineraryById = channel.unary_unary(
            "/ItineraryServices/GetItineraryById",
            request_serializer=main__pb2.Itinerary.SerializeToString,
            response_deserializer=main__pb2.Itinerary.FromString,
        )
        self.AddItineraryPlace = channel.unary_unary(
            "/ItineraryServices/AddItineraryPlace",
            request_serializer=main__pb2.AddItineraryPlaceRequest.SerializeToString,
            response_deserializer=main__pb2.AddItineraryPlaceResponse.FromString,
        )
        self.DeleteItineraryPlace = channel.unary_unary(
            "/ItineraryServices/DeleteItineraryPlace",
            request_serializer=main__pb2.ItineraryPlace.SerializeToString,
            response_deserializer=main__pb2.EmptyResponse.FromString,
        )
        self.AddItineraryExpense = channel.unary_unary(
            "/ItineraryServices/AddItineraryExpense",
            request_serializer=main__pb2.Expense.SerializeToString,
            response_deserializer=main__pb2.Expense.FromString,
        )


class ItineraryServicesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetAllStates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetStateByFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTouristPlacesByFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUserFavoritePlaces(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddUserFavoritePlace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteUserFavoritePlace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateUserItinerary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteUserItinerary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUserItineraries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateUserItinerary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetItineraryById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddItineraryPlace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteItineraryPlace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AddItineraryExpense(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ItineraryServicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateUser": grpc.unary_unary_rpc_method_handler(
            servicer.CreateUser,
            request_deserializer=main__pb2.User.FromString,
            response_serializer=main__pb2.User.SerializeToString,
        ),
        "GetAllStates": grpc.unary_unary_rpc_method_handler(
            servicer.GetAllStates,
            request_deserializer=main__pb2.EmptyRequest.FromString,
            response_serializer=main__pb2.StatesList.SerializeToString,
        ),
        "GetStateByFilter": grpc.unary_unary_rpc_method_handler(
            servicer.GetStateByFilter,
            request_deserializer=main__pb2.StateFilterRequest.FromString,
            response_serializer=main__pb2.StatesFilterResponse.SerializeToString,
        ),
        "GetTouristPlacesByFilter": grpc.unary_unary_rpc_method_handler(
            servicer.GetTouristPlacesByFilter,
            request_deserializer=main__pb2.TouristPlacesFilterRequest.FromString,
            response_serializer=main__pb2.TouristPlacesFilterResponse.SerializeToString,
        ),
        "GetUserFavoritePlaces": grpc.unary_unary_rpc_method_handler(
            servicer.GetUserFavoritePlaces,
            request_deserializer=main__pb2.User.FromString,
            response_serializer=main__pb2.FavoritePlacesList.SerializeToString,
        ),
        "AddUserFavoritePlace": grpc.unary_unary_rpc_method_handler(
            servicer.AddUserFavoritePlace,
            request_deserializer=main__pb2.AddFavoritePlaceRequest.FromString,
            response_serializer=main__pb2.AddFavoritePlaceResponse.SerializeToString,
        ),
        "DeleteUserFavoritePlace": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteUserFavoritePlace,
            request_deserializer=main__pb2.FavoritePlace.FromString,
            response_serializer=main__pb2.EmptyResponse.SerializeToString,
        ),
        "CreateUserItinerary": grpc.unary_unary_rpc_method_handler(
            servicer.CreateUserItinerary,
            request_deserializer=main__pb2.CreateUserItineraryRequest.FromString,
            response_serializer=main__pb2.CreateUserItineraryResponse.SerializeToString,
        ),
        "DeleteUserItinerary": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteUserItinerary,
            request_deserializer=main__pb2.Itinerary.FromString,
            response_serializer=main__pb2.EmptyResponse.SerializeToString,
        ),
        "GetUserItineraries": grpc.unary_unary_rpc_method_handler(
            servicer.GetUserItineraries,
            request_deserializer=main__pb2.User.FromString,
            response_serializer=main__pb2.ItinerariesList.SerializeToString,
        ),
        "UpdateUserItinerary": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateUserItinerary,
            request_deserializer=main__pb2.Itinerary.FromString,
            response_serializer=main__pb2.Itinerary.SerializeToString,
        ),
        "GetItineraryById": grpc.unary_unary_rpc_method_handler(
            servicer.GetItineraryById,
            request_deserializer=main__pb2.Itinerary.FromString,
            response_serializer=main__pb2.Itinerary.SerializeToString,
        ),
        "AddItineraryPlace": grpc.unary_unary_rpc_method_handler(
            servicer.AddItineraryPlace,
            request_deserializer=main__pb2.AddItineraryPlaceRequest.FromString,
            response_serializer=main__pb2.AddItineraryPlaceResponse.SerializeToString,
        ),
        "DeleteItineraryPlace": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteItineraryPlace,
            request_deserializer=main__pb2.ItineraryPlace.FromString,
            response_serializer=main__pb2.EmptyResponse.SerializeToString,
        ),
        "AddItineraryExpense": grpc.unary_unary_rpc_method_handler(
            servicer.AddItineraryExpense,
            request_deserializer=main__pb2.Expense.FromString,
            response_serializer=main__pb2.Expense.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "ItineraryServices", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ItineraryServices(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/CreateUser",
            main__pb2.User.SerializeToString,
            main__pb2.User.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetAllStates(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/GetAllStates",
            main__pb2.EmptyRequest.SerializeToString,
            main__pb2.StatesList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetStateByFilter(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/GetStateByFilter",
            main__pb2.StateFilterRequest.SerializeToString,
            main__pb2.StatesFilterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetTouristPlacesByFilter(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/GetTouristPlacesByFilter",
            main__pb2.TouristPlacesFilterRequest.SerializeToString,
            main__pb2.TouristPlacesFilterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetUserFavoritePlaces(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/GetUserFavoritePlaces",
            main__pb2.User.SerializeToString,
            main__pb2.FavoritePlacesList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def AddUserFavoritePlace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/AddUserFavoritePlace",
            main__pb2.AddFavoritePlaceRequest.SerializeToString,
            main__pb2.AddFavoritePlaceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteUserFavoritePlace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/DeleteUserFavoritePlace",
            main__pb2.FavoritePlace.SerializeToString,
            main__pb2.EmptyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateUserItinerary(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/CreateUserItinerary",
            main__pb2.CreateUserItineraryRequest.SerializeToString,
            main__pb2.CreateUserItineraryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteUserItinerary(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/DeleteUserItinerary",
            main__pb2.Itinerary.SerializeToString,
            main__pb2.EmptyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetUserItineraries(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/GetUserItineraries",
            main__pb2.User.SerializeToString,
            main__pb2.ItinerariesList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateUserItinerary(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/UpdateUserItinerary",
            main__pb2.Itinerary.SerializeToString,
            main__pb2.Itinerary.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetItineraryById(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/GetItineraryById",
            main__pb2.Itinerary.SerializeToString,
            main__pb2.Itinerary.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def AddItineraryPlace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/AddItineraryPlace",
            main__pb2.AddItineraryPlaceRequest.SerializeToString,
            main__pb2.AddItineraryPlaceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteItineraryPlace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/DeleteItineraryPlace",
            main__pb2.ItineraryPlace.SerializeToString,
            main__pb2.EmptyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def AddItineraryExpense(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ItineraryServices/AddItineraryExpense",
            main__pb2.Expense.SerializeToString,
            main__pb2.Expense.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
