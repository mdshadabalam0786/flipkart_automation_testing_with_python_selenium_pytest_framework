from pages.login import Login
def test_loginvalid(browser):
    p1=Login(browser)
    p1.loginInvalid()

def test_logininvalid(browser):
    p1=Login(browser)
    p1.loginvalid()


