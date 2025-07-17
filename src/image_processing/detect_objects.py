from ultralytics import YOLO
import os
import psycopg2

# Path to folder with images
IMAGE_FOLDER = './data/raw/telegram_data/'

# Initialize YOLOv8 model (pre-trained)
model = YOLO('yolov8n.pt')  # use 'yolov8n.pt' for the nano model (lightweight)

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
    for root, _, files in os.walk(IMAGE_FOLDER):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file)
                print(f"Processing: {image_path}")
                
                # Run detection
                results = model(image_path)
                
                # Parse results for each detected object
                for result in results:
                    for box in result.boxes:
                        cls = model.names[int(box.cls[0])]
                        conf = float(box.conf[0])
                        
                        # Extract message_id from filename (example: lobelia4cosmetics_18600.jpg)
                        message_id = int(file.split('_')[-1].split('.')[0])
                        
                        # Insert detection into DB (adjust table/columns as per your schema)
                        cursor.execute("""
                            INSERT INTO fct_image_detections (message_id, detected_object_class, confidence_score)
                            VALUES (%s, %s, %s)
                            ON CONFLICT DO NOTHING;
                        """, (message_id, cls, conf))
                
                conn.commit()

if __name__ == "__main__":
    detect_and_store()
    cursor.close()
    conn.close()
    print("✅ Detection complete and stored in database.")
