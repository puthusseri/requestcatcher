from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask import request
import json
import ast

from datetime import datetime
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def catch_all(path):
    
    # Process the incoming request data
    data_str = request.get_data(as_text=True)
    try:
        # Try to parse the data as JSON
        json_data = json.loads(data_str)
        # If successful, format the JSON without escaping quotes
        print("ex")
        formatted_data = json.dumps(json_data, indent=2, ensure_ascii=False)
        print(type(formatted_data))
    except json.JSONDecodeError:
        # If not JSON, try to parse using ast.literal_eval
        try:
            data_dict = ast.literal_eval(data_str)
            
            formatted_data = json.dumps(data_dict, indent=2, ensure_ascii=False)
        except (SyntaxError, ValueError):
            # If parsing fails, use the original data
            
            formatted_data = data_str
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = request.remote_addr
    meta_info = {
        'received_time' : current_time,
        'ip_address' : ip_address,
    }
    request_data = {
        'path': path,
        'method': request.method,
        'headers': dict(request.headers),
        'data': formatted_data,
        "meta_info":  meta_info,
    }
  

    # Emit the request data to the default room (all connected clients)
    socketio.emit('incoming_request', request_data)

    # Send a basic response
    return f"Request for path: {path} received and broadcasted to the homepage."

if __name__ == '__main__':
    socketio.run(app, debug=True)
