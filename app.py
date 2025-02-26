from flask import Flask, render_template, jsonify

from transfer import transfer_data, submitProfile

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/readPTV', methods=['POST'])
def transferPTVData():
    success, message, code = transfer_data()
    if success:
        return jsonify({'status': 'success', 'message': message}), code
    else:
        return jsonify({'status': 'error', 'message': message}), code
    
@app.route('/submitProfile', methods=['POST'])
def transferProfile():
    status, message, code = submitProfile()
    if status:
        return jsonify({'status': 'success', 'message': message}), code
    else:
        return jsonify({'status': 'error', 'message': message}), code

if __name__ == "__main__":
    app.run(debug=True)