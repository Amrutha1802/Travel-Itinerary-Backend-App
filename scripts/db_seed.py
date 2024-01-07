import json
import sys

sys.path.append("..")

from itinerary.db_config import db_conn2
from gen import main_pb2


def populate_state_types():
    try:
        with db_conn2:
            cursor = db_conn2.cursor()
            for key in main_pb2.StateType.keys():
                # TODO: Check if state type exist in the db
                check_type_query = "SELECT 1 FROM State_Types where type=(%s)"
                cursor.execute(check_type_query, (key,))
                state_type_db = cursor.fetchone()
                if state_type_db is not None:
                    query = "INSERT INTO State_Types(type) values(%s)"
                    val = (key,)
                    cursor.execute(query, val)
                    db_conn2.commit()
                else:
                    print("State type with given type already exists in the database")
    except Exception as e:
        raise e


def populate_states():
    # TODO: Get auto increment ids for state and union territories
    STATE_TYPE_ID = 2
    UT_TYPE_ID = 3

    state_types = {
        "state": STATE_TYPE_ID,
    }
    try:
        with open("scripts/db.json", "r") as fp:
            data = json.load(fp)
            with db_conn2:
                cursor = db_conn2.cursor()
                for state in data["states"]:
                    state_type = state["type"]
                    state_type_id = state_types.get(state_type, UT_TYPE_ID)
                    # TODO: Check if a row exists for this state
                    # Insert only if there is no state in the DB with the name
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


populate_state_types()
populate_states()
