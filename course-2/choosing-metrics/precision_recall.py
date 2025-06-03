import numpy as np

from iou import calculate_ious
from utils import get_data


def precision_recall(ious, gt_classes, pred_classes):
    """
    calculate precision and recall
    args:
    - ious [array]: NxM array of ious
    - gt_classes [array]: 1xN array of ground truth classes
    - pred_classes [array]: 1xM array of pred classes
    returns:
    - precision [float]
    - recall [float]
    """
    # IMPLEMENT THIS FUNCTION
    tp = 0
    fp = 0
    fn = 0
    iou_threshold = 0.5
    
    for i in range(len(gt_classes)):
        # Find the best predicted box for the current ground truth box.
        best_iou_index = -1
        max_iou = 0
        for j in range(len(pred_classes)):
            if ious[i, j] > max_iou and gt_classes[i] == pred_classes[j]:
                max_iou = ious[i, j]
                best_iou_index = j

        # Determine if it's a TP or FN based on the best matched predicted box.
        if max_iou >= iou_threshold:
            tp += 1
        else:
            fn += 1

    # Count FP based on predicted boxes that didn't match any ground truth box.
    fp = len(pred_classes) - tp
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    return precision, recall


if __name__ == "__main__": 
    ground_truth, predictions = get_data()
    
    # get bboxes array
    filename = 'segment-1231623110026745648_480_000_500_000_with_camera_labels_38.png'
    gt_bboxes = [g['boxes'] for g in ground_truth if g['filename'] == filename][0]
    gt_bboxes = np.array(gt_bboxes)
    gt_classes = [g['classes'] for g in ground_truth if g['filename'] == filename][0]
    

    pred_bboxes = [p['boxes'] for p in predictions if p['filename'] == filename][0]
    pred_boxes = np.array(pred_bboxes)
    pred_classes = [p['classes'] for p in predictions if p['filename'] == filename][0]
    
    ious = calculate_ious(gt_bboxes, pred_boxes)
    precision, recall = precision_recall(ious, gt_classes, pred_classes)