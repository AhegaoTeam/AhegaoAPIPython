import time

from ahegao import AhegaoAPI, APISession

if __name__ == '__main__':
    t1 = time.time()

    ses = APISession()
    api = AhegaoAPI(ses, v="1", p="ahegao", token="")
    a = api.users.get(user_id=1)
    print(a)

    print(f"Время исполнения: {time.time() - t1} sec.")
