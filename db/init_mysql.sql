-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 192.168.1.195:3306
-- Generation Time: Jul 29, 2020 at 03:32 PM
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
-- Table structure for table `devices`
--

CREATE TABLE `devices` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` char(150) DEFAULT NULL,
  `type` char(50) DEFAULT NULL,
  `topic` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `telemetry_powr2`
--

CREATE TABLE IF NOT EXISTS `telemetry_powr2` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
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
  `total_start_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
