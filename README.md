# YouTube Channel Analytics Scraper

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![YouTube API](https://img.shields.io/badge/YouTube_API-FF0000?style=flat-square&logo=youtube&logoColor=white)

## 📋 Overview

A Python tool that extracts YouTube channel analytics and video performance metrics using the YouTube Data API v3. Built for digital marketing consultants and content creators who need to track channel statistics and video performance efficiently.

This tool automates the collection of subscriber counts, view metrics, video statistics, and exports the data in both JSON and CSV formats for easy analysis.

## ✨ Features

- 📊 **Channel Statistics**
  - Subscriber count
  - Total channel views
  - Total video count
  - Channel ID lookup by name

- 🎥 **Video Metrics** (configurable number of videos)
  - Video titles and IDs
  - View counts
  - Like counts
  - Comment counts
  - Date-stamped data collection

- 💾 **Dual Export Format**
  - JSON format for programmatic access
  - CSV format for spreadsheet analysis
  - Automatic filename with current date

- 🔄 **Pagination Support**
  - Fetches videos across multiple pages
  - Configurable maximum video limit
  - Progress indicators during fetching

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **YouTube Data API v3** - Official Google API for YouTube data
- **Requests** - HTTP library for API calls
- **google-api-python-client** - Official Google API client
- **python-dotenv** - Environment variable management
- **JSON/CSV** - Data export formats

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- YouTube Data API key from Google Cloud Console
- pip (Python package installer)

### Setup

1. **Clone this repository:**
```bash
   git clone https://github.com/adenikinju-nicholas/youtube-analytics-scraper.git
```

2. **Navigate to project directory:**
```bash
   cd youtube-analytics-scraper
```

3. **Install required packages:**
```bash
   pip install -r requirements.txt
```

4. **Get YouTube Data API Key:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project (or select existing)
   - Enable **YouTube Data API v3**
   - Create credentials → API Key
   - Copy your API key

5. **Set up environment variables:**
   - Create a `.env` file in the project directory
   - Add your API key:
```
     YOUTUBE_API_KEY=your_api_key_here
```

## 🚀 Usage

### Basic Usage

1. **Run the script:**
```bash
   python main.py
```

2. **Enter channel name when prompted:**
```
   Enter channel name: MrBeast
```

3. **The script will:**
   - Find the channel ID
   - Fetch channel statistics (subscribers, views, total videos)
   - Retrieve the latest 20 videos (configurable)
   - Display video metrics in terminal
   - Export data to JSON and CSV files

### Sample Output in Terminal
```
Channel ID: UCX6OQ3DkcsbYNE6H8uQQuVA
The channel name MrBeast, has 123000000 subscribers and 25000000000 views and 741 videos

Title: I Gave My 100,000,000th Subscriber An Island
Views: 85234567
Likes: 4523456
Comments: 234567

Title: $1 vs $500,000 Experiences
Views: 72345678
Likes: 3456789
Comments: 187654

...

Saved video details to: videos_2026-01-17.json
Saved video details to: videos_2026-01-17.csv
```

### Customizing Video Limit

Edit `main.py` line 40:
```python
max_videos_to_fetch = 20  # Change to desired number (e.g., 50, 100)
```

## 📊 Sample Output Files

### JSON Output (`videos_2026-01-17.json`)
```json
[
    {
        "date_fetched": "2026-01-17",
        "title": "I Gave My 100,000,000th Subscriber An Island",
        "video_id": "abc123xyz",
        "views": "85234567",
        "likes": "4523456",
        "comments": "234567"
    },
    {
        "date_fetched": "2026-01-17",
        "title": "$1 vs $500,000 Experiences",
        "video_id": "def456uvw",
        "views": "72345678",
        "likes": "3456789",
        "comments": "187654"
    }
]
```

### CSV Output (`videos_2026-01-17.csv`)
```csv
date_fetched,title,video_id,views,likes,comments
2026-01-17,I Gave My 100,000,000th Subscriber An Island,abc123xyz,85234567,4523456,234567
2026-01-17,$1 vs $500,000 Experiences,def456uvw,72345678,3456789,187654
```

## ⚙️ Configuration

### API Key Setup
The script uses `.env` file for secure API key storage:

**.env file:**
```
YOUTUBE_API_KEY=AIzaSyDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Never commit your `.env` file to Git!** (already included in `.gitignore`)

### Adjustable Parameters

In `main.py`, you can modify:
```python
# Line 40: Maximum videos to fetch
max_videos_to_fetch = 20  # Change to 50, 100, etc.

# Line 50: Results per API request (max 50)
playlist_url = f"...&maxResults=10"  # Change to 50 for faster fetching
```

## 📁 Project Structure
```
youtube-analytics-scraper/
│
├── main.py                    # Main script (your code)
├── .env                       # API key (YOU create this - not in Git)
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
│
└── Output files (auto-generated):
    ├── videos_2026-01-17.json
    └── videos_2026-01-17.csv
```

## 🔧 Dependencies

**requirements.txt:**
```
requests==2.31.0
google-api-python-client==2.108.0
python-dotenv==1.0.0
```

Install all with:
```bash
pip install -r requirements.txt
```

## 📝 How It Works

1. **Channel Lookup**: Uses YouTube Search API to find channel ID by name
2. **Channel Statistics**: Fetches subscriber count, total views, and video count
3. **Uploads Playlist**: Retrieves the channel's uploads playlist ID
4. **Pagination**: Loops through playlist items, fetching video data in batches
5. **Video Details**: For each video, retrieves title, views, likes, and comments
6. **Export**: Saves all data to timestamped JSON and CSV files

## 🚨 Important Notes

### API Quota Limits
- YouTube Data API has **daily quota limits** (10,000 units/day by default)
- Each request consumes units:
  - Search: 100 units
  - Playlist items: 1 unit
  - Video details: 1 unit
- **20 videos ≈ 120 units** (well within limits for multiple runs)

### Best Practices
- **Don't share your API key** - keep it in `.env` file
- **Monitor your quota** in [Google Cloud Console](https://console.cloud.google.com/)
- **Respect rate limits** - the script includes pagination delays
- **Request quota increase** if needed for large-scale data collection

## 🐛 Troubleshooting

### "API key not valid" Error
```bash
# Check your .env file exists and has correct format:
YOUTUBE_API_KEY=your_actual_key_here
# No quotes, no spaces around =
```

### "Module not found" Error
```bash
# Make sure all dependencies are installed:
pip install -r requirements.txt
```

### No Videos Fetched
- Check if the channel name is correct
- Some channels may have restricted API access
- Verify your API key is active in Google Cloud Console

### Quota Exceeded
- Wait 24 hours for quota reset
- Or request quota increase in Google Cloud Console
- Reduce `max_videos_to_fetch` to conserve quota

## 🛣️ Roadmap

- [ ] Add command-line arguments for channel name and video limit
- [ ] Support for multiple channels in batch
- [ ] Historical data tracking and comparison
- [ ] Visualization dashboard with charts
- [ ] Email/Slack notifications for new videos
- [ ] Database storage option (SQLite/PostgreSQL)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool uses the official YouTube Data API v3 and complies with YouTube's Terms of Service. Users are responsible for:
- Managing their own API quotas
- Complying with YouTube's API usage policies
- Not using data for prohibited purposes

## 📧 Contact

**Adenikinju Nicholas**

- 📧 Email: adenikinjunicholas@gmail.com
- 💼 Portfolio: [View My Work](your-canva-portfolio-link)
- 🔗 LinkedIn: https://www.linkedin.com/in/adenikinju-nicholas-b1b9ba72/
- 💻 GitHub: [@adenicholas-dev](https://github.com/adenikinju-nicholas)

---

⭐ **If you find this project useful, please consider giving it a star!**

*Built with ❤️ by Nicholas | Last Updated: January 2026*