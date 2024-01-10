from itinerary.time_funcs import (
    get_date_string_from_timestamp,
    get_pb_timestamp_from_date,
    get_pb_timestamp_from_time,
    get_time_str_from_timestamp,
)
from .db_config import db_conn2
from gen import main_pb2


def exec_query(query, values, many):
    """
    many = False -> fetchone
    many = True -> fetchall

    returns lastrow id if it is a insertion query and  a single element or an array of elements
    """
    try:
        with db_conn2.cursor() as cursor:
            if values is not None:
                cursor.execute(query, values)
                db_conn2.commit()
            else:
                cursor.execute(query)
                db_conn2.commit()

            if query.strip().lower().startswith("insert"):
                return cursor.lastrowid
            if many:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
        return result
    except:
        raise


def is_user_exists(email):
    """
    return bool
    """
    query = "SELECT 1 FROM Users WHERE email=(%s)"
    values = (email,)
    result = exec_query(query, values, False)
    if result is None:
        return False
    return True


def get_user_pb(user_db):
    """
        return user pb
    if the user doesn't exist:
        1. raise exception
        2. Send empty user object
    """
    if user_db is None:
        user_pb2 = main_pb2.User()
    else:
        user_pb2 = main_pb2.User(
            id=user_db["id"],
            name=user_db["name"],
            email=user_db["email"],
            status=user_db["status"],
        )
    return user_pb2


def get_states_pb(states_db):
    states_list = [
        {
            "id": state["id"],
            "name": state["name"],
            "image_url": state["image_url"],
            "description": state["description"],
            "type": state["type"],
        }
        for state in states_db
    ]
    return main_pb2.StatesList(states=states_list)


def get_state_pb(state_db):
    if state_db is None:
        return main_pb2.State()

    return main_pb2.State(
        id=state_db["id"],
        name=state_db["name"],
        image_url=state_db["image_url"],
        description=state_db["description"],
        type=state_db["type"],
    )


def get_tourist_places_pb(places_db):
    places_list = [
        {
            "id": place["id"],
            "name": place["name"],
            "state_name": place["state_name"],
            "image_url": place["image_url"],
            "description": place["description"],
            "review": place["review"],
        }
        for place in places_db
    ]
    places_pb2 = main_pb2.TouristPlacesFilterResponse(tourist_places=places_list)
    return places_pb2


def is_state_exists(state_id):
    query = "SELECT 1 FROM States WHERE id=(%s)"
    values = (state_id,)
    result = exec_query(query, values, False)
    if result is None:
        return False
    return True


def is_user_exists_with_given_id(user_id):
    """
    Check if a user with the provided user ID exists in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            query = "SELECT 1 FROM Users where id=(%s)"
            cursor.execute(query, (user_id,))
            user_db = cursor.fetchone()
            if user_db is None:
                return False
            return True
    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def is_tourist_place_exist(tourist_place_id):
    """
    Check if a tourist place with the provided ID exists in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            query = "SELECT 1 FROM Tourist_Places where id=(%s)"
            cursor.execute(query, (tourist_place_id,))
            place_db = cursor.fetchone()
            if place_db is None:
                return False
            return True

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def is_tourist_place_in_favorites(user_id, tourist_place_id):
    """
    Check if a user has a tourist place with given id in his favorite places with the provided ID exists in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            query = (
                "SELECT 1 FROM Favorites where tourist_place_id=(%s) and user_id=(%s)"
            )
            values = (tourist_place_id, user_id)
            place_db = exec_query(query, values, False)
            if place_db is None:
                return False
            return True

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def get_tourist_place_pb_by_id(tourist_place_id):
    query = """SELECT Tourist_Places.id, Tourist_Places.name, Tourist_Places.image_url,
                    Tourist_Places.description, Tourist_Places.review, States.name as state_name
                    FROM Tourist_Places
                    INNER JOIN States ON Tourist_Places.state_id = States.id
                    WHERE Tourist_Places.id = (%s)
                    """
    values = (tourist_place_id,)
    place_db = exec_query(query, values, False)
    place_pb = main_pb2.TouristPlace(
        id=place_db["id"],
        name=place_db["name"],
        state_name=place_db["state_name"],
        image_url=place_db["image_url"],
        description=place_db["description"],
        review=place_db["review"],
    )
    return place_pb


def get_favorite_place_pb(favorite_db):
    if favorite_db is None:
        return main_pb2.FavoritePlace()

    favorite_pb = main_pb2.FavoritePlace(
        id=favorite_db["id"],
        tourist_place=get_tourist_place_pb_by_id(favorite_db["tourist_place_id"]),
    )
    return favorite_pb


def get_favorite_places_pb(favorite_places_db):
    favorites_list = []
    for place in favorite_places_db:
        favorites_list.append(
            main_pb2.FavoritePlace(
                id=place["id"],
                tourist_place=get_tourist_place_pb_by_id(place["tourist_place_id"]),
            )
        )

    favorite_places_pb = main_pb2.FavoritePlacesList(favorites=favorites_list)
    return favorite_places_pb


def is_favorite_place_exist(favorite_place_id):
    """
    Check if a favorite place with the provided ID exists in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            query = "SELECT 1 FROM Favorites where id=(%s)"
            cursor.execute(query, (favorite_place_id,))
            place_db = cursor.fetchone()
            if place_db is None:
                return False
            return True
    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def if_state_exists(state_id):
    """
    Check if a state with the provided ID exists in the database.
    """
    query = "SELECT 1 FROM States where id=(%s)"
    values = (state_id,)
    place_db = exec_query(query, values, False)
    if place_db is None:
        return False
    return True


