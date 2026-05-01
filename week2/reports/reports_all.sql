SELECT * FROM Applications WHERE category = "Development";

SELECT * FROM Vendors ORDER BY country ASC;

SELECT Applications.app_name,Vendors.vendor_name FROM Applications INNER JOIN Vendors ON Applications.vendor_id = Vendors.vendor_id;

SELECT Applications.app_name FROM Applications INNER JOIN Licenses ON Applications.app_id = Licenses.app_id WHERE Licenses.is_active = 0;

UPDATE Vendors SET country = "Germany" WHERE vendor_id = 2;
SELECT vendor_name,country FROM Vendors