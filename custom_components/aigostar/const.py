"""Constants for the Aigostar integration."""

DOMAIN = "aigostar"

# Alibaba Cloud IoT EU endpoint
ALIBABA_IOT_HOST = "eu-central-1.api-iot.aliyuncs.com"
ALIBABA_IOT_BASE = f"https://{ALIBABA_IOT_HOST}"
ENDPOINT_GET     = "/thing/properties/get"
ENDPOINT_SET     = "/thing/properties/set"

# API credentials extracted from the AigoSmart Android APK (public, not user secrets)
APP_KEY    = "28770785"
APP_SECRET = "41fd4a1eb18fa7ace5e2abbbe3867f93"

# Config entry keys
CONF_EMAIL       = "email"
CONF_PASSWORD    = "password"

# TSL properties for Aigostar TG7100C (captured via /thing/tsl/get)
PROP_SWITCH     = "LightSwitch"       # bool  0=off 1=on
PROP_BRIGHTNESS = "Brightness"        # int   1-100 (percentage)
PROP_COLOR_TEMP = "ColorTemperature"  # int   0-100 (0=warm 2700K, 100=cool 6500K)
PROP_LIGHT_MODE = "LightMode"         # enum  0=white 1=color(RGB)

# Kelvin <-> Aigostar percentage conversion
KELVIN_WARM = 2700   # ColorTemperature = 0
KELVIN_COOL = 6500   # ColorTemperature = 100

# HA brightness 1-255 <-> Aigostar 1-100
HA_BRIGHT_MAX   = 255
AIGO_BRIGHT_MIN = 1
AIGO_BRIGHT_MAX = 100

SCAN_INTERVAL_SECONDS = 30

# TSL properties for Aigostar fans (captured via /thing/tsl/get on
# productKey a1mZFNZz7pq, categoryKey "fan")
PROP_FAN_POWER     = "powerstate"              # bool  0=off 1=on
PROP_FAN_SPEED     = "windspeed"               # enum  1|2|3
PROP_FAN_MODE      = "mode"                    # enum  0=normal 1=natural 2=sleep
PROP_FAN_OSCILLATE = "angleAutoLROnOff"        # bool  left/right auto swing
PROP_FAN_TIMER     = "appointmentClosingTime"  # int   0-24 h auto-off
PROP_FAN_BUZZER    = "buzzerSwitch"            # bool  key beep

FAN_SPEEDS = [1, 2, 3]
FAN_PRESET_MODES = {0: "Normal", 1: "Natural", 2: "Sleep"}