def get_itinerary_by_id(itinerary_id):
    query = "SELECT * FROM Itineraries WHERE id = %s"
    return exec_query(query, (itinerary_id,), False)


def get_state_by_id(state_id):
    query = "SELECT * FROM States WHERE id = %s"
    return exec_query(query, (state_id,), False)


def insert_itinerary_place(itinerary_id, place):
    query = """INSERT INTO Itinerary_Places(itinerary_id,tourist_place_id,start_time,end_time,visit_date)
               VALUES(%s,%s,%s,%s,%s)"""
    values = (
        itinerary_id,
        place.tourist_place.id,
        get_time_str_from_timestamp(place.start_time),
        get_time_str_from_timestamp(place.end_time),
        get_date_string_from_timestamp(place.visit_date),
    )
    return exec_query(query, values, False)


def get_itinerary_place_pb(itinerary_place_db):
    if itinerary_place_db is None:
        return main_pb2.ItineraryPlace()
    itinerary_place_pb = main_pb2.ItineraryPlace(
        id=itinerary_place_db["id"],
        tourist_place=get_tourist_place_pb_by_id(
            itinerary_place_db["toursit_place_id"]
        ),
        itinerary_id=itinerary_place_db["itinerary_id"],
        start_time=get_pb_timestamp_from_time(itinerary_place_db["start_time"]),
        end_time=get_pb_timestamp_from_time(itinerary_place_db["end_time"]),
        visit_date=get_pb_timestamp_from_date(itinerary_place_db["visit_date"]),
    )
    return itinerary_place_pb


def get_itinerary_places_list(itinerary_places_db):
    itinerary_places_list = [
        {
            "id": place["id"],
            "tourist_place": get_tourist_place_pb_by_id(place["tourist_place_id"]),
            "itinerary_id": place["itinerary_id"],
            "start_time": get_pb_timestamp_from_time(place["start_time"]),
            "end_time": get_pb_timestamp_from_time(place["end_time"]),
            "visit_date": get_pb_timestamp_from_date(place["visit_date"]),
        }
        for place in itinerary_places_db
    ]
    return itinerary_places_list


def get_itinerary_place_by_id(itinerary_place_id):
    query = "SELECT * FROM Itinerary_Places WHERE id = %s"
    return exec_query(query, (itinerary_place_id,), False)


def get_tourist_place_by_id(tourist_place_id):
    query = "SELECT * FROM TouristPlaces WHERE id = %s"
    return exec_query(query, (tourist_place_id,), False)


def insert_expense(itinerary_id, expense):
    query = "INSERT INTO Expenses(category,itinerary_id,amount,description) VALUES(%s,%s,%s,%s)"
    values = (
        main_pb2.ExpenseCategory.Name(expense.expense_category),
        itinerary_id,
        expense.amount,
        expense.description,
    )
    return exec_query(query, values, False)


def get_expenses_list(expenses_db):
    expenses_list = [
        {
            "id": expense["id"],
            "itinerary_id": expense["itinerary_id"],
            "expense_category": expense["category"],
            "description": expense["description"],
            "amount": expense["amount"],
        }
        for expense in expenses_db
    ]
    return expenses_list


def get_expense_by_id(cursor, expense_id):
    query = """SELECT id,category,itinerary_id,amount,description FROM Expenses WHERE Expenses.id = %s"""
    cursor.execute(query, (expense_id,))
    return cursor.fetchone()


def calculate_remaining_budget(itinerary_id):
    query = "SELECT COALESCE(SUM(amount), 0) AS sum_expenses FROM Expenses WHERE itinerary_id = %s"
    values = itinerary_id
    result = exec_query(query, values, False)
    total_expenses = result["sum_expenses"]
    budget_query = "SELECT budget FROM Itineraries WHERE id=(%s)"
    result = exec_query(budget_query, values, False)
    total_budget = result["budget"]

    remaining_budget = total_budget - total_expenses
    return remaining_budget


def get_itinerary_pb(itinerary_db):
    itinerary_id = itinerary_db["id"]
    state_db = get_state_by_id(itinerary_db["state_id"])
    state_pb = get_state_pb(state_db)

    query = "SELECT * FROM Itinerary_Places where itinerary_id=(%s)"
    values = (itinerary_id,)
    itinerary_places_db = exec_query(query, values, True)
    itinerary_places_pb = get_itinerary_places_list(itinerary_places_db)

    query = "SELECT * FROM Expenses where itinerary_id=(%s)"
    values = (itinerary_id,)
    expenses_db = exec_query(query, values, True)
    expenses_pb = get_expenses_list(expenses_db)

    remaining_budget = calculate_remaining_budget(itinerary_id)

    return main_pb2.Itinerary(
        id=itinerary_db["id"],
        state=state_pb,
        start_date=get_pb_timestamp_from_date(itinerary_db["start_date"]),
        end_date=get_pb_timestamp_from_date(itinerary_db["end_date"]),
        budget=itinerary_db["budget"],
        notes=itinerary_db["notes"],
        places=itinerary_places_pb,
        expenses=expenses_pb,
        remaining_budget=remaining_budget,
    )
