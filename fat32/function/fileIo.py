def read_file(filename, seek_offset, size):
    res = bytearray()
    try:
        with open(filename, 'rb') as f:
            f.seek(int(seek_offset, 16))
            res += f.read(int(size, 16))
    except FileNotFoundError as e:
        print(f'catch FileNotFoundError exception, Please check filename: {e.filename}')
        exit()

    return res


def write_file(destination_dir, byte_array):
    try:
        with open(destination_dir, "wb") as f:
            f.write(byte_array)
    except FileNotFoundError as e:
        print(f'catch FileNotFoundError exception, Please check destination directory: {e.filename}')
        exit()
