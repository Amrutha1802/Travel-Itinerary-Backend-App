import json
import sys

sys.path.append("..")

from itinerary.db_config import db_conn2
from gen import main_pb2 as pb2


def populate_state_types():
    try:
        with db_conn2.cursor() as cursor:
            for key in pb2.StateType.keys():
                # TODO: Check if state type exist in the db
                query = "SELECT 1 FROM State_Types where type=(%s)"
                val = (key,)
                cursor.execute(query, val)
                state_type_db = cursor.fetchone()
                if state_type_db is None:
                    query = "INSERT INTO State_Types(type) values(%s)"
                    val = (key,)
                    cursor.execute(query, val)
                    db_conn2.commit()
                else:
                    print("StateType already exists in the database")
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
        with open("db.json", "r") as fp:
            data = json.load(fp)
            with db_conn2.cursor() as cursor:
                for state in data["states"]:
                    # TODO: Check if a row exists for this state
                    query = "SELECT 1 FROM States where name=(%s)"
                    values = (state["name"],)
                    cursor.execute(query, values)
                    state_db = cursor.fetchone()
                    if state_db is None:
                        # Insert only if there is no state in the DB
                        state_type = state["type"]
                        state_type_id = state_types.get(state_type, UT_TYPE_ID)
                        query = "INSERT INTO States(name,image_url,description,state_type_id) values(%s,%s,%s,%s)"
                        val = (
                            state["name"],
                            state["url"],
                            state["description"],
                            state_type_id,
                        )
                        cursor.execute(query, val)
                        db_conn2.commit()
                    else:
                        print("State already exists in the database")
    except:
        raise


def populate_tourist_places():
    try:
        with open("db.json", "r") as fp:
            data = json.load(fp)
            with db_conn2.cursor() as cursor:
                for place in data["tourist-places"]:
                    query = "SELECT 1 FROM Tourist_Places where name=(%s)"
                    values = (place["name"],)
                    cursor.execute(query, values)
                    place_db = cursor.fetchone()
                    if place_db is None:
                        # Insert only if there is no tourist_place in the DB
                        query = "INSERT INTO Tourist_Places(name,state_id,image_url,description,review) values(%s,%s,%s,%s,%s)"
                        val = (
                            place["name"],
                            place["stateid"],
                            place["images"][0]["url"],
                            place["description"],
                            place["review"],
                        )
                        cursor.execute(query, val)
                        db_conn2.commit()
                    else:
                        print("Tourist-Place already exists in the database")
    except:
        raise


def populate_expense_categories():
    try:
        with db_conn2.cursor() as cursor:
            for key in pb2.ExpenseCategory.keys():
                # TODO: Check if expense category exist in the db
                query = "SELECT 1 FROM Expense_Categories where category=(%s)"
                val = (key,)
                cursor.execute(query, val)
                expense_category_db = cursor.fetchone()
                if expense_category_db is None:
                    query = "INSERT INTO Expense_Categories(category) values(%s)"
                    val = (key,)
                    cursor.execute(query, val)
                    db_conn2.commit()
                else:
                    print("Expense Category already exists in the database")
    except Exception as e:
        raise e


# populate_state_types()
# populate_states()
# populate_tourist_places()
# populate_expense_categories()
