import inspect
from copy import copy


funcName = ""
param = ""


def judgeFuncParam(f)->dict: 
    """判断方法所需要的参数, 由于是python， 
    所以不需要判断类型， 只需要把参数名称获取出来
    """
    func = inspect.getargspec(f)
    return {
        "param": func.args,
        "defaults": fillList(func.defaults, func.args)
    }
   

def fillList(l1, l2):
    _l1, _l2 = l1.copy(), l2.copy()
    
    for i in range(len(_l2)-len(_l1)):
        l1.insert(0, "")
    return l1
 

testFuncStr = f"""
    def {funcName}Test(): 
        print("testing is running")
        args = {
            "name": "",
            "param": {param}, 
            "want": ""
        }

    def main():
        {funcName}Rst = rst{funcName}_test()
        if {funcName}Rst != want:
            print("You want {}\n but return {}\n\n".format(want, result))

    
    if __name__ == '__main__':
        
"""


def generateTestFunc(
    funcName:str,
    testCase:dict={}
    ):

    funcName = funcName
    return testFuncStr



