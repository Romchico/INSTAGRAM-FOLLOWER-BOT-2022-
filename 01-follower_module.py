

def follower_start(link, cookie="user-data-dir=C:\\Users\\Romka\\Desktop\\cookie1", post_place=0):
    """We should use same cookie, to not log in every time. For first time, you should login manually.
       For new cookie, you only need to create new folder and
       assign the path. The link depends on which account followers you want to follow.
       post_place indicates which post(starting from last post) place you want to follow the likes."""
    from time import sleep
    import random
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import smtplib
    

    def driver_start():
        option = Options()
        option.add_argument("--disable-notifications")
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.add_argument(f"{cookie}")
        print(f'{cookie}')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=option)
        return driver

    
    try:
        chrome_driver_path = "C:\\Users\\Romka\\Desktop\\SELENIUM\\chromedriver.exe"
        driver = driver_start()
        driver
        action = webdriver.ActionChains(driver)
        sleep(15)
        driver.get(link)
        sleep(15)
        bars = driver.find_elements(By.XPATH,value='//div[contains(@class,"_aabd _aa8k _aanf")]')
        sleep(10)
        bars[post_place].click()
        sleep(15)

    except:
        driver.close()
        print('Error occurred before coming to following part')
        email= "YOUR EMAIL"
        email2= "SAME EMAIL OR OTHER EMAIL"
        password = "PASSWORD FOR 3RD PARTY GMAIL" #You can create from gmail easily
        smtp_object = smtplib.SMTP("smtp.gmail.com",587)
        smtp_object.ehlo()
        smtp_object.starttls()
        smtp_object.login(email,password)
        subject = "Report-follower"
        msg = "Subject: " + subject + "\n\n" + "Error occurred before coming to following part"
        msg = msg.encode('utf8')
        smtp_object.sendmail(from_addr=email,to_addrs=email2,msg=msg)
        smtp_object.quit()


    try:
        bar = driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div')
        print('The like tab without and')
        sleep(5)                                  
        bar.click()
#The XPATH changes if the like tab with and!
    except:
        bar = driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a/div')
        print('The like tab with and')
        sleep(5)                                                    
        bar.click()                               


    sleep(10)

    bar = driver.find_elements(By.XPATH, value='//div[contains(@class, "_aacl _aaco _aacw _aad6 _aade")]')

    try:
        z = 0
        for i in range(2, random.randint(9,10)): # Random numbers to be not detected.
            if bar[i].text == 'Requested' or bar[i].text == 'Unfollow':
                print(i-1, 'person is already followed!')
                z += 1
                continue

            bar[i].click()
            print(i - z - 1, 'people has been followed')
            sleep(random.uniform(3.5, 5))


        print(i-z,'people has been followed totally!')

        email= "YOUR EMAIL" #**
        email2= "SAME EMAIL OR OTHER EMAIL"
        password = "PASSWORD FOR 3RD PARTY GMAIL" #You can create from gmail easily
        smtp_object = smtplib.SMTP("smtp.gmail.com",587)
        smtp_object.ehlo()
        smtp_object.starttls()
        smtp_object.login(email,password)
        subject = "Report-follower"
        msg = "Subject: " + subject + "\n\n" + "Succesfully completed " +f"{i-z} people has been followed"
        msg = msg.encode('utf8')
        smtp_object.sendmail(from_addr=email,to_addrs=email2,msg=msg)
        smtp_object.quit()

    except:
        driver.close()
        email= "YOUR EMAIL" #**
        email2= "SAME EMAIL OR OTHER EMAIL"
        password = "PASSWORD FOR 3RD PARTY GMAIL" #You can create from gmail easily
        smtp_object = smtplib.SMTP("smtp.gmail.com",587)
        smtp_object.ehlo()
        smtp_object.starttls()
        smtp_object.login(email,password)
        subject = "Report-follower"
        msg = "Subject: " + subject + "\n\n" + "There was an error while following."
        msg = msg.encode("utf8")
        smtp_object.sendmail(from_addr=email, to_addrs=email2  msg=msg)
        smtp_object.quit()
