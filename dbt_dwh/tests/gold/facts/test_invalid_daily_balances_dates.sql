WITH invalid_dates AS (
    SELECT
        f.balance_id,
        f.date_id
    FROM {{ ref('fact_daily_balances') }} AS f
    LEFT JOIN {{ ref('dim_date') }} AS d ON f.date_id = d.date_id
    WHERE d.date_id IS NULL
)

SELECT
    balance_id,
    date_id
FROM invalid_dates
