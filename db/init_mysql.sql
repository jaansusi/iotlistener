-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 192.168.1.195:3306
-- Generation Time: Jul 31, 2020 at 08:48 PM
-- Server version: 10.4.11-MariaDB-1:10.4.11+maria~bionic-log
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `grafana`
--

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `device`
--

CREATE TABLE `device` (
  `id` int(11) NOT NULL,
  `topic` varchar(255) NOT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Stand-in structure for view `power`
-- (See below for the actual view)
--
CREATE TABLE `power` (
`name` varchar(255)
,`time` datetime
,`power` double
,`today` double
);

-- --------------------------------------------------------

--
-- Table structure for table `telemetry_powr2`
--

CREATE TABLE `telemetry_powr2` (
  `id` bigint(20) UNSIGNED NOT NULL,
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
  `total_start_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure for view `power`
--
DROP TABLE IF EXISTS `power`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `power`  AS  select `company`.`name` AS `name`,`telemetry_powr2`.`time` AS `time`,`telemetry_powr2`.`power` AS `power`,`telemetry_powr2`.`today` AS `today` from ((`telemetry_powr2` join `device` on(`telemetry_powr2`.`topic` = `device`.`topic`)) join `company` on(`device`.`company_id` = `company`.`id`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `device`
--
ALTER TABLE `device`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `telemetry_powr2`
--
ALTER TABLE `telemetry_powr2`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `device`
--
ALTER TABLE `device`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `telemetry_powr2`
--
ALTER TABLE `telemetry_powr2`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;