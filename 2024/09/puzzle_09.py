"""Solution to Problem 9, 2024"""

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest

class ComputeChecksumFixture(unittest.TestCase):
    def test_compute_checksum(self):
        disk_map = "2333133121414131402"
        self.assertEqual(compute_checksum(disk_map), 1928)

def compute_checksum(disk_map : str) -> int:
    file_blocks = []
    for i, c in enumerate(disk_map):
        for _ in range(int(c)):
            if i % 2 == 0:
                file_id = i // 2
                file_blocks.append(file_id)
            else:
                file_blocks.append('.')
    offset = -1
    for i, c in enumerate(file_blocks):
        if c == '.':
            if i - offset > len(file_blocks):
                break
            while file_blocks[offset] == '.':
                offset -= 1
            file_blocks[i], file_blocks[offset] = file_blocks[offset], file_blocks[i]
            offset -= 1
    return sum(i * int(c) if c != '.' else 0 for i, c in enumerate(file_blocks))

if __name__ == "__main__":
    unittest.main(exit=False)

    with open("input.txt", encoding="utf-8") as f:
        # compute solution to part A - should be 6344673854800
        print(compute_checksum(f.readline()))

        # compute solution to part B - should be 1200
        # ???
