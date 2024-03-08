USE DB_Henkflix;

START TRANSACTION;

-- ----------------------------------------------------------------
-- Indexes

CREATE INDEX idx_email ON account(email);

CREATE INDEX idx_subscription_id ON subscription(subscription_id);

CREATE INDEX idx_account_id ON profile(account_id);

CREATE INDEX idx_profile_id ON agepreference(profile_id);

CREATE INDEX idx_apikey ON apikey(apikey);

CREATE INDEX idx_last_full_backup ON backup_log(last_full_backup_timestamp);
CREATE INDEX idx_last_incremental_backup ON backup_log(last_incremental_backup_time);

CREATE INDEX idx_movie_id ON classification(movie_id);
CREATE INDEX idx_episode_id ON classification(episode_id);

CREATE INDEX idx_serie_id ON episode(serie_id);

CREATE INDEX idx_movie_id_genres ON genres(movie_id);
CREATE INDEX idx_serie_id_genres ON genres(serie_id);

CREATE INDEX idx_profile_id_genrespreference ON genrespreference(profile_id);

CREATE INDEX idx_profile_id_indicationpreference ON indicationpreference(profile_id);

CREATE INDEX idx_age_restriction ON movie(age_restriction);

CREATE INDEX idx_account_id_profile ON profile(account_id);

CREATE INDEX idx_age_restriction_serie ON serie(age_restriction);

CREATE INDEX idx_language ON subtitle(language);


-- ----------------------------------------------------------------
-- Checks

ALTER TABLE backup_log
ADD CONSTRAINT chk_valid_backup_times CHECK (last_full_backup_timestamp <= last_incremental_backup_time);

ALTER TABLE backup_log
ADD CONSTRAINT chk_valid_incrementalBackup_times CHECK (backup_log.last_incremental_backup_time <= last_incremental_backup_time);

ALTER TABLE backup_log
ADD CONSTRAINT chk_valid_fullBackup_times CHECK (last_full_backup_timestamp <= last_full_backup_timestamp);

ALTER TABLE classification
ADD CONSTRAINT chk_valid_classification CHECK (movie_id IS NOT NULL OR episode_id IS NOT NULL);

ALTER TABLE genres
ADD CONSTRAINT chk_valid_genre CHECK (movie_id IS NOT NULL OR serie_id IS NOT NULL);

ALTER TABLE genrespreference
ADD CONSTRAINT chk_valid_genrespreference CHECK (profile_id IS NOT NULL);

ALTER TABLE indicationpreference
ADD CONSTRAINT chk_valid_indicationpreference CHECK (profile_id IS NOT NULL);

ALTER TABLE account
ADD CONSTRAINT chk_unique_username CHECK (LENGTH(username) > 0);

ALTER TABLE subscription
ADD CONSTRAINT chk_non_negative_price CHECK (subscription_price >= 0);

ALTER TABLE subtitle
ADD CONSTRAINT chk_unique_language CHECK (LENGTH(language) > 0);

-- ----------------------------------------------------------------
-- Triggers

-- Trigger voor de profile-tabel
DELIMITER //

CREATE TRIGGER before_insert_profile
BEFORE INSERT ON profile
FOR EACH ROW
BEGIN
    DECLARE profile_count INT;

    -- count the number of profiles present linkend to the same account.
    SELECT COUNT(*) INTO profile_count
    FROM profile
    WHERE account_id = NEW.account_id;

    -- if a an attempt is made to add an 5th profile, activate the trigger
    IF profile_count >= 4 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert more than 4 profiles for an account';
    END IF;
END;

//

DELIMITER ;

-- full back up limiter

DELIMITER //

CREATE TRIGGER before_fullBackup_log_update
BEFORE UPDATE ON backup_log
FOR EACH ROW
BEGIN
    DECLARE last_full_backup_time TIMESTAMP;
    SELECT MAX(last_full_backup_timestamp) INTO last_full_backup_time FROM backup_log;

    IF (NEW.last_full_backup_timestamp < last_full_backup_time + INTERVAL 1 WEEK) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot update full backup time more than once in a week';
    ELSE
        SET NEW.last_full_backup_timestamp = NOW();
    END IF;
END;

//

DELIMITER ;

-- incremental back up limiter
DELIMITER //

CREATE TRIGGER before_incrementalBackup_log_update
BEFORE UPDATE ON backup_log
FOR EACH ROW
BEGIN
    DECLARE last_incremental_backup_time TIMESTAMP;
    SELECT MAX(last_incremental_backup_time) INTO last_incremental_backup_time FROM backup_log;

    IF (NEW.last_incremental_backup_time >= CURDATE()) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot update incremental backup time more than once a day';
    ELSE
        SET NEW.last_incremental_backup_time = NOW();
    END IF;
END;

//


DELIMITER //

-- Trigger voor de account-tabel
CREATE TRIGGER account_before_insert
BEFORE INSERT ON account
FOR EACH ROW
SET NEW.modification_timestamp = NOW();

DELIMITER ;

DELIMITER //

CREATE TRIGGER account_before_update
BEFORE UPDATE ON account
FOR EACH ROW
BEGIN
    SET NEW.modification_timestamp = NOW();
END;

//

DELIMITER ;

DELIMITER //

-- Trigger voor de profile-tabel
CREATE TRIGGER profile_before_insert
BEFORE INSERT ON profile
FOR EACH ROW
SET NEW.modification_timestamp = NOW();

