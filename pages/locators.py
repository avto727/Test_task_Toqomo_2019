
def loc(key):
    select = {
    "LOGIN_TITLE": "div.h2-title.align-center",
    "SIGNUP_LINK" : "div.offset-top.align-center > a",
    "BUTTON_FORGET": "div.align-right.offset-bottom > button",
    "BUTTON_ENTER" : "#sign-in-login-submit",
    "NOT_YET_TEXT":"div.offset-top.align-center > div > span",
    "PHONE_SIGNIN":"div.form-group.error > input",
    "PASS_SIGNIN":"form > div:nth-child(2) > input",
            }
    return select.get(key)