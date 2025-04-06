# Multithreaded File Compressor

This is a Python-based file compression and decompression tool that splits input files into chunks and compresses them in parallel using multithreading. It supports both a command-line interface and a graphical user interface using `tkinter`.

---

## Features

- Compress and decompress large files efficiently
- Multithreaded processing for improved speed
- Uses Python’s built-in `gzip` module
- Automatically adjusts chunk size based on input file size
- Simple GUI for non-technical users
- No external dependencies

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/multithreaded-compressor.git
cd multithreaded-compressor
```

---

## Command Line Usage

Compress a file:

```bash
python compress.py input.txt output.mtc
```

Decompress a file:

```bash
python decompress.py output.mtc restored.txt
```

---

## GUI Usage

To run graphical user interface:

```bash 
python gui.py
```

From the GUI, you can:
- Select an input file
- Choose whether to compress or decompress
- Pick an output destination
- Click and run the operation

*Note (macOS): If the application is blocked on first launch, right click the app and select “Open.”*

---

## How It Works
1. The input file is read in dynamically sized chunks.
2. Each chunk is compressed using gzip compression in a separate thread.
3. A .mtc file is generated (see below).
4. Decompression reverses the process using this metadata.

---

## File Format: .mtc

This is a custom binary file format created by this application. It is not compatible with standard archive tools.

**Structure**:
- 4 bytes: number of chunks (unsigned integer)
- 4 bytes × number of chunks: size of each compressed chunk
- Compressed chunk data (GZIP) for each chunk

---

## Building a Standalone Executable

To build a Windows .exe or macOS .app using PyInstaller:
1. Install PyInstaller:
```bash
pip install pyinstaller
```
2. Build the app:
```bash
pyinstaller --windowed --onefile gui.py
```
3. The standalone executable will be found in the dist/ folder.

---

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for full terms.

---

## Author

Created by Lakeland Galinson







