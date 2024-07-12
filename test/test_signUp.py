from pages.sign_up import SignUp
def test_signupvalid(browser):
    p1=SignUp(browser)
    p1.sign_upvalid()
def test_signupinvalid(browser):
    p1=SignUp(browser)
    p1.sign_upinvalid()



