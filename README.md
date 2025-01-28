# Telegram Private Link Sniper

A lightweight tool designed to monitor and capture Telegram invite link to private chat.

## Features

- Monitor Telegram channel messages for private chat links
- Auto join private chat

## Prerequisites

- Python 3.x
- Telegram API credentials

## Installation

1. Clone the repository:

```bash
git clone https://github.com/lucky-ivanius/snipe-tg-private-link.git
cd snipe-tg-private-link
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Obtain your Telegram API credentials (api_id and api_hash) from [my.telegram.org](https://my.telegram.org)
2. Configure your credentials in the application (bot token or phone number, code, password, etc.)

## Usage

```bash
python bot.py --api_id=<api_id> --api_hash=<api_hash> --channel=<channel>
```

To remove your Telegram session, simply delete the `auth` folder in the current directory.

## Disclaimer

This tool is for educational purposes only. Be sure to comply with Telegram's Terms of Service and API usage guidelines.
