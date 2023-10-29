# filename: to_floppy.py

import sys


if __name__ == '__main__':
    try:
        inputfile = sys.argv[1]
    except IndexError:
        raise SystemExit(f"usage: {__file__} bin_file")

    with open(inputfile, "rb") as f:
        data = f.read()
        data_len = len(data)

        if data_len > 512:
            raise SystemExit("超出512字节")

        if data_len == 512 and data[-2:] == b'\x55\xaa':
            raise SystemExit(f"{inputfile}已是可启动镜像")

        zero_data = b'\x00' * (510 - data_len)
        data += zero_data
        data += b'\x55\xaa'

        with open(f"new_{inputfile}", "wb") as f:
            f.write(data)
            print(f"output to new_{inputfile}")