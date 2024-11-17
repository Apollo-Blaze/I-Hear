# I Hear

**I Hear** is a gesture-based system volume controller that uses hand gestures to adjust the audio levels dynamically. By measuring the distance between the index finger and thumb through computer vision techniques, this project offers an innovative and interactive way to control your system's sound.

## Features
- Tracks the position of your hand in real time using a webcam.
- Adjusts system volume based on the distance between your index finger and thumb.
- Provides visual feedback for gestures and current volume levels.
- Reacts to gestures such as muting when the fingers are brought close together.

## How It Works
1. **Hand Detection**: Uses MediaPipe's Hand Tracking module to detect and track hand landmarks.
2. **Distance Measurement**: Calculates the distance between the tips of the index finger and thumb.
3. **Volume Adjustment**: Maps the measured distance to the system's volume range and updates the audio levels.
4. **Visual Cues**:
   - Displays a line and circles connecting the detected landmarks.
   - Includes a dynamic volume bar and percentage for volume indication.
   - Changes circle color when muting is activated.

## Visual Feedback
- **Volume Bar**: A visual bar on the screen shows the current volume level.
- **Percentage Indicator**: Displays the current volume as a percentage below the bar.
- **Gesture Interaction**:
  - Green lines and circles show active gesture detection.
  - A red circle indicates that the volume is muted.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - OpenCV: For image processing.
  - MediaPipe: For hand landmark detection.
  - Pycaw: For managing system audio levels.
  - NumPy: For efficient numerical operations.
  - Math: For calculating distances between landmarks.

## Acknowledgments
- **MediaPipe**: For enabling accurate and robust hand tracking.
- **Pycaw**: For providing seamless control of system audio.
- **OpenCV**: For efficient real-time video processing.

---
