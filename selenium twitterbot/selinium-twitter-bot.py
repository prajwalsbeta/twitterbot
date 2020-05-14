from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()

    def login(self):
        bot=self.bot
        bot.get('https://twitter.com/login')
        assert "Twitter" in bot.title
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self,hashtag):
        bot.self.bot
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed_query')
        time.sleep(3)
        for i in range(3):
            bot.execute_script('windows.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets= bot.find_element_by_css_selector('.css-4rbku5.css-18t94o4.css-901oao.r-111h2gw.r-1loqt21.r-1q142lx.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-3s2u2q.r-qvutc0')
            links = [elem.get_attribute('href')for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                time.sleep(3)
                try:
                    bot.find_element_by_xpath('//div[@data-testid="like"]').click
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)

p = TwitterBot('prajstwitterbot@mailcupp.com','secure.password')
p.login()
p.like_tweet("hacking")
