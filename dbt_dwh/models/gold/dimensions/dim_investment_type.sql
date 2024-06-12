{{
    config(
        materialized='incremental',
        alias='dim_investment_type',
        schema=var('gold_schema'),
        unique_key='investment_type_id',
        incremental_stragey='delete+insert'
    )
}}

SELECT
    investment_type_id,
    INITCAP(investment_type_name) AS investment_type_name,
    created_at
FROM
    {{ ref('stg_dim_investment_type') }}

{% if is_incremental() %}
    WHERE created_at > (SELECT MAX(created_at) FROM {{ this}})
{% endif %}