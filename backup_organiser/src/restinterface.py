from flask import Flask, request, jsonify
from collection_manager import CollectionManager
from backup_manager import BackupManager

app = Flask(__name__)

# Skapa managers globalt
collection_mgr = CollectionManager()
backup_mgr = BackupManager(collection_mgr)


@app.route("/")
def startpage():
    return "Tjosan - BackupOrganiser API is running!"


@app.route("/hello")
def hello():
    return "hello world"


@app.route("/api/collection", methods=["POST"])
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


@app.route("/api/overview", methods=["GET"])
def get_overview():
    """Hämta översikt"""
    try:
        overview = collection_mgr.overview()
        return jsonify(overview), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/list", methods=["GET"])
def get_list():
    """Hämta detaljerad lista"""
    try:
        detailed = collection_mgr.detailed_overview()
        return jsonify(detailed), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/info", methods=["GET"])
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
        backup_mgr.add_backup(
            collection_object=collection_object,
            backup_name=data["backup_name"],
            backup_date=data["date"],
            backup_location=data["location"],
        )

        return jsonify({"status": "success", "message": "Backup added"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting BackupOrganiser REST API...")
    print("Listening on: http://localhost:8080/")
    app.run(debug=True, host="0.0.0.0", port=5000)