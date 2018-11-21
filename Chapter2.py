from Chapter2_test import find_table_index

#
nums = []
# nums在python中为连续存储，因此append的存储效率较高 时间复杂度为O(1) insert为时间复杂度O(N)
nums.append(1)
nums.insert(0,2)

import timeit
x=1
print(timeit.timeit("x=2+2"))
print(timeit.timeit("x = sum(range(100))"))
import cProfile
cProfile.run('find_table_index("D://原生docx//安投（北京）金融信息服务有限公司_自查报告（word文字版）.docx","运营总体情况")')