import requests

from bs4 import BeautifulSoup

from aiogram import Bot, Dispatcher, executor, types


# Create the bot
bot = Bot(token="6189754507:AAEqP5ZaGY1BMWZc3ZbYevC5tKcXrmqzQs4")

# Create dispatcher object to catch incoming codes

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async  def send_hello(message: types.Message):
    await message.answer("Hello there, if you want the last news enter /news code")

@dp.message_handler(commands=["news"])
async def send_news(message: types.Message):
    pass

    # Create a get requests
    response = requests.get("https://teknolojiaihl.meb.k12.tr/")

    # Look at the answer
    message.reply(f"Status code: {response.status_code}")
    print(response.status_code)
    """print(response.text)"""

    # Parse the answer with BeautifulSoup

    soup = BeautifulSoup(response.content, "html.parser")

    # Print title
    await message.answer(f"Kaynak: {soup.title.text}")
    print(soup.title.text)
    """print(soup.find_all("a"))"""

    # Get news

    news = soup.find("div", attrs={"id": "haber_blok"})
    # print(news)
    message_text = "NEWS \n"
    for report in news.find_all("p"):
        message_text += report.text + "\n"
        print(report.text)

    await  message.answer(message_text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)