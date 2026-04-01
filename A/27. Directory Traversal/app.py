from flask import Flask, request, send_file
import os

app = Flask(__name__)
BASE_DIR = 'path/to/file'

@app.route('/download')
def download_file():
    # source of vulnerability, accepting unsanitized input
    user_filename = request.args.get('filename')
    
    # concatenating the path
    file_path = os.path.join(BASE_DIR, user_filename)
    
    try:
        return send_file(file_path)
    except FileNotFoundError:
        return "File not found", 404
    
# exploit on the report