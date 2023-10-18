import cv2 as cv
import flask as f

app = f.Flask(__name__, template_folder='templates', static_folder='static')

def generator(video=0):
    cap = cv.VideoCapture(video)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv.imencode('.jpg', frame)[1].tobytes()
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'

@app.route('/')
def index():
    return f.Response(generator(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
