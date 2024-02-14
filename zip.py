import os
import zipfile

def zip_files(source, destination):
    with zipfile.ZipFile(destination, 'w') as zipf:
        if os.path.isdir(source):
            for foldername, subfolders, filenames in os.walk(source):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    zipf.write(filepath, os.path.relpath(filepath, source))
        else:
            zipf.write(source, os.path.basename(source))

    print(f"Successfully zipped '{source}' to '{destination}'")

def unzip_files(zip_file, destination):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(destination)

    print(f"Successfully unzipped '{zip_file}' to '{destination}'")

if __name__ == "__main__":
    while True:
        print("Select an option:")
        print("1. Zip files/folders")
        print("2. Unzip files")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            source = input("Enter the path of the file/folder to zip: ")
            destination = input("Enter the destination path for the zip file: ")
            zip_files(source, destination)
        elif choice == '2':
            zip_file = input("Enter the path of the zip file to unzip: ")
            destination = input("Enter the destination path for the unzipped files: ")
            unzip_files(zip_file, destination)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
