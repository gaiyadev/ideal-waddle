from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello from Python Flask App!",
        "status": "success",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "environment": os.getenv('ENVIRONMENT', 'development'),
        "deployed_with": "HNG DevOps Stage 1 - No Docker"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "Python Flask API",
        "version": "1.0.0"
    })

@app.route('/info')
def info():
    return jsonify({
        "runtime": "Python",
        "framework": "Flask",
        "deployment_method": "Direct server deployment",
        "features": ["Auto-deployment", "Nginx reverse proxy", "Process management"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)