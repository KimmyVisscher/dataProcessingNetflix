/*
    This file is used to add 4 diffrent types of users with the accompanying permissions to a mysql DBMS.
    Please be advised that certain querry's within this file will not work unless you use the appropiate database file: "DPerd.sql"
    For this transaction to pass the database name must be "DP_Netflix" otherwise be advised and refactor the name within this file.
    If you encounter an error whilst loging in with a newely created user or using recently modified access, use the "FLUSH PRIVILEGES;" command.

*/

START TRANSACTION;
--
-- User Junior
--

CREATE USER IF NOT EXISTS 'User_Junior'@'%' IDENTIFIED BY 'GerjanRulez';

GRANT SELECT, INSERT, UPDATE, DELETE ON `DP_netflix`.* TO 'User_Junior'@'%';

--
-- User Medior
--

CREATE USER IF NOT EXISTS 'User_Medior'@'%' IDENTIFIED BY 'RobRulez';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, ALTER, EVENT, TRIGGER, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EXECUTE ON `DP_netflix`.* TO 'User_Medior'@'%';

GRANT SET PASSWORD ON DP_netflix.* TO 'User_medior'@'%';

--
-- User Senior
--

CREATE USER IF NOT EXISTS 'User_Senior'@'%' IDENTIFIED BY 'JanRulez';

GRANT ALL PRIVILEGES ON *.* TO 'gebruikersnaam'@'%';

--
-- User API
--
CREATE USER IF NOT EXISTS 'User_API'@'%' IDENTIFIED BY 'APIKEY';

GRANT ALL PRIVILEGES ON DP_netflix.* TO 'User_API'@'%' WITH GRANT OPTION;


DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
    ROLLBACK;
    -- Eventuele andere foutafhandeling hier
END;

COMMIT;