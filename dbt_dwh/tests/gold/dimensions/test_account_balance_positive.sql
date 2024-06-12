SELECT account_id
FROM {{ ref('dim_account') }}
where account_balance < 0