import open3d as o3d
import numpy as np
import csv
from argparse import ArgumentParser
from scipy.spatial import KDTree
from sys import argv, setrecursionlimit
from pathlib import Path


def ply2numpy(ply_path: str) -> np.ndarray:
    r'''
    Loads a .ply file and returns it as a numpy array.

    Args:
        ply_path: the path for the .ply file.

    Returns:
        A numpy array corresponding to the points of the Point Cloud.
    '''
    pcd_load = o3d.io.read_point_cloud(ply_path)
    arr = np.asarray(pcd_load.points)
    return arr


def knnsearch(va: np.ndarray, vb: np.ndarray) -> np.ndarray:
    '''
    Compute the nearest neighbors to a given point in va for each point in vb.

    Args:
        va: an input numpy array.
        vb: a target numpy array.

    Returns:
        A numpy array with the euclidean distances to each nearest neighbor.

    References:
        https://arxiv.org/abs/cs/9901013
    '''
    min_distances = []
    kdtree = KDTree(va)
    for pb in vb:
        distance, _ = kdtree.query(pb, k=1, p=2)
        min_distances.append(distance)
    return np.asarray(min_distances)


def psnr(input_pc: np.ndarray, target_pc: np.ndarray) -> float:
    r'''
    Compute Peak Signal-to-Noise Ratio for two point clouds.

    Args:
        input_pc: an input numpy array.
        target_pc: a target numpy array.

    Returns:
        PSNR Index of similarity between two point clouds.
        If the point clouds are identical, returns inf.

    References:
        https://ieeexplore.ieee.org/abstract/document/9191233
    '''
    setrecursionlimit(1500)
    distances_A = knnsearch(input_pc, target_pc)
    distances_B = knnsearch(target_pc, input_pc)
    p2point_A = np.sum(distances_A**2) / len(target_pc)
    p2point_B = np.sum(distances_B**2) / len(input_pc)
    p2point = max(p2point_A, p2point_B)
    if p2point == 0:
        return float('inf')
    max_coord = max(abs(target_pc.max()), abs(target_pc.min()))
    max_range = np.log2(max_coord)
    max_range = 2 ** (np.ceil(max_range)) - 1
    peak_val = np.linalg.norm([max_range, max_range, max_range])
    psnr = 10 * np.log10(peak_val**2 / p2point)
    return psnr


def parse_args(argv):
    parser = ArgumentParser(description="")
    parser.add_argument('--input',
        type=str,
        default=None,
        help='Path of the input point cloud')
    parser.add_argument('--target',
        type=str,
        default=None,
        help='Path of the target point cloud')
    parser.add_argument('--result',
        type=str,
        default=None,
        help='Path to output result')
    args = parser.parse_args(argv)
    return args


def main(argv):
    args = parse_args(argv)
    if not args.input:
        raise Exception('The input path cannot be empty.')
    if not args.target:
        raise Exception('The target path cannot be empty.')
    input_pc  = ply2numpy(args.input)
    target_pc = ply2numpy(args.target)
    psnr_result = psnr(input_pc, target_pc)
    print(f'The calculated PSNR value is: {psnr_result:.4f}')
    if args.result:
        txt_name = Path(args.target).stem
        txt_name = txt_name[:-len(''.join(Path(txt_name).suffixes))]
        txt_name += "_statistics.txt"
        print(f"args.result: {Path(args.result)}" )
        txt_file = (Path(args.result) / txt_name).open("a")
        txt_file.write(f"psnr: {psnr_result:.4f}\n")
        # csv_reader = csv.writer(csv_file, delimiter=",")
        # csv_reader.writerow(["PSNR", f"{psnr_result:.4f}"])
    


if __name__ == '__main__':
    main(argv[1:])
