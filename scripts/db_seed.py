import json
import sys

sys.path.append("..")

from itinerary.db_config import db_conn2
from gen import main_pb2 as pb2
from itinerary.helper_funcs import exec_query


def populate_states():
    try:
        with open("db.json", "r") as fp:
            """
            TODO: Get the states missing in DB in a single call using set operations A - B
            query = "Select name from States"
            cursor.execute(query)
            state_names = [] # names you get from the output
            """
            data = json.load(fp)
            states_dict = {state["name"]: state for state in data["states"]}
            states_set = set(states_dict.keys())
            # states_json_set = {state["name"] for state in data["states"]}

        query = "SELECT name from States"
        states_db = exec_query(query, values=None, many=True)
        states_db_set = {state["name"] for state in states_db}
        states_not_in_db = states_set - states_db_set

        values = []
        query = "INSERT INTO States(name,image_url,description,type) values"
        for state in states_not_in_db:
            state_dict = states_dict.get(state)
            values.append(
                "('{}', '{}', '{}', '{}')".format(
                    state_dict["name"],
                    state_dict["url"],
                    state_dict["description"],
                    state_dict["type"]
                )
            )

            # state_dict = next((s for s in data["states"] if s["name"] == state), None)
            # if state_dict:
                # values = (
                    # state_dict["name"],
                    # state_dict["url"],
                    # state_dict["description"],
                    # state_dict["type"],
                # )
        query += ",".join(values)
        exec_query(query, None, many=False)

    except:
        raise


populate_states()


def populate_tourist_places():
    try:
        with open("db.json", "r") as fp:
            data = json.load(fp)
            places_data = {place["name"]: place for place in data["tourist-places"]}
            places_json_set = {place["name"] for place in data["tourist-places"]}

        query = "SELECT name from Tourist_Places"
        places_db = exec_query(query, values=None, many=True)
        places_db_set = {place["name"] for place in places_db}
        places_not_in_db = places_json_set - places_db_set

        for place in places_not_in_db:
            query = "INSERT INTO Tourist_Places(name,state_id,image_url,description,review) values(%s,%s,%s,%s,%s)"
            place_dict = places_data[place]
            if place_dict:
                values = (
                    place_dict["name"],
                    get_state_id(place_dict["statename"]),
                    place_dict["images"][0]["url"],
                    place_dict["description"],
                    place_dict["review"],
                )
                exec_query(query, values, many=False)

    except:
        raise


def get_state_id(state_name):
    with db_conn2.cursor() as cursor:
        query = "SELECT id from States where name=(%s)"
        values = state_name
        result = exec_query(query, values, False)
        return result["id"]


# populate_state_types()
# populate_states()
populate_tourist_places()
# populate_expense_categories()
