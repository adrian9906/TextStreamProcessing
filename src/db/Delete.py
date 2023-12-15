import pymongo
from pymongo import errors
from Utilitis.Conexion_MongoDB import Conection_MongoDb
import pymongo.collation
#Función para eliminar un documento
#parametros:
   #mongodb: "Nombre de la Base de Datos en MongoDB"
   #collections: "Nombre de la colección de la base de datos en MongoDB"
   #document: "Consulta de mongo que nos permitirá eliminar el documento"
def Delete(mongodb,collections,document):
    MONGO_TIME_OUT, MONGO_URI = Conection_MongoDb.serverInfo(0,"localhost","27017") #obtenemos los datos para conectarnos al servidor de Mongo
    try:
        find=False
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT) #nos conectamos al servidor de Mongo
        baseDatos = cliente[mongodb]
        colleccion = baseDatos[collections]
        colleccion.delete_one(document)#Eliminamos el documento en la Base de Datos de MongoDB

    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error en:"+errorConexion) #Se ejecuta si la conexión al servidor falla

#Función para eliminar más de un documento
#parametros:
   #mongodb: "Nombre de la Base de Datos en MongoDB"
   #collections: "Nombre de la colección de la base de datos en MongoDB"
   #document: "Consulta de mongo que nos permitirá eliminar el documento"
def DeleteMany(mongodb,collections,document):
    MONGO_TIME_OUT, MONGO_URI = Conection_MongoDb.serverInfo(0,"localhost","27017") #obtenemos los datos para conectarnos al servidor de Mongo
    try:
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT)#nos conectamos al servidor de Mongo
        baseDatos = cliente[mongodb]
        colleccion = baseDatos[collections]
        colleccion.delete_many(document)#Eliminamos los documentos en la Base de Datos de MongoDB

    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error en:"+errorConexion)#Se ejecuta si la conexión al servidor falla
doc1={"time_stamp":"Apr-8-2014-7:06:17-PM-PDT","category": "Notice","type":"WebLogicServer",
    "servername": "AdminServer","code":"BEA-000365","msg": "Server state changed to STARTING"}
DeleteMany("solr","wlslog",doc1)
