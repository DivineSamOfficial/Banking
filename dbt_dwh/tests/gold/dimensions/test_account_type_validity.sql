SELECT
    account_id,
    account_type
FROM {{ ref('dim_account')}}
where account_type not in ('Savings', 'Checking', 'Investment', 'Loan')