import time
import random
from selenium的故事.key_encapsulation.web_keys.base import keys,decrator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




class Page(keys):

    # 对于单元素定位
    # 通过id定位
    def id(self, value):
        return self.locate(By.ID, value)

    # 通过name定位
    def name(self, value):
        return self.locate(By.NAME, value)

    # 通过xpath
    def xpath(self, value,n=1):

        return self.locate(By.XPATH,value)

    # 对于一组元素
    def ids(self, value):
        return self.locates(By.ID, value)

    def names(self, value):
        return self.locates(By.NAME, value)

    def xpaths(self, value):
        return self.locates(By.XPATH, value)

    # 输入
    def i_put(self, value, text):
        self.input(By.ID, value, text)

    def nm_put(self, value, text):
        self.input(By.NAME, value, text)

    def x_put(self, value, text):
        self.input(By.XPATH, value, text)

    # 点击
    def i_click(self, value):
        self.click(By.ID, value)

    def nm_click(self, value):
        self.click(By.NAME, value)

    def x_click(self, value):
        self.click(By.XPATH, value)

    def chao_click(self, value):
        self.click(By.PARTIAL_LINK_TEXT, value)

    def click_enter(self, value):
        self.c_enter(By.ID, value)

    # 向下滚动滚轮
    def down_scoll(self, n: int):
        self.js(f'window.scrollBy(0,{n})')

    # 到底部
    @property
    def to_bottom(self):
        return self.js('window.scrollTo(0,document.body.scrollHeight)')

    # 到顶部
    @property
    def to_top(self):
        return self.js('window.scrollTo(document.body.scrollHeight,0)')

    # 对于动态加载的数据需要一直向下加载数据，才可以得到全部数据,返回到顶部
    def dong(self, n=1000):
        temp_height = 0
        while True:
            self.down_scoll(n)
            self.wait(1)
            check_height = self.js("return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
            if check_height == temp_height:
                break
            temp_height = check_height
        self.to_top

    # 下拉框的选择,用id
    def id_xz(self, value):
        a = self.id(value)
        s = Select(a)
        return s

    # 下拉框用index
    def id_index_xz(self, value, n: int):
        self.id_xz(value).select_by_value(n)

    # 下拉框用value
    def id_value_xz(self, value, a: str):
        self.id_xz(value).select_by_value(a)

    # 下拉框用text
    def id_text_xz(self, value, text):
        self.id_xz(value).select_by_visible_text(text)

    # 下拉框的选择,用name
    def name_xz(self, value):
        a = self.name(value)
        s = Select(a)
        return s

    # 下拉框用index
    def name_index_xz(self, value, n: int):
        self.name_xz(value).select_by_index(n)

    # 下拉框用value
    def name_value_xz(self, value, a: str):
        self.name_xz(value).select_by_value(a)

    # 下拉框用text
    def name_text_xz(self, value, text):
        self.name_xz(value).select_by_visible_text(text)

    # 当前屏幕截图
    def get_png_1(self, img_name: str):
        a = time.strftime('%Y%m%d%H%M%S')
        name = a + str(random.randint(11111, 99999)) + '_' + img_name + ".png"
        path = 'C:/Users/520/PycharmProjects/pythonProject4/selenium的故事/截图/'
        self.png(path + name)
        return name

    # 当前屏幕截图

    def get_png_2(self, img_name: str):
        a = time.strftime('%Y%m%d%H%M%S')
        name = a + str(random.randint(11111, 99999)) + '_' + img_name + ".png"
        path = 'C:/Users/520/PycharmProjects/pythonProject4/selenium的故事/截图/'
        self.png(path + name)
        return path + name

    # 窗口高度
    @property
    def height(self):
        return self.size()['height']

    # 窗口宽度
    @property
    def weight(self):
        return self.size()['weight']

    # 元素截图
    def yuansu_png(self, value, filename, n='xpath'):
        if n == 'id':
            self.id(value).screenshot(filename)
        elif n == 'name':
            self.name(value).screenshot(filename)
        else:
            self.xpath(value).screenshot(filename)
        return filename
    # xpath直接输入类名
    def xpath_class(self,cls,div,n=1):

        return f'//*[@class="{cls}"][{n}]'
    # xpath直接输入id
    def xpath_id(self):
        pass
    # 标签的属性
    def get_attr(self,element,value):
        data=element.get_attribute(name=value)
        return data
    # 得到标签的文本
    def get_text(self,element):
        text=element.text
        return text


