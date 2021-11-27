try:
    res = requests.get(adress,timeout=30)
except requests.ConnectionError as e:
    print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
    print(str(e))            
    continue
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
    print(str(e))
    continue
except requests.RequestException as e:
    print("OOPS!! General Error")
    print(str(e))
    continue
except KeyboardInterrupt:
    print("Someone closed the program")