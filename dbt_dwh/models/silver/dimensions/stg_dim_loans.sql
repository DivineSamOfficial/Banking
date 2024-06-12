{{
    config(
        materialized='incremental',
        alias='stg_dim_loans',
        schema=var('silver_schema'),
        unique_key='loan_id',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    loan_id,
    loan_type,
    GETDATE() as created_at
FROM
    {{ var('bronze_schema') }}.ext_loans