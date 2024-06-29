
# 🌟 Telegram Top Media Explorer

## 📝 Description

Telegram Top Media Explorer is a Python tool that analyzes Telegram groups to find the most popular media messages (images and files) based on the number of reactions. This script is perfect for those who want to discover the most engaging content in Telegram groups!

## ✨ Features

-   🔍 Automatically joins the specified Telegram group
-   📥 Downloads all messages from the group
-   🖼️ Filters messages containing files or images
-   🏆 Ranks messages by number of reactions
-   💾 Saves the top 30 most reacted messages to a text file

## 🚀 How to Use

### Prerequisites

-   Python 3.7+
-   Telethon library
-   Telegram API ID and Hash (obtain from  [https://my.telegram.org](https://my.telegram.org/))

### Installation

1.  Clone the repository:
    
    ```
    git clone https://github.com/your-username/telegram-top-media-explorer.git
    
    ```
    
2.  Enter the project directory:
    
    ```
    cd telegram-top-media-explorer
    
    ```
    
3.  Install dependencies:
    
    ```
    pip install -r requirements.txt
    
    ```
    

### Configuration

1.  Rename  `config_example.py`  to  `config.py`
2.  Edit  `config.py`  and insert your Telegram credentials:
    
    ```python
    API_ID = 'your_api_id'
    API_HASH = 'your_api_hash'
    PHONE_NUMBER = 'your_phone_number'
    GROUP_USERNAME = 'target_group_name'
    
    ```
    

### Execution

Run the main script:

```
python main.py

```

## 📊 Results

The script will generate a  `top_30_media_messages.txt`  file containing the 30 most reacted media messages from the group, including details such as:

-   Ranking position
-   Total number of reactions
-   Date and time of sending
-   Media type (file or image)
-   Message text (if any)

## ⚠️ Legal Disclaimer

This script is for educational and research purposes only. Respect Telegram's terms of service and privacy policies when using this tool.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📜 License

This project is licensed under the  [MIT License](https://chat.lmsys.org/LICENSE).
