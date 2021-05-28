
'''
元素定位:8种简单模式的定位(不算s形式)
find_element_by_name('xxx')--->name='xxx'
find_element_by_class_name('xxxx')--->class='xxxx'
find_element_by_id('xxx')--->id='xx'

面对连接(a标签),我们选用下面2种方案
完全就够了的,为什么要用一个部分的方法?  主要解决连接文字如果很长,就用部分即可
find_element_by_partial_link_text()   部分匹配文字
find_element_by_link_text()  完全匹配文字

根据标签名去定义
find_elements_by_tag_name()--->放弃它.非常非常不好

根据css去定位
find_element_by_css_selector()--->忘记它,几乎也不用,还要学css,忒烦


根据xpath去定位
find_element_by_xpath()---->超级重要
用它方法有2:
1.通过自学后自己手写(需要点时间)
2.用F12自带的(不一定准,大多数时候准)


总结:
1.上班后,id>name>css>xpath>js
2.如果控件没有id和name,请让开发补一个给你
3.有的非标准控件要采用js的方式,这种太难,在这里不细讲(弹出层)
    execute_script(js脚本)
4.find_elements_by_tag_name加复数形式表示找一堆的元素(s在英语中是复数形式)
  工作后非常少用它
5.最最常见的是id,name,xpath和link_text

'''
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
# driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
# driver.maximize_window()
#
# driver.find_element_by_xpath('//*[@id="loginPanel"]/div[1]/input').send_keys('caichang')
# driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys('caichang1')
#
# driver.find_element_by_xpath("//input[@value='登 录']").click()
# #driver.find_element_by_partial_link_text('记密').click()
#
# #
# # driver.find_element_by_name('username').send_keys('caichang')
# # driver.find_element_by_name('password').send_keys('caichang1')
# # driver.find_element_by_class_name('btn-a').click()
# # driver.find_element_by_link_text()
# driver.find_elements_by_tag_name()

# driver.get('http://192.168.1.36/ecshop/admin/privilege.php?act=login')
# driver.maximize_window()
# sleep(2)
# # driver.find_element_by_link_text('登录').click()
# # #driver.find_element_by_link_text('QQ帐号').click()
# #
# # js='document.querySelector("#pass_phoenix_btn > ul > li.bd-acc-qzone > a")'
# # print(driver.execute_script(js))
#
# print(driver.find_elements_by_tag_name('input'))
# driver.find_element()




