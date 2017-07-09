from page_objects import PageObject, PageElement, MultiPageElement

class PageElements(PageObject):
    bmw_filter = PageElement(xpath="//form[contains(@class, 'form')]/div/ul/li[6]")
    cars = MultiPageElement(class_name='car-name-top')
