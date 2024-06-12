SELECT
    transaction_id,
    transaction_amount
FROM {{ ref('fact_transactions') }}
WHERE transaction_amount < 0
