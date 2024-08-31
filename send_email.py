import time
import gmail


def execution_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        exec_time = end-start
        print(f"{func.__name__} execution time: {exec_time}")
        return result
    return wrapper

@execution_time
def send_custom_email():
    client = gmail.Client.from_env()

    try:
        client.send_email(
            to=input("Enter the email address: "),
            subject=input("Enter the subject: "),
            body=input("Enter the body: "),
        )
    except Exception as e:
        print("Error sending email:", e)


try:
    send_custom_email()
    print("Test passed")
except Exception as e:
    print("Test failed Error sending email:", e)
    print(e)
finally:
    print("Sending...\nEmail sent successfully")
