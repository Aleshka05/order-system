from flask import Flask, jsonify, request
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def send_notification():
    try:
        data = request.json
        logging.info(f"Notification: {data['message']}")
        
        return jsonify({
            'status': 'sent',
            'message': data['message'],
            'service': 'notification-service'
        })
    except Exception as e:
        logging.error(f"Error sending notification: {e}")
        return jsonify({'error': 'Bad request'}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'notification-service'})

@app.route('/')
def hello():
    return jsonify({'message': 'Notification Service is running!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)