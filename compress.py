import os
import gzip
import struct
import concurrent.futures
from utils import read_in_chunks

def compress_chunk(data):
    return gzip.compress(data)

def calculate_dynamic_chunk_size(file_size):
    if file_size == 0:
        return 512 * 1024  # fallback
    chunk_count = min(8, max(1, file_size // (512 * 1024)))
    return max(512 * 1024, file_size // chunk_count)

def compress_file(input_path, output_path):
    try:
        if not os.path.exists(input_path):
            print(f"Error: input file '{input_path}' not found.")
            return

        file_size = os.path.getsize(input_path)
        if file_size == 0:
            print(f"Error: input file '{input_path}' is empty.")
            return

        chunk_size = calculate_dynamic_chunk_size(file_size)
        print(f"Reading from: {input_path} ({file_size} bytes)")
        print(f"Using dynamic chunk size: {chunk_size} bytes")

        futures = []
        compressed_chunks = []

        with open(input_path, 'rb') as infile:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for chunk in read_in_chunks(infile, chunk_size):
                    print(f"Submitting chunk of size {len(chunk)} bytes")
                    futures.append(executor.submit(compress_chunk, chunk))

                for f in futures:
                    compressed_data = f.result()
                    compressed_chunks.append(compressed_data)
                    print(f"Compressed chunk: {len(compressed_data)} bytes")

        with open(output_path, 'wb') as outfile:
            outfile.write(struct.pack('I', len(compressed_chunks)))  # number of chunks
            for chunk in compressed_chunks:
                outfile.write(struct.pack('I', len(chunk)))
            for chunk in compressed_chunks:
                outfile.write(chunk)

        print(f"Compression complete! {len(compressed_chunks)} chunks written to '{output_path}'")

    except Exception as e:
        print(f"Compression failed: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python compress.py input.txt output.mtc")
    else:
        compress_file(sys.argv[1], sys.argv[2])