{{
    config(
        materialized='incremental',
        alias='stg_dim_location',
        schema=var('silver_schema'),
        unique_key='location_id',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    location_id,	
    city,
    state,
    country,	
    postal_code,
    GETDATE() as created_at
FROM
    {{ var('bronze_schema') }}.ext_locations