import gzip
import struct
import concurrent.futures
import os

def decompress_chunk(data):
    return gzip.decompress(data)

def decompress_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: input file '{input_path}' not found.")
        return

    with open(input_path, 'rb') as infile:
        num_chunks_bytes = infile.read(4)
        if not num_chunks_bytes:
            print("Error: input file is empty or corrupted.")
            return

        num_chunks = struct.unpack('I', num_chunks_bytes)[0]

        chunk_sizes = []
        for _ in range(num_chunks):
            size_bytes = infile.read(4)
            if not size_bytes:
                print("Error: incomplete chunk size data.")
                return
            chunk_sizes.append(struct.unpack('I', size_bytes)[0])

        compressed_chunks = []
        for size in chunk_sizes:
            chunk_data = infile.read(size)
            if len(chunk_data) != size:
                print("Error: incomplete chunk data.")
                return
            compressed_chunks.append(chunk_data)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        decompressed_chunks = list(executor.map(decompress_chunk, compressed_chunks))

    with open(output_path, 'wb') as outfile:
        for chunk in decompressed_chunks:
            outfile.write(chunk)

    print(f"✅ Decompression complete. File restored to '{output_path}'.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python decompress.py input.mtc output.txt")
    else:
        decompress_file(sys.argv[1], sys.argv[2])