# tg_voice_bot

A Telegram bot for forwarding and transcribing voice messages. The bot forwards voice messages from private chats to a group chat for transcription by a bot, then sends the transcribed text back to the original chat.

## Introduction

The `tg_voice_bot` script is designed to simplify the process of transcribing voice messages in Telegram. It forwards voice messages from private chats to a designated group chat where a transcription bot processes them. The transcribed text is then sent back to the original chat, making it easy to read and understand voice messages.

## Features

- **Forwards Voice Messages:** Forwards voice messages from private chats to a group chat.
- **Handles Transcriptions:** Receives transcriptions from a bot in the group chat.
- **Sends Back Transcriptions:** Sends the transcribed text back to the original chat with a user-friendly prefix.

## How It Works

1. **Forwarding Voice Messages:**  
   The bot forwards any voice message received in a private chat to a specified group chat.

2. **Receiving Transcriptions:**  
   When the transcription bot in the group chat edits a message with the transcribed text, the bot captures this response.

3. **Sending Back Transcriptions:**  
   The transcribed text is then sent back to the original private chat, prefixed appropriately based on the sender.

## Getting Started

### Prerequisites

To use this script, you need to have the following:

- Python 3.8 or higher
- A Telegram account
- API credentials from Telegram (API ID and API Hash)
- A group chat for the transcription bot

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Commonlist/tg_voice_bot.git
    ```

2. **Install the Required Packages:**  
   Navigate to the project directory and install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Credentials:**  
   You need to set up your API credentials for Telegram. You can find the instructions for obtaining these credentials in the respective documentation of Telegram.

### Configuration

Update the script `tg_voice_bot.py` with your API credentials:

    ```python
    api_id = "your_api_id"
    api_hash = "your_api_hash"
    group_chat_id = -100group_chat_id  # ID of your group chat
    your_username = "your_username"  # Your Telegram username
    ```

### Running the Script

To start the script, simply run:

    ```bash
    python tg_voice_bot.py
    ```

or

    ```bash
    nohup python tg_voice_bot.py &
    ```

The script will start monitoring your private chats for any voice messages.

## Example Usage

- **Step 1:** Send a voice message in a private chat.
- **Step 2:** The bot forwards the voice message to the specified group chat.
- **Step 3:** The transcription bot in the group chat transcribes the voice message.
- **Step 4:** The transcribed text is sent back to the original private chat.

## Troubleshooting

If you encounter any issues while using the script, here are some common troubleshooting steps:

- **Check API Credentials:** Ensure that your API ID and API Hash are correct.
- **Internet Connection:** Make sure your internet connection is stable.
- **Script Errors:** If there are any errors in the script, refer to the error message for more details and fix the mentioned issues.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

By using this script, you can easily transcribe voice messages in Telegram without manual intervention.
