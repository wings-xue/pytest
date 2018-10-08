
def ceshiPrint(test: dict) -> str:
    """
    args 
        test: dict , want and result ; 

    """
    want, result = test["want"], test["result"]
    if want != result:
        print("You want {}\n but return {}\n\n".format(want, result))
