-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 25, 2023 at 08:43 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_hrms_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `hr_contract_contract`
--

CREATE TABLE `hr_contract_contractmodel` (
  `id` int(11) NOT NULL,
  `contract_name` varchar(50) NOT NULL,
  `contract_id` varchar(30) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `contract_type` varchar(30) NOT NULL,
  `rank` int(11) NOT NULL,
  `terminated_date` date DEFAULT NULL,
  `terminated_reason` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `note` longtext NOT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `basic_salary` decimal(10,2) NOT NULL,
  `salary` decimal(10,2) NOT NULL,
  `allowed_annual_leave` int(11) NOT NULL,
  `contractor_name` varchar(100) NOT NULL,
  `sub_contractor_name` varchar(100) NOT NULL,
  `value` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hr_contract_contractmodel`
--

INSERT INTO `hr_contract_contractmodel` (`id`, `contract_name`, `contract_id`, `start_date`, `end_date`, `contract_type`, `rank`, `terminated_date`, `terminated_reason`, `status`, `created_date`, `updated_date`, `note`, `attachment`, `basic_salary`, `salary`, `allowed_annual_leave`, `contractor_name`, `sub_contractor_name`, `value`) VALUES
(2, 'Yae Htet Aung\'s Job Contract', '23Aug01', '2023-08-11', '2024-08-11', 'Employee', 1, NULL, '', 'Confirm', '2023-08-11 08:42:07.347253', '2023-08-11 08:42:07.347253', 'A', 'contract/b.jpg', 2000.00, 2000.00, 12, '', '', 3000.00),
(3, 'Twe Tar Ltd.', '23Aug02', '2022-08-11', '2023-08-11', 'Contractor', 4, '2023-08-11', 'Finished.', 'Confirm', '2023-08-11 09:45:41.061445', '2023-08-11 09:45:41.061445', 'T', 'contract/travelerVibeLogo.png', 2000.00, 2000.00, 12, 'Twe Tar Oo', '', 3000.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hr_contract_contractmodel`
--
ALTER TABLE `hr_contract_contractmodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `contract_id` (`contract_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hr_contract_contractmodel`
--
ALTER TABLE `hr_contract_contractmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
