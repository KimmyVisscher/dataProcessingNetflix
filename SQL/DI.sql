START TRANSACTION
--
-- Stored procedures
--

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
END 

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

CREATE PROCEDURE calculateTotalAccounts()
BEGIN
    DECLARE totalAccounts INT;

    SELECT COUNT(*) INTO totalAccounts
    FROM account;

    SELECT totalAccounts AS TotalAccounts;
END

--
-- Checks
--

ALTER TABLE profile
ADD CONSTRAINT chk_max_profiles
CHECK (NOT EXISTS (
    SELECT 1
    FROM profile p
    WHERE p.account_id = profile.account_id
    GROUP BY p.account_id
    HAVING COUNT(*) > 4
));

COMMIT;

--
-- Triggers
-- 