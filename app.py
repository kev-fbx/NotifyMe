from flask import Flask, render_template, jsonify

from transfer import transfer_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transfer', methods=['POST'])
def transfer_route():
    success, message = transfer_data()
    if success:
        return jsonify({'status': 'success', 'message': message}), 200
    else:
        return jsonify({'status': 'error', 'message': message}), 500

if __name__ == "__main__":
    app.run(debug=True)

#test commit