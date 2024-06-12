{{
    config(
        materialized='incremental',
        alias='stg_dim_currency',
        schema=var('silver_schema'),
        unique_key='currency_id',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    currency_id,
    currency_code,
    currency_name,
    GETDATE() as created_at
FROM
    {{ var('bronze_schema') }}.ext_currencies