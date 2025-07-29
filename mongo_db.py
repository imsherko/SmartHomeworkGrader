import os
from typing import Any, Dict, List

from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient

load_dotenv()

def connect_to_mongo_db(db_host: str, db_port: int) -> MongoClient:
    """
    Connect to MongoDB

    Parameters:
        db_host (str): host of MongoDB
        db_port (int): port of MongoDB
    Return:
        MongoClient
    """
    client = pymongo.MongoClient(host=db_host, port=db_port)
    return client

def create_mongo_db_collection(db_client: MongoClient):
    """
    Create MongoDB

    Parameters:
         db_client (MongoClient)
    Return:

    """
    db = db_client["mails_db"]
    mails_info_collection = db["mails_info"]
    return mails_info_collection

def insert_into_mongo_db(mails_info: List[Dict[str, Any]]) -> None:
    """
    Insert Mails information to MongoDB

    Parameters:
        mails_info (List[Dict[str]]): Dictionary of mail inforamtion
    Return:

    """
    db_host = os.getenv("MONGO_DB_HOST", "localhost")
    db_port = int(os.getenv("MONGO_DB_PORT", "27017"))
    mongo_db_client = connect_to_mongo_db(db_host=db_host, db_port=db_port)
    mongo_db_collection = create_mongo_db_collection(mongo_db_client)
    try:
        mongo_db_collection.insert_many(mails_info)
    except Exception as e:
        print(f"Error inserting documents: {e}")
    return None



