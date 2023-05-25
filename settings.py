from flask import Flask, request, jsonify
import base64
app = Flask(__name__)

@app.route('/process_frame', methods=['POST'])
def process_frame():
    frame_data = request.get_data()
    # image_data = frame_data.replace('data:image/jpeg;base64,', '')
    image_data = frame_data.decode('utf-8').replace('data:image/jpeg;base64,', '')
    # Decode the base64 string to bytes
    image_bytes = base64.b64decode(image_data)
    response = {
        'message': 'Frame received and processed'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)