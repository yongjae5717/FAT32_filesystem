def read_file(filename, seek_offset, size):
    res = bytearray()
    try:
        with open(filename, 'rb') as f:
            f.seek(int(seek_offset, 16))
            res += f.read(int(size, 16))
    except FileNotFoundError as e:
        print(f'fail to read file: {e}')
        exit()

    return res


def write_file(destination_dir, byte_array):
    try:
        with open(destination_dir, "wb") as f:
            f.write(byte_array)
    except FileNotFoundError as e:
        print(f'fail to write file: {e}')
        exit()
