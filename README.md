# EEG Data Recorder & Image Prompt Generator

This repository contains two independent programs:

1. **EEG Data Recorder and Real-Time Band Power Calculator** (`UnicornHybridBlack_DataRecorder.py`)
2. **Adjective-Based Image Prompt Generator** (`image_generator.py`)

---

## Program 1: EEG Data Recorder and Real-Time Band Power Calculator

### Filename: `UnicornHybridBlack_DataRecorder.py`

### Overview
This Python program captures EEG data from the Unicorn Hybrid Black device and performs real-time band power calculations. The data is saved directly to a CSV file and preprocessed using digital filters. It is designed for EEG data analysis and concentration tracking based on brainwave frequency bands.

### Features
- **Data Streaming and Saving**: Captures data from the Unicorn Hybrid Black device and saves it in a CSV file.
- **Real-Time Band Power Calculation**: Calculates delta, theta, alpha, beta, and gamma power using a sliding window.
- **Digital Filtering**: Applies notch, low-pass, and high-pass filters to preprocess EEG data.
- **Concentration Index Calculation**: Computes a concentration index based on band power values.

### Requirements
- Python 3.x
- Libraries: `pylsl`, `pandas`, `numpy`, `scipy`, `keyboard`

### Installation
1. Install the necessary dependencies:
   ```bash
   pip install pylsl pandas numpy scipy keyboard
   ```
2. Connect the Unicorn Hybrid Black EEG device to your computer.

### Usage
1. Run the program:
   ```bash
   python UnicornHybridBlack_DataRecorder.py
   ```
2. Press the `s` key to start a 5-second data recording.
3. Press the `esc` key to stop recording and save the data to `EEGdataTest4.csv`.

### How It Works
- **Filters**: Notch filter at 60Hz, low-pass filter at 50Hz, and high-pass filter at 0.5Hz are applied to the data.
- **Sliding Window**: Data is analyzed in a windowed format for real-time processing.
- **Band Power**: Power in each EEG band is calculated and used to compute a concentration index.

### Disclaimer
This program is provided as-is without any guarantees regarding its accuracy or reliability for clinical or diagnostic purposes.

---

## Program 2: Adjective-Based Image Prompt Generator

### Filename: `image_generator.py`

### Overview
This Python script reads data from an Excel file, calculates mean values for specific columns, and maps these to adjective pairs. Based on the average values, it generates a prompt for creating a painting using Stability AI's image generation API.

### Features
- **Excel Data Analysis**: Reads values from an Excel file, calculates mean values, and selects adjectives based on those values.
- **Dynamic Prompt Generation**: Builds an image prompt with adjectives representing warmth, setting, tone, and scene.
- **Image Generation**: Sends the prompt to Stability AI's text-to-image API to generate a painting.

### Requirements
- Python 3.x
- Libraries: `pandas`, `requests`

### Installation
1. Install the necessary dependencies:
   ```bash
   pip install pandas requests
   ```
2. Ensure your Excel data file is named `EXCELFILE.xlsx` and contains columns `A` to `H`.
3. Obtain an API key from Stability AI and replace `'YOUR-API-KEY'` in the script with your API key.

### Usage
1. Run the script:
   ```bash
   python image_generator.py
   ```
2. The script will:
   - Read data from the Excel file.
   - Generate a prompt based on the adjective pairs.
   - Send the prompt to the Stability AI API and save the generated image as `generated_image_0.png`.

### Example Prompt
The generated prompt might look like:
```
Generate a painting using a warm color palette, depicting a rural landscape with peaceful undertones, where a heartwarming scene between a young couple is taking place.
```

### Notes
- Ensure that your API key is securely stored and avoid sharing it publicly.
- The script requires an active internet connection to access Stability AI's API.

---
