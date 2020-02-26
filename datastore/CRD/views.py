from flask.views import MethodView
from flask import jsonify, request
from CRD.functions import DataStoreCRD


class CreateData(MethodView):
    def __init__(self, db_path):
        self.db_path = db_path

    def post(self):
        try:
            json_data = request.get_json(force=True)
        except Exception:
            return jsonify({"status": "error", "message": "Incorrect request data format. Only JSON object is acceptable."}), 400

        # Create/Push data into the datasource.
        valid_data, message = DataStoreCRD().check_create_data(json_data, self.db_path)
        if not valid_data:
            return jsonify({"status": "error", "message": message}), 400

        return jsonify({"status": "success", "message": message}), 200


class ReadData(MethodView):
    def __init__(self, db_path):
        self.db_path = db_path

    def get(self):
        key = request.args.get('key')
        if key is None:
            return jsonify({"status": "error", "message": "key is required as a query param."}), 400

        # Read data from the datasource with the key(data index).
        data_found, message = DataStoreCRD().check_read_data(key, self.db_path)
        if not data_found:
            return jsonify({"status": "error", "message": message}), 404

        return jsonify(message), 200


class DeleteData(MethodView):
    def __init__(self, db_path):
        self.db_path = db_path

    def delete(self):
        key = request.args.get('key')

        if key is None:
            return jsonify({"status": "error", "message": "key is required as a query param."}), 400

        # Deletes a data from the datasource with the key(data index).
        data_found, message = DataStoreCRD().check_delete_data(key, self.db_path)
        if not data_found:
            return jsonify({"status": "error", "message": message}), 404

        return jsonify({"status": "success", "message": message}), 200
