from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))

    suma = x + y
    predykcja = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": predykcja,
        "features": {"x": x, "y": y}
    })

if __name__ == '__main__':
    app.run()
