from main import main
from Data_Collection import DataCollection

class CollectionManager:

    def __init__(self):
        self.collections = []

    def add_collection(self, name, description, creation_date, last_modified_date, still_updated):
        """Skapar ett DataCollection objekt och lägger till det i listan"""
        new_collection = DataCollection()
        new_collection.name = name
        new_collection.description = description
        new_collection.creation_date = creation_date
        new_collection.last_modified_date = last_modified_date
        new_collection.still_updated = still_updated
        self.collections.append(new_collection)
        # self.name = name
        # self.description = description
        # self.creation_date = creation_date
        # self.modification_date = modification_date
        # self.updated = update


    def overview(self):
        """returnerar en lista med strängar, en sträng per DataCollection"""
        out = []
        for collection in self.collections:
            out.append(collection.brief_str()[0])
        return out


    def detailed_overview(self):
        """Returnerar en array med listor av strängar, en lista per DataCollection"""
        out = []
        for collection in self.collections:
            out.append(collection.brief_str())
        return out


    def info(collection_name):
        """Returnerar en lista med strängar för en specifik DataCollection"""
        Data_Collection.full_str()
        pass

    def get(collection_name):
        pass

if __name__ == "__main__":
main()
