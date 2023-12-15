CREATE TABLE apikey (
 apikey VARCHAR(30) NOT NULL,
 role VARCHAR(255)
);

ALTER TABLE apikey ADD CONSTRAINT PK_apikey PRIMARY KEY (apikey);


CREATE TABLE characteristics (
 characteristics_id INT NOT NULL,
 genres VARCHAR(30),
 age_restriction VARCHAR(30),
 classification VARCHAR(30)
);

ALTER TABLE characteristics ADD CONSTRAINT PK_characteristics PRIMARY KEY (characteristics_id);


CREATE TABLE movie (
 movie_id INT NOT NULL,
 title VARCHAR(255),
 movie_duration INT,
 characteristics_id INT
);

ALTER TABLE movie ADD CONSTRAINT PK_movie PRIMARY KEY (movie_id);


CREATE TABLE preference (
 preference_id INT NOT NULL,
 interest VARCHAR(255),
 username VARCHAR(255),
 characteristics_id INT NOT NULL,
 watchlist_item_id INT NOT NULL
);

ALTER TABLE preference ADD CONSTRAINT PK_preference PRIMARY KEY (preference_id);


CREATE TABLE profile (
 profile_id INT NOT NULL,
 account_id INT NOT NULL,
 subscription_id INT NOT NULL,
 profile_image VARCHAR(255),
 profile_child BIT(10),
 language VARCHAR(255),
 preference_id INT
);

ALTER TABLE profile ADD CONSTRAINT PK_profile PRIMARY KEY (profile_id,account_id,subscription_id);


CREATE TABLE Season (
 season_id INT NOT NULL
);

ALTER TABLE Season ADD CONSTRAINT PK_Season PRIMARY KEY (season_id);


CREATE TABLE serie (
 serie_id INT NOT NULL,
 serie_name VARCHAR(30)
);

ALTER TABLE serie ADD CONSTRAINT PK_serie PRIMARY KEY (serie_id);


CREATE TABLE subscription (
 subscription_id INT NOT NULL,
 description VARCHAR(255),
 subscription_price FLOAT(10)
);

ALTER TABLE subscription ADD CONSTRAINT PK_subscription PRIMARY KEY (subscription_id);


CREATE TABLE ViewerIndication (
 viewerIndication_id INT NOT NULL
);

ALTER TABLE ViewerIndication ADD CONSTRAINT PK_ViewerIndication PRIMARY KEY (viewerIndication_id);


CREATE TABLE viewing_behavior (
 watchlist_item_id INT NOT NULL,
 pause_time INT,
 viewing_history VARCHAR(255),
 times_watched INT
);

ALTER TABLE viewing_behavior ADD CONSTRAINT PK_viewing_behavior PRIMARY KEY (watchlist_item_id);


CREATE TABLE watchlist_item (
 watchlist_item_id INT NOT NULL,
 movie_id INT NOT NULL,
 serie_id INT NOT NULL,
 profile_id INT,
 account_id INT,
 subscription_id INT
);

ALTER TABLE watchlist_item ADD CONSTRAINT PK_watchlist_item PRIMARY KEY (watchlist_item_id);


CREATE TABLE account (
 account_id INT NOT NULL,
 subscription_id INT NOT NULL,
 email VARCHAR(255) NOT NULL,
 password VARCHAR(255),
 payment_method VARCHAR(255),
 blocked BIT(10),
 video_quality VARCHAR(30)
);

ALTER TABLE account ADD CONSTRAINT PK_account PRIMARY KEY (account_id,subscription_id);


CREATE TABLE episode (
 episode_id INT NOT NULL,
 serie_id INT NOT NULL,
 title VARCHAR(255),
 episode_duration INT,
 characteristics_id INT
);

ALTER TABLE episode ADD CONSTRAINT PK_episode PRIMARY KEY (episode_id,serie_id);


CREATE TABLE subtitle (
 subtitle_id INT NOT NULL,
 movie_id INT NOT NULL,
 episode_id INT NOT NULL,
 serie_id INT NOT NULL,
 language VARCHAR(30),
 subtitle_location VARCHAR(30)
);

ALTER TABLE subtitle ADD CONSTRAINT PK_subtitle PRIMARY KEY (subtitle_id,movie_id,episode_id,serie_id);


ALTER TABLE movie ADD CONSTRAINT FK_movie_0 FOREIGN KEY (characteristics_id) REFERENCES characteristics (characteristics_id);


ALTER TABLE preference ADD CONSTRAINT FK_preference_0 FOREIGN KEY (characteristics_id) REFERENCES characteristics (characteristics_id);
ALTER TABLE preference ADD CONSTRAINT FK_preference_1 FOREIGN KEY (watchlist_item_id) REFERENCES viewing_behavior (watchlist_item_id);


ALTER TABLE profile ADD CONSTRAINT FK_profile_0 FOREIGN KEY (account_id,subscription_id) REFERENCES account (account_id,subscription_id);
ALTER TABLE profile ADD CONSTRAINT FK_profile_1 FOREIGN KEY (preference_id) REFERENCES preference (preference_id);


ALTER TABLE viewing_behavior ADD CONSTRAINT FK_viewing_behavior_0 FOREIGN KEY (watchlist_item_id) REFERENCES watchlist_item (watchlist_item_id);


ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_1 FOREIGN KEY (serie_id) REFERENCES serie (serie_id);
ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_2 FOREIGN KEY (profile_id,account_id,subscription_id) REFERENCES profile (profile_id,account_id,subscription_id);


ALTER TABLE account ADD CONSTRAINT FK_account_0 FOREIGN KEY (subscription_id) REFERENCES subscription (subscription_id);


ALTER TABLE episode ADD CONSTRAINT FK_episode_0 FOREIGN KEY (serie_id) REFERENCES serie (serie_id);
ALTER TABLE episode ADD CONSTRAINT FK_episode_1 FOREIGN KEY (characteristics_id) REFERENCES characteristics (characteristics_id);


ALTER TABLE subtitle ADD CONSTRAINT FK_subtitle_0 FOREIGN KEY (movie_id) REFERENCES movie (movie_id);
ALTER TABLE subtitle ADD CONSTRAINT FK_subtitle_1 FOREIGN KEY (episode_id,serie_id) REFERENCES episode (episode_id,serie_id);


