# File Finder MCP Server

## Обзор
Данный проект реализует MCP сервер на Python, предназначенный для поиска файлов по фрагменту пути. При запросе сервер возвращает результаты в формате JSON, включающие имя файла, абсолютный путь, размер (в байтах) и дату создания.

## Требования
- Python 3.x
- Flask (устанавливается командой `pip install flask`)

## Установка
1. Клонируйте репозиторий:
   bash
   git clone https://github.com/Everest080/file-finder-mcp.git
   cd file-finder-mcp
   pip install flask
2. python file_finder_mcp.py --port 5000

## Тестирование сервера
    bash
    curl "http://localhost:5000/search?fragment=README.md"

## Пример промпта для тестирования из Cline
<use_mcp_tool>
  <server_name>file-finder-mcp</server_name>
  <tool_name>search_files</tool_name>
  <arguments>
    { "fragment": "README.md" }
  </arguments>
</use_mcp_tool>
