**🧠 YOLOv8 Object Detection API (FastAPI)**

        This project demonstrates a simple object detection pipeline using YOLOv8 and FastAPI.
        It allows you to upload an image through an API endpoint (/detect) and returns:
        
        Detected object classes
        
        Confidence scores
        
        Bounding box coordinates
        
        Path of the saved output image (with bounding boxes drawn)

**🎯 Project Objective**

        Use a pretrained YOLOv8 model (yolov8n.pt)
        
        Run inference on uploaded images
        
        Save annotated output images with bounding boxes
        
        Expose results through a FastAPI endpoint (/detect)

        Return detections as structured JSON output


**✅ requirements.txt**

        fastapi==0.115.0
        uvicorn==0.30.1
        ultralytics==8.3.12
        pillow==10.4.0
        numpy==1.26.4

**🚀 Run the Application**

        Start the FastAPI server:

        uvicorn app:app --reload

Now open your browser at:
**👉 http://127.0.0.1:8000/docs**

You’ll see the interactive Swagger UI, where you can upload images and view JSON responses.

**🧠 API Endpoint Details**
        POST /detect
        
        Description:
        Upload an image file and get detected objects with bounding boxes and confidence scores.

**✅ Example JSON Response**

{
  "detections": [
    {
      "class": "person",
      "confidence": 0.92,
      "bbox": [120.0, 50.0, 300.0, 400.0]
    },
    {
      "class": "car",
      "confidence": 0.85,
      "bbox": [450.0, 120.0, 620.0, 360.0]
    }
  ],
  "saved_image": "output/output_20251017_093012.jpg"
}

**🎥 Demo Video**

        A short demo video (demo_video.mp4) is included to show:
        
        FastAPI server running locally
        
        Image upload through Swagger UI
        
        JSON response + saved annotated image
        
                
