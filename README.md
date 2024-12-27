# Image Converter to JPEG

This Python script converts all images within a specified folder to JPEG format, reduces their file size using compression, and saves them to a designated output folder.

## Features

-   **Converts to JPEG:** Converts images of various formats (e.g., PNG, GIF, BMP) to JPEG.
-   **File Size Reduction:** Reduces image file sizes by applying JPEG compression.
-   **Quality Control:** Allows you to specify the JPEG quality level (1-100) to control the trade-off between image quality and file size.
-   **Error Handling:** Gracefully handles invalid files or errors during the conversion process, providing a summary of skipped files.
-   **Summary Report:** Provides a summary of the conversion process, including the number of files processed and any errors encountered.

## Requirements

-   Python 3.x
-   Pillow (PIL Fork) library: `pip install Pillow`

## Usage

1. **Set Input and Output Folders:**
    -   Modify the `input_folder` variable in the `main()` function to the path of the folder containing the images you want to convert.
    -   The `output_folder` will be created as a subfolder named "output" within the `input_folder`. You can change this if needed.

    ```python
    input_folder = Path(r"C:\Users\John\Folder")  # Update with your input folder
    output_folder = input_folder / "output"
    ```

2. **Adjust JPEG Quality (Optional):**
    -   Change the `quality` parameter in the `convert_images_to_jpeg()` function call within `main()` to adjust the JPEG compression quality. Lower values mean higher compression (smaller file size) but potentially lower image quality. The default is 50.

    ```python
    convert_images_to_jpeg(input_folder, output_folder, quality=50)
    ```

3. **Run the Script:**
    -   Execute the script from your terminal:

    ```bash
    python your_script_name.py
    ```

    -   The script will process all images in the input folder and save the converted JPEG files to the output folder.
    -   Progress and any errors will be printed to the console. A summary report will be displayed at the end.

## Example

Suppose you have a folder `C:\Users\John\Folder` with various images (PNG, GIF, etc.). After running the script with the default settings, the converted JPEG files will be saved in `C:\Users\John\Folder\output`.

## Error Handling

-   If the input folder does not exist or is not a directory, a `ValueError` will be raised.
-   If any error occurs during the processing of an individual image file (e.g., invalid file format, corrupted file), the script will skip that file, print an error message to the console, and continue processing the remaining files.
-   A list of skipped files and their corresponding error messages will be included in the final summary report.

## Notes

-   The script converts all images to RGB mode before saving them as JPEG, as JPEG doesn't support other color modes (like grayscale or indexed).
-   The original files in the input folder are not modified or deleted.
-   Directories within the input folder are skipped.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (You'll need to create a LICENSE file if you intend to distribute this code).