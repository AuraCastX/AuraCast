#!/usr/bin/env python3
"""
AuraCast Weather Bot - Automated Weather Alert System
Runs on GitHub Actions every 30 minutes to send weather alerts via Telegram
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path

# Configuration
OPEN_METEO_API = "https://api.open-meteo.com/v1/forecast"
TELEGRAM_API = "https://api.telegram.org/bot"
DATA_FILE = "subscribers.json"

def load_subscribers():
    """Load subscribers from JSON file"""
    if Path(DATA_FILE).exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_subscribers(subscribers):
    """Save subscribers to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(subscribers, f, indent=2)

def get_weather(lat, lng):
    """Fetch weather data from Open-Meteo API"""
    try:
        params = {
            "latitude": lat,
            "longitude": lng,
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,precipitation",
            "hourly": "precipitation_probability,rain",
            "timezone": "auto"
        }
        response = requests.get(OPEN_METEO_API, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

def get_weather_description(code):
    """Convert WMO weather code to description"""
    codes = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤️",
        2: "Partly cloudy ⛅",
        3: "Overcast ☁️",
        45: "Foggy 🌫️",
        48: "Depositing rime fog 🌫️",
        51: "Light drizzle 🌧️",
        53: "Moderate drizzle 🌧️",
        55: "Dense drizzle 🌧️",
        61: "Slight rain 🌦️",
        63: "Moderate rain 🌧️",
        65: "Heavy rain ⛈️",
        71: "Slight snow ❄️",
        73: "Moderate snow ❄️",
        75: "Heavy snow ❄️",
        80: "Rain showers 🌧️",
        81: "Moderate rain showers 🌧️",
        82: "Violent rain showers ⛈️",
        85: "Light snow showers ❄️",
        86: "Heavy snow showers ❄️",
        95: "Thunderstorm 🌩️",
        96: "Thunderstorm with hail ⛈️",
        99: "Thunderstorm with hail ⛈️"
    }
    return codes.get(code, "Unknown Weather")

def get_alert_message(weather_data, subscriber):
    """Generate alert message based on weather conditions"""
    current = weather_data.get("current", {})
    temp = current.get("temperature_2m", 0)
    humidity = current.get("relative_humidity_2m", 0)
    wind = current.get("wind_speed_10m", 0)
    precipitation = current.get("precipitation", 0)
    code = current.get("weather_code", 0)
    description = get_weather_description(code)
    
    lat = subscriber.get("lat")
    lng = subscriber.get("lng")
    user_type = subscriber.get("type", "general")
    
    # Build base message
    message = f"🌍 *AuraCast Weather Update*\n\n"
    message += f"📍 Location: {lat}, {lng}\n"
    message += f"🌡️ Temperature: {temp}°C\n"
    message += f"💧 Humidity: {humidity}%\n"
    message += f"💨 Wind: {wind} km/h\n"
    message += f"☁️ Condition: {description}\n"
    
    if precipitation > 0:
        message += f"🌧️ Precipitation: {precipitation}mm\n"
    
    message += "\n"
    
    # Generate smart advice based on user type and weather
    if code >= 95:
        message += "🚨 *SEVERE ALERT:* Thunderstorm active!\n"
        if user_type == "farmer":
            message += "• Seek shelter immediately\n• Secure loose items\n• Move livestock to shelter"
        elif user_type == "driver":
            message += "• Pull over safely\n• Turn on hazard lights\n• Avoid driving until storm passes"
        else:
            message += "• Stay indoors\n• Avoid outdoor activities"
    
    elif code >= 80:
        message += "⚠️ *WARNING:* Heavy rain detected!\n"
        if user_type == "farmer":
            message += "• Check crop drainage\n• Monitor soil moisture\n• Protect sensitive crops"
        elif user_type == "driver":
            message += "• Reduce speed\n• Increase following distance\n• Use headlights"
        else:
            message += "• Carry umbrella\n• Plan for delays"
    
    elif code >= 61:
        message += "ℹ️ *INFO:* Rain expected\n"
        if user_type == "farmer":
            message += "• Optimal for irrigation\n• Monitor for waterlogging\n• Good growing conditions"
        elif user_type == "driver":
            message += "• Drive carefully\n• Check tire tread\n• Maintain safe distance"
        else:
            message += "• Carry umbrella\n• Plan accordingly"
    
    elif temp > 35:
        message += "🔥 *HEAT ALERT:* High temperature!\n"
        if user_type == "farmer":
            message += "• Increase irrigation\n• Provide shade if possible\n• Monitor for heat stress"
        elif user_type == "driver":
            message += "• Stay hydrated\n• Check vehicle cooling\n• Take breaks"
        else:
            message += "• Stay hydrated\n• Avoid prolonged sun exposure"
    
    elif temp < 0:
        message += "❄️ *FROST ALERT:* Below freezing!\n"
        if user_type == "farmer":
            message += "• Protect frost-sensitive crops\n• Check irrigation systems\n• Monitor overnight"
        elif user_type == "driver":
            message += "• Watch for ice\n• Reduce speed\n• Use winter tires"
        else:
            message += "• Dress warmly\n• Watch for ice"
    
    else:
        message += "✅ *NORMAL:* Conditions are stable\n"
        message += "• Operations can proceed normally\n• Monitor for changes"
    
    message += "\n_Next update in 30 minutes_"
    
    return message

def send_telegram_message(bot_token, chat_id, text):
    """Send message via Telegram Bot API"""
    try:
        url = f"{TELEGRAM_API}{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return response.json().get("ok", False)
    except Exception as e:
        print(f"Error sending Telegram message: {e}")
        return False

def main():
    """Main function to process all subscribers"""
    print(f"[{datetime.now()}] AuraCast Weather Bot Started")
    
    subscribers = load_subscribers()
    print(f"Processing {len(subscribers)} subscribers...")
    
    success_count = 0
    error_count = 0
    
    for subscriber in subscribers:
        try:
            bot_token = subscriber.get("bot_token")
            chat_id = subscriber.get("chat_id")
            lat = subscriber.get("lat")
            lng = subscriber.get("lng")
            
            if not all([bot_token, chat_id, lat, lng]):
                print(f"⚠️ Skipping subscriber with incomplete data")
                continue
            
            # Fetch weather data
            weather = get_weather(lat, lng)
            if not weather:
                error_count += 1
                continue
            
            # Generate and send message
            message = get_alert_message(weather, subscriber)
            if send_telegram_message(bot_token, chat_id, message):
                success_count += 1
                print(f"✅ Alert sent to {chat_id}")
            else:
                error_count += 1
                print(f"❌ Failed to send alert to {chat_id}")
        
        except Exception as e:
            error_count += 1
            print(f"❌ Error processing subscriber: {e}")
    
    print(f"\n[{datetime.now()}] Completed: {success_count} sent, {error_count} failed")

if __name__ == "__main__":
    main()
