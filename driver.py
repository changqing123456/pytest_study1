import pytest

import os

if __name__ == '__main__':
    pytest.main()
    # 创建且保存ini文件里生成的allure测试报告，且清除上次的报告记录
    os.system('allure generate ./allure_data -o ./allure_report --clean')
    
    # os.system('allure open allure_report')


