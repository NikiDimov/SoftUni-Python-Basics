our_password = "s3cr3t!P@ssw0rd"


def password(password):
    if password == our_password:
        return "Welcome"
    return "Wrong password!"


print(password(input()))
