import os

train_out_label_dir = 'data/KITTI/old_labels/train/labels'
test_out_label_dir = 'data/KITTI/old_labels/test/labels'
val_out_label_dir = 'data/KITTI/old_labels/validation/labels'

yolo_train_labels = 'data/KITTI/train/labels/'
yolo_test_labels = 'data/KITTI/test/labels/'
yolo_val_labels = 'data/KITTI/validation/labels/'

os.makedirs(yolo_train_labels, exist_ok=True)
os.makedirs(yolo_test_labels, exist_ok=True)
os.makedirs(yolo_val_labels, exist_ok=True)


def convert_folder_kitti_to_yolo_v5(labels_folder_path, output_folder_path):
    classes = {"Car": 0, "Van": 1, "Truck": 2, "Pedestrian": 3, "Person_sitting": 4, "Cyclist": 5, "Tram": 6, "Misc": 7}
    for filename in os.listdir(labels_folder_path):
        if not filename.endswith('.txt'):
            continue
        file_path = os.path.join(labels_folder_path, filename)
        with open(file_path, 'r') as f:
            labels = f.readlines()
        output_path = os.path.join(output_folder_path, filename)
        with open(output_path, 'w') as f:
            for label in labels:
                label = label.strip().split(' ')
                cls = label[0]
                if cls in classes:
                    cls_id = classes[cls]
                    x, y, w, h = float(label[4]), float(label[5]), float(label[6]), float(label[7])
                    x, y, w, h = x / 1242, y / 375, w / 1242, h / 375
                    if x > 1 or y > 1 or w > 1 or h > 1:
                        print(f"over the limit  file:  {file_path}  data:  {cls_id} {x} {y} {w} {h} ")
                    f.write(f"{cls_id} {x} {y} {w} {h}\n")


convert_folder_kitti_to_yolo_v5(train_out_label_dir, yolo_train_labels)
convert_folder_kitti_to_yolo_v5(test_out_label_dir, yolo_test_labels)
convert_folder_kitti_to_yolo_v5(val_out_label_dir, yolo_val_labels)
