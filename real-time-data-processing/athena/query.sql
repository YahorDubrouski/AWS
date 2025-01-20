SELECT 
    array_item.action, 
    count(array_item.action) as count
FROM yahor_dubrouski_practice_kinesis_processed_data
CROSS JOIN UNNEST(array) AS t(array_item)
GROUP BY array_item.action
