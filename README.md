转换`![[]]`语法为`[]()`方便在线阅读，图床使用了阿里云图床

命令如下

```shell
# 以北京为例
git clone git@github.com:shinerio/ob_tools.git
cd ob_tools
export oss_endpoint='http://oss-cn-beijing.aliyuncs.com'
export oss_path='obsidian/'
export oss_ak=your_ak
export oss_sk=your_sk
export oss_bucket=your_bucket
python main.py your_file_full_path
python main.py --vaultpath="obsidian vault路径 \
--input="需要转换的文件相对于vaultpath的路径" \
--outputpath="输入文件根路径, 输出目录将会保持和vault一样的目录结构" \
--attachment="本地图片存储路径"
```

# 自定义快捷指令

