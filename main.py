import cv2
import numpy as np

# Function to check if a Pokémon is shiny based on RGB values
def is_shiny(rgb_value):
    # Define the RGB range for shiny detection (adjust these values as needed)
    shiny_lower_bound = np.array([200, 100, 100])  # Example lower bound
    shiny_upper_bound = np.array([255, 255, 255])  # Example upper bound

    # Check if the RGB value is within the shiny range
    return np.all(rgb_value >= shiny_lower_bound) and np.all(rgb_value <= shiny_upper_bound)

def main():
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Define the ROI (Region of Interest) where the Pokémon appears
        # Adjust these coordinates based on your setup
        roi_x, roi_y, roi_width, roi_height = 300, 200, 100, 100
        roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

        # Check the average color in the ROI
        average_color = cv2.mean(roi)[:3]  # Get RGB values

        # Check if the Pokémon is shiny
        if is_shiny(average_color):
            print("Shiny Pokémon detected!")
            # Add actions for when a shiny is detected here

        # Display the frame with the ROI rectangle
        cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)
        cv2.imshow("Webcam Feed", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
