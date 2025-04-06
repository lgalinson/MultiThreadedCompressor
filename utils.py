def read_in_chunks(file_object, chunk_size=1024 * 1024):
    """Lazy generator to read a file piece by piece."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data