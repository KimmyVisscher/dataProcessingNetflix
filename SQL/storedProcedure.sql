/*
Stored procedure for calculating the monthly revenue.
the result will be sorted by subscription type.
there is an built in check to exclude blocked accounts
*/
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

--querry version for testing purposes

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

--merge conflict resolve

DELIMiTER //

CREATE PROCEDURE calculateTotalAccounts()
BEGIN
    DECLARE totalAccounts INT;

    SELECT COUNT(*) INTO totalAccounts
    FROM account;

    SELECT totalAccounts AS TotalAccounts;
END //

DELIMIER ;

--^^calculate the total accounts^^--