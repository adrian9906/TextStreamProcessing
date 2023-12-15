from pymongo import errors
from Utilitis.Conexion_MongoDB import Conection_MongoDb
import pymongo.collation
#Función para buscar más de un documento
#parametros:
   #mongodb: "Nombre de la Base de Datos en MongoDB"
   #collections: "Nombre de la colección de la base de datos en MongoDB"
   #ID: "Consulta de mongo que nos permitirá eliminar el documento"
def findDoc(mongodb,collections,query):
    MONGO_TIME_OUT, MONGO_URI = Conection_MongoDb.serverInfo(0,"localhost","27017")#obtenemos los datos para conectarnos al servidor de Mongo
    try:
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT) #nos conectamos al servidor de Mongo
        baseDatos = cliente[mongodb]
        colleccion = baseDatos[collections]
        if query=='':
            datos=colleccion.find() #Encontramos los documentos que coincidan con la consulta
        else:
            datos=colleccion.find({query}) #Encontramos los documentos que coincidan con la consulta
        
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error en:"+errorConexion) #Se ejecuta si la conexión al servidor falla
    return datos
#Función para buscar un documento
#parametros:
   #mongodb: "Nombre de la Base de Datos en MongoDB"
   #collections: "Nombre de la colección de la base de datos en MongoDB"
   #ID: "Consulta de mongo que nos permitirá eliminar el documento
def FindOne(mongodb,collections,query):
    MONGO_TIME_OUT, MONGO_URI = Conection_MongoDb.serverInfo(0,"localhost","27017")#obtenemos los datos para conectarnos al servidor de Mongo
    try:
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT) #nos conectamos al servidor de Mongo
        baseDatos = cliente[mongodb]
        colleccion = baseDatos[collections]
        datos=colleccion.find_one({query}) #Encontramos el documento que coincida con la consulta
        colleccion.find_one()
    
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error en:"+errorConexion)
    return datos
