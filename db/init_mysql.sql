CREATE TABLE IF NOT EXISTS `telemetry_powr2` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `topic` varchar(255) NOT NULL,
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
