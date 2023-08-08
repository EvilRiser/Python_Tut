try:
    raise TypeError("Hello, World!")  # line 2
except Exception as e:
    print(
        type(e).__name__,          # TypeError
        __file__,                  # /tmp/example.py
        e.__traceback__.tb_lineno  # 2
    )