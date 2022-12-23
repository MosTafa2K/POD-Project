import os
import cv2
from Core.yolov7 import YOLOv7
from cap_from_youtube import cap_from_youtube


def image_detection(from_path: str, from_url: str = None):
    # Initialize yolov7 object detector
    model_path = "../models/yolov7_736x1280.onnx"
    yolov7_detector = YOLOv7(model_path, conf_thres=0.2, iou_thres=0.3)
    # Read image
    if from_url is not None:
        img = from_url
    else:
        img = cv2.imread(from_path)

    img_name = os.path.split(from_path)[1]
    # Detect Objects
    boxes, scores, class_ids = yolov7_detector(img)

    # Draw detections
    combined_img = yolov7_detector.draw_detections(img)
    cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
    cv2.imshow("Detected Objects", combined_img)
    cv2.imwrite(f"./Output/out_images/detected_{img_name}", combined_img)
    cv2.waitKey(0)


def video_detection(from_path: str = None, from_url: str = None):
    if from_url is not None:
        cap_url = cap_from_youtube(from_url)
        start_time = 0  # skip first {start_time} seconds
        cap_url.set(cv2.CAP_PROP_POS_FRAMES, start_time * 30)

        # out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (1280, 720))

        # Initialize YOLOv7 model
        model_path = "../models/yolov7_384x640.onnx"
        yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)

        cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
        while cap_url.isOpened():

            # Press key q to stop
            if cv2.waitKey(1) == ord('q'):
                break

            try:
                # Read frame from the video
                ret, frame = cap_url.read()
                if not ret:
                    break
            except Exception as e:
                print(e)
                continue

            # Update object localizer
            boxes, scores, class_ids = yolov7_detector(frame)

            combined_img = yolov7_detector.draw_detections(frame)
            cv2.imshow("Detected Objects", combined_img)

    elif from_path is not None:
        cap_video = cv2.VideoCapture(from_path)
        start_time = 0
        cap_video.set(cv2.CAP_PROP_POS_FRAMES, start_time * 30)
        cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
        model_path = "../models/yolov7_384x640.onnx"
        yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)

        while cap_video.isOpened():

            if cv2.waitKey(1) == ord('q'):
                break

            try:
                # Read frame from the video
                ret, frame = cap_video.read()
                if not ret:
                    break
            except Exception as e:
                print(e)
                continue

            boxes, scores, class_ids = yolov7_detector(frame)
            combined_img = yolov7_detector.draw_detections(frame)
            cv2.imshow("Detected Objects", combined_img)


def webcam_detection():
    cap_webcam = cv2.VideoCapture(0)
    # Initialize YOLOv7 object detector
    model_path = "../models/yolov7_384x640.onnx"
    yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)

    cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
    while cap_webcam.isOpened():

        # Read frame from the video
        ret, frame = cap_webcam.read()

        if not ret:
            break

        # Update object localizer
        boxes, scores, class_ids = yolov7_detector(frame)

        combined_img = yolov7_detector.draw_detections(frame)
        cv2.imshow("Detected Objects", combined_img)

        # Press key q to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main():
    """ Put your codes here """


if __name__ == "__main__":
    main()
