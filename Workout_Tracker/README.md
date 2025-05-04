# Workout Tracking Application

A Python script that tracks workouts using the Nutritionix API and saves them to a Google Sheet via Sheety API.

## Features

- Logs exercises using natural language input (e.g., "ran 5km and cycled 20 minutes")
- Retrieves exercise details (duration, calories burned) via Nutritionix API
- Stores workout data in a Google Sheet
- Simple command-line interface

## Prerequisites

- Python 3.x
- Nutritionix API account
- Sheety account connected to Google Sheets
- Google account (for Sheets access)

## Setup

### 1. API Keys Setup

1. **Nutritionix**: Sign up at [nutritionix.com/business/api](https://www.nutritionix.com/business/api)

   - Get your `APP ID` and `APP KEY`

2. **Sheety**: Sign up at [sheety.co](https://sheety.co)
   - Create a new Google Sheet
   - Create a new project and connect your Google Sheet
   - Get your:
     - Sheety API endpoint (format: `https://api.sheety.co/{your-api-id}/{project_name}/{sheet_name}`)
     - Authorization token (starts with "Bearer")

### 2. Environment Setup

1. Create a .env file with your credentials:
   NUTRITIONIX_APP_ID=your_app_id_here
   NUTRITIONIX_APP_KEY=your_app_key_here
   SHEETY_API=your_sheety_api_id
   SHEETY_AUTH=Bearer your_sheety_token_here

2. Install the requirements
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python3 main.py
```

```bash
Example: Tell me which exercises you did: ran 5km and did 30 minutes of weight training
```
