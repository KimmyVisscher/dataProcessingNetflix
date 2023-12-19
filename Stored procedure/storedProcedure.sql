CREATE PROCEDURE GetRevenue
AS
SELECT payment_method FROM account
GO;


#Account table nodig, niet de subscription table nodig. 
#In de account moeten kijken welke subscription diegene heeft, waarna je dit op telt. Daarna ga je dat x de prijzen doen.
