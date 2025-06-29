import os
import pandas as pd
import numpy as np
from sharp_curve import compute_radius, main

def test_compute_radius():
    # 三點在 (0,0), (1,0), (0,1) 外接圓半徑應該為 sqrt(2)/2 * sqrt(2) = sqrt(2)/2 * 2 = sqrt(2)
    # 其實是 0,0 1,0 0,1 為直角三角形 外接圓半徑是斜邊一半
    R = compute_radius(0, 0, 1, 0, 0, 1)
    expected = np.sqrt(2) / 2 * np.sqrt(2)  # = 1.0
    assert np.isclose(R, 1.0)

def test_main(tmp_path):
    # 建立假資料
    df = pd.DataFrame({
        'Station': [0, 1, 2, 3],
        'X': [0, 1, 0],
        'Y': [0, 0, 1, 2]
    })
    input_file = tmp_path / "input.xlsx"
    df.to_excel(input_file, index=False)

    # 執行主程式
    output_file = tmp_path / "output.xlsx"
    main(str(input_file), str(output_file))

    # 確認輸出檔存在
    assert output_file.exists()

    # 確認輸出檔有內容
    df_out = pd.read_excel(output_file)
    assert 'Start_Station' in df_out.columns
