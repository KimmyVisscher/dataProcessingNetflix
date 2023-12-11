CREATE TABLE Episode (
 episode_id INT NOT NULL,
 title VARCHAR(255),
 episode_duration TIMESTAMP(6)
);

ALTER TABLE Episode ADD CONSTRAINT PK_Episode PRIMARY KEY (episode_id);


CREATE TABLE Movie (
 movie_id INT NOT NULL,
 title VARCHAR(255),
 movie_duration TIMESTAMP(6)
);

ALTER TABLE Movie ADD CONSTRAINT PK_Movie PRIMARY KEY (movie_id);


CREATE TABLE Preference (
 preference_id INT NOT NULL,
 watchlist_id INT NOT NULL,
 characteristics_id INT NOT NULL,
 interest VARCHAR(255),
 username VARCHAR(255)
);

ALTER TABLE Preference ADD CONSTRAINT PK_Preference PRIMARY KEY (preference_id,watchlist_id,characteristics_id);


CREATE TABLE Profile (
 profile_id INT NOT NULL,
 account_id INT NOT NULL,
 subscription_id INT NOT NULL,
 profile_image VARCHAR(255),
 profile_child BIT(10),
 language VARCHAR(255),
 preference_id INT NOT NULL,
 watchlist_id INT,
 characteristics_id INT
);

ALTER TABLE Profile ADD CONSTRAINT PK_Profile PRIMARY KEY (profile_id,account_id,subscription_id);


CREATE TABLE Season (
 season_id INT NOT NULL
);

ALTER TABLE Season ADD CONSTRAINT PK_Season PRIMARY KEY (season_id);


CREATE TABLE Serie (
 serie_id INT NOT NULL,
 episode_id INT NOT NULL,
 serie_name VARCHAR(255)
);

ALTER TABLE Serie ADD CONSTRAINT PK_Serie PRIMARY KEY (serie_id,episode_id);


CREATE TABLE Subscription (
 subscription_id INT NOT NULL,
 description VARCHAR(255),
 subscription_price FLOAT(10)
);

ALTER TABLE Subscription ADD CONSTRAINT PK_Subscription PRIMARY KEY (subscription_id);


CREATE TABLE Subtitle (
 subtitle_id INT NOT NULL,
 movie_id INT NOT NULL,
 episode_id INT NOT NULL,
 language VARCHAR(255),
 subtitle_location VARCHAR(255)
);

ALTER TABLE Subtitle ADD CONSTRAINT PK_Subtitle PRIMARY KEY (subtitle_id,movie_id,episode_id);


CREATE TABLE ViewerIndication (
 viewerIndication_id INT NOT NULL
);

ALTER TABLE ViewerIndication ADD CONSTRAINT PK_ViewerIndication PRIMARY KEY (viewerIndication_id);


CREATE TABLE viewing_behavior (
 watchlist_id INT NOT NULL,
 pause_time VARCHAR(255),
 viewing_history VARCHAR(255),
 times_watched VARCHAR(10)
);

ALTER TABLE viewing_behavior ADD CONSTRAINT PK_viewing_behavior PRIMARY KEY (watchlist_id);


CREATE TABLE watchlist_item (
 watchlist_id INT NOT NULL,
 movie_id INT NOT NULL,
 serie_id INT NOT NULL,
 episode_id INT NOT NULL,
 subtitle_id INT NOT NULL,
 profile_id INT,
 account_id INT,
 subscription_id INT
);

ALTER TABLE watchlist_item ADD CONSTRAINT PK_watchlist_item PRIMARY KEY (watchlist_id);


CREATE TABLE Account (
 account_id INT NOT NULL,
 subscription_id INT NOT NULL,
 email VARCHAR(255) NOT NULL,
 password VARCHAR(255),
 payment_method VARCHAR(255),
 blocked BIT(10),
 max_profile INT(1),
 video_quality VARCHAR(10)
);

ALTER TABLE Account ADD CONSTRAINT PK_Account PRIMARY KEY (account_id,subscription_id);


CREATE TABLE characteristics (
 characteristics_id INT NOT NULL,
 episode_id INT NOT NULL,
 movie_id INT NOT NULL,
 genres VARCHAR(10),
 age_restriction VARCHAR(10),
 classification VARCHAR(10)
);

ALTER TABLE characteristics ADD CONSTRAINT PK_characteristics PRIMARY KEY (characteristics_id);


ALTER TABLE Preference ADD CONSTRAINT FK_Preference_0 FOREIGN KEY (watchlist_id) REFERENCES viewing_behavior (watchlist_id);
ALTER TABLE Preference ADD CONSTRAINT FK_Preference_1 FOREIGN KEY (characteristics_id) REFERENCES characteristics (characteristics_id);


ALTER TABLE Profile ADD CONSTRAINT FK_Profile_0 FOREIGN KEY (account_id,subscription_id) REFERENCES Account (account_id,subscription_id);
ALTER TABLE Profile ADD CONSTRAINT FK_Profile_1 FOREIGN KEY (preference_id,watchlist_id,characteristics_id) REFERENCES Preference (preference_id,watchlist_id,characteristics_id);
ALTER TABLE Profile ADD CONSTRAINT FK_Profile_2 FOREIGN KEY (watchlist_id) REFERENCES watchlist_item (watchlist_id);


ALTER TABLE Serie ADD CONSTRAINT FK_Serie_0 FOREIGN KEY (episode_id) REFERENCES Episode (episode_id);


ALTER TABLE Subtitle ADD CONSTRAINT FK_Subtitle_0 FOREIGN KEY (movie_id) REFERENCES Movie (movie_id);
ALTER TABLE Subtitle ADD CONSTRAINT FK_Subtitle_1 FOREIGN KEY (episode_id) REFERENCES Episode (episode_id);


ALTER TABLE viewing_behavior ADD CONSTRAINT FK_viewing_behavior_0 FOREIGN KEY (watchlist_id) REFERENCES watchlist_item (watchlist_id);


ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_0 FOREIGN KEY (movie_id) REFERENCES Movie (movie_id);
ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_1 FOREIGN KEY (serie_id,episode_id) REFERENCES Serie (serie_id,episode_id);
ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_2 FOREIGN KEY (subtitle_id,movie_id,episode_id) REFERENCES Subtitle (subtitle_id,movie_id,episode_id);
ALTER TABLE watchlist_item ADD CONSTRAINT FK_watchlist_item_3 FOREIGN KEY (profile_id,account_id,subscription_id) REFERENCES Profile (profile_id,account_id,subscription_id);


ALTER TABLE Account ADD CONSTRAINT FK_Account_0 FOREIGN KEY (subscription_id) REFERENCES Subscription (subscription_id);


ALTER TABLE characteristics ADD CONSTRAINT FK_characteristics_0 FOREIGN KEY (episode_id) REFERENCES Episode (episode_id);
ALTER TABLE characteristics ADD CONSTRAINT FK_characteristics_1 FOREIGN KEY (movie_id) REFERENCES Movie (movie_id);


