import time,os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.page_jiaoyimao import PageJiaoyimao
import allure


class TestJiaoyimao(object):
    def setup(self):
        self.driver=init_driver()
        self.page_jym=PageJiaoyimao(self.driver);

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @allure.severity("blocker")
    @allure.step(title="功能;用于测试登录UI和登出UI")
    def test_jym_001(self):
        #部分1：介绍测试数据
        #部分2: 测试步骤
        #步骤1：定位元素“我的”，并点击
        allure.attach("","步骤1：定位元素“我的”，并点击")
        self.page_jym.click_my();
        #步骤2：定位元素“登录/注册”，并点击
        allure.attach("","步骤2：定位元素“登录/注册”，并点击")
        self.page_jym.click_loginOrReg();
        #步骤3：定位元素“UC按钮”，并点击
        allure.attach("", "步骤3：定位元素“UC按钮”，并点击")
        self.page_jym.click_uc()
        #步骤4：定位元素“账号”，并输入“13760453683”
        allure.attach("", "步骤4：定位元素“账号”，并输入13760453683")
        self.page_jym.input_zanhao("13760453683");
        #步骤5：定位元素“密码”，并输入“JIMOqinyu319”
        allure.attach("", "步骤5：定位元素“密码”，并输入“JIMOqinyu319”")
        self.page_jym.input_pwd("JIMOqinyu319");
        #步骤6：定位元素“登录按钮”，并点击
        allure.attach("", "步骤6：定位元素“登录按钮”，并点击")
        self.page_jym.click_login();
        #步骤7: 定位元素“账号”，并点击
        allure.attach("", "步骤7: 定位元素“账号”，并点击")
        self.page_jym.click_zanhao();
        #步骤8：定位元素“退出登录”，并点击
        allure.attach("", "步骤8：定位元素“退出登录”，并点击")
        self.page_jym.click_loginOut();
        #部分3：断言