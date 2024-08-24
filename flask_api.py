from flask import Flask, request

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        # קבלת כל הפרמטרים ב-GET
        params = request.args.to_dict()
        print("Received GET request with the following parameters:")
        for key, value in params.items():
            print(f"{key} = {value}")
        return f"GET request received with parameters: {params}\n"

    if request.method == 'POST':
        # קבלת כל הפרמטרים ב-POST
        params = request.form.to_dict()
        print("Received POST request with the following parameters:")
        for key, value in params.items():
            print(f"{key} = {value}")
        return f"POST request received with parameters: {params}\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
