
from object_detection.yolo_detect import detect_objects
from path_planning.a_star_navigation import a_star
from behavior_prediction.lstm_predictor import LSTMBehaviorPredictor
from ui_interface.voice_control import listen_command

def main():
    print("Autonomous System Starting...")
    # Loop for simulation
    while True:
        cmd = listen_command()
        if "stop" in cmd:
            print("Emergency stop activated.")
            break
        print("Listening and analyzing environment...")
        # Process environment, update path, detect objects
        # Update GUI or UI here

if __name__ == "__main__":
    main()
