import pandas as pd
import numpy as np
from math import sqrt
import argparse

def compute_radius(x1, y1, x2, y2, x3, y3):
    try:
        a = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        b = sqrt((x3 - x2)**2 + (y3 - y2)**2)
        c = sqrt((x1 - x3)**2 + (y1 - y3)**2)
        s = (a + b + c) / 2
        area = sqrt(abs(s * (s - a) * (s - b) * (s - c)))
        if area == 0:
            return np.nan
        R = (a * b * c) / (4 * area)
        return R
    except:
        return np.nan

def main(input_file, output_file):
    df = pd.read_excel(input_file)

    stations = df['Station'].values
    x = df['X'].values
    y = df['Y'].values

    triplets = []
    for i in range(len(df) - 2):
        R = compute_radius(x[i], y[i], x[i+1], y[i+1], x[i+2], y[i+2])
        if not np.isnan(R) and R < 50:
            triplets.append({
                'start_idx': i,
                'mid_idx': i+1,
                'end_idx': i+2,
                'Station_start': stations[i],
                'Station_mid': stations[i+1],
                'Station_end': stations[i+2],
                'Radius_m': round(R, 2)
            })

    merged_segments = []
    if triplets:
        current = [triplets[0]]
        for t in triplets[1:]:
            if t['start_idx'] <= current[-1]['end_idx']:
                current.append(t)
            else:
                merged_segments.append({
                    'Start_Station': current[0]['Station_start'],
                    'End_Station': current[-1]['Station_end'],
                    'Start_Index': current[0]['start_idx'],
                    'End_Index': current[-1]['end_idx'],
                    'Num_Triplets': len(current),
                    'Avg_Radius': round(np.mean([c['Radius_m'] for c in current]), 2),
                    'Min_Radius': round(min([c['Radius_m'] for c in current]), 2),
                    'Total_Length_m': round(
                        sqrt((x[current[-1]['end_idx']] - x[current[0]['start_idx']])**2 +
                             (y[current[-1]['end_idx']] - y[current[0]['start_idx']])**2), 2)
                })
                current = [t]
        merged_segments.append({
            'Start_Station': current[0]['Station_start'],
            'End_Station': current[-1]['Station_end'],
            'Start_Index': current[0]['start_idx'],
            'End_Index': current[-1]['end_idx'],
            'Num_Triplets': len(current),
            'Avg_Radius': round(np.mean([c['Radius_m'] for c in current]), 2),
            'Min_Radius': round(min([c['Radius_m'] for c in current]), 2),
            'Total_Length_m': round(
                sqrt((x[current[-1]['end_idx']] - x[current[0]['start_idx']])**2 +
                     (y[current[-1]['end_idx']] - y[current[0]['start_idx']])**2), 2)
        })

    merged_df = pd.DataFrame(merged_segments)
    merged_df.to_excel(output_file, index=False)

    print(f"找到 {len(triplets)} 組急彎，合併為 {len(merged_segments)} 段")
    print(f"結果已輸出至：{output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Detect sharp curves in road centerline data.")
    parser.add_argument('--input', required=True, help='Path to input Excel file.')
    parser.add_argument('--output', default='sharp_curves_output.xlsx', help='Path to output Excel file.')
    args = parser.parse_args()
    main(args.input, args.output)
