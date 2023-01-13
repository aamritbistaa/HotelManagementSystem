-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 13, 2023 at 05:06 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelmanagementsystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ref` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `mobile` varchar(45) DEFAULT NULL,
  `nationality` varchar(45) DEFAULT NULL,
  `idproof` varchar(45) DEFAULT NULL,
  `idnumber` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `postal` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ref`, `name`, `gender`, `mobile`, `nationality`, `idproof`, `idnumber`, `email`, `address`, `postal`) VALUES
(27470, 'Amrit', 'Male', '984384986', 'Nepali', 'Citizenship', 'aishfkas', '91724kas@hotmail.com', 'shantinagar', '982392'),
(49362, 'Amrit Bista', 'Male', '9999999999', 'Nepali', 'Citizenship', '91724', 'aamritbistaa@gmail.com', 'sinamangal', '404010'),
(99476, 'Harihar Pandey', 'Male', '98491010300', 'European', 'Passport', '985326', 'harihar@google.com', 'pashupati', '9238');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `floor` varchar(45) DEFAULT NULL,
  `roomNo` varchar(45) NOT NULL,
  `roomType` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`floor`, `roomNo`, `roomType`) VALUES
('1', '102', 'Suit'),
('1', '103', 'Double'),
('1', '105', 'Single'),
('1', '109', 'Single');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `ref` varchar(45) DEFAULT NULL,
  `check_in` varchar(45) DEFAULT NULL,
  `check_out` varchar(45) DEFAULT NULL,
  `roomtype` varchar(45) DEFAULT NULL,
  `roomavailable` varchar(45) NOT NULL,
  `meal` varchar(45) DEFAULT NULL,
  `noofdays` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`ref`, `check_in`, `check_out`, `roomtype`, `roomavailable`, `meal`, `noofdays`) VALUES
('27470', '20/12/2022', '23/12/2023', 'Double', '103', 'breakfast', '368'),
('99476', '15-01-2022', '19-02-2022', 'Single', '105', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`roomNo`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`roomavailable`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
