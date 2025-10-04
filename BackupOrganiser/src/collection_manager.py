from data_collection import DataCollection

class CollectionManager:

    """Hanterar alla DataCollection objekt den är bossen av list-hanteringen
    Managern hanterar endast listorna den har inga egna collections i en lista. returnerar o olika former med hjälp av de olika funktionerna"""
    def __init__(self):
        self.collections = []

    def add_collection(self, name, description, creation_date, last_modified_date, still_updated):
        """Skapar ett DataCollection objekt och lägger till det i listan"""
        new_collection = DataCollection(
            name,
            description,
            creation_date,
            last_modified_date,
            still_updated
        )
        """Funkade ej, bytte till varianten ovan"""
        # new_collection = DataCollection()
        # new_collection.name = name
        # new_collection.description = description
        # new_collection.creation_date = creation_date
        # new_collection.last_modified_date = last_modified_date
        # new_collection.still_updated = still_updated
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
            """[0] skriver ner det första elementet"""
            out.append(collection.brief_str()[0]) 
        return out


    def detailed_overview(self):
        """Returnerar en array med listor av strängar, en lista per DataCollection"""
        out = []
        for collection in self.collections:
            out.append(collection.brief_str())
        return out


    def info(self, collection_name):
        """Returnerar en lista med strängar för EN specifik DataCollection"""
        for collection in self.collections:
            """Kollar om namnet på nuvarande collection matchar namn som söks"""
            if collection.name == collection_name:
                """körs när if är true"""
                return collection.full_str() 
        """Om ingen match hittas körs denna och endsat då"""
        return [f"Collection {collection_name} not found"]
        pass

    def get(self, collection_name):
        """Returnerar ett DataCollection objekt"""
        for collection in self.collections:
            """Kollar om namnet på nuvarande collection matchar namn som söks"""
            if collection.name == collection_name:
                return collection
        return None
