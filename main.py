from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image
from datetime import datetime
import io
import os

app = FastAPI()
model = YOLO("yolov8n.pt")


@app.post("/detect")
async def detect_object(file: UploadFile = File(...)):
    # Read image bytes
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes))

    # Run YOLOv8 inference
    results = model(img)

    detections = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            bbox = box.xyxy[0].tolist()
            detections.append({
                "class": model.names[cls_id],
                "confidence": round(conf, 3),
                "bbox": [round(x, 2) for x in bbox]
            })

    # Save annotated image with timestamp in output folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"output_{timestamp}.jpg"
    output_path = os.path.join("output", output_filename)
    
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    
    results[0].save(filename=output_path)
    return {"detections": detections, "saved_image": output_path}
