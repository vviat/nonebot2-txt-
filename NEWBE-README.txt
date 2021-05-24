运行format_r.py后
会生在当前目录下成：
plug-in_deploy.txt（配置文档）：请阅读，有默认值，可配置。
occ.txt （编写文档）

NEWBE-README
编写文档实例：

/useful
@好用哦
$“嗯嗯”

/+“”：
代表注册函数名（请使用英文，不要重复哦），此处进行on_command注册
@+“”：
代表指令（也就是机器人收到该指令后才会进行回复）
实际操作以on_command响应起始设置为准，若是未修改，则在QQ内输入：/+“”会发生响应
$+“”：
代表响应内容，
引号请用英文符
该段适用所有py，nonebit2语法
例如：
$MessageSegment.image("https://www.onexiaolaji.cn/RandomPicture/api/?class=jkfun")
为发送api的随机图片
以上3个为一组，缺少则会造成注册失败，或者响应混乱


配置：定时提醒功能 = on
注意：本功能基于https://github.com/nonebot/plugin-apscheduler
~10000000000，30，爱你哟

~a，b，c，way=minutes，model：'interval’
代表定时响应指令
可以理解为闹钟功能
该指令目前必须是一行
a：代表群号，即需要进行发送的群号
b：代表时间间隔，单位恒定为分钟
c：代表消息，适用py字符串的所有方法，
格式定义
，：，逗号和冒号必须为为中文格式
“”引号必须为英文格式

以下为可更改参数，默认时无需描述：
way意为方式：
默认参数model：'interval’下
可选参数有
minutes：分钟
hours：小时
model意为模式
可选参数以及用法参考：
https://www.cnblogs.com/gdjlc/p/11432526.html


~500，1/2，'holle word'
意为：
每半分钟，向群号为500的群，发送一次“holle word”消息


U-README
/useful（注册）
@好用哦（指令）
$'嗯嗯'（响应,适用py，nonebot2语法）


~gid，30，爱你哟，
注意：本功能基于https://github.com/nonebot/plugin-apscheduler
~群号，时间间隔（分钟），信息，way=minutes，model：'interval’（后两项为默认值）
~500，1/2，hello word
每半分钟，向群号为500的群，发送一次“hello word”消息

 a:=b
仅可写入全局变量（必须用英文符，参考py语法，建议不要加空格）











