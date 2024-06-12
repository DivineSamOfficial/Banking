WITH customer_behavior as (
    SELECT
        account_number,
        count(transaction_id) as num_transactions,
        avg(transaction_amount) as avg_transaction_amount
    FROM {{ ref('fact_transactions') }}
    group by account_number
)

SELECT
    cb.account_number,
    cb.num_transactions,
    cb.avg_transaction_amount,
    CASE
        WHEN cb.avg_transaction_amount > 5000 THEN 'High'
        WHEN cb.avg_transaction_amount between 4000 and 5000 THEN 'Medium'
        ELSE 'Low'
    END as customer_segment
FROM customer_behavior cb