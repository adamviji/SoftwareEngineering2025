
from collection_manager import CollectionManager
from backup_manager import BackupManager
print("hello")
def main():
    """Main function to test the application"""
    print("BackupOrganiser starting...")
    # Your test code here
    collection_mgr = CollectionManager()
    backup_mgr = BackupManager(collection_mgr)

    print("=" * 50)
    print("TESTING BACKUPORGANISER")
    print("=" * 50)

    print("\n--- TEST 1: Adding Collections ---")
    collection_mgr.add_collection(
        "Customer Data", "All customer information", "2024-01-15", "2024-12-20", True
    )
    collection_mgr.add_collection(
        "Old Surveys", "Survey results from 2020", "2020-03-10", "2020-06-15", False
    )
    collection_mgr.add_collection(
        "Project Files", "Development project files", "2023-05-01", "2024-10-01", True
    )
    print("Added 3 collections")

    """ Test 2: Overview """
    print("\n--- TEST 2: Overview ---")
    for line in collection_mgr.overview():
        print(line)

    """ Test 3: Detailed Overview """
    print("\n--- TEST 3: Detailed Overview ---")
    for collection_info in collection_mgr.detailed_overview():
        for line in collection_info:
            print(line)

    """ Test 4: Info för specifik collection """
    print("\n--- TEST 4: Info for 'Customer Data' ---")
    for line in collection_mgr.info("Customer Data"):
        print(line)

    """ Test 5: Get collection object """
    print("\n--- TEST 5: Get Collection Object ---")
    cust_data = collection_mgr.get("Customer Data")
    if cust_data:
        print(f"Successfully retrieved: {cust_data.name}")

    """Test 6: Add backups"""
    print("\n--- TEST 6: Adding Backups ---")
    cust_data = collection_mgr.get("Customer Data")
    backup_mgr.add_backup(cust_data, "Backup-Jan", "2024-01-15", "/backups/jan/")
    backup_mgr.add_backup(cust_data, "Backup-Jun", "2024-06-20", "/backups/jun/")
    backup_mgr.add_backup(cust_data, "Backup-Dec", "2024-12-20", "/backups/dec/")

    proj_files = collection_mgr.get("Project Files")
    backup_mgr.add_backup(proj_files, "Backup-May", "2023-05-01", "/backups/projects/may/")
    backup_mgr.add_backup(proj_files, "Backup-Oct", "2024-10-01", "/backups/projects/oct/")

    print("Added backups to 'Customer Data' and 'Project Files'")

    """ Test 7: Visa info efter backups """
    print("\n--- TEST 7: Info After Adding Backups ---")
    print("\nCustomer Data:")
    for line in collection_mgr.info("Customer Data"):
        print(line)

    print("\nProject Files:")
    for line in collection_mgr.info("Project Files"):
        print(line)

    """ Test 8: Test med collection som inte finns """
    print("\n--- TEST 8: Getting Non-Existent Collection ---")
    missing = collection_mgr.get("Does Not Exist")
    if missing is None:
        print("Correctly returned None for non-existent collection")

    for line in collection_mgr.info("Does Not Exist"):
        print(line)

    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED")
    print("=" * 50)

if __name__ == "__main__":
    main()
