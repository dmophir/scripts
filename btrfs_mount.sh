#!/bin/bash

mount /dev/nvme0n1p2 /mnt -o subvol=@
mount /dev/nvme0n1p1 /mnt/boot
mount /dev/nvme0n1p2 /mnt/home -o subvol=@home
mount /dev/nvme0n1p2 /mnt/var/log -o subvol=@log
mount /dev/nvme0n1p2 /mnt/var/cache/pacman/pkg -o subvol=@pkg
mount /dev/nvme0n1p2 /mnt/.snapshots -o subvol=@.snapshots
