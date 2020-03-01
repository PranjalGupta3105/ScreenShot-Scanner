import cv2
import io
import os
import os.path
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

img = ''

def settingImagePath(imageLoc):
    img = cv2.imread(imageLoc)
    return img

def image_ocr(image_path, output_txt_file_name):
  if os.path.isfile(image_path):
    os.remove(image_path)
  else:
    image_text = pytesseract.image_to_string(image_path, lang='eng', config=tessdata_dir_config)
    with io.open(output_txt_file_name, 'w+', encoding='utf-8') as f:
      f.write(image_text)

