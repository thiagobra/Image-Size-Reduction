import os
from pathlib import Path
from PIL import Image

def convert_images_to_jpeg(input_folder: Path, output_folder: Path, quality: int = 50) -> None:
    """
    Converts all images in the input folder to JPEG format, reduces their file size,
    and saves them in the output folder.

    Args:
        input_folder (Path): Path to the folder containing images.
        output_folder (Path): Path to the folder where converted images will be saved.
        quality (int): JPEG quality (1-100) for compression. Lower values mean higher compression.

    Raises:
        ValueError: If the input folder does not exist or is not a directory.
    """
    # Validate input folder
    if not input_folder.exists() or not input_folder.is_dir():
        raise ValueError(f"Input folder '{input_folder}' does not exist or is not a directory.")

    # Create the output folder if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)

    skipped_files = []
    processed_count = 0

    for item in input_folder.iterdir():
        if item.is_dir():
            # Skip directories
            continue

        try:
            with Image.open(item) as img:
                # Convert to RGB (necessary for JPEG format)
                img = img.convert("RGB")

                # Prepare the output file path
                output_file = output_folder / f"{item.stem}.jpg"

                # Save the image as JPEG with specified quality
                img.save(output_file, "JPEG", quality=quality)
                processed_count += 1
                print(f"✅ Converted: {item.name} -> {output_file}")
        except Exception as e:
            skipped_files.append((item.name, str(e)))
            print(f"⚠️ Skipped: {item.name} (Error: {e})")

    # Provide a summary of results
    print("\n=== Conversion Summary ===")
    print(f"Total files processed: {processed_count}")
    if skipped_files:
        print(f"Total files skipped: {len(skipped_files)}")
        for file_name, error in skipped_files:
            print(f"  - {file_name}: {error}")
    else:
        print("All files were successfully processed!")


def main() -> None:
    """
    Main entry point of the script. Defines input and output folders, and runs the conversion process.
    """
    # Define paths
    input_folder = Path(r"C:\Users\John\Desktop")  # Update with your desired input folder path
    output_folder = input_folder / "output"

    # Run the conversion
    try:
        convert_images_to_jpeg(input_folder, output_folder, quality=50)
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
