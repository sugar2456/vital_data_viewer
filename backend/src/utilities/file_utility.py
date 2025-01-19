import json

class FileUtility:
    @staticmethod
    def load_json(file_path):
        try:
            with open(file_path, 'r') as json_file:
                json_data = json.load(json_file)  # JSONファイルを読み込む
                return json_data
        except Exception as err:
            print(f"Error occurred: {err}")