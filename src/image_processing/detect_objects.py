from ultralytics import YOLO
import os
import psycopg2

# Path to folder with images (adjust if needed)
IMAGE_FOLDER = r'C:\Users\hp\OneDrive\Documents\10 Academy\week-7\telegram-medical-analytics-pipeline\data\raw\telegram_data'


# Initialize YOLOv8 model (pre-trained)
model = YOLO('yolov8n.pt')  # adjust path if model is not in working directory

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="telegramdb",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()


def detect_and_store():
    total_files_processed = 0
    total_detections_inserted = 0

    for root, _, files in os.walk(IMAGE_FOLDER):
        print(f"Scanning folder: {root}")
        print(f"{len(files)} files found")

        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                total_files_processed += 1

                image_path = os.path.join(root, file)
                print(f"\n Processing Image: {image_path}")

                # Run detection
                results = model(image_path)

                detections_in_image = 0

                for result in results:
                    boxes = result.boxes
                    if boxes is None or len(boxes) == 0:
                        print(" No objects detected.")
                        continue

                    for box in boxes:
                        cls_idx = int(box.cls[0])
                        cls_name = model.names[cls_idx]
                        conf_score = float(box.conf[0])

                        # Extract message_id from filename (format: channelname_messageid.jpg)
                        try:
                            message_id = int(file.split('_')[-1].split('.')[0])
                        except Exception as e:
                            print(f" Error parsing message_id from {file}: {e}")
                            continue

                        # Insert detection into DB
                        cursor.execute("""
                            INSERT INTO fct_image_detections (message_id, detected_object_class, confidence_score)
                            VALUES (%s, %s, %s);
                        """, (message_id, cls_name, conf_score))

                        detections_in_image += 1
                        total_detections_inserted += 1

                        print(f" Inserted: message_id={message_id} | class={cls_name} | conf={conf_score:.2f}")

                conn.commit()

                if detections_in_image == 0:
                    print("⚠️ Image processed but no detections saved.")

    print(f"\n Summary:")
    print(f"   Total Images Processed: {total_files_processed}")
    print(f"   Total Detections Inserted: {total_detections_inserted}")


if __name__ == "__main__":
    detect_and_store()
    cursor.close()
    conn.close()
    print("\n Detection complete and stored in database.")
