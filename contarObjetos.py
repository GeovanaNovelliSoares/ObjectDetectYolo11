from ultralytics import YOLO
from ultralytics import solutions
import cv2
 
cap = cv2.VideoCapture("C:\\Users\\genov\\Documents\\vecteezy_turkey-istanbul-12-january-2023-traffic-in-a-high-away-in_24222097.mp4")

assert cap.isOpened(), "Erro ao ler o video"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define as regioes dos pontos
region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]  


# Video writer
video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))


counter = solutions.ObjectCounter(
    show=True,  # Onde vai ser a saida do video
    region=region_points,  # os pontos e regioes para carregar
    model="yolo11n.pt",  #modelo que foi utilizado e carregado
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video completo com sucesso")
        break
    im0 = counter.count(im0)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()

