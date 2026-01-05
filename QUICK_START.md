# AuraCast Quick Start Guide ⚡

Get up and running in 5 minutes!

## Step 1: Create Your Telegram Bot (2 minutes)

1. Open Telegram
2. Search for **@BotFather** and open it
3. Send `/newbot`
4. Follow the prompts to name your bot
5. **Copy your Bot Token** (save it somewhere safe)

Example token: `1234567890:ABCdefGHIjklmnoPQRstuvWXYZ`

## Step 2: Get Your Chat ID (1 minute)

1. Send a message to your bot (any message)
2. Open this URL in your browser (replace with your token):
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
3. Look for `"id": 123456789` - that's your Chat ID

## Step 3: Fork the Repository (1 minute)

1. Go to [GitHub AuraCast Repository](https://github.com/yourusername/auracast)
2. Click **Fork** button (top right)
3. This creates your own copy

## Step 4: Update Your Data (1 minute)

1. In your forked repository, click on `subscribers.json`
2. Click the **Edit** button (pencil icon)
3. Replace the example data:
   ```json
   [
     {
       "bot_token": "YOUR_BOT_TOKEN_HERE",
       "chat_id": "YOUR_CHAT_ID_HERE",
       "lat": 52.52,
       "lng": 13.41,
       "type": "farmer",
       "name": "Your Name"
     }
   ]
   ```
4. Click **Commit changes**

## Step 5: Enable GitHub Actions (1 minute)

1. Go to **Actions** tab in your repository
2. Click **Enable workflows**
3. Done! ✅

## That's It! 🎉

Your weather bot is now running! You'll receive alerts every 30 minutes automatically.

### Test It

1. Go to the **Actions** tab
2. Click on the latest workflow run
3. Check if it says ✅ (success) or ❌ (failed)

### First Alert

You should receive your first alert within the next 30 minutes. If not, check:
- Is your bot token correct?
- Is your chat ID correct?
- Have you sent at least one message to your bot on Telegram?

## Customize Your Location

To change your location:

1. Open `subscribers.json`
2. Update `lat` and `lng` values
3. Find coordinates at [Google Maps](https://maps.google.com) - right-click and select coordinates

Example coordinates:
- **New York**: lat: 40.7128, lng: -74.0060
- **London**: lat: 51.5074, lng: -0.1278
- **Dubai**: lat: 25.2048, lng: 55.2708
- **Tokyo**: lat: 35.6762, lng: 139.6503

## Add More Users

To add more people receiving alerts, add more entries to `subscribers.json`:

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

## User Types

Choose the type that matches your needs:
- **farmer**: Alerts for crops, irrigation, frost
- **driver**: Alerts for road safety, visibility
- **company**: Alerts for operational impact
- **general**: Generic weather alerts

## Need Help?

Check the full [README.md](README.md) for detailed troubleshooting and advanced setup.

---

**Enjoy your weather intelligence! 🌤️**
