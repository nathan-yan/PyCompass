from flask import render_template, redirect, request

import pymongo
from pymongo import MongoClient as mc

import json

from . import application

#client = mc("mongodb://admin:@10.104.43.76:27017")
client = mc("mongodb://admin:@recordbookcluster0-shard-00-00-l24me.mongodb.net:27017,recordbookcluster0-shard-00-01-l24me.mongodb.net:27017,recordbookcluster0-shard-00-02-l24me.mongodb.net:27017/test?ssl=true&replicaSet=RecordBookCluster0-shard-0&authSource=admin")

@application.route("/")
def show_auth():
    return render_template("auth/connection_template.html")

@application.route("/connect", methods = ['POST', 'GET'])
def connect():
    connection_string = request.form.get("connection-string")
    print(connection_string)
    
    database_names = client.database_names()

    collections = []
    for name in database_names:
        collections.append(client[name].list_collection_names())

    print(collections)

    return render_template('home/databases_template.html', databases = database_names, collections = collections)

@application.route("/db/<database>")
def show_db(database):
    collection = request.args.get("collection")

    if collection:
        to_get = collection
    else:
        to_get = client[database].list_collection_names()[0];

    documents = client[database][to_get].find()
    num_documents= client[database][to_get].count()
    collections = client[database].list_collection_names()

    if (num_documents == 0):
        return render_template("home/database_template.html", name = database, collections = collections, collection_name = to_get, documents = "false")

    documents_ = []

    for d in range (num_documents):
        document = documents[d]
        document['_id'] = str(document['_id'])

        documents_.append(document)
        
    print(documents)
    string_documents = str(documents_).replace("True", 'true').replace('False', 'false').replace('None', 'null');
    return render_template("home/database_template.html", name = database, collections = collections, collection_name = to_get, documents = string_documents)
