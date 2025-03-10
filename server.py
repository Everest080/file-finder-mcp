"""
File Finder MCP Server
Запускается локально, ищет файлы по фрагменту пути и возвращает результат в формате JSON.
Результат содержит: имя файла, абсолютный путь, размер файла (в байтах) и дату создания.
"""

import os
import datetime
import argparse
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_files():
    fragment = request.args.get('fragment')
    if not fragment:
        return jsonify({"error": "Отсутствует параметр 'fragment'"}), 400

    results = []
    # Поиск файлов, начиная с текущей директории.
    for root, dirs, files in os.walk("."):
        for file in files:
            if fragment.lower() in file.lower():
                file_path = os.path.join(root, file)
                try:
                    stats = os.stat(file_path)
                    size = stats.st_size
                    creation_time = datetime.datetime.fromtimestamp(stats.st_ctime).isoformat()
                except Exception as e:
                    size = None
                    creation_time = None
                results.append({
                    "filename": file,
                    "path": os.path.abspath(file_path),
                    "size": size,
                    "creation_date": creation_time
                })
    return jsonify(results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Finder MCP Server")
    parser.add_argument('--port', type=int, default=5000, help="Порт для запуска сервера")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port)