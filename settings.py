from flask import Flask, request, Response, jsonify
import base64

app = Flask(__name__)

@app.route('/send_frame', methods=['POST'])
def receive_frame():
    frame_data = request.get_json()
    frame_base64 = frame_data['frame']

    # Process the frame (e.g., save it as an image file)
    # Decode the base64-encoded frame and perform any required image processing

    # Return the processed frame back to the frontend
    # return Response(response=frame_base64, status=200, mimetype='image/jpeg')
    return jsonify({'message': 'Frame received'})

if __name__ == '__main__':
    app.run(debug=True)
