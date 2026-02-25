-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 25, 2026 at 12:42 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `truhamsokogarden`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_detail`
--

CREATE TABLE `product_detail` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` text DEFAULT NULL,
  `product_cost` int(11) DEFAULT NULL,
  `product_photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_detail`
--

INSERT INTO `product_detail` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'Dalmere Yoghurt', 'strawberry flavour', 150, '<FileStorage: \'salad.jpg\' (\'image/jpeg\')>'),
(3, 'Dalmere Yoghurt', 'strawberry flavour', 150, 'salad.jpg'),
(4, 'probiotic yorghurt', 'Vanilla flavour', 200, 'banana.jpg'),
(5, 'Mara yorghurt', 'lemon flavour', 130, 'beef.jpg'),
(6, 'Brookside yorghurt', 'strawberry flavour', 120, 'sea.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `phone`) VALUES
(1, 'Lil Shuri', '876752', 'lilshuri@gmail.com', '0789654734'),
(2, 'Baraka Musa', '76542pt', 'barakamusa@gmail.com', '0709283451'),
(3, 'Samuel Shon', '45py67', 'samuelshon@gmail.com', '0722543609'),
(4, 'Joshua Chapakazi', 'jo89wr', 'joshuachapakazi@gmail.com', '0109986354'),
(5, 'Peter Pombe', 'rt56678', 'peterpombe@gmail.com', '0132546668'),
(6, 'Kariuki Kevin', '098uhgh', 'kariukikevin@gmail.com', '0788445653'),
(7, 'Zawadi Wamboi', 'yyht76r', 'zawadiwamboi@gmail.com', '0127387676'),
(8, 'Mary', '1234', 'mary@gmail.com', '0712398470'),
(9, 'Ian', '9y7u', 'ian@gmail.com', '0790384646'),
(11, 'Mercy', '093f', 'mercy@gmail.com', '0702637487'),
(12, 'Richie', 'fa73', 'richie@gmail.com', '0188363509'),
(13, 'Oprah', '9yh3', 'oprah@gmail.com', '0196323450'),
(14, 'Wilfred', 't5756', 'wilfred@gmail.com', '0709563412'),
(15, 'Sumih', '76tghs', 'sumih@gmail.com', '0790875431'),
(16, 'Trevor', '09po', 'trevor@gmail.com', '0798764563'),
(17, 'Gabi', '98uh', 'gabi@gmail.com', '0798765423'),
(18, 'Kevin', '87yt4', 'kevin@gmail.com', '0787673404'),
(19, 'Jackson', '98ht6', 'jackson@gmail.com', '0764854256');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_detail`
--
ALTER TABLE `product_detail`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_detail`
--
ALTER TABLE `product_detail`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
