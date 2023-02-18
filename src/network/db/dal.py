from multiprocessing.heap import Arena
from urllib import response
from pymongo import MongoClient, errors
from model.swiss import Swiss
from model.arena import Arena
from config.environment_keys import db_client, db_name

def check_db_connection():
    try:
        client = MongoClient(db_client)
        database = client[db_name]
        collection = database['keep_alive']
        query = { "is_alive": "1" }
        collection.find(query)
        client.close()
        return(True)
    except MongoClient.err as err:
        print(err)
        return(False)

def insert_new_swiss_tournament(swiss: Swiss, pattern_name):
    new_data = {
        "type": "S",
        "pattern_name": pattern_name,
        "title": swiss.title, 
        "description": swiss.description, 
        "clock": swiss.clock, 
        "increment": swiss.increment, 
        "hour": fix_hour_for_database(swiss.hour), 
        "minute": swiss.minute, 
        "rounds": swiss.rounds,  
        "interval": swiss.interval
    }
    client = MongoClient(db_client)
    database = client[db_name]
    collection = database['torneios']
    addition = collection.insert_one(new_data)
    if addition.inserted_id != None:
        response = True
    else:
        response = False
    client.close()
    return(response)

def insert_new_arena_tournament(arena: Arena, pattern_name):
    new_data = {
        "type": "A",
        "pattern_name": pattern_name,
        "title": arena.title, 
        "description": arena.description, 
        "clock": arena.clock, 
        "increment": arena.increment, 
        "hour": fix_hour_for_database(arena.hour), 
        "minute": arena.minute, 
        "duration": arena.duration
    }
    client = MongoClient(db_client)
    database = client[db_name]
    collection = database['torneios']
    addition = collection.insert_one(new_data)
    if addition.inserted_id != None:
        response = True
    else:
        response = False
    client.close()
    return(response)

def load_tournament_list(list_name):
    client = MongoClient(db_client)
    database = client[db_name]
    collection = database['torneios']
    query = { "pattern_name": list_name }
    response = tuple(collection.find(query).sort("hour"))
    client.close()
    return(response)

def delete_tournament(pattern_name, title):
    client = MongoClient(db_client)
    database = client[db_name]
    collection = database['torneios']
    query = { 
        "pattern_name": { "$eq" : pattern_name },
        "title": { "$eq" : title }
    }
    deleted_data = collection.delete_one(query)
    if (deleted_data.deleted_count > 0):
        response = True
    else:
        response = False
    client.close()
    return(response)

def delete_all_tournaments_by_pattern_namet(pattern_name):
    client = MongoClient(db_client)
    database = client[db_name]
    collection = database['torneios']
    query = { 
        "pattern_name": { "$eq" : pattern_name }
    }
    deleted_data = collection.delete_many(query)
    if (deleted_data.deleted_count > 0):
        response = True
    else:
        response = False
    client.close()  
    return(response)

def fix_hour_for_database(hour):
    fixed_hour = 0
    match hour:
        case 0:
            fixed_hour = 24
        case 1:
            fixed_hour = 25
        case 2:
            fixed_hour = 26
        case other:
            fixed_hour = hour
    return(fixed_hour)