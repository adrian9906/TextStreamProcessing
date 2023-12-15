from pymongo import errors
from Utilitis.Conexion_MongoDB import Conection_MongoDb
import pymongo.collation
import pysolr
#Función para buscar más de un documento
#parametros:
   #mongodb: "Nombre de la Base de Datos en MongoDB"
   #collections: "Nombre de la colección de la base de datos en MongoDB"
   #filter: "Consulta para filtrar el documento en la base de datos en MongoDB"
   #update: "Nuevos argumentos que se remplazaran en el documento filtrado
def Ramplace(mongodb,collections,filter,update):
    MONGO_TIME_OUT, MONGO_URI = Conection_MongoDb.serverInfo(0,"localhost","27017")
    try:
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT)#nos conectamos al servidor de Mongo
        baseDatos = cliente[mongodb]
        colleccion = baseDatos[collections]
        if (colleccion.find_one(update)==None):  #verificamos si el documento no se encuentra en la Base de Datos en Mongo
            colleccion.find_one_and_replace(filter,update) #Remplazamos el documento
        else:
            print("Ese documento ya se encuentra en la base")
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error en:"+errorConexion)
