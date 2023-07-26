from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
import pytest
from utilities.customlogging import LogGen

class Test_001_loginPage:
    baseURL=Readconfig.getApplicationUrl()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.LogGen()


    def test_home_page_title(self,setup):
        self.logger.info("**************** test_home_page_title ****************")
        self.logger.info("**************** Verify home page title ****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title =="Your store. Login":
            assert True
            self.logger.info("**************** test_home_page_title Test is Passed ****************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_home_page_title.png")
            self.logger.error("**************** test_home_page_title Test is Failed ****************")
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.logger.info("**************** test login ****************")
        self.logger.info("**************** Verify login page ****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************** login page is Passed  ****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.logger.error("**************** Login page test is failed ****************")
            self.driver.close()
            assert False











