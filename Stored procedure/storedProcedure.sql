DELIMITER //

CREATE PROCEDURE calculateTotalRevenue()
BEGIN
    DECLARE totalRevenue FLOAT(10);

    SELECT SUM(subscription_price) INTO totalRevenue
    FROM subscription;

    SELECT totalRevenue AS TotalRevenue;
END //

DELIMITER ;


--^^calculate the total revenue^^--

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

