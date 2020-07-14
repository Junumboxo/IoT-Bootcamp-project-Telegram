# IoT-Bootcamp-project-Telegram
Telegram bot for the IoT bootcamp 2020 project - an IoT system which helps people with breathing problems and chronic diseases of the respiratory system have more control of their health.

The project is being developed by the team "On Fire" (https://www.facebook.com/makingIoTbeOnFire) within the IoT Bootcamp 2020 organized by Clubul Ingineresc Micro Lab (https://www.facebook.com/MicrolabClub/).

## Structure of the code
*main.py* - main file  
*production.py* - config for deploy  
*development.py* - config for development  
*config.py* - loading the config from production.py or development.py  
*msg_texts.py* - text messages for easier editing in a separated file  
*utils.py* - tools for debugging  
*pip-requirements.txt* - necessary libraries, need to install via `pip install -r pip-requirements.txt`  
*server-requests.py* - get and post requests to the local MQTT server  

Link to the bot - https://t.me/iot_climate_control_bot  
The bot is hosted on https://www.pythonanywhere.com/

## Related repositories:
Arduino code - https://github.com/Junumboxo/IoT-Bootcamp-project-Arduino  
ESP code - https://github.com/rms11-source/IoT---BOOTCAMP/  
Web page with statistics - https://github.com/alexandra0292/alexandra0292.github.io  
Telegram bot - https://github.com/Junumboxo/IoT-Bootcamp-project-Telegram  
Local MQTT server - https://github.com/rms11-source/Smart-Home  
AI - https://github.com/Junumboxo/IoT-project-bootcamp-AI
