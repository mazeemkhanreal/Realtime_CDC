import requests
import psycopg2
from datetime import datetime
import time

USERNAME = os.getenv("OPENSKY_USERNAME")
PASSWORD = os.getenv("OPENSKY_PASSWORD")

def fetch_flight_data():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url, auth=(USERNAME, PASSWORD))

    if response.status_code == 200:
        data = response.json()
        return data['states']
    else:
        print("Error fetching flight data:", response.status_code)
        return []

def create_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            icao24 VARCHAR(50),
            callsign VARCHAR(50),
            origin_country VARCHAR(100),
            time_position TIMESTAMP,
            last_contact TIMESTAMP,
            longitude FLOAT,
            latitude FLOAT,
            baro_altitude FLOAT,
            on_ground BOOLEAN,
            velocity FLOAT,
            heading FLOAT,
            vertical_rate FLOAT,
            PRIMARY KEY (icao24, last_contact)
        )
    """)
    conn.commit()
    cur.close()

def insert_flight(conn, state):
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO flights (
                icao24, callsign, origin_country,
                time_position, last_contact, longitude, latitude,
                baro_altitude, on_ground, velocity, heading, vertical_rate
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        """, (
            state[0],                       # icao24
            state[1].strip() if state[1] else None,  # callsign
            state[2],                       # origin_country
            datetime.utcfromtimestamp(state[3]) if state[3] else None,
            datetime.utcfromtimestamp(state[4]) if state[4] else None,
            state[5], state[6], state[7],  # lon, lat, altitude
            state[8],                      # on_ground
            state[9],                      # velocity
            state[10],                     # heading
            state[11]                      # vertical_rate
        ))
        conn.commit()
    except Exception as e:
        print("Insert failed:", e)
    finally:
        cur.close()

if __name__ == "__main__":
    conn = psycopg2.connect(
        host='localhost',
        database='flights',
        user='flights_wrapper',
        password='flights_wrapper',
        port=5432
    )

   # create_table(conn)

    while True:
        print("Fetching real-time flight data...")
        states = fetch_flight_data()
        if states:
            for state in states:  # limit to 50 records per run
                insert_flight(conn, state)
        else:
            print("No data received.")

        print('Sleeping')
        time.sleep(120)  # Fetch data every 30 seconds (adjust as needed)
