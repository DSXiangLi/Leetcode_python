```python
import os
from glob import glob 
dirs = os.listdir('/Users/lixiang.2533/Desktop/Blogs/Leetcode/')
dir = '/Users/lixiang.2533/Desktop/Blogs/Leetcode'
dirs = ['哈希表', '树', '二分法', '数学题', '链表','字符串', '数组', '栈']
for a in dirs:
    md_list = glob(os.path.join(dir, a,'*.md'))
    md_list = sorted(md_list)
    contents = []
    file_name = [i.split('/')[-1].split('.md')[0] for i in md_list]
    file_name = dict([(i.split('.')[0], i) for i in file_name])
    ## 给总结md加入title  
    with open(md_list[0],'r') as f:
      lines = f.readlines()
    new_lines = []
    for i in lines:
        if i.strip():
            nums = i.split('- ')[1]
            if nums.isdigit():
                new_lines.append('   - ' + file_name.get(nums, nums) + '\n')
            else:
                new_lines.append('- ' + file_name.get(nums, nums) + '\n')

    with open(md_list[0], 'w') as f:
        f.writelines(new_lines)
    for md in md_list:
        md_name = md.split('/')[-1]
        contents.append('### ' + md_name + "\n")
        with open(md, 'r') as f:
            contents.append(f.read() + "\n")

    with open(os.path.join(dir, "{}总结.md".format(a)), "w") as f:
        f.writelines(contents)
```



1. 总结文档里填充名字

