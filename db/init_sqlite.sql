CREATE TABLE IF NOT EXISTS telemetry_powr2 (
  id INTEGER PRIMARY KEY,
  topic TEXT NOT NULL,
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
