from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def download_file():
    path = './soluzione.py'  # percorso al file che vuoi inviare
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
