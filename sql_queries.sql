-- Q1: Show all orders where the food item is exactly 'Dal Makhani'

SELECT * FROM 
FOOD_ORDERS
WHERE FOOD_ITEM = 'Dal Makhani';


-- Q2: What is the highest order amount placed?

SELECT MAX(ORDER_AMOUNT) HIGHEST_ORDER_AMOUNT 
FROM FOOD_ORDERS;


-- Q3: 🍽️ How many times was each food item ordered?

SELECT FOOD_ITEM , COUNT(*) NO_TIMES_ORDERED
FROM FOOD_ORDERS
GROUP BY FOOD_ITEM;

-- Q4: Which food items were ordered more than 10 times?

SELECT FOOD_ITEM , COUNT(*) NO_TIMES_ORDERED
FROM FOOD_ORDERS 
GROUP BY FOOD_ITEM
HAVING COUNT(*) > 1000;

-- Q: Add a new column called 'DELIVERY_REVIEW' that classifies each order as:
--    'Fast' if DELIVERY_TIME_MINS is less than 30,
--    'Normal' if between 30 and 90 (inclusive),
--    and 'Slow' otherwise.

SELECT 
  *,
  CASE 
    WHEN DELIVERY_TIME_MINS < 30 THEN 'Fast'
    WHEN DELIVERY_TIME_MINS BETWEEN 30 AND 90 THEN 'Normal'
    ELSE 'Slow'
  END AS DELIVERY_REVIEW
FROM FOOD_ORDERS;

-- Q6: Show only the distinct food items available in the dataset.
SELECT DISTINCT FOOD_ITEM
FROM FOOD_ORDERS;

-- Q7: Show all orders that do not have a delivery time recorded.

SELECT * 
FROM 
FOOD_ORDERS
WHERE DELIVERY_TIME_MINS IS NULL;


-- Q8: Display each order along with the rank based on order amount (highest = Rank 1).

SELECT 
*,
RANK() OVER(ORDER BY ORDER_AMOUNT DESC) ORDER_RANK
FROM FOOD_ORDERS;

--  Q9: Show the top 5 most expensive orders.


SELECT 
*
FROM FOOD_ORDERS
ORDER BY ORDER_AMOUNT DESC
LIMIT 5;

-- Q10 Show all orders where the food item contains the word 'Paneer'

SELECT * 
FROM FOOD_ORDERS
WHERE FOOD_ITEM LIKE "%Paneer%";
