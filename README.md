# 📏 Sharp Curve Detector

A simple Python tool for detecting sharp curves from road centerline survey data.

專案介紹

這是一套應用於台灣道路調查專案中道路急彎項目的工具，它可以提高承包商工作團隊效率與降低人工作業產生的錯誤。

一、專案背景與問題說明
在道路規劃、設計及後續維護管理階段，對於道路線形的安全性與舒適性分析極為重要。
傳統上，工程單位需依據測繪成果（如每公尺中心樁位座標）透過人工方式或半自動計算，判別急彎（小曲率半徑）路段，進行安全設計或改善。

此作業往往耗費大量時間與人力，易受人為計算疏失影響，且難以快速套用於大範圍路網或多期資料比對。

二、解決方案
本提案提出一套以 Python 實現的道路中心線急彎自動化偵測工具，採用連續三點外接圓半徑法，自動比對樁位座標資料，快速找出半徑小於特定閾值（如 50 公尺）的潛在急彎路段，並支援連續急彎區段自動合併輸出。

此工具具備以下特點：

自動化：減少人工作業，執行後自動輸出急彎段結果檔。
彈性化：可自定急彎曲率閾值、樁距精度與合併邏輯。
可擴充性：程式以開源 Python 撰寫，可依需要進一步串接 GIS、CAD 或其他交通設計工具。

三、適用場景
道路新建或拓寬工程之線形檢核
既有道路線形安全診斷與改善
案場測繪成果資料後端自動化處理
政府或顧問單位建立道路幾何特徵資料庫

四、預期效益
提升效率：作業時間大幅縮短，1 秒可完成人工數小時之檢核。
減少錯誤：降低人工作業疏失風險。
可追溯：以 Excel 或 GIS 直接比對輸出結果，利於後續驗證。
擴充彈性：後續可結合現有道路安全指標模型進行多元分析。

五、服務內容
提供急彎偵測工具程式（含原始碼與使用說明）
協助導入至使用者內部流程（如需）
客製化調整（如需特定格式輸入輸出、GIS 串接等）

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
- `Station` — chainage or stake number(道路中心線公尺樁) 
- `X` — X coordinate（坐標建議為TWD97 TM2）
- `Y` — Y coordinate（坐標建議為TWD97 TM2）

Example:
| Station | X       | Y       |
|---------|---------|---------|
| 0K+000  | 255999  | 2709999 |
| 0K+001  | 256000  | 2710000 |
| ...     | ...     | ...     |

## 👤 Author

[@alexintw](https://github.com/alexintw)

Feel free to open an issue or pull request!
---

## ⚙️ Install

1️⃣ Clone this repository  
```bash
git clone https://github.com/alexintw/sharp-curve-detector.git
cd sharp-curve-detector

pip install -r requirements.txt

python sharp_curve.py --input path/to/your_input.xlsx --output path/to/output.xlsx
Parameters:

--input : Path to your input Excel file
--output : Optional. Path to save the output Excel. Default: sharp_curves_output.xlsx

python sharp_curve.py --input examples/sample_input.xlsx --output sharp_curves_output.xlsx
