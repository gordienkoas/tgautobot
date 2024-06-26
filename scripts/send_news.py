import os
from telebot import TeleBot
import requests
import time

from news_sources.nytimes_news_source import NYTimesNewsSource

bot = TeleBot(
    token=os.environ.get("BOT_TOKEN"),
    parse_mode='html',
    disable_web_page_preview=True
)
chat_id = os.environ.get("CHANNEL_ID")
source = NYTimesNewsSource()

if __name__ == '__main__':
    news_to_post = source.get_news()

    for news in news_to_post:
        photo = source.create_mem_from_photo(news=news)
        caption = source.construct_caption(news=news)

        #photo = requests.get(news.img_url).content
        #caption = source.construct_message(news=news)

        bot.send_photo(
            chat_id=chat_id,
            photo=open(photo, 'rb'),
            caption=caption
        )
        print(f'News {news.title} ')
        photo.unlink()
        time.sleep(5)