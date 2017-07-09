from selenium import webdriver
from unittestzero import Assert
import unittest, time, re
from PageElements import PageElements

class TestAuto1(unittest.TestCase, PageElements):
    
    def setUp(self):
        self.driver = webdriver.Chrome('C:\Python27\Scripts\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.auto1.com/en/our-cars"

    def open_and_select_filter(self):
        driver=self.driver
        page = PageElements(driver)
        page.get(self.base_url)
        page.bmw_filter.click()
        time.sleep(20)
        cars = page.cars
        return page, cars
        
    def test_bmw_filter_was_selected(self):
        page, cars = self.open_and_select_filter()
        assert "checked" in page.bmw_filter.get_attribute("class")

    def test_only_bmw_cars_are_in_list(self):
        cars = self.open_and_select_filter()
        for i in range(1, len(cars)):
            car_names = self.driver.find_element_by_xpath("//*[@id='car-list']/li[%s]/div[1]" % i).get_attribute('innerHTML')
            assert "BMW" in car_names

    def test_each_car_has_picture(self):
        cars = self.open_and_select_filter()
        for i in range(1, len(cars)):
            car_images = self.driver.find_element_by_xpath("//*[@id='car-list']/li[%s]/div[2]/img" % i).get_attribute('src')
            assert "img-pa.auto1.com" in car_images

    def test_each_car_has_complete_info(self):
        cars = self.open_and_select_filter()
        for i in range(1, len(cars)):
            for j in range(1, 7):
                car_info_table = self.driver.find_element_by_xpath("//*[@id='car-list']/li[%s]/div[3]/table/tbody/tr[%s]/td[2]" % (i,j)).get_attribute('innerHTML')
                assert car_info_table != ""

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
