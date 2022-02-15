import cv2

# tracker = cv2.TrackerKCF_create()
tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture("street.mp4")

ok, frame = video.read()

bbox = cv2.selectROI(frame)

tracker.init(frame, bbox)

while True:
    ok, frame = video.read()
    if not ok:
        break
    _, bbox = tracker.update(frame)
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Error", (100, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
