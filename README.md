# WebP to PNG Converter

This repository contains two Python scripts, `webp2png.py` and `webp2png_service.py`, designed to automatically convert `.webp` image files to `.png` format. The conversion process helps solve the common issue where `.webp` files, which are often downloaded from the web, are not widely supported when uploading to many websites.

The `webp2png.py` script can be run manually to watch your Downloads folder, while the `webp2png_service.py` script can be set up as a Windows service to run automatically in the background.

## Features
- Automatically converts downloaded `.webp` images in your Downloads folder to `.png` format.
- Deletes the original `.webp` file after conversion.
- Can run manually or as a Windows service, allowing hands-off background operation.

## Prerequisites

- Python 3.x installed on your machine.
- Pip (comes with Python) for installing required libraries.

### Libraries Used
- **Pillow**: For image conversion.
- **Watchdog**: To monitor your Downloads folder for changes.
- **pywin32**: For creating a Windows service (only needed for `webp2png_service.py`).

## Installation

### Step 1: Install Python

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Download and install Python 3.x.
3. During installation, ensure you check the box that says **"Add Python to PATH"**.

### Step 2: Clone This Repository

Download the repository or clone it using Git:

```sh
git clone https://github.com/jgravelle/webp2png.git
```

### Step 3: Install Required Libraries

Use `pip` to install the required Python libraries.

Open Command Prompt (Windows) or Terminal (Mac/Linux) and navigate to the repository folder:

```sh
cd path/to/webp2png
```

Install the necessary libraries by running:

```sh
pip install pillow watchdog pywin32
```

## Usage

### Option 1: Run Manually (`webp2png.py`)

The `webp2png.py` script can be run to manually monitor your Downloads folder and convert any `.webp` images to `.png`.

1. Open Command Prompt and navigate to the repository folder.
2. Run the script:

   ```sh
   python webp2png.py
   ```

3. The script will start watching your Downloads folder for any new `.webp` files and automatically convert them to `.png` when they appear.

### Option 2: Set Up as a Windows Service (`webp2png_service.py`)

The `webp2png_service.py` script allows you to set up a Windows service that will automatically monitor your Downloads folder and convert `.webp` files without needing to manually run the script.

#### Step 1: Update the Downloads Path

Before proceeding, make sure to update the path to your Downloads folder in `webp2png_service.py`. Replace the line:

```python
DOWNLOADS_FOLDER = r"C:\Users\<your_username>\Downloads"
```

with the correct path to your Downloads folder. Replace `<your_username>` with your actual Windows username.

#### Step 2: Install the Service

1. Open Command Prompt as **Administrator**.
2. Navigate to the folder containing `webp2png_service.py`.
3. Install the service by running:

   ```sh
   python webp2png_service.py install
   ```

4. Start the service by running:

   ```sh
   python webp2png_service.py start
   ```

The service will now run in the background and automatically convert `.webp` files to `.png` whenever they are downloaded to your Downloads folder.

## Troubleshooting

### Common Issues

1. **FileNotFoundError**: Ensure the path to your Downloads folder is correct. The path must be updated manually in `webp2png_service.py`.
2. **Permission Issues**: If the service fails to access your Downloads folder, ensure that the service has the necessary permissions. You may need to run Command Prompt as **Administrator** to install and start the service.
3. **Service Not Starting**: Double-check that `pywin32` is installed and that the `DOWNLOADS_FOLDER` path is correctly specified.

### Stopping or Uninstalling the Service

To stop the service:

```sh
python webp2png_service.py stop
```

To uninstall the service:

```sh
python webp2png_service.py remove
```

## How It Works

- The scripts use **Watchdog** to monitor the Downloads folder for new `.webp` files.
- When a new `.webp` file is detected, **Pillow** is used to convert it to `.png` format.
- Once the conversion is successful, the original `.webp` file is deleted to save space.

## Additional Notes

- This solution is specific to Windows users since it involves a Windows service. However, `webp2png.py` can be manually run on other operating systems like macOS or Linux.
- Feel free to modify the script to monitor a different folder if needed.

## Contributions

Contributions are welcome! If you have suggestions for improving the script or adding new features, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or run into issues, please reach out by creating an issue on this repository.

