Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import logging
... from telegram.ext import Updater, CommandHandler
... import requests
... 
... # توکن ربات تلگرامی که از BotFather گرفتی
... TOKEN = '7661699236:AAF02TDKZPfs_N3naErzO29GiOWhqA7p8tg'
... 
... # تنظیمات logging برای خطاها
... logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
...                     level=logging.INFO)
... logger = logging.getLogger(__name__)
... 
... # تابع برای ارسال قیمت ارز دیجیتال
... def get_price(update, context):
...     # نام ارز دیجیتال (مثلاً 'bitcoin' یا 'ethereum') از کاربر می‌گیریم
...     coin = ' '.join(context.args).lower()
...     if not coin:
...         update.message.reply_text('لطفاً نام ارز دیجیتال رو وارد کن. مثلا /price bitcoin')
...         return
... 
...     # گرفتن قیمت ارز از CoinGecko
...     url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
...     response = requests.get(url)
...     data = response.json()
... 
...     # بررسی اینکه آیا ارز در دسترس است یا نه
...     if coin in data:
...         price = data[coin]['usd']
...         update.message.reply_text(f'قیمت {coin} در حال حاضر: ${price}')
...     else:
...         update.message.reply_text(f'ارز {coin} پیدا نشد. لطفاً نام ارز رو درست وارد کن.')
... 
... # تنظیمات اصلی ربات
... def main():
    # ایجاد updater و dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # دستور /price که قیمت ارز رو نمایش می‌ده
    dp.add_handler(CommandHandler('price', get_price))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
