# Simple Login Logic in Python Using Boolean


user_username = "biswaszin"
user_password = "biswaszin123"


def check_login_credentials(login_username, login_password):
    username_match = user_username == login_username
    password_match = user_password == login_password

    both_match = username_match & password_match

    return both_match


login_creds_username = "biswaszin"
login_creds_password = "biswaszin124"


isLogin = check_login_credentials(login_creds_username, login_creds_password)
print(f"Login Status: {isLogin}")
