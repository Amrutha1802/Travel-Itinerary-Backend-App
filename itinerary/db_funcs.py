import sys

sys.path.append("..")

from itinerary.db_config import db_conn2
from gen import main_pb2
from .time_funcs import (
    get_timestamp_from_time,
    get_date_string_from_timestamp,
    get_time_str_from_timestamp,
    get_pb_timestamp_from_date,
)


def create_user(request):
    """
    Getting name, email in request
    Create a user with these details
    TODO: validation
    user(name, email)
    """
    try:
        with db_conn2.cursor() as cursor:
            name = request.name
            email = request.email
            status = main_pb2.Status.Name(main_pb2.Status.ACTIVE)


            # TODO: validations - later
            # name
            # validation-1: shouldn't be empty
            # validation-2: name should contain only alphabets
            # email
            # validation-1: email should be a valid email address format

            # TODO: validation-2: check if a user exists with the same email
            def is_user_exist(email):
                """
                return bool
                """
                pass
            query = "SELECT 1 FROM Users WHERE email=(%s)"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            if result is not None:
                # Do not use exception
                raise Exception("User with given email id already exists ")

            # if is_user_exists(email):
                # raise Exception("User with given email id already exists ")

            query = "INSERT INTO Users(name,email,status) VALUES(%s,%s,%s)"
            values = (name, email, status)
            cursor.execute(query, values)
            db_conn2.commit()
            last_inserted_id = cursor.lastrowid

            """
            querying a user with id and creating a User proto msg
            """
            def get_user_pb(user_db):
                """
                return user pb
            if the user doesn't exist:
                1. raise exception
                2. Send empty user object
                """
                pass
            def get_users_pb(users_db):
                pass

            query = "SELECT name, email, status FROM Users WHERE id = %s"
            values = (last_inserted_id,)
            cursor.execute(query, values)
            user_db = cursor.fetchone()

            user_pb2 = main_pb2.User(
                id=last_inserted_id,
                name=user_db["name"],
                email=user_db["email"],
                status=user_db["status"],
            )

            return user_pb2

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def get_all_states():
    """
    Retrieve information about all states from the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            state_query = """
                    SELECT States.id, States.name, States.image_url, States.description, State_Types.type
                    FROM States
                    INNER JOIN State_Types ON States.state_type_id = State_Types.id
                """
            cursor.execute(state_query)
            states_db = cursor.fetchall()
            states_db = exec_query(query, None, many=True)
            def get_states_pb(states_db):
                """
                return states pb
                """
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

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def get_states_by_filter(request):
    """
    Retrieve states from the database based on the specified filter in the request.
    The function supports two filter types:
    1. FILTER_BY_STATE_ID: Retrieves a single state based on the provided state ID.
    2. FILTER_BY_STATE_TYPE: Retrieves states based on the provided state type.

    """
    try:
        with db_conn2.cursor() as cursor:
            place_type_filter = request.place_type_filter

            # if place_type_filter is FILTER_BY_STATE_ID ,retreive the state with given id
            if place_type_filter == main_pb2.FILTER_BY_STATE_ID:
                state_id = request.state_id
                state_query = """SELECT States.id,States.name,States.image_url,States.description,State_Types.type
                                FROM States
                                INNER JOIN State_Types ON States.state_type_id = State_Types.id
                                WHERE States.id = (%s)"""
                values = (state_id,)
                cursor.execute(state_query, values)
                states_db = cursor.fetchall()
                states_db = exec_query(query, values, many=True)
                # TODO: refactor
                def exec_query(query, values, many):
                    """
                    many = False -> fetchone
                    many = True -> fetchall

                    return either a single element or an array of elements
                    """

                if len(states_db) == 0:
                    raise Exception(
                        "State with given id is not present in the database"
                    )

            # if place_type_filter is FILTER_BY_STATE_TYPE ,retreive states with given state_type
            elif place_type_filter == main_pb2.FILTER_BY_STATE_TYPE:
                state_type = main_pb2.StateType.Name(request.type)
                if state_type == "UNDEFINED_STATE_TYPE":
                    raise Exception("Provided undefined_state_type")

                state_query = """SELECT States.id, States.name, States.image_url, States.description, State_Types.type
                                FROM States
                                INNER JOIN State_Types ON States.state_type_id = State_Types.id
                                WHERE State_Types.type = (%s)"""
                values = (state_type,)
                cursor.execute(state_query, values)
                states_db = cursor.fetchall()

            else:
                raise Exception("Cannot filter states based on given Filter type")

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
            states_pb2 = main_pb2.StatesFilterResponse(states=states_list)
            return states_pb2
    except:
        raise


def get_tourist_places_by_filter(request):
    """
    Retrieve tourist places from the database based on the specified filter in the request.
    The function supports two filter types:
    1. FILTER_BY_TOURIST_PLACE_ID: Retrieves a single tourist place based on the provided tourist place ID.
    2. FILTER_BY_STATE_ID: Retrieves tourist places based on the provided state ID.
    """
    try:
        with db_conn2.cursor() as cursor:
            place_type_filter = request.place_type_filter

            # if place_type_filter is FILTER_BY_TOURIST_PLACE_ID ,retreive the toruist place with given id
            if place_type_filter == main_pb2.FILTER_BY_TOURIST_PLACE_ID:
                tourist_place_id = request.tourist_place_id
                query = """SELECT Tourist_Places.id, Tourist_Places.name, Tourist_Places.image_url,
                        Tourist_Places.description, Tourist_Places.review, States.name as state_name
                        FROM Tourist_Places
                        INNER JOIN States ON Tourist_Places.state_id = States.id
                        WHERE Tourist_Places.id = (%s)
                        """
                values = (tourist_place_id,)
                cursor.execute(query, values)
                places_db = cursor.fetchall()

                # check if tourist_place with given id exists in the database
                if len(places_db) == 0:
                    raise Exception("Tourist Place with given id donot exist")

            # if place_type_filter is FILTER_BY_STATE_ID ,retreive tourist places with given state_id
            elif place_type_filter == main_pb2.FILTER_BY_STATE_ID:
                state_id = request.state_id

                # check if state with given id exists in the database
                state_query = "SELECT 1 from States where id=(%s)"
                cursor.execute(state_query, (state_id,))
                state_db = cursor.fetchone()
                if state_db is None:
                    raise Exception("State with given id donot exist in the database")

                places_query = """SELECT Tourist_Places.id, Tourist_Places.name, Tourist_Places.state_id, Tourist_Places.image_url,
                                Tourist_Places.description, Tourist_Places.review, States.name as state_name
                                FROM Tourist_Places
                                INNER JOIN States ON Tourist_Places.state_id = States.id
                                WHERE Tourist_Places.state_id = (%s)
                            """
                cursor.execute(places_query, (state_id,))
                places_db = cursor.fetchall()

            else:
                raise Exception(
                    "Cannot filter tourist places based on given Filter type"
                )

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
            places_pb2 = main_pb2.TouristPlacesFilterResponse(
                tourist_places=places_list
            )
            return places_pb2

    except:
        raise


def check_for_user(user_id):
    """
    Check if a user with the provided user ID exists in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            query = "SELECT 1 FROM Users where id=(%s)"
            cursor.execute(query, (user_id,))
            user_db = cursor.fetchone()
            if user_db is None:
                raise Exception("User with given id donot exist")
    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def check_for_tourist_place(tourist_place_id):
    """
    Check if a tourist place with the provided ID exists in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            query = "SELECT 1 FROM Tourist_Places where id=(%s)"
            cursor.execute(query, (tourist_place_id,))
            place_db = cursor.fetchone()
            if place_db is None:
                raise Exception("TouristPlace with given id donot exist")
    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def add_user_favorite_place(request):
    """
    Add a tourist place to the user's favorites in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            user_id = request.user_id
            tourist_place_id = request.tourist_place_id

            # check if user with given id exists in the database
            check_for_user(user_id)

            # check if tourist place with given id exists in the database
            check_for_tourist_place(tourist_place_id)

            query = (
                "SELECT 1 FROM Favorites where user_id=(%s) and tourist_place_id=(%s)"
            )
            values = (user_id, tourist_place_id)
            cursor.execute(query, values)
            favorite_place_db = cursor.fetchone()

            # idempodency- insert into favorites if tourist place with given id is not present in the database
            if favorite_place_db is None:
                query = "INSERT INTO Favorites(user_id,tourist_place_id) VALUES(%s,%s)"
                values = (user_id, tourist_place_id)
                cursor.execute(query, values)
                last_inserted_id = cursor.lastrowid
                db_conn2.commit()

                query = (
                    "SELECT id,user_id,tourist_place_id FROM Favorites WHERE id = %s"
                )
                values = (last_inserted_id,)
                cursor.execute(query, values)
                favorite_db = cursor.fetchone()

                # retreive details of tourist place with given id
                tourist_place_request = main_pb2.TouristPlacesFilterRequest(
                    tourist_place_id=favorite_db["tourist_place_id"],
                    place_type_filter="FILTER_BY_TOURIST_PLACE_ID",
                )
                tourist_place_pb2 = get_tourist_places_by_filter(tourist_place_request)
                tourist_place = tourist_place_pb2.tourist_places[0]

                favorite_pb2 = main_pb2.FavoritePlace(
                    id=last_inserted_id,
                    tourist_place=tourist_place,
                )

                return main_pb2.AddFavoritePlaceResponse(place=favorite_pb2)

            else:
                raise Exception(
                    "The given tourist place is already present in favorites of given user"
                )

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def get_user_favorite_places(request):
    """
    Retrieve the list of favorite places for a user from the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            user_id = request.id
            check_for_user(user_id)
            favorite_place_query = (
                "SELECT id,tourist_place_id FROM Favorites WHERE user_id=(%s)"
            )
            val = (request.id,)
            cursor.execute(favorite_place_query, val)
            favorite_places_db = cursor.fetchall()
            favorites_list = []

            for place in favorite_places_db:
                # retrieve details of the tourist place with given id
                place_request = main_pb2.TouristPlacesFilterRequest(
                    tourist_place_id=place["tourist_place_id"],
                    place_type_filter="FILTER_BY_TOURIST_PLACE_ID",
                )
                places_pb2 = get_tourist_places_by_filter(place_request)
                favorites_list.append(
                    main_pb2.FavoritePlace(
                        id=place["tourist_place_id"],
                        tourist_place=places_pb2.tourist_places[0],
                    )
                )

            return main_pb2.FavoritePlacesList(favorites=favorites_list)

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def check_for_favorite_place(favorite_place_id):
    """
    Check if a favorite place with the provided ID exists in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            query = "SELECT 1 FROM Favorites where id=(%s)"
            cursor.execute(query, (favorite_place_id,))
            place_db = cursor.fetchone()
            if place_db is None:
                raise Exception("Favorite Place with given id donot exist")
    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def delete_user_favorite_place(request):
    """
    Delete a favorite place from the user's favorites in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            favorite_place_id = request.id
            # check if favorite place with given id exists in database
            check_for_favorite_place(favorite_place_id)

            favorite_query = "DELETE FROM Favorites WHERE id=(%s)"
            val = (favorite_place_id,)
            cursor.execute(favorite_query, val)
            db_conn2.commit()

            return main_pb2.EmptyResponse()

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def check_for_state(state_id):
    """
    Check if a state with the provided ID exists in the database.
    """
    try:
        with db_conn2.cursor() as cursor:
            query = "SELECT 1 FROM States where id=(%s)"
            cursor.execute(query, (state_id,))
            place_db = cursor.fetchone()
            if place_db is None:
                raise Exception("State with given id donot exist")
    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def create_user_itinerary(request):
    try:
        with db_conn2.cursor() as cursor:
            user_id = request.user_id
            state_id = request.state_id
            start_date = request.start_date
            end_date = request.end_date
            budget = request.budget
            notes = request.notes
            itinerary_places = request.itinerary_places
            expenses = request.expenses
            # check if user with given id exists in the database
            check_for_user(user_id)
            # check if state with given id exists in the database
            check_for_state(state_id)

            itinerary_query = "INSERT INTO Itineraries(state_id,user_id,start_date,end_date,notes,budget) VALUES(%s,%s,%s,%s,%s,%s)"
            values = (
                state_id,
                user_id,
                get_date_string_from_timestamp(start_date),
                get_date_string_from_timestamp(end_date),
                notes,
                budget,
            )
            cursor.execute(itinerary_query, values)
            itinerary_id = cursor.lastrowid
            db_conn2.commit()

            itinerary_query = "SELECT * FROM Itineraries where id=(%s)"
            cursor.execute(itinerary_query, (itinerary_id,))
            itinerary_db = cursor.fetchone()

            state_request = main_pb2.StateFilterRequest(
                state_id=itinerary_db["state_id"],
                place_type_filter="FILTER_BY_STATE_ID",
            )
            state_db = get_states_by_filter(state_request).states[0]

            itinerary_places_pb2 = []
            # add itinerary places
            # tourist_place

            for place in itinerary_places:
                tourist_place_id = place.tourist_place.id
                check_for_tourist_place(tourist_place_id)

                start_time = place.start_time
                end_time = place.end_time
                visit_date = place.visit_date
                # place validation
                # date validation
                place_query = "INSERT INTO Itinerary_Places(itinerary_id,tourist_place_id,start_time,end_time,visit_date) VALUES(%s,%s,%s,%s,%s)"
                values = (
                    itinerary_id,
                    tourist_place_id,
                    get_time_str_from_timestamp(start_time),
                    get_time_str_from_timestamp(end_time),
                    get_date_string_from_timestamp(visit_date),
                )
                cursor.execute(place_query, values)
                db_conn2.commit()

                itinerary_place_id = cursor.lastrowid
                place_query = "SELECT id,itinerary_id,tourist_place_id,start_time,end_time,visit_date from Itinerary_Places where id=(%s)"
                cursor.execute(place_query, (itinerary_place_id,))
                itinerary_place_pb2 = cursor.fetchone()

                tourist_place_request = main_pb2.TouristPlacesFilterRequest(
                    tourist_place_id=place.tourist_place.id,
                    place_type_filter="FILTER_BY_TOURIST_PLACE_ID",
                )
                tourist_place_pb2 = get_tourist_places_by_filter(tourist_place_request)

                itinerary_place = main_pb2.ItineraryPlace(
                    id=itinerary_place_pb2["id"],
                    tourist_place=tourist_place_pb2.tourist_places[0],
                    itinerary_id=itinerary_place_pb2["itinerary_id"],
                    start_time=get_timestamp_from_time(
                        itinerary_place_pb2["start_time"]
                    ),
                    end_time=get_timestamp_from_time(itinerary_place_pb2["end_time"]),
                    visit_date=get_pb_timestamp_from_date(
                        itinerary_place_pb2["visit_date"]
                    ),
                )
                itinerary_places_pb2.append(itinerary_place)

            expenses_pb2 = []
            # add expenses to itinerary
            for expense in expenses:
                expense_category = main_pb2.ExpenseCategory.Name(
                    expense.expense_category
                )
                expense_description = expense.description
                expense_amount = expense.amount

                expense_category_id_query = (
                    "SELECT id from Expense_Categories where category=(%s)"
                )
                cursor.execute(expense_category_id_query, (expense_category,))
                expense_category_db = cursor.fetchone()
                expense_category_id = expense_category_db["id"]

                expense_query = "INSERT INTO Expenses(category_id,itinerary_id,amount,description) VALUES(%s,%s,%s,%s)"
                values = (
                    expense_category_id,
                    itinerary_id,
                    expense_amount,
                    expense_description,
                )
                cursor.execute(expense_query, values)
                db_conn2.commit()
                expense_id = cursor.lastrowid
                place_query = """SELECT Expenses.id,Expense_Categories.category,Expenses.itinerary_id,Expenses.amount,Expenses.description from Expenses
                                INNER JOIN Expense_Categories ON
                                Expenses.category_id=Expense_Categories.id
                                where Expenses.id=(%s)"""
                cursor.execute(place_query, (expense_id,))
                expense_db = cursor.fetchone()

                expense = main_pb2.Expense(
                    id=expense_db["id"],
                    expense_category=expense_db["category"],
                    itinerary_id=expense_db["itinerary_id"],
                    amount=expense_db["amount"],
                    description=expense_db["description"],
                )
                expenses_pb2.append(expense)

            # calculate remaining budget
            expenses_query = "SELECT COALESCE(sum(amount),0) as sum_expenses FROM Expenses WHERE itinerary_id=(%s)"
            cursor.execute(expenses_query, (itinerary_id,))
            result = cursor.fetchone()
            total_expenses = result["sum_expenses"]

            budget_query = "SELECT budget FROM Itineraries WHERE id=(%s)"
            cursor.execute(budget_query, (itinerary_id,))
            result = cursor.fetchone()
            total_budget = result["budget"]

            remaining_budget = total_budget - total_expenses

            itinerary_pb2 = main_pb2.Itinerary(
                id=itinerary_id,
                state=state_db,
                start_date=get_pb_timestamp_from_date(itinerary_db["start_date"]),
                end_date=get_pb_timestamp_from_date(itinerary_db["end_date"]),
                budget=itinerary_db["budget"],
                notes=itinerary_db["notes"],
                places=itinerary_places_pb2,
                expenses=expenses_pb2,
                remainingbudget=remaining_budget,
            )
            return main_pb2.CreateUserItineraryResponse(itinerary=itinerary_pb2)

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def check_for_itinerary(itinerary_id):
    try:
        with db_conn2.cursor() as cursor:
            query = "SELECT 1 FROM Itineraries where id=(%s)"
            cursor.execute(query, (itinerary_id,))
            place_db = cursor.fetchone()
            if place_db is None:
                raise Exception("Itinerary with given id donot exist")
    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def delete_user_itinerary(request):
    try:
        with db_conn2.cursor() as cursor:
            itinerary_id = request.id
            # check if itinerary exists
            check_for_itinerary(itinerary_id)
            # remove itinerary_places of given itinerary
            sql = "DELETE FROM ItineraryPlaces WHERE itinerary_id=(%s)"
            val = (itinerary_id,)
            cursor.execute(sql, val)
            db_conn2.commit()

            # remove expense of given itinerary
            sql = "DELETE FROM Expenses WHERE itinerary_id=(%s)"
            val = (itinerary_id,)
            cursor.execute(sql, val)
            db_conn2.commit()

            # remove itinerary from itineraries table
            sql = "DELETE FROM Itineraries WHERE id=(%s)"
            val = (itinerary_id,)
            cursor.execute(sql, val)
            db_conn2.commit()

            return main_pb2.EmptyResponse()
    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


def update_user_itinerary(request):
    try:
        with db_conn2.cursor() as cursor:
            itinerary_id = request.id
            check_for_itinerary(itinerary_id)
            budget = request.budget
            notes = request.notes

            query = "INSERT INTO Itineraries(state_id,user_id,start_date,end_date,notes,budget) VALUES(%s,%s,%s,%s,%s,%s)"
            values = (
                state_id,
                user_id,
                get_date_string(start_date),
                get_date_string(end_date),
                notes,
                budget,
            )
            cursor.execute(query, values)
            itinerary_id = cursor.lastrowid
            db_conn2.commit()

            itinerary_query = "SELECT * FROM Itineraries where id=(%s)"
            cursor.execute(itinerary_query, (itinerary_id,))
            itinerary_db = cursor.fetchone()

            state_request = main_pb2.StateFilterRequest(
                state_id=itinerary_db["state_id"],
                place_type_filter="FILTER_BY_STATE_ID",
            )
            state_db = get_states_by_filter(state_request)

            itinerary_places_pb2 = []
            # add itinerary places
            # tourist_place

            for place in itinerary_places:
                # place validation
                # date validation
                print("it", place)
                query = "INSERT INTO ItineraryPlaces(itinerary_id,tourist_place_id,start_time,end_time,visit_date) VALUES(%s,%s,%s,%s,%s)"
                values = (
                    itinerary_id,
                    place["tourist_place_id"],
                    get_time_from_timestamp(place["start_time"]),
                    get_time_from_timestamp(place["end_time"]),
                    get_date_string(place["visit_date"]),
                )
                cursor.execute(query, values)
                db_conn2.commit()
                itinerary_place_id = cursor.lastrowid
                place_query = "SELECT id,itinerary_id,tourist_place_id,start_time,end_time,visit_date where id=(%s)"
                cursor.execute(place_query, (itinerary_place_id,))
                itinerary_place_pb2 = cursor.fetchone()

                tourist_place_request = main_pb2.TouristPlacesFilterRequest(
                    tourist_place_id=place["tourist_place_id"],
                    place_type_filter="FILTER_BY_TOURIST_PLACE_ID",
                )
                tourist_place_pb2 = get_tourist_places_by_filter(tourist_place_request)
                itinerary_place = main_pb2.ItineraryPlace(
                    id=itinerary_place_pb2["id"],
                    tourist_place=tourist_place_pb2,
                    itinerary_id=itinerary_place_pb2["itinerary_id"],
                    start_time=itinerary_place_pb2["start_time"],
                    end_time=itinerary_place_pb2["end_time"],
                    visit_date=itinerary_place_pb2["visit_date"],
                )
                itinerary_places_pb2.append(itinerary_place)

            expenses_pb2 = []
            # add expenses to itinerary
            for expense in expenses:
                expense_category = expense.expense_category
                expense_description = expense.description
                expense_amount = expense.amount

                expense_category_id_query = (
                    "SELECT id from ExpenseCategories where category=(%s)"
                )
                cursor.execute(expense_category_id_query, (expense_category,))
                expense_category_db = cursor.fetchone()
                expense_category_id = expense_category_db["id"]

                expense_query = "INSERT INTO Expenses(category_id,itinerary_id,amount,description) VALUES(%s,%s,%s,%s)"
                values = (
                    expense_category_id,
                    itinerary_id,
                    expense_amount,
                    expense_description,
                )
                cursor.execute(expense_query, values)
                db_conn2.commit()
                expense_id = cursor.lastrowid
                place_query = "SELECT id,category_id,itinerary_id,amount where id=(%s)"
                cursor.execute(place_query, (expense_id,))
                expense_db = cursor.fetchone()

                expense = main_pb2.Expense(
                    id=expense_db["id"],
                    category_id=expense_db["category_id"],
                    itinerary_id=expense_db["itinerary_id"],
                    description=expense_db["description"],
                )
                expenses_pb2.append(expense)

            itinerary_pb2 = main_pb2.Itinerary(
                id=itinerary_db["id"],
                state=state_db,
                start_date=itinerary_db["start_date"],
                end_date=itinerary_db["end_date"],
                budget=itinerary_db["budget"],
                notes=itinerary_db["notes"],
                # places=itinerary_places_pb2,
                expenses=expenses_pb2,
            )
            return itinerary_pb2

    except db_conn2.Error as e:
        raise e
    except Exception as e:
        raise e


# def get_itineraries_of_user(request):
#     try:
#         check_for_user(request.id)
#         cursor = db_conn.cursor()
#         sql = "SELECT id,state_id,start_date,end_date,notes,budget FROM Itineraries WHERE user_id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         result = cursor.fetchall()
#         itineraries_list = []
#         for row in result:
#             state = get_state_by_id(pb2.StateId(id=row[1]))
#             start_timestamp = create_timestamp_from_mysql_date(row[2])
#             end_timestamp = create_timestamp_from_mysql_date(row[3])
#             itinerary = {
#                 "id": row[0],
#                 "state": state,
#                 "start_date": start_timestamp,
#                 "end_date": end_timestamp,
#                 "notes": row[4],
#                 "budget": row[5],
#             }
#             itineraries_list.append(itinerary)
#         return pb2.Itineraries(itineraries=itineraries_list)
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def update_itinerary(request):
#     try:
#         check_for_itinerary(request.id)
#         cursor = db_conn.cursor()
#         sql = "UPDATE Itineraries SET"
#         val = []
#         if request.notes:
#             sql += " notes=(%s),"
#             val.append(request.notes)
#         if request.budget:
#             sql += " budget=(%s),"
#             val.append(request.budget)
#         sql = sql.rstrip(",")
#         sql += " WHERE id=(%s) "
#         val.append(request.id)
#         if len(val) == 1:
#             raise Exception("Budget or Notes is required to edit a todo")
#         cursor.execute(sql, val)
#         db_conn.commit()
#         sql = "SELECT id,state_id,start_date,end_date,notes,budget FROM Itineraries WHERE id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         result = cursor.fetchone()
#         state = get_state_by_id(pb2.StateId(id=result[1]))
#         start_timestamp = create_timestamp_from_mysql_date(result[2])
#         end_timestamp = create_timestamp_from_mysql_date(result[3])
#         return pb2.Itinerary(
#             id=result[0],
#             state=state,
#             start_date=start_timestamp,
#             end_date=end_timestamp,
#             notes=result[4],
#             budget=result[5],
#         )
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def delete_itinerary(request):
#     try:
#         check_for_itinerary(request.id)
#         cursor = db_conn.cursor()
#         sql = "DELETE FROM ItineraryPlaces where itinerary_id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         sql = "DELETE FROM Itineraries WHERE id=(%s)"
#         cursor.execute(sql, val)
#         db_conn.commit()
#         return pb2.EmptyResponse()
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def get_itinerary_by_id(request):
#     try:
#         check_for_itinerary(request.id)
#         cursor = db_conn.cursor()
#         sql = "SELECT id,state_id,start_date,end_date,notes,budget FROM Itineraries WHERE id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         result = cursor.fetchone()
#         state = get_state_by_id(pb2.StateId(id=result[1]))
#         start_timestamp = create_timestamp_from_mysql_date(result[2])
#         end_timestamp = create_timestamp_from_mysql_date(result[3])
#         return pb2.Itinerary(
#             id=result[0],
#             state=state,
#             start_date=start_timestamp,
#             end_date=end_timestamp,
#             notes=result[4],
#             budget=result[5],
#         )
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def add_place_to_itinerary(request):
#     try:
#         check_for_itinerary(request.itinerary_id)
#         cursor = db_conn.cursor()
#         place_request = pb2.TouristPlaceId(id=request.tourist_place_id)
#         tourist_place = get_tourist_place_by_id(place_request)
#         sql = "INSERT INTO ItineraryPlaces(itinerary_id,tourist_place_id,start_time,end_time,visit_date) VALUES(%s, %s,%s,%s,%s)"
#         val = (
#             request.itinerary_id,
#             request.tourist_place_id,
#             create_mysql_time_from_timestamp(request.start_time),
#             create_mysql_time_from_timestamp(request.end_time),
#             create_mysql_date_from_timestamp(request.visit_date),
#         )
#         cursor.execute(sql, val)
#         db_conn.commit()
#         itinerary_place_id = cursor.lastrowid
#         sql = "SELECT id,tourist_place_id,start_time,end_time FROM ItineraryPlaces WHERE id=(%s)"
#         val = (itinerary_place_id,)
#         cursor.execute(sql, val)
#         result = cursor.fetchone()
#         start_time = create_timestamp_from_mysql_time(result[2])
#         end_time = create_timestamp_from_mysql_time(result[3])
#         return pb2.ItineraryPlace(
#             id=result[0],
#             tourist_place=tourist_place,
#             start_time=start_time,
#             end_time=end_time,
#         )
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def check_for_itinerary_place(id):
#     try:
#         cursor = db_conn.cursor()
#         sql = "SELECT 1 FROM ItineraryPlaces where id=(%s)"
#         val = (id,)
#         cursor.execute(sql, val)
#         result = cursor.fetchone()
#         if result is None:
#             raise Exception("Itinerary Place with given id donot exist")
#     except:
#         raise


# def update_place_in_itinerary(request):
#     try:
#         check_for_itinerary_place(request.id)
#         cursor = db_conn.cursor()
#         sql = "UPDATE ItineraryPlaces SET"
#         val = []
#         if request.start_time:
#             sql += " start_time=(%s),"
#             val.append(
#                 create_mysql_time_from_timestamp(request.start_time),
#             )
#         if request.end_time:
#             sql += " end_time=(%s),"
#             val.append(
#                 create_mysql_time_from_timestamp(request.end_time),
#             )
#         sql = sql.rstrip(",")
#         sql += " WHERE id=(%s) "
#         val.append(request.id)
#         cursor.execute(sql, val)
#         db_conn.commit()
#         sql = "SELECT id,tourist_place_id,start_time,end_time FROM ItineraryPlaces WHERE id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         result = cursor.fetchone()
#         place_request = pb2.TouristPlaceId(id=result[1])
#         tourist_place = get_tourist_place_by_id(place_request)
#         start_time = create_timestamp_from_mysql_time(result[2])
#         end_time = create_timestamp_from_mysql_time(result[3])
#         return pb2.ItineraryPlace(
#             id=result[0],
#             tourist_place=tourist_place,
#             start_time=start_time,
#             end_time=end_time,
#         )
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def get_itinerary_places_by_date_and_id(request):
#     try:
#         check_for_itinerary(request.itinerary_id)
#         cursor = db_conn.cursor()
#         sql = "SELECT id,tourist_place_id,start_time,end_time FROM ItineraryPlaces WHERE itinerary_id=(%s) and visit_date=(%s)"
#         visit_date = create_mysql_date_from_timestamp(request.visit_date)
#         val = (request.itinerary_id, visit_date)
#         cursor.execute(sql, val)
#         result = cursor.fetchall()
#         places_list = []
#         for row in result:
#             tourist_place_request = pb2.TouristPlaceId(id=row[1])
#             tourist_place = get_tourist_place_by_id(tourist_place_request)
#             itinerary_place = {
#                 "id": row[0],
#                 "tourist_place": tourist_place,
#                 "start_time": create_timestamp_from_mysql_time(row[2]),
#                 "end_time": create_timestamp_from_mysql_time(row[3]),
#             }
#             places_list.append(itinerary_place)
#         return pb2.ItineraryPlaces(itinerary_places=places_list)
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def delete_place_in_itinerary(request):
#     try:
#         check_for_itinerary_place(request.id)
#         cursor = db_conn.cursor()
#         sql = "DELETE FROM ItineraryPlaces WHERE id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         db_conn.commit()
#         return pb2.EmptyResponse()
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def get_expense_categories(request):
#     try:
#         cursor = db_conn.cursor()
#         sql = "SELECT id,category FROM ExpenseCategories"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         if len(result) == 0:
#             raise Exception("There are no Expense Categories")
#         categories_list = []
#         for row in result:
#             category = {"id": row[0], "category": row[1]}
#             categories_list.append(category)
#         return pb2.ExpenseCategories(expense_categories=categories_list)
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def add_expense_to_itinerary(request):
#     try:
#         check_for_itinerary(request.itinerary_id)
#         cursor = db_conn.cursor()
#         sql = "SELECT 1 FROM ExpenseCategories WHERE id=(%s)"
#         val = (request.category_id,)
#         cursor.execute(sql, val)
#         result = cursor.fetchone()
#         if result is None:
#             raise Exception("Expense Category with given category id donot exist")
#         sql = "INSERT INTO Expenses(itinerary_id,category_id,description,amount) VALUES(%s, %s,%s,%s)"
#         val = (
#             request.itinerary_id,
#             request.category_id,
#             request.description,
#             request.amount,
#         )
#         cursor.execute(sql, val)
#         db_conn.commit()
#         expense_id = cursor.lastrowid
#         print("id is", expense_id)
#         sql = "SELECT amount,description FROM Expenses WHERE id=(%s)"
#         val = (expense_id,)
#         cursor.execute(sql, val)
#         expense = cursor.fetchone()
#         print("expense is", expense)
#         sql = "SELECT category FROM ExpenseCategories WHERE id=(%s)"
#         val = (request.category_id,)
#         cursor.execute(sql, val)
#         category = cursor.fetchone()
#         print("category is ", category)
#         return pb2.Expense(
#             expense_category=category[0], description=expense[1], amount=expense[0]
#         )
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def get_expenses_of_itinerary(request):
#     try:
#         check_for_itinerary(request.id)
#         cursor = db_conn.cursor()
#         sql = "SELECT category_id,amount,description FROM Expenses WHERE itinerary_id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         result = cursor.fetchall()
#         if len(result) == 0:
#             raise Exception("There are no Expense Categories")
#         expenses_list = []
#         for row in result:
#             sql = "SELECT category FROM ExpenseCategories WHERE id=(%s)"
#             val = (row[0],)
#             cursor.execute(sql, val)
#             category = cursor.fetchone()
#             expense = {
#                 "expense_category": category[0],
#                 "description": row[2],
#                 "amount": row[1],
#             }
#             expenses_list.append(expense)
#         return pb2.Expenses(expenses=expenses_list)
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e


# def get_remaining_budget(request):
#     try:
#         check_for_itinerary(request.id)
#         cursor = db_conn.cursor()
#         sql = "SELECT sum(amount) FROM Expenses WHERE itinerary_id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         total_expenses = cursor.fetchone()
#         print(total_expenses)
#         sql = "SELECT budget FROM Itineraries WHERE id=(%s)"
#         val = (request.id,)
#         cursor.execute(sql, val)
#         total_budget = cursor.fetchone()
#         if total_expenses[0] is None:
#             return pb2.RemainingBudget(remaining_budget=total_budget[0])
#         remaining_budget = total_budget[0] - total_expenses[0]
#         return pb2.RemainingBudget(remaining_budget=remaining_budget)
#     except db_conn.Error as e:
#         raise e
#     except Exception as e:
#         raise e
