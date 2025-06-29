# 📏 Sharp Curve Detector

A simple Python tool for detecting sharp curves from road centerline survey data.

# Sharp Curve Detector

一個用 Python 實現的道路中心線急彎偵測工具（依外接圓半徑）。

## 功能
- 從 Excel 讀取每公尺樁位的 X、Y 座標
- 依照三點外接圓計算半徑
- 找出半徑小於 50 公尺的三點組合
- 合併連續的急彎段
- 輸出結果為 Excel

## 安裝
```bash
pip install -r requirements.txt
---

## 🚧 Features

✅ Read road centerline coordinates from an Excel file (station, X, Y)  
✅ Calculate circle radius using any 3 consecutive points  
✅ Flag segments with radius < 50m  
✅ Merge continuous sharp curve segments into longer sections  
✅ Export results to Excel for reporting and mapping

---

## 📂 Folder Structure

sharp-curve-detector/
├── sharp_curve.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── examples/
└── tests/


- **sharp_curve.py** : Main script.
- **requirements.txt** : Dependencies.
- **examples/** : Example input files.


---

## 🗂️ Input File Format

Your input `.xlsx` must contain **3 columns**:
- `Station` — chainage or stake number
- `X` — X coordinate
- `Y` — Y coordinate

Example:
| Station | X       | Y       |
|---------|---------|---------|
| 0       | 120.123 | 23.456  |
| 1       | 120.124 | 23.457  |
| ...     | ...     | ...     |

---

## ⚙️ Install

1️⃣ Clone this repository  
```bash
git clone https://github.com/YOUR_USERNAME/sharp-curve-detector.git
cd sharp-curve-detector

pip install -r requirements.txt

python sharp_curve.py --input path/to/your_input.xlsx --output path/to/output.xlsx
Parameters:

--input : Path to your input Excel file
--output : Optional. Path to save the output Excel. Default: sharp_curves_output.xlsx

python sharp_curve.py --input examples/sample_input.xlsx --output sharp_curves_output.xlsx
