SELECT ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Margin_Pct,
    COUNT(DISTINCT "Order ID") AS Total_Orders,
    COUNT(DISTINCT "Customer ID") AS Total_Customers
FROM Superstore;

SELECT Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM Superstore
GROUP BY Region
ORDER BY Total_Profit DESC;

SELECT
  "Sub-Category",
  ROUND(SUM(Sales), 2)   AS Total_Sales,
  ROUND(SUM(Profit), 2)  AS Total_Profit
FROM Superstore
GROUP BY "Sub-Category"
ORDER BY Total_Profit ASC;

SELECT
  CASE
    WHEN Discount = 0      THEN '0% No Discount'
    WHEN Discount <= 0.2   THEN '1-20%'
    WHEN Discount <= 0.4   THEN '21-40%'
    WHEN Discount <= 0.6   THEN '41-60%'
    ELSE '60%+ Deep'
  END AS Discount_Band,
  COUNT(*) AS Orders,
  ROUND(AVG(Profit), 2) AS Avg_Profit,
  ROUND(SUM(Profit), 2) AS Total_Profit
FROM Superstore
GROUP BY Discount_Band
ORDER BY Discount_Band;

SELECT
  "Customer Name",
  Segment,
  Region,
  ROUND(SUM(Sales), 2)  AS Total_Sales,
  ROUND(SUM(Profit), 2) AS Total_Profit
FROM Superstore
GROUP BY "Customer Name"
ORDER BY Total_Profit DESC
LIMIT 10;