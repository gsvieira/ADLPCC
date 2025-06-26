import argparse
import glob
import sys
import os
import numpy as np
from absl import app
from absl.flags import argparse_flags
from pathlib import Path

import pc2vox

def convert(args):
    NUM_SIZE = 128
    pc_name = Path(args.train_data)

    
    # Load input PC, get list of coordinates
    in_points = pc2vox.load_pc(args.train_data)
    # Divide PC into blocks of the desired size. Get list of relative coordinates for points in each block
    blocks, _ = pc2vox.pc2blocks(in_points, 64)
    # Ignore blocks with fewer than 500 points
    # total_blocks = [blk for blk in blocks if len(blk) <= 2000]
    total_blocks = blocks
    
    block_save_path = Path.joinpath(pc_name.parents[1], "testing-blocks-full", pc_name.stem)
    Path.mkdir(block_save_path, parents=True, exist_ok=True)
    for j in range(NUM_SIZE):
        np.save(Path.joinpath(block_save_path, f"block_{j:04d}.npy"), total_blocks[j])

    vox_data = np.zeros([len(total_blocks), 64, 64, 64, 1], dtype=np.float32)
    # Iterate all blocks
    for j in range(len(total_blocks)):
        # Convert coordinates to 3D block
        vox_data[j, :, :, :, :] = pc2vox.point2vox(total_blocks[j], 64)
    
    block_save_path = Path.joinpath(pc_name.parents[1], "blocks-full", pc_name.stem)
    Path.mkdir(block_save_path, parents=True, exist_ok=True)
    for j in range(NUM_SIZE):
        np.save(Path.joinpath(block_save_path, f"block_{j:04d}.npy"), vox_data[j, :, :, :, :])


def parse_args(argv):
    """Parses command line arguments."""
    parser = argparse_flags.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(
        title="commands", dest="command",
        help="What to do: 'train' loads training data and trains a new model."
             "'compress' reads the test PC file and writes a compressed binary stream."
             "'decompress' reads the binary stream and reconstructs the PC."
             "input filenames need to be provided. Invoke '<command> -h' for more information.")

    # 'train' subcommand
    train_cmd = subparsers.add_parser(
        "train",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Trains a new model.")
    train_cmd.add_argument(
        "train_data",
        help="Directory containing PC data for training. Filenames should be provided with"
             " a glob pattern that expands into a list of PCs: data/*.ply ")

    # Parse arguments
    args = parser.parse_args(argv[1:])
    return args


def main(args):
    convert(args)

if __name__ == "__main__":
    app.run(main, flags_parser=parse_args)
