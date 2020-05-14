import tweepy
import time
import apiconfig 
from get_data import Get_data



if __name__ == "__main__":
    auth = tweepy.OAuthHandler(apiconfig.API_KEY,apiconfig.API_SECRET_KEY)
    auth.set_access_token(apiconfig.ACCESS_TOKEN,apiconfig.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    user = api.me()

    # # Test if We are Connected
    try:
        api.verify_credentials()
    except Exception as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(str(e))
        print("Error during authentication")

    ## Test Tweet using api
    # api.update_status("Test Tweet via API") 

    data = Get_data()
    data.get_data()
    status = api.update_status(f"India:\nconfirmed cases: {data.india_today_count['totalconfirmed']} (+{data.india_today_count['dailyconfirmed']}) \ndeaths:{data.india_today_count['totaldeceased']} (+{data.india_today_count['dailydeceased']})\nrecovered:{data.india_today_count['totalrecovered']} (+{data.india_today_count['dailyrecovered']})\nactive cases:{int(data.india_today_count['totalconfirmed'])-int(data.india_today_count['totaldeceased'])-int(data.india_today_count['totalrecovered'])}\nMaharashtra:\nconfirmed cases:{data.maharashtra_today_count['confirmed']} (+{data.maharashtra_today_count['deltaconfirmed']})\ndeaths:{data.maharashtra_today_count['deaths']} (+{data.maharashtra_today_count['deltadeaths']})\nrecovered:{data.maharashtra_today_count['recovered']} (+{data.maharashtra_today_count['deltarecovered']})\nactive cases:{data.maharashtra_today_count['active']}\nPune:\nconfirmed cases:{data.pune_today_count['confirmed']} (+{data.pune_today_count['delta']['confirmed']})\ndeaths:{data.pune_today_count['deceased']}\nrecovered:{data.pune_today_count['recovered']}\nactive cases:{data.pune_today_count['active']}")    
    with open("log.txt", 'a') as log_file:
        log_file.write(str(status))
    print(status)

#    print(f"India:\nconfirmed cases: {data.india_today_count['totalconfirmed']} (+{data.india_today_count['dailyconfirmed']}) \ndeaths:{data.india_today_count['totaldeceased']} (+{data.india_today_count['dailydeceased']})\nrecovered:{data.india_today_count['totalrecovered']} (+{data.india_today_count['dailyrecovered']})\nactive cases:{int(data.india_today_count['totalconfirmed'])-int(data.india_today_count['totaldeceased'])-int(data.india_today_count['totalrecovered'])}\nMaharashtra:\nconfirmed cases:{data.maharashtra_today_count['confirmed']} (+{data.maharashtra_today_count['deltaconfirmed']})\ndeaths:{data.maharashtra_today_count['deaths']} (+{data.maharashtra_today_count['deltadeaths']})\nrecovered:{data.maharashtra_today_count['recovered']} (+{data.maharashtra_today_count['deltarecovered']})\nactive cases:{data.maharashtra_today_count['active']}\nPune:\nconfirmed cases:{data.pune_today_count['confirmed']} (+{data.pune_today_count['delta']['confirmed']})\ndeaths:{data.pune_today_count['deceased']}\nrecovered:{data.pune_today_count['recovered']}\nactive cases:{data.pune_today_count['active']}")
    
    ##test for sorted tweet
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)
    #     print((''.join(sorted(tweet.text))).strip())