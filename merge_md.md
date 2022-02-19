```
dirs = os.listdir('/Users/lixiang.2533/Desktop/Blogs/Leetcode/')
dir = '/Users/lixiang.2533/Desktop/Blogs/Leetcode'
dirs = ['二分法']
for a in dirs:
    md_list = glob(os.path.join(dir, a, '*.md'))
    md_list = sorted(md_list)
    contents = []

    for md in md_list:
        md_name = md.split('/')[-1]
        contents.append('### ' + md_name + "\n")
        with open(md, 'r') as f:
            contents.append(f.read() + "\n")

    with open(os.path.join(dir, "{}总结.md".format(a)), "w") as f:
        f.writelines(contents)

```







