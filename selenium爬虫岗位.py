import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime,date
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()

df = pd.DataFrame()
for page in range(1,2):
    driver.get(r'https://www.zhipin.com/web/geek/job?query=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&city=100010000&position=101308&jobType=1901')
    current_handle = driver.current_window_handle
    for item in range(1,31):

        xpath = f"/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[{item}]/div[1]/a/div[1]"
        time.sleep(3)
        # 切换到第二个标签页
        for handle in driver.window_handles:  # 始终获得当前最后的窗口
            driver.switch_to.window(handle)

        name = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
            item) + ']/div[1]/div/div[2]/h3/a').text
        gangwei = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
            item) + ']/div[1]/a/div[1]/span[1]').text

        try:
            guimo = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
                item) + ']/div[1]/div/div[2]/ul/li[3]').text
        except:
            guimo = None
        hangye = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
            item) + ']/div[1]/div/div[2]/ul/li[1]').text
        gongzi = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
            item) + ']/div[1]/a/div[2]/span').text
        try:
            fuli = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
                item) + ']/div[2]/div').text
        except:
            fuli = None
        jingyan = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
            item) + ']/div[1]/a/div[2]/ul/li[1]').text
        xueli = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
            item) + ']/div[1]/a/div[2]/ul/li[2]').text
        address = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
            item) + ']/div[1]/a/div[1]/span[2]/span').text
        try:
            keys = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(
                item) + ']/div[2]/ul').text
        except:
            keys = None
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)
        for handle in driver.window_handles:
            if handle != current_handle and handle != driver.current_window_handle:
                driver.switch_to.window(handle)
                break
        time.sleep(1)
        try:
            yaoqiu = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]').text
        except:
            yaoqiu = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]').text
        data = {
            '公司名字': [name],
            '岗位': [gangwei],
            '规模': [guimo],
            '行业': [hangye],
            '工资': [gongzi],
            '福利': [fuli],
            '经验': [jingyan],
            '学历': [xueli],
            '地址': [address],
            '职责': [yaoqiu],
            '关键词': [keys],
        }
        df = df._append(data, ignore_index=True)
        print(df)
        driver.close()
        time.sleep(1)


    for handle in driver.window_handles:  # 始终获得当前最后的窗口
        driver.switch_to.window(handle)
    time.sleep(1)

# 保存DataFrame为Excel文件
df.to_excel('E:/Boss-人工智能12.xlsx', index=False)
