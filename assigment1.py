from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    temperature = data.get('t')
    humidity = data.get('h')
    if temperature is not None and humidity is not None:
        print(f"Temperature: {temperature} °C, Humidity: {humidity} %")
        return jsonify({"message": "Successful"})
    else:
        return jsonify({"message": "Failed"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
