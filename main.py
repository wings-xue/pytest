from test_func import generateTestFunc
from test_func import judgeFuncParam

def main():
    s = generateTestFunc(funcName="func")
    print(s)
def  t(a, b =1, c=2): 
        return a

if __name__ == '__main__':
    
    print(judgeFuncParam(t))