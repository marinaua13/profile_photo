# profile_photo

This project automates LinkedIn login and extracts profile photos from specified LinkedIn profiles using Selenium. It also includes logging for each process step.

## Features

- Automated login to LinkedIn
- Profile photo extraction and storage
- Configurable with `.env` for storing login credentials securely
- Robust logging for tracking each stage of execution
- Handles potential `recaptcha` challenges

## Requirements

- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically handled by `webdriver-manager`)
- Selenium
- Requests
- python-dotenv

## Setup Instructions

1. **Clone this repository** and navigate to the project directory:
    ```bash
    git clone https://github.com/marinaua13/profile_photo
    cd profile_photo
    ```

2. **Create a virtual environment** and install the dependencies:
    ```bash
    python -m venv venv
    source venv\Scripts\activate  # for Windows
    pip install -r requirements.txt
    ```

3. **Configure environment variables**:
   - Create a `.env` file in the project directory:
     ```plaintext
     USER=your_linkedin_email@example.com
     PASSWORD=your_linkedin_password
     ```
   - **NOTE**: Never share this file with anyone or upload it to a public repository.

4. **Run the script**:
    ```bash
    python profile_photo.py
    ```

5. **Logs**: Check `out.log` for detailed logs about each operation.

## Handling reCAPTCHA

LinkedIn may display a reCAPTCHA challenge to detect automated logins. While this script does not directly solve reCAPTCHA, here are a few tips to reduce the chance of encountering it:

1. **Use realistic wait times**: Adding random wait times between actions makes automation appear more human-like.
2. **Avoid excessive requests**: Only scrape profiles as needed to minimize bot detection.
3. **Consider third-party services**: If reCAPTCHA persists, consider using third-party services that provide CAPTCHA solving for Selenium-based automations.
4. **Manual intervention**: If reCAPTCHA occurs, manually complete it and let the script resume afterward.

## Example Profile Data

In the script, profiles are listed as dictionaries with URLs and the respective alt text for identifying profile images.

