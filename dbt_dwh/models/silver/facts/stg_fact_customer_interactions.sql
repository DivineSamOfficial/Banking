{{
    config(
        materialized='incremental',
        alias='stg_fact_customer_interactions',
        schema=var('silver_schema'),
        unique_key='interaction_id',
        incremental_strategy='delete+insert',
        primary_key='interaction_id',
        distribution='even'
    )
}}

SELECT
    interaction_id,	
    date_id,
    customer_id,
    channel_id,
    location_id,
    interaction_type,
    interaction_rating,
    GETDATE() as created_at
FROM
    {{ var('bronze_schema') }}.ext_fact_customer_interactions