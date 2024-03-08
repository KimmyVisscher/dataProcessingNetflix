START TRANSACTION;

CREATE DATABASE IF NOT EXISTS DB_Henkflix;
USE DB_Henkflix;

-- ----------------------------------------------------------------
-- Table structures

--
-- Table structure: account
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
  `subscription_id` int(11) NOT NULL,
  `modification_timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: agepreference
--

CREATE TABLE `agepreference` (
  `agepreference_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `agerestriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: apikey
--

CREATE TABLE `apikey` (
  `apikey` varchar(100) NOT NULL,
  `role` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: backup_log
--

CREATE TABLE `backup_log` (
  `last_full_backup_timestamp` timestamp NULL DEFAULT NULL,
  `last_incremental_backup_time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: classification
--

CREATE TABLE `classification` (
  `classification_id` int(11) NOT NULL,
  `classification` varchar(255) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `episode_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


--
-- Table structure: episode
--

CREATE TABLE `episode` (
  `episode_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `episode_duration` int(11) DEFAULT NULL,
  `serie_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: genres
--

CREATE TABLE `genres` (
  `genres_id` int(11) NOT NULL,
  `genre` varchar(255) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `serie_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


--
-- Table structure: genrespreference
--

CREATE TABLE `genrespreference` (
  `genrepreference_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `genre` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: indicationpreference
--

CREATE TABLE `indicationpreference` (
  `indicationpreference_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `indication` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: movie
--

CREATE TABLE `movie` (
  `movie_id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `movie_duration` int(11) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: profile
--

CREATE TABLE `profile` (
  `profile_id` int(11) NOT NULL,
  `profile_image` varchar(255) DEFAULT NULL,
  `profile_child` int(11) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `modification_timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: serie
--

CREATE TABLE `serie` (
  `serie_id` int(11) NOT NULL,
  `serie_name` varchar(255) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: subscription
--

CREATE TABLE `subscription` (
  `subscription_id` int(11) NOT NULL,
  `subscription_price` float(10,2) NOT NULL,
  `video_quality` varchar(100) DEFAULT NULL,
  `modification_timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: subtitle
--

CREATE TABLE `subtitle` (
  `subtitle_id` int(11) NOT NULL,
  `language` varchar(100) DEFAULT NULL,
  `subtitle_location` varchar(100) NOT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `episode_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: viewing_behavior
--

CREATE TABLE `viewing_behavior` (
  `viewing_behavior_id` int(11) NOT NULL,
  `pause_time` int(11) DEFAULT NULL,
  `profile_id` int(11) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `episode_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Table structure: watchlist
--

CREATE TABLE `watchlist` (
  `watchlist_id` int(11) NOT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `serie_id` int(11) DEFAULT NULL,
  `profile_id` int(11) NOT NULL,
  `modification_timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- ----------------------------------------------------------------
-- key additions

--
-- Keys for table `account`
--

ALTER TABLE `account`
  ADD PRIMARY KEY (`account_id`),
  ADD KEY `FK_account_0` (`subscription_id`);

--
-- Keys for table `agepreference`
--

ALTER TABLE `agepreference`
  ADD PRIMARY KEY (`agepreference_id`),
  ADD KEY `FK_agepreference_0` (`profile_id`);

--
-- Keys for table `apikey`
--

ALTER TABLE `apikey`
  ADD PRIMARY KEY (`apikey`);

--
-- Keys for table `classification`
--

ALTER TABLE `classification`
  ADD PRIMARY KEY (`classification_id`),
  ADD KEY `FK_classification_0` (`movie_id`),
  ADD KEY `FK_classification_1` (`episode_id`);

--
-- Keys for table `episode`
--

ALTER TABLE `episode`
  ADD PRIMARY KEY (`episode_id`),
  ADD KEY `FK_episode_0` (`serie_id`);

--
-- Keys for table `genres`
--

ALTER TABLE `genres`
  ADD PRIMARY KEY (`genres_id`),
  ADD KEY `FK_genres_0` (`movie_id`),
  ADD KEY `FK_genres_1` (`serie_id`);

--
-- Keys for table `genrespreference`
--

ALTER TABLE `genrespreference`
  ADD PRIMARY KEY (`genrepreference_id`),
  ADD KEY `FK_genrepreference_0` (`profile_id`);

--
-- Keys for table `indicationpreference`
--

ALTER TABLE `indicationpreference`
  ADD PRIMARY KEY (`indicationpreference_id`),
  ADD KEY `FK_indicationpreference_0` (`profile_id`);

--
-- Keys for table `movie`
--

ALTER TABLE `movie`
  ADD PRIMARY KEY (`movie_id`);

--
-- Keys for table `profile`
--

ALTER TABLE `profile`
  ADD PRIMARY KEY (`profile_id`),
  ADD KEY `FK_profile_0` (`account_id`);

--
-- Keys for table `serie`
--

ALTER TABLE `serie`
  ADD PRIMARY KEY (`serie_id`);

--
-- Keys for table `subscription`
--

ALTER TABLE `subscription`
  ADD PRIMARY KEY (`subscription_id`);

--
-- Keys for table `subtitle`
--

ALTER TABLE `subtitle`
  ADD PRIMARY KEY (`subtitle_id`),
  ADD KEY `FK_subtitle_0` (`movie_id`),
  ADD KEY `FK_subtitle_1` (`episode_id`);

--
-- Keys for table `viewing_behavior`
--

ALTER TABLE `viewing_behavior`
  ADD PRIMARY KEY (`viewing_behavior_id`),
  ADD KEY `FK_viewing_behavior_0` (`profile_id`),
  ADD KEY `FK_viewing_behavior_1` (`movie_id`),
  ADD KEY `FK_viewing_behavior_2` (`episode_id`);

--
-- Keys for table `watchlist`
--

ALTER TABLE `watchlist`
  ADD PRIMARY KEY (`watchlist_id`),
  ADD KEY `FK_watchlist_0` (`movie_id`),
  ADD KEY `FK_watchlist_1` (`serie_id`),
  ADD KEY `FK_watchlist_2` (`profile_id`);

-- ----------------------------------------------------------------
-- AUTO_INCREMENT alteration

--
-- AUTO_INCREMENT for table `account`
--

ALTER TABLE `account`
  MODIFY `account_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `agepreference`
--

ALTER TABLE `agepreference`
  MODIFY `agepreference_id` int(11) NOT NULL AUTO_INCREMENT;

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
-- AUTO_INCREMENT for table `genrespreference`
--

ALTER TABLE `genrespreference`
  MODIFY `genrepreference_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `indicationpreference`
--

ALTER TABLE `indicationpreference`
  MODIFY `indicationpreference_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `movie`
--

ALTER TABLE `movie`
  MODIFY `movie_id` int(11) NOT NULL AUTO_INCREMENT;

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
-- AUTO_INCREMENT for table `watchlist`
--

ALTER TABLE `watchlist`
  MODIFY `watchlist_id` int(11) NOT NULL AUTO_INCREMENT;

-- ----------------------------------------------------------------
-- Foreign key constraints

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

COMMIT;