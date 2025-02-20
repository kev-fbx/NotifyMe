import os
from db_utils import connect_to_db


def transfer_data():
    """Reads and writes data from one database to another.

    Returns:
        Tuple[bool, str]: Return status and message.
    """
    SRC_Path = os.path.join('NotifyMe', 'db', 'SAMPLEPTV.accdb')
    DST_Path = os.path.join('NotifyMe', 'db', 'SAMPLEProfile.accdb')

    SRC_conn = None
    DST_conn = None

    try:
        # Connect to source database and execute query
        SRC_conn = connect_to_db(SRC_Path)
        SRC_cursor = SRC_conn.cursor()

        SRC_cursor.execute("SELECT station_ID, stationName FROM Station")
        stations = SRC_cursor.fetchall()

        # Connect to destination database and execute query
        DST_conn = connect_to_db(DST_Path)
        DST_cursor = DST_conn.cursor()

        # Insert data into destination database
        for station in stations:
            station_ID, stationName = station

            # Skip over existing stations
            DST_cursor.execute(
                "SELECT station_ID FROM Station WHERE station_ID = ?",
                (station_ID)
            )

            if DST_cursor.fetchone() is not None:
                continue

            # Transfer Station data
            DST_cursor.execute(
                "INSERT INTO Station (station_ID, stationName) VALUES (?, ?)",
                (station_ID, stationName)
            )

            # Transfer DepartureTime data
            SRC_cursor.execute(
                "SELECT departure_ID, station_ID, departureTime, toCity FROM DepartureTime WHERE station_ID = ?",
                (station_ID)
            )
            departures = SRC_cursor.fetchall()

            for departure in departures:
                departure_ID, station_ID, departureTime, toCity = departure
                DST_cursor.execute(
                    "INSERT INTO DepartureTime (departure_ID, station_ID, departureTime, toCity) VALUES (?, ?, ?, ?)",
                    (departure_ID, station_ID, departureTime, toCity)
                )

        # Commit changes
        DST_conn.commit()

        return True, "Data transfer successful."

    except Exception as e:
        if SRC_conn:
            SRC_conn.rollback()

        return False, str(e)
    
    finally:
        if SRC_conn:
            SRC_conn.close()
        if DST_conn:
            DST_conn.close()