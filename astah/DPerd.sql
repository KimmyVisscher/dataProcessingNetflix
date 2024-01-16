-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Generation Time: Jan 16, 2024 at 01:04 PM
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
-- Database: `DP_Netflix`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `account_id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `addres` varchar(255) DEFAULT NULL,
  `zip_code` int(11) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `payment_method` varchar(255) NOT NULL,
  `blocked` int(11) DEFAULT NULL,
  `subscription_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`account_id`, `email`, `username`, `password`, `addres`, `zip_code`, `city`, `payment_method`, `blocked`, `subscription_id`) VALUES
(1, 'john.doe@example.com', 'john_doe', 'hashed_password', NULL, NULL, NULL, 'credit_card', NULL, 1),
(2, 'jane.smith@example.com', 'jane_smith', 'hashed_password', NULL, NULL, NULL, 'paypal', NULL, 2),
(3, 'alice.jones@example.com', 'alice_jones', 'hashed_password', NULL, NULL, NULL, 'debit_card', NULL, 1),
(4, 'bob.white@example.com', 'bob_white', 'hashed_password', NULL, NULL, NULL, 'credit_card', 1, 3),
(5, 'mary.green@example.com', 'mary_green', 'hashed_password', NULL, NULL, NULL, 'paypal', NULL, 2),
(6, 'sam.brown@example.com', 'sam_brown', 'hashed_password', NULL, NULL, NULL, 'debit_card', NULL, 1),
(7, 'emily.wilson@example.com', 'emily_wilson', 'hashed_password', NULL, NULL, NULL, 'credit_card', NULL, 3),
(8, 'charlie.rogers@example.com', 'charlie_rogers', 'hashed_password', NULL, NULL, NULL, 'paypal', NULL, 1),
(9, 'olivia.hall@example.com', 'olivia_hall', 'hashed_password', NULL, NULL, NULL, 'debit_card', 1, 2),
(10, 'david.lee@example.com', 'david_lee', 'hashed_password', NULL, NULL, NULL, 'credit_card', NULL, 3),
(11, 'sophie.collins@example.com', 'sophie_collins', 'hashed_password', NULL, NULL, NULL, 'paypal', NULL, 2),
(12, 'max.miller@example.com', 'max_miller', 'hashed_password', NULL, NULL, NULL, 'debit_card', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `apikey`
--

CREATE TABLE `apikey` (
  `apikey` varchar(100) NOT NULL,
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
  `episode_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `classification`
--

INSERT INTO `classification` (`classification_id`, `classification`, `movie_id`, `episode_id`) VALUES
(1, 'ACTION', 1, NULL),
(2, 'ACTION', 1, NULL),
(3, 'SCIFI', 1, NULL),
(4, 'DRAMA', 1, NULL),
(5, 'REALITY', 1, NULL),
(6, 'THRILLER', 1, NULL),
(7, 'FANTASY', 1, NULL),
(8, 'ANIMATION', 1, NULL),
(9, 'COMEDY', 1, NULL),
(10, 'FAMILY', 1, NULL),
(11, 'ROMANCE', 1, NULL),
(12, 'HORROR', 1, NULL),
(13, 'ACTION', 2, NULL),
(14, 'FANTASY', 2, NULL),
(15, 'SCIFI', 2, NULL),
(16, 'DRAMA', 2, NULL),
(17, 'REALITY', 2, NULL),
(18, 'THRILLER', 2, NULL),
(19, 'FANTASY', 2, NULL),
(20, 'ANIMATION', 2, NULL),
(21, 'COMEDY', 2, NULL),
(22, 'FAMILY', 2, NULL),
(23, 'ROMANCE', 2, NULL),
(24, 'HORROR', 2, NULL),
(25, 'ACTION', NULL, 1),
(26, 'ADVENTURE', NULL, 1),
(27, 'SCIFI', NULL, 1),
(28, 'DRAMA', NULL, 1),
(29, 'REALITY', NULL, 1),
(30, 'THRILLER', NULL, 1),
(31, 'FANTASY', NULL, 1),
(32, 'ANIMATION', NULL, 1),
(33, 'COMEDY', NULL, 1),
(34, 'FAMILY', NULL, 1),
(35, 'ROMANCE', NULL, 1),
(36, 'HORROR', NULL, 1),
(37, 'ACTION', NULL, 13),
(38, 'ADVENTURE', NULL, 13),
(39, 'SCIFI', NULL, 13),
(40, 'DRAMA', NULL, 13),
(41, 'REALITY', NULL, 13),
(42, 'THRILLER', NULL, 13),
(43, 'FANTASY', NULL, 13),
(44, 'ANIMATION', NULL, 13),
(45, 'COMEDY', NULL, 13),
(46, 'FAMILY', NULL, 13),
(47, 'ROMANCE', NULL, 13),
(48, 'HORROR', NULL, 13);

-- --------------------------------------------------------

--
-- Table structure for table `episode`
--

CREATE TABLE `episode` (
  `episode_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `episode_duration` int(11) DEFAULT NULL,
  `serie_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `episode`
--

INSERT INTO `episode` (`episode_id`, `title`, `episode_duration`, `serie_id`) VALUES
(1, 'The Beginning', 45, 1),
(2, 'Secrets Unveiled', 42, 1),
(3, 'Into the Abyss', 40, 1),
(4, 'Hidden Truths', 38, 1),
(5, 'Fallen Heroes', 41, 1),
(6, 'Deception', 37, 1),
(7, 'Betrayal', 44, 1),
(8, 'Rising Tensions', 39, 1),
(9, 'The Reckoning', 43, 1),
(10, 'Final Stand', 36, 1),
(11, 'Epiphany', 40, 1),
(12, 'Closure', 42, 1),
(13, 'New Horizons', 50, 2),
(14, 'Lost and Found', 48, 2),
(15, 'Dawn of Destiny', 52, 2),
(16, 'Echoes of the Past', 45, 2),
(17, 'Fading Light', 47, 2),
(18, 'Shattered Dreams', 49, 2),
(19, 'Whispers in the Wind', 46, 2),
(20, 'Crimson Skies', 51, 2),
(21, 'Dystopian Realms', 50, 2),
(22, 'The Final Chapter', 53, 2),
(23, 'Fragments of Reality', 48, 2),
(24, 'Redemption', 50, 2),
(25, 'Beginnings', 35, 3),
(26, 'Lost Memories', 32, 3),
(27, 'Echoing Voices', 38, 3),
(28, 'Forgotten Tales', 40, 3),
(29, 'Veil of Shadows', 36, 3),
(30, 'Whispers in the Dark', 37, 3),
(31, 'Fading Echoes', 39, 3),
(32, 'Twisted Fate', 34, 3),
(33, 'Shattered Illusions', 33, 3),
(34, 'Fractured Reality', 36, 3),
(35, 'Spectral Visions', 35, 3),
(36, 'Eternal Twilight', 31, 3);

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

--
-- Dumping data for table `genres`
--

INSERT INTO `genres` (`genres_id`, `genre`, `movie_id`, `serie_id`) VALUES
(1, 'Action', 1, NULL),
(2, 'Adventure', 1, NULL),
(3, 'Sci-Fi', 1, NULL),
(4, 'Drama', 1, NULL),
(5, 'Comedy', 1, NULL),
(6, 'Thriller', 1, NULL),
(7, 'Horror', 1, NULL),
(8, 'Romance', 1, NULL),
(9, 'Fantasy', 1, NULL),
(10, 'Mystery', 1, NULL),
(11, 'Animation', 1, NULL),
(12, 'Documentary', 1, NULL),
(13, 'Action', 2, NULL),
(14, 'Adventure', 2, NULL),
(15, 'Sci-Fi', 2, NULL),
(16, 'Drama', 2, NULL),
(17, 'Comedy', 2, NULL),
(18, 'Thriller', 2, NULL),
(19, 'Horror', 2, NULL),
(20, 'Romance', 2, NULL),
(21, 'Fantasy', 2, NULL),
(22, 'Mystery', 2, NULL),
(23, 'Animation', 2, NULL),
(24, 'Documentary', 2, NULL),
(25, 'Action', NULL, 1),
(26, 'Adventure', NULL, 1),
(27, 'Sci-Fi', NULL, 1),
(28, 'Drama', NULL, 1),
(29, 'Comedy', NULL, 1),
(30, 'Thriller', NULL, 1),
(31, 'Horror', NULL, 1),
(32, 'Romance', NULL, 1),
(33, 'Fantasy', NULL, 1),
(34, 'Mystery', NULL, 1),
(35, 'Animation', NULL, 1),
(36, 'Documentary', NULL, 1),
(37, 'Action', NULL, 2),
(38, 'Adventure', NULL, 2),
(39, 'Sci-Fi', NULL, 2),
(40, 'Drama', NULL, 2),
(41, 'Comedy', NULL, 2),
(42, 'Thriller', NULL, 2),
(43, 'Horror', NULL, 2),
(44, 'Romance', NULL, 2),
(45, 'Fantasy', NULL, 2),
(46, 'Mystery', NULL, 2),
(47, 'Animation', NULL, 2),
(48, 'Documentary', NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `genresPreference`
--

CREATE TABLE `genresPreference` (
  `genres_id` int(11) NOT NULL,
  `preference_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `interestPreference`
--

CREATE TABLE `interestPreference` (
  `preference_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL
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

--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`movie_id`, `title`, `movie_duration`, `age_restriction`) VALUES
(1, 'The Shawshank Redemption', 142, 'SIXTEEN_YEARS'),
(2, 'The Godfather', 175, 'ALL_AGES'),
(3, 'Pulp Fiction', 154, 'ALL_AGES'),
(4, 'The Dark Knight', 152, 'SIXTEEN_YEARS'),
(5, 'Schindler\'s List', 195, 'SIXTEEN_YEARS'),
(6, 'Inception', 148, 'SIXTEEN_YEARS'),
(7, 'Fight Club', 139, 'SIXTEEN_YEARS'),
(8, 'Forrest Gump', 142, 'ALL_AGES'),
(9, 'The Matrix', 136, 'SIX_YEARS'),
(10, 'The Silence of the Lambs', 118, 'TWELVE_YEARS'),
(11, 'The Green Mile', 189, 'SIXTEEN_YEARS'),
(12, 'The Godfather: Part II', 202, 'TWELVE_YEARS');

-- --------------------------------------------------------

--
-- Table structure for table `preference`
--

CREATE TABLE `preference` (
  `preference_id` int(11) NOT NULL,
  `interest` varchar(255) DEFAULT NULL,
  `watchlist_id` int(11) NOT NULL,
  `viewing_behavior_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `profile_id` int(11) NOT NULL,
  `profile_image` varchar(255) DEFAULT NULL,
  `profile_child` int(11) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `account_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`profile_id`, `profile_image`, `profile_child`, `language`, `account_id`) VALUES
(1, NULL, NULL, 'DUTCH', 1),
(2, NULL, NULL, 'DUTCH', 1),
(3, NULL, NULL, 'DUTCH', 2),
(4, NULL, NULL, 'ENGLISH', 2),
(5, NULL, NULL, 'ENGLISH', 3),
(6, NULL, NULL, 'DUTCH', 2),
(7, NULL, 1, 'DUTCH', 4),
(8, NULL, NULL, 'DUTCH', 5),
(9, NULL, 1, 'DUTCH', 6),
(10, NULL, NULL, 'DUTCH', 8),
(11, NULL, NULL, 'DUTCH', 8),
(12, NULL, 1, 'ENGLISH', 7),
(13, NULL, NULL, 'DUTCH', 8),
(14, NULL, NULL, 'DUTCH', 9),
(15, NULL, NULL, 'DUTCH', 10),
(16, NULL, NULL, 'ENGLISH', 12),
(17, NULL, NULL, 'ENGLISH', 11),
(18, NULL, NULL, 'DUTCH', 12),
(19, NULL, 1, 'DUTCH', 7),
(20, NULL, NULL, 'DUTCH', 5),
(21, NULL, 1, 'DUTCH', 6),
(22, NULL, NULL, 'DUTCH', 5),
(23, NULL, NULL, 'DUTCH', 10),
(24, NULL, 1, 'ENGLISH', 4);

-- --------------------------------------------------------

--
-- Table structure for table `serie`
--

CREATE TABLE `serie` (
  `serie_id` int(11) NOT NULL,
  `serie_name` varchar(255) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `serie`
--

INSERT INTO `serie` (`serie_id`, `serie_name`, `age_restriction`) VALUES
(1, 'Stranger Things', 'SIXTEEN_YEARS'),
(2, 'The Crown', 'SIXTEEN_YEARS'),
(3, 'Breaking Bad', 'SIXTEEN_YEARS'),
(4, 'Friends', 'ALL_AGES'),
(5, 'Black Mirror', 'SIXTEEN_YEARS'),
(6, 'The Mandalorian', 'TWELVE_YEARS'),
(7, 'Money Heist', 'SIXTEEN_YEARS'),
(8, 'Narcos', 'SIXTEEN_YEARS'),
(9, 'The Witcher', 'SIXTEEN_YEARS'),
(10, 'Peaky Blinders', 'ALL_AGES'),
(11, 'The Office', 'ALL_AGES'),
(12, 'Game of Thrones', 'SIXTEEN_YEARS');

-- --------------------------------------------------------

--
-- Table structure for table `subscription`
--

CREATE TABLE `subscription` (
  `subscription_id` int(11) NOT NULL,
  `subscription_price` float(10,2) NOT NULL,
  `video_quality` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subscription`
--

INSERT INTO `subscription` (`subscription_id`, `subscription_price`, `video_quality`) VALUES
(1, 7.99, 'SD'),
(2, 10.99, 'HD'),
(3, 13.99, 'UHD');

-- --------------------------------------------------------

--
-- Table structure for table `subtitle`
--

CREATE TABLE `subtitle` (
  `subtitle_id` int(11) NOT NULL,
  `language` varchar(100) DEFAULT NULL,
  `subtitle_location` varchar(100) NOT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `episode_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subtitle`
--

INSERT INTO `subtitle` (`subtitle_id`, `language`, `subtitle_location`, `movie_id`, `episode_id`) VALUES
(1, 'English', '/path/to/subtitles/movie1_eng.srt', 1, NULL),
(2, 'Dutch', '/path/to/subtitles/movie1_nl.srt', 1, NULL),
(3, 'French', '/path/to/subtitles/movie1_fr.srt', 1, NULL),
(4, 'Spanish', '/path/to/subtitles/movie1_es.srt', 1, NULL),
(5, 'German', '/path/to/subtitles/movie1_de.srt', 1, NULL),
(6, 'Italian', '/path/to/subtitles/movie1_it.srt', 1, NULL),
(7, 'Japanese', '/path/to/subtitles/movie1_jp.srt', 1, NULL),
(8, 'Chinese', '/path/to/subtitles/movie1_cn.srt', 1, NULL),
(9, 'Russian', '/path/to/subtitles/movie1_ru.srt', 1, NULL),
(10, 'Portuguese', '/path/to/subtitles/movie1_pt.srt', 1, NULL),
(11, 'Arabic', '/path/to/subtitles/movie1_ar.srt', 1, NULL),
(12, 'Korean', '/path/to/subtitles/movie1_kr.srt', 1, NULL),
(13, 'English', '/path/to/subtitles/movie2_eng.srt', 2, NULL),
(14, 'Dutch', '/path/to/subtitles/movie2_nl.srt', 2, NULL),
(15, 'French', '/path/to/subtitles/movie2_fr.srt', 2, NULL),
(16, 'Spanish', '/path/to/subtitles/movie2_es.srt', 2, NULL),
(17, 'German', '/path/to/subtitles/movie2_de.srt', 2, NULL),
(18, 'Italian', '/path/to/subtitles/movie2_it.srt', 2, NULL),
(19, 'Japanese', '/path/to/subtitles/movie2_jp.srt', 2, NULL),
(20, 'Chinese', '/path/to/subtitles/movie2_cn.srt', 2, NULL),
(21, 'Russian', '/path/to/subtitles/movie2_ru.srt', 2, NULL),
(22, 'Portuguese', '/path/to/subtitles/movie2_pt.srt', 2, NULL),
(23, 'Arabic', '/path/to/subtitles/movie2_ar.srt', 2, NULL),
(24, 'Korean', '/path/to/subtitles/movie2_kr.srt', 2, NULL),
(25, 'English', '/path/to/subtitles/episode1_eng.srt', NULL, 1),
(26, 'Dutch', '/path/to/subtitles/episode1_nl.srt', NULL, 1),
(27, 'French', '/path/to/subtitles/episode1_fr.srt', NULL, 1),
(28, 'Spanish', '/path/to/subtitles/episode1_es.srt', NULL, 1),
(29, 'German', '/path/to/subtitles/episode1_de.srt', NULL, 1),
(30, 'Italian', '/path/to/subtitles/episode1_it.srt', NULL, 1),
(31, 'Japanese', '/path/to/subtitles/episode1_jp.srt', NULL, 1),
(32, 'Chinese', '/path/to/subtitles/episode1_cn.srt', NULL, 1),
(33, 'Russian', '/path/to/subtitles/episode1_ru.srt', NULL, 1),
(34, 'Portuguese', '/path/to/subtitles/episode1_pt.srt', NULL, 1),
(35, 'Arabic', '/path/to/subtitles/episode1_ar.srt', NULL, 1),
(36, 'Korean', '/path/to/subtitles/episode1_kr.srt', NULL, 1),
(37, 'English', '/path/to/subtitles/episode13_eng.srt', NULL, 13),
(38, 'Dutch', '/path/to/subtitles/episode13_nl.srt', NULL, 13),
(39, 'French', '/path/to/subtitles/episode13_fr.srt', NULL, 13),
(40, 'Spanish', '/path/to/subtitles/episode13_es.srt', NULL, 13),
(41, 'German', '/path/to/subtitles/episode13_de.srt', NULL, 13),
(42, 'Italian', '/path/to/subtitles/episode13_it.srt', NULL, 13),
(43, 'Japanese', '/path/to/subtitles/episode13_jp.srt', NULL, 13),
(44, 'Chinese', '/path/to/subtitles/episode13_cn.srt', NULL, 13),
(45, 'Russian', '/path/to/subtitles/episode13_ru.srt', NULL, 13),
(46, 'Portuguese', '/path/to/subtitles/episode13_pt.srt', NULL, 13),
(47, 'Arabic', '/path/to/subtitles/episode13_ar.srt', NULL, 13),
(48, 'Korean', '/path/to/subtitles/episode13_kr.srt', NULL, 13);

-- --------------------------------------------------------

--
-- Table structure for table `viewing_behavior`
--

CREATE TABLE `viewing_behavior` (
  `viewing_behavior_id` int(11) NOT NULL,
  `watchlist_id` int(11) NOT NULL,
  `pause_time` int(11) DEFAULT NULL,
  `viewing_history` varchar(255) DEFAULT NULL,
  `times_watched` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `watchlist`
--

CREATE TABLE `watchlist` (
  `watchlist_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `serie_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`account_id`),
  ADD KEY `FK_account_0` (`subscription_id`);

--
-- Indexes for table `apikey`
--
ALTER TABLE `apikey`
  ADD PRIMARY KEY (`apikey`);

--
-- Indexes for table `classification`
--
ALTER TABLE `classification`
  ADD PRIMARY KEY (`classification_id`),
  ADD KEY `FK_classification_0` (`movie_id`),
  ADD KEY `FK_classification_1` (`episode_id`);

--
-- Indexes for table `episode`
--
ALTER TABLE `episode`
  ADD PRIMARY KEY (`episode_id`),
  ADD KEY `FK_episode_0` (`serie_id`);

--
-- Indexes for table `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`genres_id`),
  ADD KEY `FK_genres_0` (`movie_id`),
  ADD KEY `FK_genres_1` (`serie_id`);

--
-- Indexes for table `genresPreference`
--
ALTER TABLE `genresPreference`
  ADD PRIMARY KEY (`genres_id`,`preference_id`),
  ADD KEY `FK_genresPreference_1` (`preference_id`);

--
-- Indexes for table `interestPreference`
--
ALTER TABLE `interestPreference`
  ADD PRIMARY KEY (`preference_id`,`profile_id`),
  ADD KEY `FK_interestPreference_1` (`profile_id`);

--
-- Indexes for table `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`movie_id`);

--
-- Indexes for table `preference`
--
ALTER TABLE `preference`
  ADD PRIMARY KEY (`preference_id`),
  ADD KEY `FK_preference_0` (`watchlist_id`,`viewing_behavior_id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`profile_id`),
  ADD KEY `FK_profile_0` (`account_id`);

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
  ADD PRIMARY KEY (`subtitle_id`),
  ADD KEY `FK_subtitle_0` (`movie_id`),
  ADD KEY `FK_subtitle_1` (`episode_id`);

--
-- Indexes for table `viewing_behavior`
--
ALTER TABLE `viewing_behavior`
  ADD PRIMARY KEY (`viewing_behavior_id`),
  ADD KEY `FK_viewing_behavior_0` (`watchlist_id`);

--
-- Indexes for table `watchlist`
--
ALTER TABLE `watchlist`
  ADD PRIMARY KEY (`watchlist_id`),
  ADD KEY `FK_watchlist_0` (`movie_id`),
  ADD KEY `FK_watchlist_1` (`serie_id`),
  ADD KEY `FK_watchlist_2` (`profile_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `account_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `classification`
--
ALTER TABLE `classification`
  MODIFY `classification_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `episode`
--
ALTER TABLE `episode`
  MODIFY `episode_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `genres`
--
ALTER TABLE `genres`
  MODIFY `genres_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `movie`
--
ALTER TABLE `movie`
  MODIFY `movie_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `preference`
--
ALTER TABLE `preference`
  MODIFY `preference_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `profile_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `serie`
--
ALTER TABLE `serie`
  MODIFY `serie_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `subscription`
--
ALTER TABLE `subscription`
  MODIFY `subscription_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `subtitle`
--
ALTER TABLE `subtitle`
  MODIFY `subtitle_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `viewing_behavior`
--
ALTER TABLE `viewing_behavior`
  MODIFY `viewing_behavior_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `watchlist`
--
ALTER TABLE `watchlist`
  MODIFY `watchlist_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `FK_account_0` FOREIGN KEY (`subscription_id`) REFERENCES `subscription` (`subscription_id`);

--
-- Constraints for table `classification`
--
ALTER TABLE `classification`
  ADD CONSTRAINT `FK_classification_0` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  ADD CONSTRAINT `FK_classification_1` FOREIGN KEY (`episode_id`) REFERENCES `episode` (`episode_id`);

--
-- Constraints for table `episode`
--
ALTER TABLE `episode`
  ADD CONSTRAINT `FK_episode_0` FOREIGN KEY (`serie_id`) REFERENCES `serie` (`serie_id`);

--
-- Constraints for table `genres`
--
ALTER TABLE `genres`
  ADD CONSTRAINT `FK_genres_0` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  ADD CONSTRAINT `FK_genres_1` FOREIGN KEY (`serie_id`) REFERENCES `serie` (`serie_id`);

--
-- Constraints for table `genresPreference`
--
ALTER TABLE `genresPreference`
  ADD CONSTRAINT `FK_genresPreference_0` FOREIGN KEY (`genres_id`) REFERENCES `genres` (`genres_id`),
  ADD CONSTRAINT `FK_genresPreference_1` FOREIGN KEY (`preference_id`) REFERENCES `preference` (`preference_id`);

--
-- Constraints for table `interestPreference`
--
ALTER TABLE `interestPreference`
  ADD CONSTRAINT `FK_interestPreference_0` FOREIGN KEY (`preference_id`) REFERENCES `preference` (`preference_id`),
  ADD CONSTRAINT `FK_interestPreference_1` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`profile_id`);

--
-- Constraints for table `preference`
--
ALTER TABLE `preference`
  ADD CONSTRAINT `FK_preference_0` FOREIGN KEY (`watchlist_id`,`viewing_behavior_id`) REFERENCES `viewing_behavior` (`watchlist_id`, `viewing_behavior_id`);

--
-- Constraints for table `profile`
--
ALTER TABLE `profile`
  ADD CONSTRAINT `FK_profile_0` FOREIGN KEY (`account_id`) REFERENCES `account` (`account_id`);

--
-- Constraints for table `subtitle`
--
ALTER TABLE `subtitle`
  ADD CONSTRAINT `FK_subtitle_0` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  ADD CONSTRAINT `FK_subtitle_1` FOREIGN KEY (`episode_id`) REFERENCES `episode` (`episode_id`);

--
-- Constraints for table `viewing_behavior`
--
ALTER TABLE `viewing_behavior`
  ADD CONSTRAINT `FK_viewing_behavior_0` FOREIGN KEY (`watchlist_id`) REFERENCES `watchlist` (`watchlist_id`);

--
-- Constraints for table `watchlist`
--
ALTER TABLE `watchlist`
  ADD CONSTRAINT `FK_watchlist_0` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  ADD CONSTRAINT `FK_watchlist_1` FOREIGN KEY (`serie_id`) REFERENCES `serie` (`serie_id`),
  ADD CONSTRAINT `FK_watchlist_2` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`profile_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
