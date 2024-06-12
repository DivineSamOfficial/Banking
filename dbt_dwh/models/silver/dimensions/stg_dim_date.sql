{{
    config(
        materialized='incremental',
        alias='stg_dim_dates',
        schema=var('silver_schema'),
        unique_key='date_id',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    date_id,
    date,
    day,
    month,
    year,
    week_day,
    GETDATE() as created_at
FROM
    {{ var('bronze_schema') }}.ext_dates