import pytest
from time import sleep
from Src.PageObject.Pages.HomePage import Home
from Src.PageObject.Pages.SearchResultPage import SearchResult


@pytest.mark.usefixtures("page")
def test_Youtube(page):

   home = Home(page)
   SearchResultObj = SearchResult(page)
   home.ClickonSearchbox()
   home.AddSearchWord("LambdaTest")
   home.PressSumbit()
   sleep(3)
   AssertionCheck = SearchResultObj.ReturnURLs()
   assert AssertionCheck==1
