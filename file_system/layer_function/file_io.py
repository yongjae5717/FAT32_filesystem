def ReadFile(filename, seek_offset, size):
    res = bytearray()
    with open(filename, 'rb') as f:
        f.seek(int(seek_offset, 16))
        res += f.read(int(size, 16))
    return res


def WriteFile(destination_dir, byte_array):
    with open(destination_dir, "wb") as f:
        f.write(byte_array)
