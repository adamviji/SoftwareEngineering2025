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
        overview = collection_mgr.overview_json()
        return jsonify(overview), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/list", methods=["GET"])
def get_list():
    """Hämta detaljerad lista"""
    try:
        detailed = collection_mgr.detailed_overview_json()
        return jsonify(detailed), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/info", methods=["GET"])
def get_info():
    """Hämta info för specifik collection"""
    try:
        collection_name = request.args.get("name")

        if not collection_name:
            return jsonify({"error": "Missing 'name' parameter"}), 400

        info = collection_mgr.info_json(collection_name)

        if "error" in info:
            return jsonify(info), 404

        return jsonify(info), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/backup", methods=["POST"])
def add_backup():
    """Lägg till backup"""
    try:
        data = request.get_json()

        success = backup_mgr.add_backup(
            collection_name=data["name"],
            backup_name=data["backupname"],
            backup_date=data["date"],
            backup_location=data["location"],
        )

        if success:
            return jsonify({"status": "success", "message": "Backup added"}), 201
        else:
            return jsonify({"error": "Collection not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting BackupOrganiser REST API...")
    print("Listening on: http://localhost:8080/")
    app.run(debug=True, host="0.0.0.0", port=5000)