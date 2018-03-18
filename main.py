import telebot 
import pywapi 

token = 'TOKEN' 
startAnswer = "привет. введите /help для получения информации. либо название города и страны через запятую для получения прогноза погоды" 
helpAnswer = "я показываю погоду. пример для ввода: rome, italy" 
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['help']) 
def handle_text(message): 
    bot.send_message(message.chat.id, helpAnswer) 

@bot.message_handler(commands=['start']) 
def handle_start(message): 
    bot.send_message(message.chat.id, startAnswer)  

@bot.message_handler(content_types=['text']) 
def handle_text(message): 
    try:
        city = pywapi.get_location_ids(message.text)
        for i in city: 
            cityCode = i 
        weather_com_result = pywapi.get_weather_from_weather_com(cityCode) 
        weatherReport = "It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "°C now in " + message.text + "." + "\n" + "Feels like " + weather_com_result['current_conditions']['feels_like'] + "°C. \n" + "Last update - " + weather_com_result['current_conditions']['last_updated']
        bot.send_message(message.chat.id, weatherReport) 
    except:
        bot.send_message(message.chat.id, 'нет такого города и страны') 

bot.polling(none_stop=True, interval=0)