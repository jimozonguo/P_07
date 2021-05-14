import os, sys
sys.path.append(os.getcwd())
from base.page_base import PageBase #导入页面基类
from selenium.webdriver.common.by import By

class PageJiaoyimao(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver)

    loc_my=By.XPATH,["text,我的,1","resource-id,com.jym.mall:id/indicator_tab_tv,1","class,android.widget.TextView,1"]
    loc_loginOrReg=By.ID,"com.jym.mall:id/user_account"
    loc_uc=By.ID,"com.jym.mall:id/btn_login_uc"
    loc_zanhao=By.ID,"com.jym.mall:id/login_input"
    loc_pwd=By.ID,"com.jym.mall:id/login_input"
    loc_login=By.ID,"com.jym.mall:id/login_normal"
    loc_username=By.ID,"com.jym.mall:id/user_account"
    loc_loginOut=By.ID,"com.jym.mall:id/tv_logout"

    # 步骤1：定位元素“我的”，并点击
    def click_my(self):
        self.click(loc=PageJiaoyimao.loc_my)


    # 步骤2：定位元素“登录/注册”，并点击
    def click_loginOrReg(self):
        self.click(loc=PageJiaoyimao.loc_loginOrReg)

    # 步骤3：定位元素“UC按钮”，并点击
    def click_uc(self):
        self.click(loc=PageJiaoyimao.loc_uc,time=10)

    # 步骤4：定位元素“账号”，并输入“13760453683”
    def input_zanhao(self,zanhao):
        self.input_text(loc=PageJiaoyimao.loc_zanhao,text=zanhao)

    # 步骤5：定位元素“密码”，并输入“JIMOqinyu319”
    def input_pwd(self,pwd):
        ele_pwd=self.find_elements(loc=PageJiaoyimao.loc_pwd)[1]
        ele_pwd.send_keys(pwd);

    # 步骤6：定位元素“登录按钮”，并点击
    def click_login(self):
        self.click(loc=PageJiaoyimao.loc_login)

    # 步骤7: 定位元素“用户名”，并点击
    def click_zanhao(self):
        self.click(loc=PageJiaoyimao.loc_username)

    # 步骤8：定位元素“退出登录”，并点击
    def click_loginOut(self):
        self.click(loc=PageJiaoyimao.loc_loginOut)

