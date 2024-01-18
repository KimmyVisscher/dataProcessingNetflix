/*
CALL CalculateMonthlyRevenue();
*/

START TRANSACTION
--
-- Stored procedures
--

-- total monthly revenue sorted by type with the number of accounts

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
-- returns 1 single value with the monthly revenue

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

-- returns total accounts

DELIMITER //

CREATE PROCEDURE calculateTotalAccounts()
BEGIN
    DECLARE totalAccounts INT;

    SELECT COUNT(*) INTO totalAccounts
    FROM account;

    SELECT totalAccounts AS TotalAccounts;
END //

DELIMITER ;

--
-- Trigger
--

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

/* querry for testing
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
*/

--
-- Views
--
COMMIT;