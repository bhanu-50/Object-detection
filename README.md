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

** 📦 yolo-fastapi-detection**
│
├── app.py                 # Main FastAPI application
├── requirements.txt       # Project dependencies
├── output/                # Folder to save annotated images
├── test_images/           # Sample input images
├── README.md              # Documentation
└── demo_video.mp4         # (Optional) short demo recording

