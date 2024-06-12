WITH orphaned_transactions AS (
    SELECT f.transaction_id
    FROM {{ ref('fact_transactions') }} AS f
    LEFT JOIN {{ ref('dim_account') }} AS a ON f.account_id = a.account_id
    WHERE a.account_id IS NULL
)

SELECT transaction_id
FROM orphaned_transactions
