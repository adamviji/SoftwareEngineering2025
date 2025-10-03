from main import main
class BackupManager:

    def __init__(self):
        pass

    def add_backup(self, collection_object, backup_name, backup_date, backup_location):
        self.collection_object = collection_object
        self.backup_name = backup_name
        self.backup_date = backup_date
        self.backup_location = backup_location


if __name__ == "__main__":
    main()
