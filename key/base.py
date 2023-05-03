"""
 selenium关键字驱动类:常用操作行为封装为各类关键字
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.common.exceptions import NoSuchElementException,InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium的故事.mouse_keyboard.mouse_keyboard import m
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with
import os
options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)  # 不自动关闭
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument("--disable-blink-features=AutomationControlled")  # 防止检测到webdriver
# options.add_argument('headless') # 无头模式
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")  # 防反爬
class decrator:
    def __init__(self,func):
        self.func=func
    def __get__(self,instance,owner):
        return self.func(instance)

class keys(object):

    # 构造函数
    def __init__(self):
        self.driver = webdriver.Edge(options=options)
        self.driver.implicitly_wait(10)
        self.m = m()

    # 访问url
    def open(self, url: str):
        self.driver.get(url)

    # 定位元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 定位一组元素
    def locates(self, name, value):
        return self.driver.find_elements(name, value)

    # 点击操作
    def click(self, name, value):
        self.locate(name, value).click()

    # 输入
    def input(self, name, value, text):
        self.locate(name, value).send_keys(text)

    # 退出
    @property
    def quit(self):
        return self.driver.quit

    # 显示等待
    def web_el_wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locate(name, value), message='没找到')

    # 强制等待
    def wait(self, txt):
        sleep(txt)

    # 切换iframe
    def switch_frame(self, value, name=None):
        try:
            self.driver.switch_to.frame(self.locate(By.ID, value))
        except InvalidSelectorException:
            try:
                self.driver.switch_to.frame(self.locate(By.NAME, value))
            except InvalidSelectorException:
                self.driver.switch_to.frame(self.locate(By.XPATH, value))

    # 切换default窗体
    def switch_default(self):
        self.driver.switch_to.default_content()

    # 切换Windows窗体
    def switch_handle(self, a: int, close=False):
        handles = self.driver.window_handles  # 获取句柄，得到的是一个列表
        if close:
            self.driver.close()
        else:
            self.driver.switch_to.window(handles[a])  # 切换至最新句柄

    # 断言文本信息
    def assert_text(self):
        try:
            reality = self.locate(name, value).text
            assert expect == reality, f'断言失败，实际结果wei{reality}'
            return True
        except Exception as e:
            print('断言失败信息:' + str(e))
            return False

    # 运用js
    def js(self, value, *args):
        return self.driver.execute_script(value, *args)

    # 键盘点enter
    def c_enter(self, name, value):
        self.locate(name, value).send_keys(Keys.ENTER)

    # 接受断言

    def accept_assert(self):
        a = self.driver.switch_to.alert
        return a.accept()

    def dismiss_assert(self):
        a = self.driver.switch_to.alert
        return a.dismiss()

    # 最大化并点击edge出来的断言
    @decrator
    def max(self):
        self.driver.maximize_window()
        self.m.left_click(891, 384)
        return None

    # 获得当前url
    @property
    def get_url(self):
        return self.driver.current_url

    # 截屏
    def png(self, filename):
        self.driver.get_screenshot_as_file(filename)

    # 窗口大小
    @property
    def size(self):
        return self.driver.get_window_size()

    # 设置窗口大小
    def set_size(self, width, height):
        return self.driver.set_window_size(width, height)

    # 动作链的开始
    @property
    def actionchain(self):
        return ActionChains(self.driver)
    # 删除文件
    def remove(self,path):
        os.remove(path)

    # 相对定位的右边
    def right(self, tag_name, element):
        try:
            return self.driver.find_element(locate_with(By.TAG_NAME, tag_name).to_right_of(element))
        except NoSuchElementException:
            return self.driver.find_element(locate_with(By.XPATH, tag_name).to_right_of(element))


    # 相对定位的左边
    def left(self,tag_name,elememnt):
        return self.driver.find_element(locate_with(By.TAG_NAME,tag_name).to_left_of(elememnt))

    # 相对定位的上面
    def above(self,value,element_or_locator):
        return self.driver.find_element(locate_with(By.TAG_NAME,value).above(element_or_locator=element_or_locator))
    # 相对定位的下面
    def buttom(self,value,element_or_locator):
        return self.driver.find_element(locate_with(By.TAG_NAME,value).below(element_or_locator=element_or_locator))
    def near(self,value,element_or_locator):
        return self.driver.find_element(locate_with(By.TAG_NAME,value).near())
    # 刷新页面
    def re_page(self):
        self.driver.refresh()
    def back(self):
        self.driver.back()
