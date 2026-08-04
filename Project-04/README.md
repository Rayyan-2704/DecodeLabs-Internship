# Project 04: OCR Text Recognition

**DecodeLabs Internship — Project 04**
**Author:** Rayyan Aamir

## Description

An end-to-end Optical Character Recognition (OCR) pipeline built with **OpenCV** and **Tesseract**. The script preprocesses an input image (grayscale conversion, Gaussian blur, adaptive thresholding), extracts text using Tesseract, benchmarks each detection against an **80% confidence threshold**, and visualizes the results by drawing labeled bounding boxes around passing detections.

## Features

- Image preprocessing pipeline: grayscale → Gaussian blur → adaptive thresholding, to improve OCR accuracy on varied lighting/backgrounds
- Text extraction with per-word confidence scores via `pytesseract.image_to_data`
- Confidence benchmarking — detections are flagged **PASSED** (≥ 80% confidence) or **FAILED** (< 80%)
- Bounding-box visualization with detected text and confidence percentage overlaid on the image
- Console table summarizing detected text, confidence score, and pass/fail status

## How It Works

1. **Setup Check** — Verifies Tesseract is installed and accessible on the system `PATH`.
2. **Image Loading** — Reads `sample.jpg` and converts it to RGB for display/annotation.
3. **Preprocessing** — Converts to grayscale, applies Gaussian blur to reduce noise, then adaptive thresholding to binarize the image for cleaner text edges.
4. **OCR Extraction** — Runs Tesseract on the preprocessed image, retrieving per-word text, confidence scores, and bounding box coordinates.
5. **Confidence Filtering** — Each detected word is checked against an 80% confidence threshold; passing words get a green bounding box and label drawn on the original image.
6. **Output** — Prints a formatted table of all detections and displays the preprocessed and final annotated images.

## Requirements

```
opencv-python>=4.8.0
pytesseract>=0.3.10
numpy>=1.24.0
Pillow>=9.5.0
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

You'll also need the **Tesseract OCR engine** installed separately (it's a system binary, not a Python package):

- **Windows/macOS/Linux:** [Tesseract installation guide](https://github.com/tesseract-ocr/tesseract#installing-tesseract)
- Make sure `tesseract` is available on your system `PATH`

> **Note:** The original script was written in Google Colab and uses `google.colab.patches.cv2_imshow` for displaying images. To run it locally, replace `cv2_imshow(...)` calls with `cv2.imshow(...)` (plus `cv2.waitKey(0)` and `cv2.destroyAllWindows()`), since `cv2_imshow` is only available in the Colab environment.

## Usage

Run the script from the terminal (with `sample.jpg` in the same directory):

```bash
python OCR-text-recognition.py
```

Or open and run the notebook version:

```
OCR-Text-Recognition.ipynb
```

Example console output:

```
Tesseract found at: /usr/bin/tesseract
Connection was successful

=================================================================
Detected Text            | Confidence Score   | Status
=================================================================
Hello                    |             94.32% | PASSED
World                    |             88.71% | PASSED
smudged                  |             42.10% | FAILED (<80%)
=================================================================

--- Pre-processed (Adaptive Threshold) Image ---
--- Final Visual Confirmation (Resized Output) ---
```

## Project Structure

```
Project-04/
├── OCR-Text-Recognition.ipynb
├── OCR-text-recognition.py
├── sample.jpg
└── requirements.txt
```

## Possible Improvements

- Support batch processing of multiple images instead of a single hardcoded file
- Make the image path and confidence threshold configurable via command-line arguments
- Add adaptive preprocessing parameters (auto-tune blur/threshold based on image characteristics)
- Export detected text and results to a structured file (CSV/JSON) in addition to console output
- Replace Colab-specific `cv2_imshow` calls with a cross-platform display/save method for local runs