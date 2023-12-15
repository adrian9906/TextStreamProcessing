import pymongo
from pymongo import errors
from Utilitis.Conexion_MongoDB import Conection_MongoDb
import pymongo.collation
#Función para buscar más de un documento
#parametros:
   #mongodb: "Nombre de la Base de Datos en MongoDB"
   #collections: "Nombre de la colección de la base de datos en MongoDB"
   #ID: "Consulta de mongo que nos permitirá insertar un documento"
def Insert(mongodb,collections,document):
    MONGO_TIME_OUT, MONGO_URI = Conection_MongoDb.serverInfo(0,"localhost","27017")#obtenemos los datos para conectarnos al servidor de Mongo
    try:
        find=False
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT)#nos conectamos al servidor de Mongo
        baseDatos = cliente[mongodb]
        colleccion = baseDatos[collections]

        if(colleccion.find_one(document)==None): #verificamos si el documento se encuentra en la Base de Datos en Mongo
            colleccion.insert_one(document) #Insertamos el documento en caso que este no se encuentre en la Base de Datos
        else:
            find=True

        if find==True:
            print("Documentos Repetidos")

    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error en:"+errorConexion)

#Función para buscar más de un documento
#parametros:
   #mongodb: "Nombre de la Base de Datos en MongoDB"
   #collections: "Nombre de la colección de la base de datos en MongoDB"
   #documents: "Consulta de mongo que nos permitirá insertar documentos"
def InsertMany(mongodb,collections,documents):
    MONGO_TIME_OUT, MONGO_URI = Conection_MongoDb.serverInfo(0,"localhost","27017")
    try:
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT)#nos conectamos al servidor de Mongo
        baseDatos = cliente[mongodb]
        colleccion = baseDatos[collections]
        colleccion.insert_many(documents) #Insertamos los documentos
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error en:"+errorConexion)
