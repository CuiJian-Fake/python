
import  sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(sys.path)
from module import main

if __name__ == '__main__':
    # print(__file__)
    # print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.dirname(__file__)))
    main.main()

