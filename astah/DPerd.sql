CREATE TABLE apikey (
 apikey VARCHAR(100) NOT NULL,
 role VARCHAR(255)
);

ALTER TABLE apikey ADD CONSTRAINT PK_apikey PRIMARY KEY (apikey);


CREATE TABLE movie (
 movie_id INT NOT NULL,
 title VARCHAR(255),
 movie_duration INT,
 age_restriction VARCHAR(255)
);

ALTER TABLE movie ADD CONSTRAINT PK_movie PRIMARY KEY (movie_id);


CREATE TABLE serie (
 serie_id INT NOT NULL,
 serie_name VARCHAR(255),
 age_restriction VARCHAR(255)
);

ALTER TABLE serie ADD CONSTRAINT PK_serie PRIMARY KEY (serie_id);


CREATE TABLE subscription (
 subscription_id INT NOT NULL,
 description VARCHAR(255),
 subscription_price FLOAT(10) NOT NULL
);

ALTER TABLE subscription ADD CONSTRAINT PK_subscription PRIMARY KEY (subscription_id);


CREATE TABLE account (
 account_id INT NOT NULL,
 email VARCHAR(255) NOT NULL,
 username VARCHAR(255) NOT NULL,
 password VARCHAR(255) NOT NULL,
 payment_method VARCHAR(255) NOT NULL,
 blocked INT,
 subscription_id INT NOT NULL,
 video_quality VARCHAR(100)
);

ALTER TABLE account ADD CONSTRAINT PK_account PRIMARY KEY (account_id);


CREATE TABLE episode (
 episode_id INT NOT NULL,
 title VARCHAR(255),
 episode_duration INT,
 serie_id INT NOT NULL
);

ALTER TABLE episode ADD CONSTRAINT PK_episode PRIMARY KEY (episode_id);


CREATE TABLE genres (
 genres_id INT NOT NULL,
 genre VARCHAR(255),
 movie_id INT,
 serie_id INT
);

ALTER TABLE genres ADD CONSTRAINT PK_genres PRIMARY KEY (genres_id);


CREATE TABLE profile (
 profile_id INT NOT NULL,
 profile_image VARCHAR(255),
 profile_child INT,
 language VARCHAR(255),
 account_id INT NOT NULL
);

ALTER TABLE profile ADD CONSTRAINT PK_profile PRIMARY KEY (profile_id);


CREATE TABLE subtitle (
 subtitle_id INT NOT NULL,
 language VARCHAR(100),
 subtitle_location VARCHAR(100),
 movie_id INT NOT NULL,
 episode_id INT NOT NULL
);

ALTER TABLE subtitle ADD CONSTRAINT PK_subtitle PRIMARY KEY (subtitle_id);


CREATE TABLE watchlist (
 watchlist_id INT NOT NULL,
 movie_id INT NOT NULL,
 serie_id INT NOT NULL,
 profile_id INT NOT NULL
);

ALTER TABLE watchlist ADD CONSTRAINT PK_watchlist PRIMARY KEY (watchlist_id);


CREATE TABLE classification (
 classification_id INT NOT NULL,
 classification VARCHAR(255),
 movie_id INT NOT NULL,
 episode_id INT NOT NULL
);

ALTER TABLE classification ADD CONSTRAINT PK_classification PRIMARY KEY (classification_id);


CREATE TABLE viewing_behavior (
 viewing_behavior_id INT NOT NULL,
 watchlist_id INT NOT NULL,
 pause_time INT,
 viewing_history VARCHAR(255),
 times_watched INT
);

ALTER TABLE viewing_behavior ADD CONSTRAINT PK_viewing_behavior PRIMARY KEY (viewing_behavior_id,watchlist_id);


CREATE TABLE preference (
 preference_id INT NOT NULL,
 interest VARCHAR(255),
 watchlist_id INT NOT NULL,
 viewing_behavior_id INT
);

ALTER TABLE preference ADD CONSTRAINT PK_preference PRIMARY KEY (preference_id);


CREATE TABLE genresPreference (
 genres_id INT NOT NULL,
 preference_id INT NOT NULL
);

ALTER TABLE genresPreference ADD CONSTRAINT PK_genresPreference PRIMARY KEY (genres_id,preference_id);


CREATE TABLE interestPreference (
 preference_id INT NOT NULL,
 profile_id INT NOT NULL
);

ALTER TABLE interestPreference ADD CONSTRAINT PK_interestPreference PRIMARY KEY (preference_id,profile_id);


ALTER TABLE account ADD CONSTRAINT FK_account_0 FOREIGN KEY (subscription_id) REFERENCES subscription (subscription_id);


ALTER TABLE episode ADD CONSTRAINT FK_episode_0 FOREIGN KEY (serie_id) REFERENCES serie (serie_id);


ALTER TABLE genres ADD CONSTRAINT FK_genres_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE genres ADD CONSTRAINT FK_genres_1 FOREIGN KEY (serie_id) REFERENCES serie (serie_id);


ALTER TABLE profile ADD CONSTRAINT FK_profile_0 FOREIGN KEY (account_id) REFERENCES account (account_id);


ALTER TABLE subtitle ADD CONSTRAINT FK_subtitle_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE subtitle ADD CONSTRAINT FK_subtitle_1 FOREIGN KEY (episode_id) REFERENCES episode (episode_id);


ALTER TABLE watchlist ADD CONSTRAINT FK_watchlist_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE watchlist ADD CONSTRAINT FK_watchlist_1 FOREIGN KEY (serie_id) REFERENCES serie (serie_id);
ALTER TABLE watchlist ADD CONSTRAINT FK_watchlist_2 FOREIGN KEY (profile_id) REFERENCES profile (profile_id);


ALTER TABLE classification ADD CONSTRAINT FK_classification_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE classification ADD CONSTRAINT FK_classification_1 FOREIGN KEY (episode_id) REFERENCES episode (episode_id);


ALTER TABLE viewing_behavior ADD CONSTRAINT FK_viewing_behavior_0 FOREIGN KEY (watchlist_id) REFERENCES watchlist (watchlist_id);


ALTER TABLE preference ADD CONSTRAINT FK_preference_0 FOREIGN KEY (watchlist_id,viewing_behavior_id) REFERENCES viewing_behavior (watchlist_id,viewing_behavior_id);


ALTER TABLE genresPreference ADD CONSTRAINT FK_genresPreference_0 FOREIGN KEY (genres_id) REFERENCES genres (genres_id);
ALTER TABLE genresPreference ADD CONSTRAINT FK_genresPreference_1 FOREIGN KEY (preference_id) REFERENCES preference (preference_id);


ALTER TABLE interestPreference ADD CONSTRAINT FK_interestPreference_0 FOREIGN KEY (preference_id) REFERENCES preference (preference_id);
ALTER TABLE interestPreference ADD CONSTRAINT FK_interestPreference_1 FOREIGN KEY (profile_id) REFERENCES profile (profile_id);


