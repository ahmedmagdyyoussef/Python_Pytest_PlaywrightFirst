from Src.PageObject.Locators.HomePageLocators import Locator

class Home():
    def __init__(self, page):

        self.page = page
        self.SearchBox = self.page.get_by_placeholder(Locator.search_box)#driver.find_element(By.XPATH, Locator.search_box)


    def getSearchText(self):
        return self.SearchBox
    def PressSumbit(self):
        self.SearchBox.press("Enter")

    def ClickonSearchbox(self):
         self.SearchBox.click()
    def AddSearchWord(self,SearchKeyWord):
        self.SearchBox.fill(SearchKeyWord)
