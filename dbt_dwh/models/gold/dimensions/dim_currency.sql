{{
    config(
        materialized='incremental',
        alias='dim_currency',
        schema=var('gold_schema'),
        unique_key='currency_id',
        incremental_stragey='delete+insert'
    )
}}

SELECT
    currency_id,
    created_at,
    UPPER(currency_code) as currency_code,
    INITCAP(currency_name) as currency_name
FROM
    {{ ref('stg_dim_currency') }}

{% if is_incremental() %}
    WHERE created_at > (SELECT MAX(created_at) FROM {{ this}})
{% endif %}