//

DELIMITER ;

DELIMITER //

CREATE TRIGGER profile_before_update
BEFORE UPDATE ON profile
FOR EACH ROW
BEGIN
    SET NEW.modification_timestamp = NOW();
END;

//

DELIMITER ;

DELIMITER //

-- Trigger voor de subscription-tabel
CREATE TRIGGER subscription_before_insert
BEFORE INSERT ON subscription
FOR EACH ROW
SET NEW.modification_timestamp = NOW();

//

DELIMITER ;

DELIMITER //

CREATE TRIGGER subscription_before_update
BEFORE UPDATE ON subscription
FOR EACH ROW
BEGIN
    SET NEW.modification_timestamp = NOW();
END;

//

DELIMITER ;

DELIMITER //

-- Trigger voor de watchlist-tabel
CREATE TRIGGER watchlist_before_insert
BEFORE INSERT ON watchlist
FOR EACH ROW
SET NEW.modification_timestamp = NOW();

//

DELIMITER ;

DELIMITER //

CREATE TRIGGER watchlist_before_update
BEFORE UPDATE ON watchlist
FOR EACH ROW
BEGIN
    SET NEW.modification_timestamp = NOW();
END;

//

DELIMITER ;

-- ----------------------------------------------------------------
-- Stored procedures

-- total monthly revenue sorted by type with the number of accounts with the exclusion of blocked accounts.

DELIMITER //

CREATE PROCEDURE CalculateMonthlyRevenue()
BEGIN
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
END //

DELIMITER ;

-- returns 1 single value with the monthly revenue with the exclusion of blocked accounts. 

DELIMITER //

CREATE PROCEDURE CalculateTotalMonthlyRevenue()
BEGIN
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
END //

DELIMITER ;

-- returns total number of accounts.

DELIMITER //

CREATE PROCEDURE calculateTotalAccounts()
BEGIN
    DECLARE totalAccounts INT;

    SELECT COUNT(*) INTO totalAccounts
    FROM account;

    SELECT totalAccounts AS TotalAccounts;
END //

DELIMITER ;

-- returns total number of accounts with the given video_quality paramater. 

DELIMITER //

CREATE PROCEDURE calculateTotalAccountsWithParam(IN video_quality VARCHAR(255))
BEGIN
    DECLARE totalAccounts INT;

    SELECT COUNT(DISTINCT a.account_id) INTO totalAccounts
    FROM account a
    INNER JOIN subscription s ON a.subscription_id = s.subscription_id
    WHERE s.video_quality = video_quality;

    SELECT totalAccounts AS TotalAccounts;
END //

DELIMITER ;


/* please be advised that the back up procedures only work with the correct filepath and writing/read privileges.*/

--
--  daily (partial) incremental back-up.
--

DELIMITER //

DELIMITER //

CREATE PROCEDURE daily_partial_incremental_backup()
BEGIN
  DECLARE last_incremental_backup_time TIMESTAMP;
  DECLARE query_text VARCHAR(255);

  -- Retrieve the last incremental backup time for all tables
  SELECT MAX(last_incremental_backup_time) INTO last_incremental_backup_time
  FROM backup_log;

  -- Generate a unique timestamp for the current backup
  SET @current_timestamp = DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s');

  -- Construct the filename for the incremental backup
  SET @backup_filename = CONCAT('FILEPATH\\incremental_backup_', @current_timestamp, '.sql');

  -- Create a dynamic SQL query to make an incremental backup of the changes since the last backup
  SET @query_text = CONCAT(
    'SELECT * INTO DUMPFILE ''', @backup_filename, ''' ',
    'FROM `account`, `profile`, `subscription`, `watchlist` ',
    'WHERE ',
    'account.modification_timestamp > "', last_incremental_backup_time, '" OR ',
    'profile.modification_timestamp > "', last_incremental_backup_time, '" OR ',
    'subscription.modification_timestamp > "', last_incremental_backup_time, '" OR ',
    'watchlist.modification_timestamp > "', last_incremental_backup_time, '";'
  );

  -- Execute the dynamic SQL query
  PREPARE stmt FROM @query_text;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Update the backup-log with the current time
  INSERT INTO backup_log (last_incremental_backup_time) VALUES (CURRENT_TIMESTAMP);

END //

DELIMITER ;


--
-- Monthly full backup. 
--

DELIMITER //

CREATE PROCEDURE monthly_full_backup()
BEGIN

  -- Setting an dynamic query to collect all of the tables for an full back-up.
  SET SESSION group_concat_max_len = 1000000;
  SET @tables_query = (
    SELECT GROUP_CONCAT(table_name SEPARATOR ', ')
    FROM information_schema.tables
    WHERE table_schema = 'DB_Henkflix'
  );

  -- Run the dynamic query.
  SET @current_datetime = DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s');
  SET @full_backup_query = CONCAT('SELECT * INTO OUTFILE ''FILEPATH\\full_backup_', @current_datetime, '.sql'' FROM ', @tables_query);
  PREPARE full_backup_stmt FROM @full_backup_query;
  EXECUTE full_backup_stmt;
  DEALLOCATE PREPARE full_backup_stmt;

  -- Update the back-up log
  INSERT INTO backup_log (last_full_backup_timestamp) VALUES (CURRENT_TIMESTAMP);

END //

DELIMITER ;

COMMIT;



