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
  	inserted_by text NULL,
	inserted_at timestamp NULL,
    PRIMARY KEY (icao24, last_contact)
);

CREATE OR REPLACE FUNCTION set_modified_on_insert()
RETURNS TRIGGER AS $$
BEGIN
    NEW.inserted_by = CURRENT_USER;
    NEW.inserted_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER flights_insert_trigger
BEFORE INSERT ON flights
FOR EACH ROW
EXECUTE FUNCTION set_modified_on_insert();


CREATE USER flights_wrapper WITH PASSWORD 'flights_wrapper';

ALTER USER flights_wrapper WITH SUPERUSER;
