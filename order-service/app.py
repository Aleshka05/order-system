from flask import Flask, jsonify, request
import consul
import os
import requests
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

# Конфигурация через Consul
consul_client = consul.Consul(host='consul-server', port=8500)

def get_config(key):
    try:
        index, data = consul_client.kv.get(key)
        return data['Value'].decode('utf-8') if data else None
    except Exception as e:
        logging.error(f"Error getting config from Consul: {e}")
        return None

@app.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.json
        
        # Получаем конфигурацию из Consul
        max_amount = get_config('order/max_amount') or "1000"
        tax_rate = get_config('order/tax_rate') or "0.1"
        
        if data['amount'] > float(max_amount):
            return jsonify({'error': f'Amount exceeds limit of {max_amount}'}), 400
        
        total = data['amount'] * (1 + float(tax_rate))
        
        # Отправляем уведомление
        try:
            notification_service = "http://notification-service:5001"
            requests.post(f"{notification_service}/notify", json={
                'message': f'New order created: ${total:.2f}',
                'order_id': data.get('id')
            }, timeout=2)
        except requests.exceptions.RequestException as e:
            logging.warning(f"Notification service unavailable: {e}")
        
        return jsonify({
            'order_id': data.get('id'),
            'amount': data['amount'],
            'tax_rate': float(tax_rate),
            'total_amount': total,
            'status': 'created'
        })
    except Exception as e:
        logging.error(f"Error creating order: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'order-service'})

@app.route('/')
def hello():
    return jsonify({'message': 'Order Service is running!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)