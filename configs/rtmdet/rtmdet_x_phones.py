_base_ = './rtmdet_l_phones.py'

# ========================Frequently modified parameters======================
# -----data related-----
data_root = 'data/phones/'
# Path of train annotation file
train_ann_file = 'annotations/train_phones.json'
train_data_prefix = 'train/'  # Prefix of train image path
# Path of val annotation file
val_ann_file = 'annotations/valid_phones.json'
val_data_prefix = 'valid/'  # Prefix of val image path
# Path of val annotation file
test_ann_file = 'annotations/test_phones.json'
test_data_prefix = 'test/'  # Prefix of val image path

num_classes = 1  # Number of classes for classification
class_name = ('phone', )
num_classes = len(class_name)
metainfo = dict(classes=class_name, palette=[(20, 220, 60)])

# ========================modified parameters======================
deepen_factor = 1.33
widen_factor = 1.25

# =======================Unmodified in most cases==================
model = dict(
    backbone=dict(deepen_factor=deepen_factor, widen_factor=widen_factor),
    neck=dict(deepen_factor=deepen_factor, widen_factor=widen_factor),
    bbox_head=dict(head_module=dict(widen_factor=widen_factor)))
