from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'password'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 31891
        #DB = 'AAC'
        #COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        #self.client = MongoClient('mongodb://aacuser:password@nv-desktop-services.apporto.com:31891' )
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print(USER,PASS)
        print("Connection successful")

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            return self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return False

    # Create method to implement the R in CRUD.
    def read_all(self, readData):
        cursor = self.database.animals.find(readData, {"_id" :False} )
        return cursor
    def read(self, readData):
        return self.database.animals.find(readData)
    
    # Update Method
    def update(self, data, updateData):
        if data is not None:
            result = self.database.animals.update_many(data, { "$set" : updateData})
                
        else:
            return "{}"
        print ("Update Complete")
        return result.raw_result
        
            
    # Delete Method
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        print ("Deleted")
        return result.raw_result