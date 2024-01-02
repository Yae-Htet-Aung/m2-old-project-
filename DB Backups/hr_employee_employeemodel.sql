-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 25, 2023 at 08:41 PM
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
-- Table structure for table `hr_employee_employeemodel`
--

CREATE TABLE `hr_employee_employeemodel` (
  `id` int(11) NOT NULL,
  `employee_id` varchar(10) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `employment_status` tinyint(1) NOT NULL,
  `bank_account` varchar(20) NOT NULL,
  `bank_name` varchar(50) NOT NULL,
  `joining_date` date NOT NULL,
  `emergency_contact` varchar(15) NOT NULL,
  `identity_number` varchar(30) NOT NULL,
  `address` varchar(200) NOT NULL,
  `marital_status` varchar(10) NOT NULL,
  `date_of_birth` date NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `citizen` varchar(50) NOT NULL,
  `picture` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hr_employee_employeemodel`
--

INSERT INTO `hr_employee_employeemodel` (`id`, `employee_id`, `first_name`, `last_name`, `email`, `phone_number`, `employment_status`, `bank_account`, `bank_name`, `joining_date`, `identity_number`, `address`, `marital_status`, `date_of_birth`, `age`, `gender`, `citizen`, `picture`) VALUES
(6, '23Jul001', 'Brian', 'Brown', 'brian@gmail.com', '90001', 1, '111122223333001', 'KBZ', '2023-07-30', '12/TGK(C)112201', 'Suniaraja No. 633', 'Single', '2000-07-30', 23, 'Male', 'Myanmar', 'employee/b2.jpg'),
(7, '23Jul002', 'Yae Htet', 'Aung', 'yae@gmail.com', '90002', 1, '111122223333002', 'AYA', '2022-07-30', '12/TGK(C)112202', 'Yangon', 'Single', '1998-07-30', 25, 'Male', 'Myanmar', 'employee/b3.jpg'),
(8, '23Aug003', 'Twal Tar', 'Ngl', 'twe@gmail.com', '90003', 1, '111122223333003', 'AGD', '2022-11-30', '14/MMK(C)112203', 'Maw Kyun', 'Single', '2000-07-12', 23, 'Female', 'Myanmar', 'employee/g.jpg'),
(10, '23Aug004', 'Su Myat', 'Mon', 'sumyat@gmail.com', '090004', 0, '111122223333004', 'A Bank', '2023-07-04', '12/SOK(C)112204', 'South Oakkalapa', 'Single', '1998-07-19', 15, 'Female', 'Myanmar', 'employee/g3.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hr_employee_employeemodel`
--
ALTER TABLE `hr_employee_employeemodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `employee_id` (`employee_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hr_employee_employeemodel`
--
ALTER TABLE `hr_employee_employeemodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
