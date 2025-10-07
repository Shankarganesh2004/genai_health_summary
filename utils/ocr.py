import re
import pytesseract
from PIL import Image
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_from_image(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    lines = text.split("\n")
    data = {}

    for line in lines:
        if "Hemoglobin" in line:
            match = re.search(r"[-+]?\d*\.\d+|\d+", line)
            if match:
                data["Hemoglobin (g/dL)"] = float(match.group())
        # Add more mappings using the same pattern:
        elif "Glucose" in line:
            match = re.search(r"[-+]?\d*\.\d+|\d+", line)
            if match:
                data["Glucose (mg/dL)"] = float(match.group())
        elif "HbA1c" in line:
            match = re.search(r"[-+]?\d*\.\d+|\d+", line)
            if match:
                data["HbA1c (%)"] = float(match.group())
        elif "ALT" in line:
            match = re.search(r"[-+]?\d*\.\d+|\d+", line)
            if match:
                data["ALT (U/L)"] = float(match.group())
        elif "Platelets" in line:
            match = re.search(r"[-+]?\d*\.\d+|\d+", line.replace(",", ""))
            if match:
                data["Platelets (10^3/L)"] = float(match.group())

    return pd.DataFrame([data])