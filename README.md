# DiskFormatting
A Python script for data destruction

#### Principle
1. Delete all the files and directories;
2. Formatting the disk:
   * Firstly, use b'\x01' to overwrite the disk.
   * Secondly, use b'0xff' to overwrite the disk, which is the complement of b'\x01'.
   * Thirdly, choose a random byte to overwrite the disk.

