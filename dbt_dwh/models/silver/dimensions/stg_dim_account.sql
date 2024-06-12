{{
    config(
        materialized='incremental',
        alias='stg_dim_account',
        schema=var('silver_schema'),
        unique_key='account_id',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    account_id,
    customer_id,
    account_number,
    account_type,
    account_balance,
    credit_score,
    getdate() as created_at
FROM
    {{ var('bronze_schema') }}.ext_accounts
