# File Zipper and Unzipper

This Python program allows you to zip and unzip files and folders. It provides functions to zip files/folders and unzip zip files.

## Prerequisites

- Python 3.x installed on your system.

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/file-zipper-unzipper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd file-zipper-unzipper
    ```

3. Run the Python script:

    ```bash
    python zip_and_unzip.py
    ```

4. Follow the prompts to choose the desired operation and provide input paths.

## Functions

### `zip_files(source, destination)`

Zips files and folders.

**Parameters:**
- `source`: The path of the file/folder to zip.
- `destination`: The destination path for the zip file.

### `unzip_files(zip_file, destination)`

Unzips zip files.

**Parameters:**
- `zip_file`: The path of the zip file to unzip.
- `destination`: The destination path for the unzipped files.

## Example

```python
# Zipping files/folders
source = "path/to/source"
destination = "path/to/destination.zip"
zip_files(source, destination)

# Unzipping files
zip_file = "path/to/zip/file.zip"
destination = "path/to/destination"
unzip_files(zip_file, destination)
```

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
