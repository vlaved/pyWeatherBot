from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="ZZZZZZZZZZ:ZZZZZZZZZZZZZZZZZZ-ZZZZZZZZZZZZZZZZ")
dp = Dispatcher(bot)
client = python_weather.Client(unit=python_weather.IMPERIAL, locale=python_weather.Locale.RUSSIAN)

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)

    celsius = round((weather.current.temperature - 32) / 1.8)
    # Не нашел вывод локации в удобочитаемом виде, распарсим area
    location = str(weather.nearest_area)
    location = location.replace("<Area name='", "")
    location = location.replace("' country='", ", ")
    location = location[:location.find("' region=")]

    resp_msg = location+ "\n"
    resp_msg += f"Текущая температура {celsius}° \n"
    resp_msg += weather.current.description + "\n"

    await message.answer(resp_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
