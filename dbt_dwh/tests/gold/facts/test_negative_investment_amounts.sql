SELECT
    investment_id,
    investment_amount
FROM {{ ref('fact_investments') }}
WHERE investment_amount < 0
