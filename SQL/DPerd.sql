-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Generation Time: Jan 21, 2024 at 07:19 PM
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
-- Database: `DP5`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`%` PROCEDURE `CalculateMonthlyRevenue` ()   BEGIN
    SELECT
        s.subscription_id,
        COUNT(a.account_id) AS number_of_accounts,
        SUM(s.subscription_price) AS monthly_revenue
    FROM
        subscription s
    JOIN
        account a ON s.subscription_id = a.subscription_id
    WHERE
        a.blocked IS NULL OR a.blocked = 0
    GROUP BY
        s.subscription_id;
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `calculateTotalAccounts` ()   BEGIN
    DECLARE totalAccounts INT;

    SELECT COUNT(*) INTO totalAccounts
    FROM account;

    SELECT totalAccounts AS TotalAccounts;
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `calculateTotalAccountsWithParam` (IN `video_quality` VARCHAR(255))   BEGIN
    DECLARE totalAccounts INT;

    SELECT COUNT(DISTINCT a.account_id) INTO totalAccounts
    FROM account a
    INNER JOIN subscription s ON a.subscription_id = s.subscription_id
    WHERE s.video_quality = video_quality;

    SELECT totalAccounts AS TotalAccounts;
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `CalculateTotalMonthlyRevenue` ()   BEGIN
    DECLARE total_revenue DECIMAL(10, 2);

    SELECT
        SUM(s.subscription_price) INTO total_revenue
    FROM
        subscription s
    JOIN
        account a ON s.subscription_id = a.subscription_id
    WHERE
        a.blocked IS NULL OR a.blocked = 0;

    SELECT total_revenue AS total_monthly_revenue;
END$$

CREATE DEFINER=`root`@`%` PROCEDURE `daily_incremental_backup` ()   BEGIN

  DECLARE last_incremental_backup_time TIMESTAMP;

  -- Retrieve the last incremental backup time for all tables
  SELECT MAX(last_incremental_backup_time) INTO last_incremental_backup_time
  FROM backup_log;

  -- Make an incremental backup of the changes since the last backup
  -- Assuming all tables have the column 'modification_timestamp'
  SELECT * INTO OUTFILE 'C:\\Users\\Bram\\Desktop\\incremental_backup.sql'
  FROM `account`, `profile`, `subscription`, `watchlist`
  WHERE modification_timestamp > last_incremental_backup_time;

  -- Update the backup-log with the current time
  UPDATE backup_log
  SET last_incremental_backup_time = CURRENT_TIMESTAMP;

END$$

CREATE DEFINER=`root`@`%` PROCEDURE `monthly_full_backup` ()   BEGIN

  -- Setting an dynamic query to collect all of the tables for an full back-up.
  SET SESSION group_concat_max_len = 1000000;
  SET @tables_query = (
    SELECT GROUP_CONCAT(table_name SEPARATOR ', ')
    FROM information_schema.tables
    WHERE table_schema = 'DP5'
  );

  -- Run the dynamic query.
  SET @current_datetime = DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s');
  SET @full_backup_query = CONCAT('SELECT * INTO OUTFILE ''C:\\Users\\Bram\\Desktop\\full_backup_', @current_datetime, '.sql'' FROM ', @tables_query);
  PREPARE full_backup_stmt FROM @full_backup_query;
  EXECUTE full_backup_stmt;
  DEALLOCATE PREPARE full_backup_stmt;

  -- Update the back-up log
  INSERT INTO backup_log (last_full_backup_timestamp) VALUES (CURRENT_TIMESTAMP);

END$$

DELIMITER ;

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
-- Table structure for table `agepreference`
--

