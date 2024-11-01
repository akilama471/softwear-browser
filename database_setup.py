from peewee import *

db = SqliteDatabase('software_setups.db')

class SoftwareSetup(Model):
    name = CharField()
    publisher = CharField(null=True)
    category = CharField(null=True)
    version = CharField(null=True)
    path = CharField()

    class Meta:
        database = db

def initialize_database():
    db.connect()
    db.create_tables([SoftwareSetup])

# Call this function in the main file to initialize
