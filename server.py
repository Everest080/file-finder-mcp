import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def find_files(query, search_paths=None, max_results=100):
    if search_paths is None:
        search_paths = [f"{d}:/" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:/")]

    result = []
    print(f"Searching for: {query} in {search_paths}")  # Debugging

    for search_path in search_paths:
        for root, dirs, files in os.walk(search_path):
            try:
                for file in files:
                    if query.lower() in file.lower():
                        file_path = os.path.join(root, file)
                        file_info = {
                            "name": file,
                            "path": file_path,
                            "size": os.path.getsize(file_path),
                            "created_at": os.path.getctime(file_path),
                        }
                        result.append(file_info)
                        print(f"Found: {file_info}")  # Debugging

                        if len(result) >= max_results:
                            return result  # Stop early if max results reached
            except (PermissionError, FileNotFoundError):
                continue  # Skip directories with permission issues

    return result

@app.route('/search', methods=['GET'])
def search_files():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    results = find_files(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
