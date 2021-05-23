import os


def cs_remove(y_str: str, *args: str):
    for ar in args:
        y_str = y_str.replace(ar, "")
    return y_str


def cuts(origin: str, heads: str, ends: str):
    (non, op, a_1) = origin.partition(heads)
    (result, op, nin) = a_1.partition(ends)
    return result


if not os.path.exists("occ.txt"):
    with open("occ.txt", "w", encoding="utf-8") as f:
        f.write("/love\n"
                "@爱你哟\n"
                "$’爱你哟‘\n\n"
                "~10000000000，30，爱你哟，way=minutes，model：'interval'\n")

if not os.path.exists("plug-in_deploy.txt"):
    with open("plug-in_deploy.txt", "w", encoding="utf-8") as rf:
        rf.write("target_file_name（目标文件名称）= occ\n"
                 "#指你编辑的文件，不要书写文件格式\n\n"
                 "py_file_name（py文件名） = siy\n"
                 "#指运行后生成的文件，不要书写文件格式\n"
                 "#默认保存为当前文件夹\n\n"
                 "定时提醒功能 = off\n"
                 "#本功能基于https: // github.com / nonebot / plugin - apscheduler\n"
                 "#请先做好基本配置再开启本功能\n\n")

with open("plug-in_deploy.txt", "r", encoding="utf-8") as rfs:
    for x in rfs.readlines():
        if x.startswith("py"):
            a = cuts(x, "= ", "\n")
        elif x.startswith("tar"):
            b = cuts(x, "= ", "\n")
        elif x.startswith("定时提醒功能"):
            c = cuts(x, "= ", "\n")

fix_py = a + ".py"
target_file = b + ".txt"
# 运行后生成的文件


Base_import = f"from nonebot import *\n" \
              f"from nonebot.typing import T_State\n" \
              f"from nonebot.adapters.cqhttp import *\n\n" \
    # 基础导入

SET_ON_import = Base_import + \
                f"import time\n" \
                f"from nonebot import require\n" \
                f"scheduler = require('nonebot_plugin_apscheduler').scheduler\n\n"
# 打开定时提醒功能后的导入

with open(fix_py, "w", encoding='utf-8') as f:
    if c == "off":
        f.write(Base_import)
    if c == "on":
        f.write(SET_ON_import)


# 必要的导入


def read_target(target_file_=target_file):
    f_named = []  # 命名"/"
    f_instruction = []  # 指令"@"
    f_compile = []  # 回应"$"
    f_time_in = []  # 计时任务"~"
    f_variable = {}  # 变量，":="
    f_lines = []

    def list_app(line_a, addin: list, fh="", hh=""):
        if line_a.startswith(fh):
            line_b = cs_remove(line_a, fh, hh)
            addin.append(line_b)

    with open(target_file_, 'r', encoding='utf-8') as target_f:
        for line in target_f.readlines():
            if ":=" in line:
                (the_variable, the_value) = line.split(":")
                f_variable[the_variable] = f"{the_variable}{the_value}"
            list_app(line, addin=f_instruction, fh="@")
            list_app(line, addin=f_compile, fh="$")
            list_app(line, addin=f_named, fh="/")
            if c == "on":
                list_app(line, addin=f_time_in, fh="~")
    with open(fix_py, "a", encoding='utf-8') as f_py:
        for value in f_variable.values():
            f_py.write(f"{value}\n")
    return f_named, f_instruction, f_compile, f_time_in, f_lines


def instruction():
    (f_named, f_instruction, f_compile, f_time_in, non) = read_target(target_file_=target_file)
    for i in range(len(f_named)):
        code = f"{f_named[i]} = on_command(\"{(f_instruction[i])}\", priority=1)\n@{f_named[i]}.handle()\n" \
               f"async def u_city(bot: Bot, event:Event, state: T_State):\n" \
               f"    msg = \"{f_compile[i]}\"\n" \
               f"    await {f_named[i]}.send(msg)\n\n"
        with open(fix_py, "a", encoding='utf-8')as f_py:
            f_py.write(code)

    if c == "on":
        c_a = 0
        litem = []

        def default_setting():
            litem[3] = "way=minutes"
            litem[4] = "model：'interval'"

        def if_try():
            if len(litem) == 3:
                default_setting()
            elif len(litem) == 4:
                if litem[3].startswith("way="):
                    litem[4] = "'interval'"
                elif litem[3].startswith("model："):
                    default_setting()
            elif len(litem) == 5:
                pass

        for clock in f_time_in:
            litem.append(clock.split("，"))
            if_try()
            c_a += 1
            litem = litem[0]
            litem3 = litem[3].replace("way=", "")
            litem4 = litem[4].replace("model：", "")
            scheduler_id = "id" + str(0 + int(a))
            clocks = f"@scheduler.scheduled_job({litem4},{litem3}={int(litem[1])}, id=\"{scheduler_id}\")\n" \
                     f"async def {scheduler_id}():\n" \
                     f"    bots = get_bots()\n" \
                     f"    gid = {litem[0]}\n" \
                     f"    for bot in bots.values():\n" \
                     f"        msg = {litem[2]}\n" \
                     f"        await bot.send_msg(message=msg,group_id=gid)\n\n"
            with open(fix_py, "a", encoding='utf-8')as f_py:
                f_py.write(clocks)


if __name__ == "__main__":
    instruction()
