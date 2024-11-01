from database_setup import SoftwareSetup

def search_software(name=None, publisher=None, category=None):
    query = SoftwareSetup.select()
    if name:
        query = query.where(SoftwareSetup.name.contains(name))
    if publisher:
        query = query.where(SoftwareSetup.publisher.contains(publisher))
    if category:
        query = query.where(SoftwareSetup.category.contains(category))
    
    for setup in query:
        print(f"Found: {setup.name}, Publisher: {setup.publisher}, Category: {setup.category}")
