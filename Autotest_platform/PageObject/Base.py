from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Product.models import Element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from Autotest_platform.PageObject.logger import Logger
import time
import requests
import json
import random

log = Logger(__name__).logger

class PageObject:
    driver = None

    def sleep(self, second):
        if str(second).isdigit():
            time.sleep(int(second))
        else:
            time.sleep(0.5)

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        
    def open_url(self, url):
        """打开URL地址"""
        self.driver.get(url)

    def max_size(self):
        """屏幕最大化"""
        self.driver.maximize_window()

    def click(self, locator):
        """点击元素"""
        if locator is None:
            return
        else:
            try:
                PageObject.find_element(self.driver, locator).click()
            except:
                raise

    def click_point(self, x, y, left_click=True):
        """点击x,y坐标的点"""
        if left_click:
            ActionChains(self.driver).move_by_offset(x, y - 103).click().perform()
        else:
            ActionChains(self.driver).move_by_offset(x, y - 103).context_click().perform()

    def send_keys(self, locator, value):
        """输入框清除内容，然后输入文本"""
        if locator is None:
            return
        if value is None:
            self.clear(locator)
        else:
            PageObject.find_element(self.driver, locator).send_keys(value)
        log.info('开始对%s元素 [输入文本]：%s'%(locator,text))

    def clear(self, locator):
        if locator is None:
            return
        else:
            self.driver.clear()

    def alert_accept(self):
        """获取alert弹窗"""
        self.driver.switch_to.alert().accept()

    def alert_dismiss(self):
        self.driver.switch_to.alert().dismiss()

    def switch_to_window(self, title=None):
        """切换标签页，多个标签页切换"""
        handle = self.driver.current_window_handle
        if title:
            for handle_ in self.driver.window_handles:
                if handle != handle_:
                    self.driver.switch_to.window(handle)
                    if self.driver.title == title:
                        break
            else:
                log.error("未找到标题为：" + title + " 的页面")
                raise ValueError("未找到标题为：" + title + " 的页面")
                
        else:
            for handle_ in self.driver.window_handles:
                if handle != handle_:
                    self.driver.switch_to.window(handle)

    def switch_to_frame(self, locator=None):
        """切换frame"""
        if locator:
            self.driver.switch_to.frame(PageObject.find_element(self.driver, locator))
        else:
            self.driver.switch_to.default_content()

    def forward(self):
        """前进"""
        self.driver.forward()

    def back(self):
        """后退"""
        self.driver.back()
        self.sleep(1)

    def refresh(self):
        """刷新"""
        self.driver.refresh()

    def close(self):
        """关闭页面"""
        self.driver.close()

    def quit(self):
        """关闭浏览器"""
        self.driver.quit()

    def select_by_text(self, element, value, visible=False):
        """下拉框选择"""
        if element is None:
            return
        element = PageObject.find_element(self.driver, element)
        if not visible:
            Select(element).select_by_text(value)
        else:
            Select(element).select_by_visible_text(value)

    @staticmethod
    def find_element(driver, locator, more=False, timeout=20):
        message = locator
        if isinstance(locator, dict):
            locator = (locator.get("by", None), locator.get("locator", None))
            message = locator
        elif isinstance(locator, list) and len(locator) > 2:
            locator = (locator[0], locator[1])
            message = locator
        elif isinstance(locator, Element):
            message = locator.name
            locator = (locator.by, locator.locator)
        elif isinstance(locator, str):
            locator = tuple(locator.split(".", 1))
            message = locator
        else:
            log.error("element参数类型错误: type:" + str(type(locator)))
            raise TypeError("element参数类型错误: type:" + str(type(locator)))
            
        try:
            try:
                if more:
                    return WebDriverWait(driver, timeout).until(ec.visibility_of_all_elements_located(locator))
                else:
                    return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))
            except:
                if more:
                    return WebDriverWait(driver, timeout).until(ec.presence_of_all_elements_located(locator))
                else:
                    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))
        except Exception:
            log.error("找不到元素:" + str(message))
            raise RuntimeError("找不到元素:" + str(message))

    def move_to_element(self, locator):
        """0000"""
        ActionChains(self.driver).move_to_element(self.find_element(self.driver, locator)).perform()

    # def autologin(self, locator1, locator2):
    #     telephone = '181'+''.join(str(random.choice(range(10))) for _ in range(8))
    #     payload = {"telephone": telephone}
    #     r = requests.post('https://your_website/your_api/code', data = payload)
    #     dic = r.json()
    #     code = dic['data']['code']
    #     self.sleep(3)
    #     self.send_keys(locator1, telephone)
    #     self.send_keys(locator2, code)

    def move_jindutiao(self, locator):
        """移动进度条"""
        self.driver.execute_script("arguments[0].scrollIntoView();", PageObject.find_element(self.driver, locator))

    # 鼠标悬停
    def xuanting(self, locator):
        """悬停到元素上"""
        el = PageObject.find_element(self.driver, locator)
        ActionChains(self.driver).move_to_element(el).perform()

    def get_text(self, locator):
        '''获取文本'''
        element =PageObject.find_element(self.driver, locator)
        print('base:获取文本：%s' % element.text)
        return element.text

    def keyboard(self, locator, operation=Keys.ENTER):
        ''' 键盘事件，operation=模拟的键盘值 Keys. '''
        try:
            elememt = PageObject.find_element(self.driver, locator)
            self.send_keys(locator, *operation)
        except BaseException as e:
            log.info("键盘事件异常！ Reason:%s" % e)




    

