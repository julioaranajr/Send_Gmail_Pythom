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
def test_gmail():
    client = gmail.Client.from_env()

    try:
        client.send_email(
            client.email,
            'Testing Python Gmail API',
            'Hello! 👋\n\nThis is a email from Python!\n\nBest Regards!\n\nJulio Arana, Jr.\n@julioaranajr',
        )
    except Exception as e:
        print("Error sending email:", e)

try:
    test_gmail()
    print("Test passed")
except Exception as e:
    print("Test failed Error sending email:", e)
    print(e)
finally:
    print("Sending...\nEmail sent successfully")

# To Run the test type in the terminal:
# python test_send_email.py
