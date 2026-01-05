# AuraCast 🌍

**Beyond the Forecast. Into the Decision.**

AuraCast is a free, intelligent weather alert system that transforms raw weather data into actionable intelligence. Stop reacting to weather. Start deciding with precision.

## Features

✨ **For Farmers**: Protect your crops with precision weather alerts for rain, frost, and extreme heat.

✨ **For Drivers**: Navigate safely with real-time warnings about visibility, heavy rain, and storms.

✨ **For Companies**: Monitor weather impacts on operations with automated team alerts.

## How It Works

1. **Register Your Location**: Enter your coordinates and Telegram bot details on the landing page.
2. **Continuous Monitoring**: Our system checks weather every 30 minutes automatically using GitHub Actions.
3. **Smart Alerts**: Receive intelligent notifications with actionable advice based on weather changes.
4. **Make Better Decisions**: Act on real-time intelligence, not just forecasts.

## Setup Instructions

### Step 1: Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/start` and then `/newbot`
3. Follow the prompts to create a new bot
4. Copy your **Bot Token** (looks like: `123456789:ABCdef...`)

### Step 2: Get Your Chat ID

1. Send a message to your newly created bot
2. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Replace `<YOUR_BOT_TOKEN>` with your actual token
4. Look for the `"id"` field in the response - this is your **Chat ID**

### Step 3: Fork This Repository

1. Click the **Fork** button on GitHub to create your own copy
2. This ensures the workflow runs on your account

### Step 4: Update Subscribers

1. Edit `subscribers.json` in your forked repository
2. Replace the example data with your actual information:
   ```json
   [
     {
       "bot_token": "YOUR_BOT_TOKEN",
       "chat_id": "YOUR_CHAT_ID",
       "lat": 52.52,
       "lng": 13.41,
       "type": "farmer",
       "name": "Your Name"
     }
   ]
   ```
3. Commit and push the changes

### Step 5: Enable GitHub Actions

1. Go to your forked repository
2. Click the **Actions** tab
3. Click **Enable workflows**
4. The weather bot will now run automatically every 30 minutes

### Step 6: Deploy the Landing Page

You can deploy the landing page in multiple ways:

#### Option A: GitHub Pages (Free)
1. Go to **Settings** → **Pages**
2. Select **Deploy from a branch**
3. Choose **main** branch and **/ (root)** folder
4. Your site will be available at `https://yourusername.github.io/auracast`

#### Option B: Netlify (Free)
1. Go to [netlify.com](https://netlify.com)
2. Click **New site from Git**
3. Connect your GitHub repository
4. Deploy!

#### Option C: Vercel (Free)
1. Go to [vercel.com](https://vercel.com)
2. Click **New Project**
3. Import your GitHub repository
4. Deploy!

## File Structure

```
auracast/
├── index.html                    # Landing page
├── weather_bot.py               # Python script that sends alerts
├── subscribers.json             # User data (bot token, location, etc.)
├── .github/
│   └── workflows/
│       └── weather_alerts.yml   # GitHub Actions configuration
└── README.md                    # This file
```

## How the Automation Works

1. **GitHub Actions** runs the `weather_bot.py` script every 30 minutes
2. The script reads all subscribers from `subscribers.json`
3. For each subscriber, it:
   - Fetches current weather from **Open-Meteo API** (free, no key needed)
   - Generates smart alerts based on user type (farmer, driver, company)
   - Sends the alert via **Telegram Bot API**
4. The workflow runs even when your computer is off!

## Weather Alert Types

### For Farmers 🌾
- **Thunderstorm Alert**: Seek shelter, secure items, move livestock
- **Heavy Rain**: Check drainage, monitor soil moisture
- **Heat Alert**: Increase irrigation, provide shade
- **Frost Alert**: Protect crops, check irrigation systems

### For Drivers 🚚
- **Thunderstorm Alert**: Pull over safely, avoid driving
- **Heavy Rain**: Reduce speed, increase following distance
- **Heat Alert**: Stay hydrated, check vehicle cooling
- **Frost Alert**: Watch for ice, use winter tires

### For Companies 🏢
- **Operational Impact**: Monitor weather effects on logistics
- **Team Safety**: Alert teams about severe conditions
- **Schedule Optimization**: Adjust operations based on weather

## API Credits

- **Weather Data**: [Open-Meteo](https://open-meteo.com/) - Free, no API key required
- **Messaging**: [Telegram Bot API](https://core.telegram.org/bots/api) - Free
- **Automation**: [GitHub Actions](https://github.com/features/actions) - Free for public repos

## Customization

### Add More Subscribers

Edit `subscribers.json` and add more entries:

```json
[
  {
    "bot_token": "TOKEN1",
    "chat_id": "ID1",
    "lat": 52.52,
    "lng": 13.41,
    "type": "farmer",
    "name": "User 1"
  },
  {
    "bot_token": "TOKEN2",
    "chat_id": "ID2",
    "lat": 40.71,
    "lng": -74.01,
    "type": "driver",
    "name": "User 2"
  }
]
```

### Change Alert Frequency

Edit `.github/workflows/weather_alerts.yml`:

```yaml
on:
  schedule:
    - cron: '*/15 * * * *'  # Every 15 minutes
```

Cron format: `minute hour day month day-of-week`

### Modify Alert Messages

Edit `weather_bot.py` in the `get_alert_message()` function to customize messages.

## Troubleshooting

### Alerts Not Sending?

1. **Check your Bot Token**: Make sure it's correct in `subscribers.json`
2. **Check your Chat ID**: Verify it's a number (not a username)
3. **Check GitHub Actions**: Go to **Actions** tab and check the logs
4. **Test your bot**: Send a message to your bot on Telegram first

### How to Check GitHub Actions Logs

1. Go to your repository
2. Click **Actions** tab
3. Click on the latest workflow run
4. Click on **send-alerts** job
5. Expand **Run weather bot** to see logs

### Workflow Not Running?

1. Make sure **Actions** are enabled in your repository
2. Check that you've committed the `.github/workflows/weather_alerts.yml` file
3. GitHub Actions might have a slight delay (up to 5 minutes)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the GitHub Actions logs
3. Verify your Telegram bot token and chat ID
4. Open an issue on GitHub

## License

This project is free and open-source. Feel free to modify and share!

## Made with ❤️

AuraCast is built to help farmers, drivers, and companies make better decisions based on weather intelligence. Free for everyone, always.

---

**Happy forecasting! 🌤️**
