
SELECT
    ProductCode AS Product_Code,
    AVG(T_Height) AS Mean_Height,
    STDEV(T_Height) AS StdDev_Height,
    AVG(T_Weight) AS Mean_Weight,
    STDEV(T_Weight) AS StdDev_Weight
FROM
    Book1
    GROUP BY ProductCode