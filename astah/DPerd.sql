-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Generation Time: Dec 15, 2023 at 07:44 PM
-- Server version: 11.1.2-MariaDB-1:11.1.2+maria~ubu2204
-- PHP Version: 8.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `DP`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `account_id` int(11) NOT NULL,
  `subscription_id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `payment_method` varchar(255) DEFAULT NULL,
  `blocked` bit(10) DEFAULT NULL,
  `video_quality` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `apikey`
--

CREATE TABLE `apikey` (
  `apikey` varchar(30) NOT NULL,
  `role` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `classification`
--

CREATE TABLE `classification` (
  `classification_id` int(11) NOT NULL,
  `classification` varchar(255) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `episode_id` int(11) DEFAULT NULL,
  `serie_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `episode`
--

CREATE TABLE `episode` (
  `episode_id` int(11) NOT NULL,
  `serie_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `episode_duration` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `genres`
--

CREATE TABLE `genres` (
  `genres_id` int(11) NOT NULL,
  `genre` varchar(255) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `serie_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE `movie` (
  `movie_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `movie_duration` int(11) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `preference`
--

CREATE TABLE `preference` (
  `preference_id` int(11) NOT NULL,
  `interest` varchar(255) DEFAULT NULL,
  `watchlist_item_id` int(11) NOT NULL,
  `genres_id` int(11) DEFAULT NULL,
  `viewing_behavior_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `profile_id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `subscription_id` int(11) NOT NULL,
  `profile_image` varchar(255) DEFAULT NULL,
  `profile_child` bit(10) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `preference_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `serie`
--

CREATE TABLE `serie` (
  `serie_id` int(11) NOT NULL,
  `serie_name` varchar(255) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subscription`
--

CREATE TABLE `subscription` (
  `subscription_id` int(11) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `subscription_price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subtitle`
--

CREATE TABLE `subtitle` (
  `subtitle_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `episode_id` int(11) NOT NULL,
  `serie_id` int(11) NOT NULL,
  `language` varchar(100) DEFAULT NULL,
  `subtitle_location` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `viewing_behavior`
--

CREATE TABLE `viewing_behavior` (
  `viewing_behavior_id` int(11) NOT NULL,
  `watchlist_item_id` int(11) NOT NULL,
  `pause_time` int(11) DEFAULT NULL,
  `viewing_history` varchar(255) DEFAULT NULL,
  `times_watched` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `watchlist_item`
--

CREATE TABLE `watchlist_item` (
  `watchlist_item_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `serie_id` int(11) NOT NULL,
  `profile_id` int(11) DEFAULT NULL,
  `account_id` int(11) DEFAULT NULL,
  `subscription_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`account_id`,`subscription_id`);

--
-- Indexes for table `apikey`
--
ALTER TABLE `apikey`
  ADD PRIMARY KEY (`apikey`);

--
-- Indexes for table `classification`
--
ALTER TABLE `classification`
  ADD PRIMARY KEY (`classification_id`);

--
-- Indexes for table `episode`
--
ALTER TABLE `episode`
  ADD PRIMARY KEY (`episode_id`,`serie_id`);

--
-- Indexes for table `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`genres_id`);

--
-- Indexes for table `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`movie_id`);

--
-- Indexes for table `preference`
--
ALTER TABLE `preference`
  ADD PRIMARY KEY (`preference_id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`profile_id`,`account_id`,`subscription_id`);

--
-- Indexes for table `serie`
--
ALTER TABLE `serie`
  ADD PRIMARY KEY (`serie_id`);

--
-- Indexes for table `subscription`
--
ALTER TABLE `subscription`
  ADD PRIMARY KEY (`subscription_id`);

--
-- Indexes for table `subtitle`
--
ALTER TABLE `subtitle`
  ADD PRIMARY KEY (`subtitle_id`,`movie_id`,`episode_id`,`serie_id`);

--
-- Indexes for table `viewing_behavior`
--
ALTER TABLE `viewing_behavior`
  ADD PRIMARY KEY (`viewing_behavior_id`,`watchlist_item_id`);

--
-- Indexes for table `watchlist_item`
--
ALTER TABLE `watchlist_item`
  ADD PRIMARY KEY (`watchlist_item_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `account_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `classification`
--
ALTER TABLE `classification`
  MODIFY `classification_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `episode`
--
ALTER TABLE `episode`
  MODIFY `episode_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `genres`
--
ALTER TABLE `genres`
  MODIFY `genres_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `movie`
--
ALTER TABLE `movie`
  MODIFY `movie_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `preference`
--
ALTER TABLE `preference`
  MODIFY `preference_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `profile_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `serie`
--
ALTER TABLE `serie`
  MODIFY `serie_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subscription`
--
ALTER TABLE `subscription`
  MODIFY `subscription_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subtitle`
--
ALTER TABLE `subtitle`
  MODIFY `subtitle_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `viewing_behavior`
--
ALTER TABLE `viewing_behavior`
  MODIFY `viewing_behavior_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `watchlist_item`
--
ALTER TABLE `watchlist_item`
  MODIFY `watchlist_item_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
