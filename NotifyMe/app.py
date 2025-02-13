from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

# Connect to accdb files
def connect_to_db(path):
    return pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
        f'DBQ={path}')

@app.route('/process_DB', methods=['POST'])
def process_data():
    try:
        srcDB = 'NotifyMe/db/SAMPLEPTV.accdb'
        tgtDB = 'NotifyMe/db/SAMPLEProfile.accdb'

        srcCon = connect_to_db(srcDB)
        srcCur = srcCon.cursor()

        srcCur.execute("SELECT * FROM Timetable")

        data = srcCur.fetchall()

        srcCon.close()

        tgtCon = connect_to_db(tgtDB)
        tgtCur = tgtCon.cursor()

        for row in data:
            tgtCur.execute("INSERT INTO Timetable VALUES (?, ?, ?)", row)

        tgtCon.commit()
        tgtCon.close()

        return jsonify({'status': 'success', 'message': 'Data successfully copied!'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)