SELECT
    message_id,
    detected_object_class,
    confidence_score
FROM {{ ref('stg_image_detections') }}
