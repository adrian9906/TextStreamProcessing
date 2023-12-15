from pymongo import errors
from Utilitis.Conexion_MongoDB import Conection_MongoDb
import pymongo.collation
#Función para buscar más de un documento
#parametros:
   #mongodb: "Nombre de la Base de Datos en MongoDB"
   #collections: "Nombre de la colección de la base de datos en MongoDB"
   #filter: "Consulta para filtrar el documento en la base de datos en MongoDB"
   #update: "Nuevos argumentos que se remplazaran en el documento filtrado
def Update(mongodb,collections,filter,update):
    MONGO_TIME_OUT, MONGO_URI = Conection_MongoDb.serverInfo(0,"localhost","27017")
    try:
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT)#nos conectamos al servidor de Mongo
        baseDatos = cliente[mongodb]
        colleccion = baseDatos[collections]
        colleccion.find_one_and_update(filter,{"$set":update}) #Actualizamos el documento
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Error en:"+errorConexion)


