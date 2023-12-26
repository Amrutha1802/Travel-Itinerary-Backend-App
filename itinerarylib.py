import main_pb2 as pb2
from config import db_conn
from timestamplib import (
    create_timestamp_from_mysql_date,
    create_mysql_date_from_timestamp,
    create_mysql_time_from_timestamp,
    create_timestamp_from_mysql_time,
)


def check_for_email(email):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT 1 FROM Users WHERE email=(%s)"
        cursor.execute(sql, (email,))
        result = cursor.fetchone()
        if result is not None:
            raise Exception("User with given email id already exists")
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def check_for_user(user_id):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT 1 FROM Users WHERE id=(%s)"
        cursor.execute(sql, (user_id,))
        result = cursor.fetchone()
        if result is None:
            raise Exception("User with given id donot exists")
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def create_user(request):
    try:
        if len(request.name) == 0:
            raise Exception("Name cannot be empty")
        check_for_email(request.email)
        cursor = db_conn.cursor()
        sql = "INSERT INTO Users(name, email, mobile_no, status_id) VALUES(%s, %s, %s, %s)"
        val = (
            request.name,
            request.email,
            request.mobile_no,
            1,
        )
        cursor.execute(sql, val)
        db_conn.commit()
        last_inserted_id = cursor.lastrowid
        sql = "SELECT name, email, mobile_no, status_id FROM Users WHERE id = %s"
        val = (last_inserted_id,)
        cursor.execute(sql, val)
        user = cursor.fetchone()
        return pb2.User(
            id=last_inserted_id,
            name=user[0],
            email=user[1],
            mobile_no=user[2],
            status="Active",
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_user_statuses():
    try:
        cursor = db_conn.cursor()
        sql = "SELECT id,status FROM Status"
        cursor.execute(sql)
        result = cursor.fetchall()
        status_list = []
        for row in result:
            status = {"id": row[0], "status": row[1]}
            status_list.append(status)
        return pb2.Statuses(statuses=status_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_all_states():
    try:
        cursor = db_conn.cursor()
        sql = "SELECT id,name,image_url,description,state_type_id FROM States"
        cursor.execute(sql)
        result = cursor.fetchall()
        states_list = []
        for row in result:
            sql = "SELECT type FROM State_Types WHERE id=(%s)"
            val = (row[4],)
            cursor.execute(sql, val)
            type_row = cursor.fetchone()
            state = {
                "id": row[0],
                "name": row[1],
                "image_url": row[2],
                "description": row[3],
                "type": type_row[0],
            }
            states_list.append(state)
        return pb2.States(states=states_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_states_by_type(request):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT 1 FROM State_Types WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result is None:
            raise Exception("State-Type with given id donot exist")
        sql = "SELECT id,name,image_url,description,state_type_id FROM States WHERE state_type_id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        states_list = []
        for row in result:
            sql = "SELECT type FROM State_Types WHERE id=(%s)"
            val = (row[4],)
            cursor.execute(sql, val)
            type_row = cursor.fetchone()
            state = {
                "id": row[0],
                "name": row[1],
                "image_url": row[2],
                "description": row[3],
                "type": type_row[0],
            }
            states_list.append(state)
        return pb2.States(states=states_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_state_types():
    try:
        cursor = db_conn.cursor()
        sql = "SELECT id,type FROM State_Types"
        cursor.execute(sql)
        result = cursor.fetchall()
        types_list = []
        for row in result:
            status = {"id": row[0], "type": row[1]}
            types_list.append(status)
        return pb2.StateTypes(state_types=types_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_state_by_id(request):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT id,name,image_url,description,state_type_id FROM States WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        state = cursor.fetchone()
        if state is None:
            raise Exception("State with given id donot exist")
        sql = "SELECT type FROM State_Types WHERE id=(%s)"
        val = (state[4],)
        cursor.execute(sql, val)
        state_type = cursor.fetchone()
        return pb2.State(
            id=state[0],
            name=state[1],
            image_url=state[2],
            description=state[3],
            type=state_type[0],
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_tourist_places_in_state(request):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT name FROM States WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        state_name = cursor.fetchone()
        if state_name is None:
            raise Exception("State with given id donot exist")
        sql = "SELECT id,name,image_url,description,review FROM Tourist_Places WHERE state_id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        places = cursor.fetchall()
        tourist_places_list = []
        for row in places:
            place = {
                "id": row[0],
                "name": row[1],
                "image_url": row[2],
                "description": row[3],
                "review": row[4],
                "state_name": state_name[0],
            }
            tourist_places_list.append(place)
        return pb2.TouristPlaces(tourist_places=tourist_places_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_tourist_place_by_id(request):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT id,name,image_url,description,state_id,review FROM Tourist_Places WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        place = cursor.fetchone()
        if place is None:
            raise Exception("Tourist Place with given id donot exist")
        sql = "SELECT name FROM States WHERE id=(%s)"
        val = (place[4],)
        cursor.execute(sql, val)
        state_type = cursor.fetchone()
        return pb2.TouristPlace(
            id=place[0],
            name=place[1],
            image_url=place[2],
            description=place[3],
            review=place[5],
            state_name=state_type[0],
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def add_to_favorites_of_user(request):
    try:
        cursor = db_conn.cursor()
        check_for_user(request.user_id)
        sql = "SELECT id,name,state_id,image_url,description,review FROM Tourist_Places WHERE id = %s"
        val = (request.tourist_place_id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result is None:
            raise Exception("Tourist place with given id donot exist")
        sql = "SELECT 1 FROM Favorites WHERE user_id=(%s) and tourist_place_id=(%s)"
        val = (request.user_id, request.tourist_place_id)
        cursor.execute(sql, val)
        favorite_exists = cursor.fetchone()
        if favorite_exists:
            raise Exception("Favorite Already Exists")
        sql = "INSERT INTO Favorites(user_id,tourist_place_id) VALUES(%s, %s)"
        val = (request.user_id, request.tourist_place_id)
        cursor.execute(sql, val)
        db_conn.commit()
        last_inserted_id = cursor.lastrowid
        place = {
            "id": result[0],
            "name": result[1],
            "state_id": result[2],
            "image_url": result[3],
            "description": result[4],
            "review": result[5],
        }
        sql = "SELECT name FROM States WHERE id=(%s)"
        val = (place["state_id"],)
        cursor.execute(sql, val)
        state_name = cursor.fetchone()
        tourist_place = pb2.TouristPlace(
            id=place["id"],
            name=place["name"],
            state_name=state_name[0],
            image_url=place["image_url"],
            description=place["description"],
            review=place["review"],
        )
        return pb2.Favorite(id=last_inserted_id, tourist_place=tourist_place)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_favorites_of_user(request):
    try:
        cursor = db_conn.cursor()
        check_for_user(request.id)
        sql = "SELECT id,tourist_place_id FROM Favorites WHERE user_id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if len(result) == 0:
            raise Exception("User dont have any favorites")
        favorites_list = []
        for row in result:
            request = pb2.TouristPlaceId(id=row[1])
            tourist_place = get_tourist_place_by_id(request)
            favorite = {"id": row[0], "tourist_place": tourist_place}
            favorites_list.append(favorite)
        return pb2.Favorites(favorites=favorites_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def delete_from_favorites_of_user(request):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT 1 FROM Favorites WHERE id=(%s)"
        val = request.id
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result is None:
            raise Exception("Favorite with given id donot exist")
        sql = "DELETE FROM Favorites WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        db_conn.commit()
        return pb2.EmptyResponse()
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def check_for_state(state_id):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT 1 FROM States where id=(%s)"
        cursor.execute(sql, (state_id,))
        result = cursor.fetchone()
        if result is None:
            raise Exception("state with given id donot exist")
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def create_itinerary(request):
    try:
        cursor = db_conn.cursor()
        check_for_user(request.user_id)
        check_for_state(request.state_id)
        sql = "INSERT INTO Itineraries(state_id,user_id,start_date,end_date,notes,budget) VALUES(%s, %s,%s,%s,%s,%s)"
        val = (
            request.state_id,
            request.user_id,
            create_mysql_date_from_timestamp(request.start_date),
            create_mysql_date_from_timestamp(request.end_date),
            request.notes,
            request.budget,
        )
        cursor.execute(sql, val)
        db_conn.commit()
        itinerary_id = cursor.lastrowid
        sql = (
            "SELECT id,start_date,end_date,budget,notes FROM Itineraries WHERE id=(%s)"
        )
        val = (itinerary_id,)
        cursor.execute(sql, val)
        itinerary = cursor.fetchone()
        state_request = pb2.StateId(id=request.state_id)
        state = get_state_by_id(state_request)
        start_timestamp = create_timestamp_from_mysql_date(itinerary[1])
        end_timestamp = create_timestamp_from_mysql_date(itinerary[1])
        return pb2.Itinerary(
            id=itinerary[0],
            state=state,
            start_date=start_timestamp,
            end_date=end_timestamp,
            budget=itinerary[3],
            notes=itinerary[4],
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def check_for_itinerary(id):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT 1 FROM Itineraries where id=(%s)"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        if result is None:
            raise Exception("Itinerary with given id donot exist")
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_itineraries_of_user(request):
    try:
        check_for_user(request.id)
        cursor = db_conn.cursor()
        sql = "SELECT id,state_id,start_date,end_date,notes,budget FROM Itineraries WHERE user_id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        itineraries_list = []
        for row in result:
            state = get_state_by_id(pb2.StateId(id=row[1]))
            start_timestamp = create_timestamp_from_mysql_date(row[2])
            end_timestamp = create_timestamp_from_mysql_date(row[3])
            itinerary = {
                "id": row[0],
                "state": state,
                "start_date": start_timestamp,
                "end_date": end_timestamp,
                "notes": row[4],
                "budget": row[5],
            }
            itineraries_list.append(itinerary)
        return pb2.Itineraries(itineraries=itineraries_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def update_itinerary(request):
    try:
        check_for_itinerary(request.id)
        cursor = db_conn.cursor()
        sql = "UPDATE Itineraries SET"
        val = []
        if request.notes:
            sql += " notes=(%s),"
            val.append(request.notes)
        if request.budget:
            sql += " budget=(%s),"
            val.append(request.budget)
        sql = sql.rstrip(",")
        sql += " WHERE id=(%s) "
        val.append(request.id)
        if len(val) == 1:
            raise Exception("Budget or Notes is required to edit a todo")
        cursor.execute(sql, val)
        db_conn.commit()
        sql = "SELECT id,state_id,start_date,end_date,notes,budget FROM Itineraries WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        state = get_state_by_id(pb2.StateId(id=result[1]))
        start_timestamp = create_timestamp_from_mysql_date(result[2])
        end_timestamp = create_timestamp_from_mysql_date(result[3])
        return pb2.Itinerary(
            id=result[0],
            state=state,
            start_date=start_timestamp,
            end_date=end_timestamp,
            notes=result[4],
            budget=result[5],
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def delete_itinerary(request):
    try:
        check_for_itinerary(request.id)
        cursor = db_conn.cursor()
        sql = "DELETE FROM ItineraryPlaces where itinerary_id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        sql = "DELETE FROM Itineraries WHERE id=(%s)"
        cursor.execute(sql, val)
        db_conn.commit()
        return pb2.EmptyResponse()
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_itinerary_by_id(request):
    try:
        check_for_itinerary(request.id)
        cursor = db_conn.cursor()
        sql = "SELECT id,state_id,start_date,end_date,notes,budget FROM Itineraries WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        state = get_state_by_id(pb2.StateId(id=result[1]))
        start_timestamp = create_timestamp_from_mysql_date(result[2])
        end_timestamp = create_timestamp_from_mysql_date(result[3])
        return pb2.Itinerary(
            id=result[0],
            state=state,
            start_date=start_timestamp,
            end_date=end_timestamp,
            notes=result[4],
            budget=result[5],
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def add_place_to_itinerary(request):
    try:
        check_for_itinerary(request.itinerary_id)
        cursor = db_conn.cursor()
        place_request = pb2.TouristPlaceId(id=request.tourist_place_id)
        tourist_place = get_tourist_place_by_id(place_request)
        sql = "INSERT INTO ItineraryPlaces(itinerary_id,tourist_place_id,start_time,end_time,visit_date) VALUES(%s, %s,%s,%s,%s)"
        val = (
            request.itinerary_id,
            request.tourist_place_id,
            create_mysql_time_from_timestamp(request.start_time),
            create_mysql_time_from_timestamp(request.end_time),
            create_mysql_date_from_timestamp(request.visit_date),
        )
        cursor.execute(sql, val)
        db_conn.commit()
        itinerary_place_id = cursor.lastrowid
        sql = "SELECT id,tourist_place_id,start_time,end_time FROM ItineraryPlaces WHERE id=(%s)"
        val = (itinerary_place_id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        start_time = create_timestamp_from_mysql_time(result[2])
        end_time = create_timestamp_from_mysql_time(result[3])
        return pb2.ItineraryPlace(
            id=result[0],
            tourist_place=tourist_place,
            start_time=start_time,
            end_time=end_time,
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def check_for_itinerary_place(id):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT 1 FROM ItineraryPlaces where id=(%s)"
        val = (id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result is None:
            raise Exception("Itinerary Place with given id donot exist")
    except:
        raise


def update_place_in_itinerary(request):
    try:
        check_for_itinerary_place(request.id)
        cursor = db_conn.cursor()
        sql = "UPDATE ItineraryPlaces SET"
        val = []
        if request.start_time:
            sql += " start_time=(%s),"
            val.append(
                create_mysql_time_from_timestamp(request.start_time),
            )
        if request.end_time:
            sql += " end_time=(%s),"
            val.append(
                create_mysql_time_from_timestamp(request.end_time),
            )
        sql = sql.rstrip(",")
        sql += " WHERE id=(%s) "
        val.append(request.id)
        cursor.execute(sql, val)
        db_conn.commit()
        sql = "SELECT id,tourist_place_id,start_time,end_time FROM ItineraryPlaces WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        place_request = pb2.TouristPlaceId(id=result[1])
        tourist_place = get_tourist_place_by_id(place_request)
        start_time = create_timestamp_from_mysql_time(result[2])
        end_time = create_timestamp_from_mysql_time(result[3])
        return pb2.ItineraryPlace(
            id=result[0],
            tourist_place=tourist_place,
            start_time=start_time,
            end_time=end_time,
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_itinerary_places_by_date_and_id(request):
    try:
        check_for_itinerary(request.itinerary_id)
        cursor = db_conn.cursor()
        sql = "SELECT id,tourist_place_id,start_time,end_time FROM ItineraryPlaces WHERE itinerary_id=(%s) and visit_date=(%s)"
        visit_date = create_mysql_date_from_timestamp(request.visit_date)
        val = (request.itinerary_id, visit_date)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        places_list = []
        for row in result:
            tourist_place_request = pb2.TouristPlaceId(id=row[1])
            tourist_place = get_tourist_place_by_id(tourist_place_request)
            itinerary_place = {
                "id": row[0],
                "tourist_place": tourist_place,
                "start_time": create_timestamp_from_mysql_time(row[2]),
                "end_time": create_timestamp_from_mysql_time(row[3]),
            }
            places_list.append(itinerary_place)
        return pb2.ItineraryPlaces(itinerary_places=places_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def delete_place_in_itinerary(request):
    try:
        check_for_itinerary_place(request.id)
        cursor = db_conn.cursor()
        sql = "DELETE FROM ItineraryPlaces WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        db_conn.commit()
        return pb2.EmptyResponse()
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_expense_categories(request):
    try:
        cursor = db_conn.cursor()
        sql = "SELECT id,category FROM ExpenseCategories"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            raise Exception("There are no Expense Categories")
        categories_list = []
        for row in result:
            category = {"id": row[0], "category": row[1]}
            categories_list.append(category)
        return pb2.ExpenseCategories(expense_categories=categories_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def add_expense_to_itinerary(request):
    try:
        check_for_itinerary(request.itinerary_id)
        cursor = db_conn.cursor()
        sql = "SELECT 1 FROM ExpenseCategories WHERE id=(%s)"
        val = (request.category_id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result is None:
            raise Exception("Expense Category with given category id donot exist")
        sql = "INSERT INTO Expenses(itinerary_id,category_id,description,amount) VALUES(%s, %s,%s,%s)"
        val = (
            request.itinerary_id,
            request.category_id,
            request.description,
            request.amount,
        )
        cursor.execute(sql, val)
        db_conn.commit()
        expense_id = cursor.lastrowid
        print("id is", expense_id)
        sql = "SELECT amount,description FROM Expenses WHERE id=(%s)"
        val = (expense_id,)
        cursor.execute(sql, val)
        expense = cursor.fetchone()
        print("expense is", expense)
        sql = "SELECT category FROM ExpenseCategories WHERE id=(%s)"
        val = (request.category_id,)
        cursor.execute(sql, val)
        category = cursor.fetchone()
        print("category is ", category)
        return pb2.Expense(
            expense_category=category[0], description=expense[1], amount=expense[0]
        )
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_expenses_of_itinerary(request):
    try:
        check_for_itinerary(request.id)
        cursor = db_conn.cursor()
        sql = "SELECT category_id,amount,description FROM Expenses WHERE itinerary_id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        if len(result) == 0:
            raise Exception("There are no Expense Categories")
        expenses_list = []
        for row in result:
            sql = "SELECT category FROM ExpenseCategories WHERE id=(%s)"
            val = (row[0],)
            cursor.execute(sql, val)
            category = cursor.fetchone()
            expense = {
                "expense_category": category[0],
                "description": row[2],
                "amount": row[1],
            }
            expenses_list.append(expense)
        return pb2.Expenses(expenses=expenses_list)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e


def get_remaining_budget(request):
    try:
        check_for_itinerary(request.id)
        cursor = db_conn.cursor()
        sql = "SELECT sum(amount) FROM Expenses WHERE itinerary_id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        total_expenses = cursor.fetchone()
        print(total_expenses)
        sql = "SELECT budget FROM Itineraries WHERE id=(%s)"
        val = (request.id,)
        cursor.execute(sql, val)
        total_budget = cursor.fetchone()
        if total_expenses[0] is None:
            return pb2.RemainingBudget(remaining_budget=total_budget[0])
        remaining_budget = total_budget[0] - total_expenses[0]
        return pb2.RemainingBudget(remaining_budget=remaining_budget)
    except db_conn.Error as e:
        raise e
    except Exception as e:
        raise e
