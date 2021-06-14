-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2021 at 02:21 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `simpro_dashboard`
--

-- --------------------------------------------------------

--
-- Table structure for table `dashboard`
--

CREATE TABLE `dashboard` (
  `id_dashboard` int(11) NOT NULL,
  `id_data` int(11) NOT NULL,
  `id_templates` int(11) NOT NULL,
  `data_join` text NOT NULL,
  `icon` varchar(40) NOT NULL,
  `view_group` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dashboard`
--

INSERT INTO `dashboard` (`id_dashboard`, `id_data`, `id_templates`, `data_join`, `icon`, `view_group`) VALUES
(1, 1, 1, '{\r\n\"#INFO_BOX_VALUE\":\"$.data.total_user\",\r\n\"#INFO_BOX_TITLE\":\"total_user\",\r\n\"#INFO_BOX_ICON\":\"fas fa-icon\"\r\n}', '-', 'dashboard');

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id_data` int(11) NOT NULL,
  `url` varchar(255) NOT NULL,
  `result_key` text NOT NULL,
  `method` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id_data`, `url`, `result_key`, `method`) VALUES
(1, 'http://127.0.0.1:9701/data', '{\r\n\"total_user\":\"data.total_user\"\r\n}', 'GET');

-- --------------------------------------------------------

--
-- Table structure for table `templates`
--

CREATE TABLE `templates` (
  `id_templates` int(11) NOT NULL,
  `type` varchar(100) NOT NULL,
  `requirements` text NOT NULL,
  `html` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `templates`
--

INSERT INTO `templates` (`id_templates`, `type`, `requirements`, `html`) VALUES
(1, 'info_box', '[\'#INFO_BOX_ICON\',\'INFO_BOX_TITLE\',\'INFO_BOX_VALUE\']', '<div class=\"info-box\">\r\n                <span class=\"info-box-icon bg-info elevation-1\"><i class=\"#INFO_BOX_ICON\"></i></span>\r\n  \r\n                <div class=\"info-box-content\">\r\n                  <span class=\"info-box-text\">#INFO_BOX_TITLE</span>\r\n                  <span class=\"info-box-number\">\r\n                    #INFO_BOX_VALUE\r\n                  </span>\r\n                </div>\r\n                <!-- /.info-box-content -->\r\n              </div>');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dashboard`
--
ALTER TABLE `dashboard`
  ADD PRIMARY KEY (`id_dashboard`);

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id_data`);

--
-- Indexes for table `templates`
--
ALTER TABLE `templates`
  ADD PRIMARY KEY (`id_templates`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dashboard`
--
ALTER TABLE `dashboard`
  MODIFY `id_dashboard` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id_data` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `templates`
--
ALTER TABLE `templates`
  MODIFY `id_templates` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
