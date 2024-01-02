from flask import Flask, jsonify, request
from grpc import insecure_channel
import main_pb2 as pb2
import main_pb2_grpc as pb2_grpc

app = Flask(__name__)
grpc_channel = insecure_channel("localhost:50051")
grpc_stub = pb2_grpc.ItineraryServicesStub(grpc_channel)


@app.route("/v1/itinerary-service/create-user", methods=["POST"])
def create_user():
    try:
        request_data = request.get_json()
        grpc_request = pb2.CreateUserRequest(**request_data)

        grpc_response = grpc_stub.CreateUser(grpc_request)

        response_data = {
            "id": grpc_response.id,
            "name": grpc_response.name,
            "email": grpc_response.email,
            "mobile_no": grpc_response.mobile_no,
            "status": grpc_response.status,
        }

        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/v1/itinerary-service/get-user-statuses", methods=["GET"])
def get_user_statuses():
    try:
        grpc_request = pb2.EmptyRequest()

        grpc_response = grpc_stub.GetUserStatuses(grpc_request)

        statuses = [
            {"id": status.id, "status": status.status}
            for status in grpc_response.statuses
        ]

        return jsonify({"statuses": statuses})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=8080)
