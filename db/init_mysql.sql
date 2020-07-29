CREATE TABLE IF NOT EXISTS `devices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(150) DEFAULT NULL,
  `type` char(50) DEFAULT NULL,
  `topic` varchar(255) NOT NULL,
  primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `telemetry_powr2` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `device_id` int(11) NOT NULL,
  `time` datetime NOT NULL,
  `today` double DEFAULT NULL,
  `period` double DEFAULT NULL,
  `power` double DEFAULT NULL,
  `voltage` double DEFAULT NULL,
  `current` double DEFAULT NULL,
  `factor` double DEFAULT NULL,
  `apparent_power` double DEFAULT NULL,
  `reactive_power` double DEFAULT NULL,
  `yesterday` double DEFAULT NULL,
  `total` double DEFAULT NULL,
  `total_start_time` datetime DEFAULT NULL,
  primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

TRUNCATE TABLE devices;
INSERT INTO devices (id, name, type, topic) VALUES (1, "test_powr2", "POWR_2", "tele/tasmota_6879C1/SENSOR");