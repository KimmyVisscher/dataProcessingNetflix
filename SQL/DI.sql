START TRANSACTION;
--
-- Stored procedures
--

-- total monthly revenue sorted by type with the number of accounts with the exclusion of blocked accounts. ---------

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

-- returns 1 single value with the monthly revenue with the exclusion of blocked accounts. ------------

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

-- returns total number of accounts.-------------------------------------------------

DELIMITER //

CREATE PROCEDURE calculateTotalAccounts()
BEGIN
    DECLARE totalAccounts INT;

    SELECT COUNT(*) INTO totalAccounts
    FROM account;

    SELECT totalAccounts AS TotalAccounts;
END //

DELIMITER ;

--returns number of accounts with an SD subscription. ------------------------------

DELIMITER //

CREATE PROCEDURE calculateTotalSubscriptionSD()
BEGIN
    SELECT COUNT(*) AS account_count
    FROM account
    WHERE subscription_id = 1;
END //

DELIMTER ;


--returns number of accounts with an HD subscription. ------------------------------

DELIMTER //

CREATE PROCEDURE calculateTotalSubscriptionHD()
BEGIN
    SELECT COUNT(*) AS account_count
    FROM account
    WHERE subscription_id = 2;
END //

DELIMITER ;

--returns number of accounts with an UHD subscription. -----------------------------

DELIMITER //

CREATE PROCEDURE calculateTotalSubscriptionUHD()
BEGIN
    SELECT COUNT(*) AS account_count
    FROM account
    WHERE subscription_id = 3;
END //

DELIMITER ;

/* please be advised that the back up procedures only work with the correct filepath and writing/read privileges.*/
--  daily (partial) incremental back-up. -----------------------------------------------------

DELIMITER //

CREATE PROCEDURE daily_incremental_backup()
BEGIN

  DECLARE last_backup_time TIMESTAMP;

  -- retrieve the last backup time for the account table
  SELECT last_account_backup_time INTO last_backup_time FROM backup_log;

  -- Make a backup of the changes since the last backup
  SELECT * INTO OUTFILE 'C:\\Users\\Bram\\Desktop\\incremental_backup.sql'
  FROM `account`
  WHERE modification_timestamp > last_backup_time;

  -- Update the backup-log with the current time
  UPDATE backup_log
  SET last_account_backup_time = CURRENT_TIMESTAMP;

END //

DELIMITER ;


-- Monthly full backup. -------------------------------------------------------------

DELIMITER //

CREATE PROCEDURE monthly_full_backup()
BEGIN

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

END //

DELIMITER ;

--
-- Triggers
--

-- Prevent the addition of an 5th profile to an account. ---------------------------

DELIMITER //

CREATE TRIGGER before_insert_profile
BEFORE INSERT ON profile
FOR EACH ROW
BEGIN
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
END;

//

DELIMITER ;

COMMIT;