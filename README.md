# Appium-API-Automation

This repository contains an automation script using **Appium** for mobile app testing and **API testing** for verifying functionalities. The project demonstrates the integration of Appium for automating mobile applications and Postman API testing for validating API responses.

## Project Overview

- **Appium**: Automates mobile applications (Android/iOS) for functional testing.
- **API Testing**: Uses APIs to verify responses and behaviors of backend services.
- **Integration**: The project combines both Appium-based mobile testing and API validation to ensure end-to-end system functionality.

## Prerequisites

Before running the scripts, ensure that the following are installed:

1. **Appium**: For mobile automation testing.
   - [Appium Installation Guide](https://appium.io/docs/en/about-appium/intro/)
2. **Python**: Version 3.6+ for running the automation scripts.
3. **Postman** (optional): For manual API testing, or Postman collection for automated API tests.
4. **Appium Inspector**: For inspecting mobile elements and generating locators.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Appium-API-Automation.git

2. Install dependencies:
   python Appium-API.py

🚀 Running the Tests
1. Start Appium Server
   appium
2. Execute the Test Script
   python Appium-API.py

Code Explanation
🔹 Appium Mobile Automation
The script launches the calculator app on an Android device.
It locates the number buttons and operator using their element IDs.
After performing the calculation, it extracts the displayed result.

🔹 API Validation
The script sends the same arithmetic operation to an API.
It receives the expected result from the API response.
Finally, it compares the API result with the Appium result to ensure they match.

🔧 Troubleshooting
Appium cannot find elements?

Ensure Appium Inspector is correctly identifying UI elements.
The calculator app may display results differently (e.g., "5 계산 결과" instead of just "5"). Adjust the code accordingly.
Appium server connection issue?

Make sure Appium Server is running (http://127.0.0.1:4723/wd/hub).
Incorrect API response?

Check if the API endpoint is reachable.
Verify the request format and parameters.
