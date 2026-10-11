cd 0_vo  (This version needs Ubuntu 24.04, ROS2 Jazzy, and GZ Harmonic 8.9.0 combination)

📌 🧭 ❤️ ✅ 🔥 🎯 ➡️ ⭐
###################


####    Run 0_vo
This folder contain many workspaces
(yard_20x20, house, and saye_world) in addition to the default world.


# If you also want to use your custom world
ros2 launch nav2_bringup tb4_simulation_launch.py \
  slam:=False \
  use_localization:=True \
  map:=/home/dhayaa/0_vo/maps/map1.yaml \
  world:=/home/dhayaa/0_vo/my_worlds/yard_20x20.sdf \
  headless:=False


# To run bag 
ros2 bag record \
  /rgbd_camera/image \
  /rgbd_camera/camera_info \
  /tf \
  /tf_static \
  /odom \
  /imu

# To extract information form .mcap file
🔥 form inside the folder 🔥 OR 🔥 add the path to the file name 
python3 extract_vo_dataset.py \
  --bag /home/dhayaa/0_vo/vo_dataset/export/rosbag2_2026_01_07-22_33_49/rosbag2_2026_01_07-22_33_49_0.mcap \
  --out /home/dhayaa/0_vo/vo_dataset/sequences/seq_01 \
  --image_topic /rgbd_camera/image \
  --odom_frame odom \
  --base_frame base_link \
  --max_tf_dt 0.05

# Quick dataset sanity checks (do these now)
Check label columns + basic stats
python3 - <<'EOF'
import pandas as pd
p = "/home/dhayaa/0_vo/vo_dataset/sequences/seq_01/vo_pairs.csv"
df = pd.read_csv(p)
print("Rows:", len(df))
print("Columns:", df.columns.tolist())
for c in ["dx","dy","dz","droll","dpitch","dyaw"]:
    print(c, "min", df[c].min(), "max", df[c].max(), "mean", df[c].mean())
EOF
✅ Output
Rows: 1660
Columns: ['img_t', 'img_t1', 't', 't1', 'dx', 'dy', 'dz', 'droll', 'dpitch', 'dyaw']
dx min -0.026957 max 0.051 mean 0.042132386746987945
dy min -0.000438 max 0.001201 mean 5.298493975903614e-05
dz min 0.0 max 0.0 mean 0.0
droll min 0.0 max 0.0 mean 0.0
dpitch min -0.0 max -0.0 mean 0.0
dyaw min -0.097797 max 0.062558 mean 0.0031425536144578316

# Detect any “jumps” (bad TF sync)
python3 - <<'EOF'
import pandas as pd, numpy as np
p = "/home/dhayaa/0_vo/vo_dataset/sequences/seq_01/vo_pairs.csv"
df = pd.read_csv(p)
dist = np.sqrt(df["dx"]**2 + df["dy"]**2 + df["dz"]**2)
print("Translation norm: 99th percentile =", np.quantile(dist, 0.99))
print("Max translation norm =", dist.max())
print("Max abs dyaw =", np.abs(df["dyaw"]).max())
EOF

# Make it training-friendly (recommended preprocessing)
For a first model, I suggest you train on (dx, dy, dyaw) only.
It’s the most stable and matches TB4 kinematics.
Create a new CSV with those 3 targets:

python3 - <<'EOF'
import pandas as pd, os
src = "/home/dhayaa/0_vo/vo_dataset/sequences/seq_01/vo_pairs.csv"
dst = "/home/dhayaa/0_vo/vo_dataset/sequences/seq_01/vo_pairs_xyyaw.csv"
df = pd.read_csv(src)
df2 = df[["img_t","img_t1","t","t1","dx","dy","dyaw"]].copy()
df2.to_csv(dst, index=False)
print("Wrote:", dst, "rows:", len(df2))
EOF
# Activate virtual environment
source ~/dl_env/bin/activate
deactivate
# Training CLI
source ~/dl_env/bin/activate
cd ~/0_vo/vo_code/training

python train_vo_baseline.py \
  --seq_dir /home/dhayaa/0_vo/vo_dataset/sequences/seq_01 \
  --out /home/dhayaa/0_vo/runs/vo_baseline_seq01 \
  --epochs 30 \
  --batch 32 \
  --lr 3e-4 \
  --img_h 192 \
  --img_w 256

# Evaluation Command
python3 eval_vo_metrics.py \
  --seq_dir /home/dhayaa/0_vo/vo_dataset/sequences/seq_01 \
  --csv vo_pairs_xyyaw.csv \
  --ckpt /home/dhayaa/0_vo/runs/vo_baseline_seq01/checkpoints/best.pt \
  --out /home/dhayaa/0_vo/runs/vo_baseline_seq01/eval_full \
  --dk 1,5,10,20

# CNN LSTM (window 5, reqiire_chain)
python train_vo_cnn_lstm.py \
  --seq_dir /home/dhayaa/0_vo/vo_dataset/sequences/seq_01 \
  --out /home/dhayaa/0_vo/runs/vo_cnn_lstm_L5_seq01 \
  --epochs 30 \
  --batch 16 \
  --lr 3e-4 \
  --img_h 192 \
  --img_w 256 \
  --window 5 \
  --stride 1 \
  --require_chain

# CNN+LSTM with L = 7 (For better ATE drift reduction, especially in simulation)
python train_vo_cnn_lstm.py \
  --seq_dir /home/dhayaa/0_vo/vo_dataset/sequences/seq_01 \
  --out /home/dhayaa/0_vo/runs/vo_cnn_lstm_L7_seq01 \
  --epochs 30 \
  --batch 16 \
  --lr 3e-4 \
  --img_h 192 \
  --img_w 256 \
  --window 7 \
  --stride 1 \
  --require_chain

# View TenserBoard 
tensorboard --logdir /home/dhayaa/0_vo/runs/vo_cnn_lstm_L5_seq01/tb

# Evaluation Command (Figures, metrics.json, and pred_pairs_full.csv)
python eval_vo_metrics_cnn_lstm.py \
  --seq_dir /home/dhayaa/0_vo/vo_dataset/sequences/seq_01 \
  --ckpt /home/dhayaa/0_vo/runs/vo_cnn_lstm_L5_seq01/checkpoints/best.pt \
  --out  /home/dhayaa/0_vo/runs/vo_cnn_lstm_L5_seq01/eval \
  --batch 64 \
  --img_h 192 \
  --img_w 256

# metrics.json provide summary (ATE/RPE/drift)