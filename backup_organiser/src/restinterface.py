from flask import Flask, request, jsonify, render_template
from collection_manager import CollectionManager
from backup_manager import BackupManager

app = Flask(__name__)

""" Skapa managers globalt """
collection_mgr = CollectionManager()
backup_mgr = BackupManager(collection_mgr)


@app.route("/")
def startpage():
    return render_template('index.html')



@app.route("/api/Collection", methods=["POST"])
def add_collection():
    """Lägg till ny collection"""
    try:
        data = request.get_json()
        collection_mgr.add_collection(
            name=data["name"],
            description=data["description"],
            creation_date=data["creation_date"],
            last_modified_date=data["modification_date"],
            still_updated=data["still_updated"],
        )
        return jsonify({"status": "success", "message": "Collection added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/Overview", methods=["GET"])
def get_overview():
    """Hämta översikt"""
    try:
        overview = collection_mgr.overview()
        return jsonify(overview), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/List", methods=["GET"])
def get_list():
    """Hämta detaljerad lista"""
    try:
        detailed = collection_mgr.detailed_overview()
        return jsonify(detailed), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/Info", methods=["GET"])
def get_info():
    """hämta info om lista"""
    name = request.args.get("name")
    try:
        info_list = collection_mgr.info(name)
        return jsonify(info_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/Backup", methods=["POST"])
def add_backup():
    """add a backup"""
    try:
        data = request.get_json()
        print(data)
        collection_name = data["name"]
        collection_object = collection_mgr.get(collection_name)
        if collection_object is None: 
            return "not found", 404

        backup_mgr.add_backup(
            collection_object=collection_object,
            backup_name=data["backupname"],
            backup_date=data["date"],
            backup_location=data["location"],
        )
        return jsonify({"status": "success", "message": "Backup added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/Unbackup", methods=["POST"])
def unbackup():
    """Ta bort en backup från en collection"""
    try:
        data = request.get_json()
        """ Validera att alla fält finns """
        required_fields = ["name", "backupname", "date"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        """Anropa backup_manager för att ta bort backupen"""
        success = backup_mgr.remove_backup(
            collection_name=data["name"],
            backup_name=data["backupname"],
            backup_date=data["date"],
        )
        if success:
            return jsonify({"status": "success", "message": "Backup removed"}), 200
        else:
            return jsonify({"error": "Collection or backup not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/Delete", methods=["DELETE"])
def delete_collection():
    """Ta bort en collection"""
    try:
        collection_name = request.args.get("name")
        if not collection_name:
            return jsonify({"error": "Missing 'name' parameter"}), 400
        success = collection_mgr.delete(collection_name)
        if success:
            return jsonify({"message": f"Collection '{collection_name}' deleted"}), 200
        else:
            return jsonify({"error": "Collection not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/Edit", methods=["POST"])
def edit_collection():
    """Redigerar collections genom modification_date eller still_updated"""
    try:
        data = request.get_json()
        collection_name = data.get("name")
        if not collection_name:
            return jsonify({"error": "Missing 'name' parameter"}), 400
        modification_date = data.get("modification_date")
        still_updated = data.get("still_updated")
        """Anropa edit med rätt parametrar"""
        success = collection_mgr.edit(
            collection_name = collection_name,
            last_modified_date = modification_date,
            still_updated = still_updated
        )
        if success:
            return jsonify({"message": f"Collection '{collection_name}' updated"}), 200
        else:
            return jsonify({"error": "Collection not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/Search', methods=['GET'])
def search():
    """Söker collections efter namn"""
    try:
        search_term = request.args.get('name')
        if not search_term:
            return jsonify({"error": "Missing 'name' parameter"}), 400
        """ HTML förväntar sig samma format som Overview """
        results = collection_mgr.search(search_term)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting BackupOrganiser REST API...")
    print("Listening on: http://localhost:8080/")
    app.run(debug=True, host="0.0.0.0", port=5000)