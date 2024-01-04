import json
import sys

sys.path.append("..")

from itinerary.db_config import db_conn2
from generated import main_pb2


def populate_state_types():
    try:
        with db_conn2:
            cursor = db_conn2.cursor()
            state_type_enum_items = main_pb2.StateType.items()
            for item in state_type_enum_items:
                if item[1] != 0:
                    query = "INSERT INTO State_Types(type) values(%s)"
                    val = (item[0],)
                    cursor.execute(query, val)
                    db_conn2.commit()
    except Exception as e:
        raise e


def populate_states(file):
    try:
        with open(file, "r") as json_file:
            data = json.load(json_file)
            with db_conn2:
                cursor = db_conn2.cursor()
                for state in data["states"]:
                    if state["type"] == "state":
                        state_type_id = 1
                    else:
                        state_type_id = 2
                    query = "INSERT INTO States(name,image_url,description,state_type_id) values(%s,%s,%s,%s)"
                    val = (
                        state["name"],
                        state["url"],
                        state["description"],
                        state_type_id,
                    )
                    cursor.execute(query, val)
                    db_conn2.commit()
    except:
        raise


# populate_state_types()
# populate_states("db.json")
