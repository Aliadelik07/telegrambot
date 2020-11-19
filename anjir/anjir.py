import datetime
from BotHandler import BotHandler
#what bot to whom
token = '809514744:AAFWCeoM-XjFvndmjlG1GNJ6ayG6QNJr8ww'
cid = '-1001392689777'
me = '80987657'

Anjir = BotHandler(token)

#timespace
i = datetime.datetime.today().weekday()
guys =["@MmdFoov","@the_doomed_fallen","@NedKt","@Aliadelimahi","@AidaaAl","@TheManWithoutConcentration","@ryoeyi"]
'''
#cleaning
new_offset = 0
all_updates=Anjir.get_updates(new_offset)
if len(all_updates) > 0:
    for current_update in all_updates:
        first_update_id = current_update['update_id']
        if 'message' in current_update:
            Anjir.delete_message(cid,int(current_update['message']['message_id'])-20)
        new_offset += 1
'''
#instruction

p1 = 'هر روز یک یا چند نفر از اعضا ( به ترتیب تعیین شده در هر دوره)  یک پست ( یا بیشتر) برای روز آماده می کند. این پست می تواند یکی از وقایعی باشد که در منابع موجود منتشر شده است یا شرحی از واقعه دیگری درباره ایران یا منطقه که در این منابع نیامده اند. اولویت انتخاب با مطالب مربوط به اقدامات موفق در مبارزات و جنبش های اجتماعی و سیاسی و بعد از آن تولد یا مرگ شخصیت های مبارز است.'
p2 = 'درصورتی که مقاله یا مطلب تکمیلی درباره موضوع موجود است، لینک آن را در انتهای پست بیاورید.'
p3 = 'بعد از اینکه هر پست در گروه قرار می گیرد، باقی اعضا آن را می خوانند و اصلاحات ترجمه، نگارش و ویرایش را مطرح می کنند. بعد از چند ساعت (در همان تاریخ) نگارنده پست آن را در کانال منتشر می کند.'
p4 = 'در انتهای هر پست آدرس کانال را بنویسید: @TarTaKar'
p5 = 'https://twitter.com/wrkclasshistory?s=09'
p6 = 'https://twitter.com/radicaldaily'
p7 = 'http://www.iranianshistoryonthisday.com/farsi.asp'
p8 = 'http://www.thepeoplehistory.com/this-day-in-history.html'
p9 = 'https://mashruteh.org/wiki/index.php?title=روزنامه_اطلاعات'
Anjir.send_message(cid, p1+'\n'+p2+'\n'+p3+'\n'+p4+'\n'+p5+'\n'+p6+'\n'+p7+'\n'+p8+'\n'+p9)
Anjir.send_message(cid,guys[i])
