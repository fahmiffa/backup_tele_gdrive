import gzip
import shutil

def compress_file(file_path):
    gz_path = file_path + ".gz"

    with open(file_path, 'rb') as f_in:
        with gzip.open(gz_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    return gz_path