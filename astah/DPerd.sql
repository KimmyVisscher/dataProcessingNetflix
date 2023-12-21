CREATE TABLE apikey (
 apikey VARCHAR(100) NOT NULL,
 role VARCHAR(255)
);

CREATE TABLE movie (
 movie_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 title VARCHAR(255),
 movie_duration INT,
 age_restriction VARCHAR(255)
);

CREATE TABLE serie (
 serie_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 serie_name VARCHAR(255),
 age_restriction VARCHAR(255)
);

CREATE TABLE subscription (
 subscription_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 description VARCHAR(255),
 subscription_price FLOAT(10)
);

CREATE TABLE account (
 account_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 email VARCHAR(255) NOT NULL,
 username VARCHAR(255),
 password VARCHAR(255),
 payment_method VARCHAR(255),
 blocked BIT(10),
 subscription_id INT NOT NULL,
 video_quality VARCHAR(100)
);

CREATE TABLE episode (
 episode_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 serie_id INT NOT NULL,
 title VARCHAR(255),
 episode_duration INT
);

CREATE TABLE genres (
 genres_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 genre VARCHAR(255),
 movie_id INT,
 serie_id INT
);

CREATE TABLE profile (
 profile_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 profile_image VARCHAR(255),
 profile_child BIT(10),
 language VARCHAR(255),
 account_id INT
);

CREATE TABLE subtitle (
 subtitle_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 movie_id INT NOT NULL,
 episode_id INT NOT NULL,
 serie_id INT NOT NULL,
 language VARCHAR(100),
 subtitle_location VARCHAR(100)
);

CREATE TABLE watchlist_item (
 watchlist_item_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 movie_id INT NOT NULL,
 serie_id INT NOT NULL,
 profile_id INT
);

CREATE TABLE classification (
 classification_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 classification VARCHAR(255),
 movie_id INT,
 episode_id INT,
 serie_id INT
);

CREATE TABLE viewing_behavior (
 viewing_behavior_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 watchlist_item_id INT NOT NULL,
 pause_time INT,
 viewing_history VARCHAR(255),
 times_watched INT
);

CREATE TABLE preference (
 preference_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 interest VARCHAR(255),
 watchlist_item_id INT NOT NULL,
 viewing_behavior_id INT
);

CREATE TABLE genresPreference (
 genres_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 preference_id INT NOT NULL
);

CREATE TABLE interestPreference (
 preference_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 profile_id INT NOT NULL
);

ALTER TABLE account ADD CONSTRAINT FK_account_0 FOREIGN KEY (subscription_id) REFERENCES subscription (subscription_id);
ALTER TABLE episode ADD CONSTRAINT FK_episode_0 FOREIGN KEY (serie_id) REFERENCES serie (serie_id);
ALTER TABLE genres ADD CONSTRAINT FK_genres_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE genres ADD CONSTRAINT FK_genres_1 FOREIGN KEY (serie_id) REFERENCES serie (serie_id);
ALTER TABLE profile ADD CONSTRAINT FK_profile_0 FOREIGN KEY (account_id) REFERENCES account (account_id);
ALTER TABLE subtitle ADD CONSTRAINT FK_subtitle_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE subtitle ADD CONSTRAINT FK_subtitle_1 FOREIGN KEY (episode_id,serie_id) REFERENCES episode (episode_id,serie_id);
ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_1 FOREIGN KEY (serie_id) REFERENCES serie (serie_id);
ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_2 FOREIGN KEY (profile_id) REFERENCES profile (profile_id);
ALTER TABLE classification ADD CONSTRAINT FK_classification_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE classification ADD CONSTRAINT FK_classification_1 FOREIGN KEY (episode_id,serie_id) REFERENCES episode (episode_id,serie_id);
ALTER TABLE viewing_behavior ADD CONSTRAINT FK_viewing_behavior_0 FOREIGN KEY (watchlist_item_id) REFERENCES watchlist_item (watchlist_item_id);
ALTER TABLE preference ADD CONSTRAINT FK_preference_0 FOREIGN KEY (watchlist_item_id,viewing_behavior_id) REFERENCES viewing_behavior (watchlist_item_id,viewing_behavior_id);
ALTER TABLE genresPreference ADD CONSTRAINT FK_genresPreference_0 FOREIGN KEY (genres_id) REFERENCES genres (genres_id);
ALTER TABLE genresPreference ADD CONSTRAINT FK_genresPreference_1 FOREIGN KEY (preference_id) REFERENCES preference (preference_id);
ALTER TABLE interestPreference ADD CONSTRAINT FK_interestPreference_0 FOREIGN KEY (preference_id) REFERENCES preference (preference_id);
ALTER TABLE interestPreference ADD CONSTRAINT FK_interestPreference_1 FOREIGN KEY (profile_id) REFERENCES profile (profile_id);
