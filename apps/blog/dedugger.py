import time


def debugger(func):
    from django.db import connection

    def inner(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        after = time.time()
        print("\n\n")
        print("-" * 80)
        for query in connection.queries:
            print(query["sql"], query["time"])
        print("COUNT: ", len(connection.queries))
        print("TIME: ", after - before)
        print("-" * 80)
        print("\n\n")
        return result

    return inner
