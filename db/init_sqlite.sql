CREATE TABLE IF NOT EXISTS devices (
  id INTEGER,
  name TEXT,
  type TEXT,
  topic TEXT
);

CREATE TABLE IF NOT EXISTS telemetry_powr2 (
  id INTEGER PRIMARY KEY,
  device_id INTEGER NOT NULL,
  time datetime NOT NULL,
  today REAL DEFAULT NULL,
  period REAL DEFAULT NULL,
  power REAL DEFAULT NULL,
  voltage REAL DEFAULT NULL,
  current REAL DEFAULT NULL,
  factor REAL DEFAULT NULL,
  apparent_power REAL DEFAULT NULL,
  reactive_power REAL DEFAULT NULL,
  yesterday REAL DEFAULT NULL,
  total REAL DEFAULT NULL,
  total_start_time TEXT DEFAULT NULL
);

DELETE FROM devices;
INSERT INTO devices (id, name, type, topic) VALUES (1, "test_powr2", "POWR_2", "tele/tasmota_6879C1/SENSOR");