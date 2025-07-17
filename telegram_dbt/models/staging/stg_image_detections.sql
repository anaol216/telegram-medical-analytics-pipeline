SELECT
    id,
    message_id,
    detected_object_class,
    confidence_score
FROM {{ source('public', 'raw_image_detections') }}
