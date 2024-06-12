WITH account_balances AS (
    SELECT
        account_id,
        SUM(transaction_amount) AS total_transactions
    FROM {{ ref('fact_transactions') }}
    GROUP BY account_id
),

exceeding_transactions AS (
    SELECT
        t.transaction_id,
        t.account_id,
        t.transaction_amount,
        ab.total_transactions
    FROM {{ ref('fact_transactions') }} AS t
    LEFT JOIN account_balances AS ab ON t.account_id = ab.account_id
    LEFT JOIN {{ ref('dim_account') }} AS a ON t.account_id = a.account_id
    WHERE t.transaction_amount + ab.total_transactions > a.account_balance
)

SELECT
    transaction_id,
    account_id,
    transaction_amount,
    total_transactions
FROM exceeding_transactions
WHERE total_transactions IS null
