--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `account_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `payment_method` varchar(255) NOT NULL,
  `blocked` int(11) DEFAULT NULL,
  `subscription_id` int(11) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `classification_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `classification` varchar(255) DEFAULT NULL,
  `movie_id` int(11) NOT NULL,
  `episode_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `episode`
--

CREATE TABLE `episode` (
  `episode_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `episode_duration` int(11) DEFAULT NULL,
  `serie_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `genres`
--

CREATE TABLE `genres` (
  `genres_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `genre` varchar(255) DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `serie_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `preference_id` int(11) NOT NULL ,
  `profile_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE `movie` (
  `movie_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `movie_duration` int(11) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `preference`
--

CREATE TABLE `preference` (
  `preference_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `interest` varchar(255) DEFAULT NULL,
  `watchlist_id` int(11) NOT NULL,
  `viewing_behavior_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `profile_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `profile_image` varchar(255) DEFAULT NULL,
  `profile_child` int(11) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `account_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `serie`
--

CREATE TABLE `serie` (
  `serie_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `serie_name` varchar(255) DEFAULT NULL,
  `age_restriction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subscription`
--

CREATE TABLE `subscription` (
  `subscription_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `subscription_price` float NOT NULL
  `video_quality` varchar(255) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subtitle`
--

CREATE TABLE `subtitle` (
  `subtitle_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `language` varchar(100) DEFAULT NULL,
  `subtitle_location` varchar(100) DEFAULT NULL,
  `movie_id` int(11) NOT NULL,
  `episode_id` int(11) NOT NULL 
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `viewing_behavior`
--

CREATE TABLE `viewing_behavior` (
  `viewing_behavior_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
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
  `watchlist_id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
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
  ADD KEY `FK_classification_0` (`movie_id`),
  ADD KEY `FK_classification_1` (`episode_id`);

--
-- Indexes for table `episode`
--
ALTER TABLE `episode`
  ADD KEY `FK_episode_0` (`serie_id`);

--
-- Indexes for table `genres`
--
ALTER TABLE `genres`
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
-- Indexes for table `preference`
--
ALTER TABLE `preference`
  ADD KEY `FK_preference_0` (`watchlist_id`,`viewing_behavior_id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD KEY `FK_profile_0` (`account_id`);

--
-- Indexes for table `subtitle`
--
ALTER TABLE `subtitle`
  ADD KEY `FK_subtitle_0` (`movie_id`),
  ADD KEY `FK_subtitle_1` (`episode_id`);

--
-- Indexes for table `viewing_behavior`
--
ALTER TABLE `viewing_behavior`
  ADD KEY `FK_viewing_behavior_0` (`watchlist_id`);

--
-- Indexes for table `watchlist`
--
ALTER TABLE `watchlist`
  ADD KEY `FK_watchlist_0` (`movie_id`),
  ADD KEY `FK_watchlist_1` (`serie_id`),
  ADD KEY `FK_watchlist_2` (`profile_id`);

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

