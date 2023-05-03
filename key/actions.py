from selenium的故事.key_encapsulation.web_keys.page import Page
from PIL import Image

class A(Page):
    # 需要在无头模式下
    def get_long_png(self,wait=1,name=1):
        self.dong()
        page_height = self.js('return document.documentElement.scrollHeight')
        page_width = self.js('return document.documentElement.scrollWidth')
        self.set_size(page_width, page_height)
        self.wait(wait)
        a=self.get_png(f'{name}')
        return a
    # 元素截图
    def yuansu_jpg(self,value,img_name='1'):
        path='C:/Users/520/PycharmProjects/pythonProject4/selenium的故事/截图/'
        self.js('document.body.style.zoom="0.8"')
        file_name = self.get_png_1(img_name)
        a = self.id(value)
        x = a.location['x']
        y = a.location['y']
        dx = x + a.size['width']
        dy = y + a.size['height']
        img = Image.open(f'{path+file_name}')
        img = img.crop((x, y, dx, dy))
        img = img.convert('RGB')
        path=path+img_name+'.jpg'
        img.save(path)
    def get_href(self,element):
        href=self.get_attr(element,value='href')
        return href
