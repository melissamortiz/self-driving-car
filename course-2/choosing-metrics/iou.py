import numpy as np

from utils import get_data, check_results


def calculate_ious(gt_bboxes, pred_bboxes):
    """
    calculate ious between 2 sets of bboxes 
    args:
    - gt_bboxes [array]: Nx4 ground truth array
    - pred_bboxes [array]: Mx4 pred array
    returns:
    - iou [array]: NxM array of ious
    """
    ious = np.zeros((gt_bboxes.shape[0], pred_bboxes.shape[0]))
    for i, gt_bbox in enumerate(gt_bboxes):
        for j, pred_bbox in enumerate(pred_bboxes):
            ious[i,j] = calculate_iou(gt_bbox, pred_bbox)
    return ious


def calculate_iou(gt_bbox, pred_bbox):
    """
    calculate iou 
    args:
    - gt_bbox [array]: 1x4 single gt bbox
    - pred_bbox [array]: 1x4 single pred bbox
    returns:
    - iou [float]: iou between 2 bboxes
    """
    ## IMPLEMENT THIS FUNCTION  
    x1_gt, y1_gt, x2_gt, y2_gt = gt_bbox
    x1_pred, y1_pred, x2_pred, y2_pred = pred_bbox

    x1_intersect = max(x1_gt, x1_pred)
    y1_intersect = max(y1_gt, y1_pred)
    x2_intersect = min(x2_gt, x2_pred)
    y2_intersect = min(y2_gt, y2_pred)

    width_intersect = max(0, x2_intersect - x1_intersect)
    height_intersect = max(0, y2_intersect - y1_intersect)
    area_intersection = width_intersect * height_intersect

    area_gt = (x2_gt - x1_gt) * (y2_gt - y1_gt)
    area_pred = (x2_pred - x1_pred) * (y2_pred - y1_pred)
    
    area_union = area_gt + area_pred - area_intersection
    if area_union == 0:
        return 0.0

    iou = area_intersection / area_union    
    return iou


if __name__ == "__main__": 
    ground_truth, predictions = get_data()
    # get bboxes array
    filename = 'segment-1231623110026745648_480_000_500_000_with_camera_labels_38.png'
    gt_bboxes = [g['boxes'] for g in ground_truth if g['filename'] == filename][0]
    gt_bboxes = np.array(gt_bboxes)
    pred_bboxes = [p['boxes'] for p in predictions if p['filename'] == filename][0]
    pred_boxes = np.array(pred_bboxes)
    
    ious = calculate_ious(gt_bboxes, pred_boxes)
    check_results(ious)