CREATE TABLE `agepreference` (
  `agepreference_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `agerestriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `agepreference`
--

INSERT INTO `agepreference` (`agepreference_id`, `profile_id`, `agerestriction`) VALUES
(1, 1, 'SIX_YEARS'),
(2, 1, 'TWELVE_YEARS'),
(3, 2, 'SIX_YEARS'),
(4, 2, 'SIXTEEN_YEARS');

-- --------------------------------------------------------

--
-- Table structure for table `apikey`
--

CREATE TABLE `apikey` (
  `apikey` varchar(100) NOT NULL,
  `role` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `apikey`
--

INSERT INTO `apikey` (`apikey`, `role`) VALUES
('senior', 'SENIOR'),
('seniorkey', 'SENIOR'),
('unauthorized', 'UNAUTHORIZED'),
('unauthorizedkey', 'UNAUTHORIZED');

-- --------------------------------------------------------

--
-- Table structure for table `backup_log`
--

CREATE TABLE `backup_log` (
  `last_full_backup_timestamp` timestamp NULL DEFAULT NULL,
  `last_incremental_backup_time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `backup_log`
--

INSERT INTO `backup_log` (`last_full_backup_timestamp`, `last_incremental_backup_time`) VALUES
('2024-01-21 17:38:26', NULL),
('2024-01-21 17:41:40', NULL),
('2024-01-21 17:42:14', NULL),
('2024-01-21 18:01:25', NULL);

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
(49, 'ACTION', 1, NULL),
(50, 'ACTION', 1, NULL),
(51, 'SCIFI', 1, NULL),
(52, 'DRAMA', 1, NULL),
(53, 'REALITY', 1, NULL),
(54, 'THRILLER', 1, NULL),
(55, 'FANTASY', 1, NULL),
(56, 'ANIMATION', 1, NULL),
(57, 'COMEDY', 1, NULL),
(58, 'FAMILY', 1, NULL),
(59, 'ROMANCE', 1, NULL),
(60, 'HORROR', 1, NULL),
(61, 'ACTION', 2, NULL),
(62, 'FANTASY', 2, NULL),
(63, 'SCIFI', 2, NULL),
(64, 'DRAMA', 2, NULL),
(65, 'REALITY', 2, NULL),
(66, 'THRILLER', 2, NULL),
(67, 'FANTASY', 2, NULL),
(68, 'ANIMATION', 2, NULL),
(69, 'COMEDY', 2, NULL),
(70, 'FAMILY', 2, NULL),
(71, 'ROMANCE', 2, NULL),
(72, 'HORROR', 2, NULL),
(73, 'ACTION', NULL, 1),
(74, 'ACTION', NULL, 1),
(75, 'ADVENTURE', NULL, 1),
(76, 'SCIFI', NULL, 1),
(77, 'DRAMA', NULL, 1),
(78, 'REALITY', NULL, 1),
(79, 'THRILLER', NULL, 1),
(80, 'FANTASY', NULL, 1),
(81, 'ANIMATION', NULL, 1),
(82, 'COMEDY', NULL, 1),
(83, 'FAMILY', NULL, 1),
(84, 'ROMANCE', NULL, 1),
(85, 'HORROR', NULL, 1),
(86, 'ACTION', NULL, 13),
(87, 'ADVENTURE', NULL, 13),
(88, 'SCIFI', NULL, 13),
(89, 'DRAMA', NULL, 13),
(90, 'REALITY', NULL, 13),
(91, 'THRILLER', NULL, 13),
(92, 'FANTASY', NULL, 13),
(93, 'ANIMATION', NULL, 13),
(94, 'COMEDY', NULL, 13),
(95, 'FAMILY', NULL, 13),
(96, 'ROMANCE', NULL, 13);

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
(1, 'ACTION', 1, NULL),
(2, 'ADVENTURE', 1, NULL),
(3, 'SCIFI', 1, NULL),
(4, 'DRAMA', 1, NULL),
(5, 'COMEDY', 1, NULL),
(6, 'THRILLER', 1, NULL),
(7, 'HORROR', 1, NULL),
(8, 'ROMANCE', 1, NULL),
(9, 'FANTASY', 1, NULL),
(10, 'MYSTERY', 1, NULL),
(11, 'ANIMATION', 1, NULL),
(12, 'DOCUMENTARY', 1, NULL),
(13, 'ACTION', 2, NULL),
(14, 'ADVENTURE', 2, NULL),
(15, 'SCIFI', 2, NULL),
(16, 'DRAMA', 2, NULL),
(17, 'COMEDY', 2, NULL),
(18, 'THRILLER', 2, NULL),
(19, 'HORROR', 2, NULL),
(20, 'ROMANCE', 2, NULL),
(21, 'FANTASY', 2, NULL),
(22, 'MYSTERY', 2, NULL),
(23, 'ANIMATION', 2, NULL),
(24, 'DOCUMENTARY', 2, NULL),
(25, 'ACTION', NULL, 1),
(26, 'ADVENTURE', NULL, 1),
(27, 'SCIFI', NULL, 1),
(28, 'DRAMA', NULL, 1),
(29, 'COMEDY', NULL, 1),
(30, 'THRILLER', NULL, 1),
(31, 'HORROR', NULL, 1),
(32, 'ROMANCE', NULL, 1),
(33, 'FANTASY', NULL, 1),
(34, 'MYSTERY', NULL, 1),
(35, 'ANIMATION', NULL, 1),
(36, 'DOCUMENTARY', NULL, 1),
(37, 'ACTION', NULL, 2),
(38, 'ADVENTURE', NULL, 2),
(39, 'SCIFI', NULL, 2),
(40, 'DRAMA', NULL, 2),
(41, 'COMEDY', NULL, 2),
(42, 'THRILLER', NULL, 2),
(43, 'HORROR', NULL, 2),
(44, 'ROMANCE', NULL, 2),
(45, 'FANTASY', NULL, 2),
(46, 'MYSTERY', NULL, 2),
(47, 'ANIMATION', NULL, 2),
(48, 'DOCUMENTARY', NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `genrespreference`
--

CREATE TABLE `genrespreference` (
  `genrepreference_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `genre` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `genrespreference`
--

INSERT INTO `genrespreference` (`genrepreference_id`, `profile_id`, `genre`) VALUES
(1, 1, 'ACTION'),
(2, 1, 'FANTASY'),
(3, 2, 'ACTION'),
(4, 2, 'SCIFI');

-- --------------------------------------------------------

--
-- Table structure for table `indicationpreference`
--

CREATE TABLE `indicationpreference` (
  `indicationpreference_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `indication` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `indicationpreference`
--

INSERT INTO `indicationpreference` (`indicationpreference_id`, `profile_id`, `indication`) VALUES
(1, 1, 'VIOLENCE'),
(2, 1, 'PROFANITY_USAGE'),
(3, 2, 'VIOLENCE'),
(4, 2, 'FEAR');

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
(12, 'The Godfather: Part II', 202, 'TWELVE_YEARS'),
(13, 'unavailable movie', 150, 'SIX_YEARS');

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
(1, '/path/to/image', 0, 'DUTCH', 1),
(2, '/path/to/image', 0, 'DUTCH', 1),
(3, NULL, NULL, 'DUTCH', 2),
(4, NULL, NULL, 'ENGLISH', 2),
(5, NULL, NULL, 'ENGLISH', 3),
(6, NULL, NULL, 'GERMAN', 2),
(7, NULL, 1, 'GERMAN', 4),
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
(18, NULL, NULL, 'GERMAN', 12),
(19, NULL, 1, 'GERMAN', 7),
(20, NULL, NULL, 'DUTCH', 5),
(21, NULL, 1, 'DUTCH', 6),
(22, NULL, NULL, 'DUTCH', 5),
(23, NULL, NULL, 'DUTCH', 10),
(24, NULL, 1, 'ENGLISH', 4);

--
-- Triggers `profile`
--
DELIMITER $$
CREATE TRIGGER `before_insert_profile` BEFORE INSERT ON `profile` FOR EACH ROW BEGIN
    DECLARE profile_count INT;

    -- Controleer het aantal profielen voor het account
    SELECT COUNT(*) INTO profile_count
    FROM profile
    WHERE account_id = NEW.account_id;

    -- Als het aantal profielen groter is dan 4, voorkom het invoegen
    IF profile_count >= 4 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert more than 4 profiles for an account';
    END IF;
END
$$
DELIMITER ;

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
(12, 'Game of Thrones', 'SIXTEEN_YEARS'),
(13, 'unavailable series', 'SIX_YEARS');

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
(1, 'ENGLISH', '/path/to/subtitles/movie1_eng.srt', 1, NULL),
(2, 'DUTCH', '/path/to/subtitles/movie1_nl.srt', 1, NULL),
(3, 'FRENCH', '/path/to/subtitles/movie1_fr.srt', 1, NULL),
(4, 'SPANISH', '/path/to/subtitles/movie1_es.srt', 1, NULL),
(5, 'GERMAN', '/path/to/subtitles/movie1_de.srt', 1, NULL),
(6, 'ITALIAN', '/path/to/subtitles/movie1_it.srt', 1, NULL),
(7, 'JAPANESE', '/path/to/subtitles/movie1_jp.srt', 1, NULL),
(8, 'CHINESE', '/path/to/subtitles/movie1_cn.srt', 1, NULL),
(9, 'RUSSIAN', '/path/to/subtitles/movie1_ru.srt', 1, NULL),
(10, 'PORTUGUESE', '/path/to/subtitles/movie1_pt.srt', 1, NULL),
(11, 'ARABIC', '/path/to/subtitles/movie1_ar.srt', 1, NULL),
(12, 'KOREAN', '/path/to/subtitles/movie1_kr.srt', 1, NULL),
(13, 'ENGLISH', '/path/to/subtitles/movie2_eng.srt', 2, NULL),
(14, 'DUTCH', '/path/to/subtitles/movie2_nl.srt', 2, NULL),
(15, 'FRENCH', '/path/to/subtitles/movie2_fr.srt', 2, NULL),
(16, 'SPANISH', '/path/to/subtitles/movie2_es.srt', 2, NULL),
(17, 'GERMAN', '/path/to/subtitles/movie2_de.srt', 2, NULL),
(18, 'ITALIAN', '/path/to/subtitles/movie2_it.srt', 2, NULL),
(19, 'JAPANESE', '/path/to/subtitles/movie2_jp.srt', 2, NULL),
(20, 'CHINESE', '/path/to/subtitles/movie2_cn.srt', 2, NULL),
(21, 'RUSSIAN', '/path/to/subtitles/movie2_ru.srt', 2, NULL),
(22, 'PORTUGUESE', '/path/to/subtitles/movie2_pt.srt', 2, NULL),
(23, 'ARABIC', '/path/to/subtitles/movie2_ar.srt', 2, NULL),
(24, 'KOREAN', '/path/to/subtitles/movie2_kr.srt', 2, NULL),
(25, 'ENGLISH', '/path/to/subtitles/episode1_eng.srt', NULL, 1),
(26, 'DUTCH', '/path/to/subtitles/episode1_nl.srt', NULL, 1),
(27, 'FRENCH', '/path/to/subtitles/episode1_fr.srt', NULL, 1),
(28, 'SPANISH', '/path/to/subtitles/episode1_es.srt', NULL, 1),
(29, 'GERMAN', '/path/to/subtitles/episode1_de.srt', NULL, 1),
(30, 'ITALIAN', '/path/to/subtitles/episode1_it.srt', NULL, 1),
(31, 'JAPANESE', '/path/to/subtitles/episode1_jp.srt', NULL, 1),
(32, 'CHINESE', '/path/to/subtitles/episode1_cn.srt', NULL, 1),
(33, 'RUSSIAN', '/path/to/subtitles/episode1_ru.srt', NULL, 1),
(34, 'PORTUGUESE', '/path/to/subtitles/episode1_pt.srt', NULL, 1),
(35, 'ARABIC', '/path/to/subtitles/episode1_ar.srt', NULL, 1),
(36, 'KOREAN', '/path/to/subtitles/episode1_kr.srt', NULL, 1),
(37, 'ENGLISH', '/path/to/subtitles/episode13_eng.srt', NULL, 13),
(38, 'DUTCH', '/path/to/subtitles/episode13_nl.srt', NULL, 13),
(39, 'FRENCH', '/path/to/subtitles/episode13_fr.srt', NULL, 13),
(40, 'SPANISH', '/path/to/subtitles/episode13_es.srt', NULL, 13),
(41, 'GERMAN', '/path/to/subtitles/episode13_de.srt', NULL, 13),
(42, 'ITALIAN', '/path/to/subtitles/episode13_it.srt', NULL, 13),
(43, 'JAPANESE', '/path/to/subtitles/episode13_jp.srt', NULL, 13),
(44, 'CHINESE', '/path/to/subtitles/episode13_cn.srt', NULL, 13),
(45, 'RUSSIAN', '/path/to/subtitles/episode13_ru.srt', NULL, 13),
(46, 'PORTUGUESE', '/path/to/subtitles/episode13_pt.srt', NULL, 13),
(47, 'ARABIC', '/path/to/subtitles/episode13_ar.srt', NULL, 13),
(48, 'KOREAN', '/path/to/subtitles/episode13_kr.srt', NULL, 13);

-- --------------------------------------------------------

--
-- Table structure for table `viewing_behavior`
--

CREATE TABLE `viewing_behavior` (
  `viewing_behavior_id` int(11) NOT NULL,
  `pause_time` int(11) DEFAULT NULL,
  `profile_id` int(11) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `episode_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `watchlist`
--

CREATE TABLE `watchlist` (
  `watchlist_id` int(11) NOT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `serie_id` int(11) DEFAULT NULL,
  `profile_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `watchlist`
--

INSERT INTO `watchlist` (`watchlist_id`, `movie_id`, `serie_id`, `profile_id`) VALUES
(1, 1, NULL, 1),
(2, NULL, 1, 1);

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
-- Indexes for table `agepreference`
--
ALTER TABLE `agepreference`
  ADD PRIMARY KEY (`agepreference_id`),
  ADD KEY `FK_agepreference_0` (`profile_id`);

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
-- Indexes for table `genrespreference`
--
ALTER TABLE `genrespreference`
  ADD PRIMARY KEY (`genrepreference_id`),
  ADD KEY `FK_genrepreference_0` (`profile_id`);

--
-- Indexes for table `indicationpreference`
--
ALTER TABLE `indicationpreference`
  ADD PRIMARY KEY (`indicationpreference_id`),
  ADD KEY `FK_indicationpreference_0` (`profile_id`);

--
-- Indexes for table `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`movie_id`);

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
  ADD KEY `FK_viewing_behavior_0` (`profile_id`),
  ADD KEY `FK_viewing_behavior_1` (`movie_id`),
  ADD KEY `FK_viewing_behavior_2` (`episode_id`);

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
-- AUTO_INCREMENT for table `agepreference`
--
ALTER TABLE `agepreference`
  MODIFY `agepreference_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `classification`
--
ALTER TABLE `classification`
  MODIFY `classification_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

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
-- AUTO_INCREMENT for table `genrespreference`
--
ALTER TABLE `genrespreference`
  MODIFY `genrepreference_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `indicationpreference`
--
ALTER TABLE `indicationpreference`
  MODIFY `indicationpreference_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `movie`
--
ALTER TABLE `movie`
  MODIFY `movie_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `profile_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `serie`
--
ALTER TABLE `serie`
  MODIFY `serie_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

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
  MODIFY `watchlist_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `FK_account_0` FOREIGN KEY (`subscription_id`) REFERENCES `subscription` (`subscription_id`);

--
-- Constraints for table `agepreference`
--
ALTER TABLE `agepreference`
  ADD CONSTRAINT `FK_agepreference_0` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`profile_id`);

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
-- Constraints for table `genrespreference`
--
ALTER TABLE `genrespreference`
  ADD CONSTRAINT `FK_genrepreference_0` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`profile_id`);

--
-- Constraints for table `indicationpreference`
--
ALTER TABLE `indicationpreference`
  ADD CONSTRAINT `FK_indicationpreference_0` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`profile_id`);

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
  ADD CONSTRAINT `FK_viewing_behavior_0` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`profile_id`),
  ADD CONSTRAINT `FK_viewing_behavior_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  ADD CONSTRAINT `FK_viewing_behavior_2` FOREIGN KEY (`episode_id`) REFERENCES `episode` (`episode_id`);

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
