
def loc(key):
    select = {
    "LOGIN_TITLE": "div.h2-title.align-center",
    "SIGNUP_LINK" : "div.offset-top.align-center > a",
    "BUTTON_FORGET": "div.align-right.offset-bottom > button",
    "BUTTON_ENTER" : "#sign-in-login-submit",
    "NOT_YET_TEXT":"div.offset-top.align-center > div > span",
    "PHONE_SIGNIN":"form > div:nth-child(1) > input",
    "PASS_SIGNIN":"form > div:nth-child(2) > input",
    "TEXT_MIN_LOGIN":"div.form-group.error > div.error-message",
    "ERROR_LOGIN":"div > div.col-xs-10 > div.title",
            }
    return select.get(key)