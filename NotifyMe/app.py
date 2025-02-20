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

        srcCur.execute("SELECT * FROM Station")

        stationData = srcCur.fetchall()

        if stationData:
            station_ID, stationName = stationData

            srcCur.execute("SELECT * FROM DepartureTime WHERE station_ID = ?", station_ID)
            departureData = srcCur.fetchall()

            tgtCon = connect_to_db(tgtDB)
            tgtCur = tgtCon.cursor()

            tgtCur.execute("INSERT INTO Station (station_ID, stationName) VALUES (?, ?)", station_ID, stationName)
            
            for departure in departureData:
                tgtCur.execute("INSERT INTO DepartureTime (departure_ID, station_ID, departureTime, toCity) VALUES (?, ?, ?, ?)", departure)

            tgtCon.commit()

        return jsonify({'status': 'success', 'message': 'Data successfully copied!'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    
    finally:
        if srcCon:
            srcCon.close()
        if tgtCon:
            tgtCon.close()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)