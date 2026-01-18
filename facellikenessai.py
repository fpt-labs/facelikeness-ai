import os
import sys
import shutil
import pandas as pd
import numpy as np
import cv2

# --- TensorFlowの警告を完全に非表示にする ---
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

from deepface import DeepFace

# --- 1. ディレクトリ設定 ---
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DIR_REF      = os.path.join(BASE_DIR, "1比較基準画像")
DIR_INPUT    = os.path.join(BASE_DIR, "2解析したい画像")
DIR_LOW_SIM  = os.path.join(BASE_DIR, "3判定結果：低類似")
DIR_HIGH_SIM = os.path.join(BASE_DIR, "4判定結果：高類似")

# 神5モデル設定
GATEKEEPERS = ["Facenet512", "SFace"]
SCORERS = ["Facenet", "VGG-Face", "ArcFace"]

def setup_directories():
    for d in [DIR_REF, DIR_INPUT, DIR_LOW_SIM, DIR_HIGH_SIM]:
        if not os.path.exists(d): os.makedirs(d)

def load_img_jp(path):
    """日本語パス対応の画像読み込み"""
    return cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)

def get_similarity_score(distance, threshold):
    """人間感覚に合わせたスコア算出"""
    if distance <= threshold:
        return 100 - (40 * (distance / threshold))
    else:
        return max(0, 60 * (1 - (distance - threshold) / threshold))

def main():
    setup_directories()
    valid_exts = ('.jpg', '.jpeg', '.png', '.webp')
    
    targets = [f for f in os.listdir(DIR_REF) if f.lower().endswith(valid_exts)]
    others = [f for f in os.listdir(DIR_INPUT) if f.lower().endswith(valid_exts)]

    if not targets or not others:
        print(f"[-] Waiting: Target({len(targets)}) or Input({len(others)}) files missing.")
        return

    all_results_data = []
    print(f"\n--- FaceLikeness AI 複合判断スキャン ---")
    print(f"基準画像: {', '.join(targets)}")
    print(f"解析対象: {len(others)}枚\n")

    target_imgs = [load_img_jp(os.path.join(DIR_REF, t)) for t in targets]

    for img_name in others:
        display_name = img_name.replace("低類似と判定_", "").replace("別人と判定_", "")
        print(f"🔍 解析中: {display_name} ... ", end="", flush=True)
        
        img_path = os.path.join(DIR_INPUT, img_name)
        test_img = load_img_jp(img_path)
        row_data = {"FileName": display_name}
        is_passed = True
        
        try:
            # --- 第1段階：門番モデル ---
            for model in GATEKEEPERS:
                distances = [DeepFace.verify(t, test_img, model_name=model, enforce_detection=False)['distance'] for t in target_imgs]
                threshold = DeepFace.verify(target_imgs[0], test_img, model_name=model, enforce_detection=False)['threshold']
                avg_dist = sum(distances) / len(distances)
                sim = get_similarity_score(avg_dist, threshold)
                
                if avg_dist > threshold:
                    row_data[model] = f"{sim:.1f}% [NG]"
                    is_passed = False
                else:
                    row_data[model] = f"{sim:.1f}%"

            # --- 第2段階：詳細スコア算出 ---
            if is_passed:
                score_sum = 0
                for model in SCORERS:
                    distances = [DeepFace.verify(t, test_img, model_name=model, enforce_detection=False)['distance'] for t in target_imgs]
                    threshold = DeepFace.verify(target_imgs[0], test_img, model_name=model, enforce_detection=False)['threshold']
                    avg_dist = sum(distances) / len(distances)
                    sim = get_similarity_score(avg_dist, threshold)
                    score_sum += sim
                    row_data[model] = f"{sim:.1f}%"
                
                avg_score = score_sum / len(SCORERS)
                row_data["TotalScore"] = f"{avg_score:.1f}%"
                row_data["Status"] = "✅ 高類似"
                # 【修正】ログに Score 表記を追加
                print(f"✅ 高類似 (Score {avg_score:.1f}%)")
                shutil.copy2(img_path, os.path.join(DIR_HIGH_SIM, f"{avg_score:.1f}_{display_name}"))
            else:
                for model in SCORERS:
                    row_data[model] = "-"
                row_data["TotalScore"] = "-"
                # 【修正】ステータスを日本語に変更
                row_data["Status"] = "❌ 低類似"
                print("❌ 低類似")
                shutil.copy2(img_path, os.path.join(DIR_LOW_SIM, f"低類似と判定_{display_name}"))

        except Exception as e:
            print(f"⚠️ Error: {e}")
            row_data["Status"] = "ERROR"
        
        all_results_data.append(row_data)

    # --- 詳細レポート表示 ---
    df = pd.DataFrame(all_results_data)
    df = df.fillna("-")
    
    cols = ["FileName"] + GATEKEEPERS + SCORERS + ["TotalScore", "Status"]
    df = df[cols]

    print(f"\n📊 最終解析レポート一覧")
    print("="*120)
    print(df.to_string(index=False))
    print("="*120)
    
    input("\n全工程完了。Enterキーで終了します。")

if __name__ == "__main__":
    main()