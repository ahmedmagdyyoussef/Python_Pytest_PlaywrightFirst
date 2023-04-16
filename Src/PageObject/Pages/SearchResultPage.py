
class SearchResult():
    def __init__(self, page):
        self.page = page
    def ReturnURLs(self):
        AssertionFlag = 0
        Counter = 1
        all_quotes = self.page.query_selector_all("//a[@id='video-title']")
        for quote in all_quotes:
            if "LambdaTest" in quote.get_attribute('title'):
                Title = quote.get_attribute('title')
                URL = quote.get_attribute('href')
                print(Title)
                print('www.youtube.com'+URL)
                Counter = Counter + 1
                if Counter >= 11:
                    AssertionFlag = 1
                    print("done ", AssertionFlag)
                    break
        return AssertionFlag
