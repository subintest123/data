# suite套件示例
"""
每轮(每次版本)测试,我就增加一个测试套件
在这个套件中加入你要测试的测试用例,执行即可
这样就能说这轮测试到底过关了哪些内容
"""
import unittest

from automation.unittest_study.demo import Mtesting
from automation.unittest_study.demo2 import Ecshop

suite = unittest.TestSuite()
suite.addTest(Mtesting('test_2_one'))
suite.addTest(Ecshop('test_3_tow'))
suite.addTest(Mtesting('test_3_tow'))
suite.addTest(Ecshop('test_5_four'))
runner = unittest.TextTestRunner()
runner.run(suite)