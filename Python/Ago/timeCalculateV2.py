# import openpyxl
from openpyxl import load_workbook, workbook, worksheet

def file_init():
    raw_address = input("请输入文件路径(如：C:\\Users\somnolency\Desktop\\1_report.xlsx)：\n")
    for i in raw_address:
        if i == '\\':
            i = r'\\'
    work_book = load_workbook(raw_address)
    modified_address = raw_address[:-5] + "_mod" + raw_address[-5:]
    return work_book, modified_address


work_book, modified_address = file_init()
active_sheet = work_book.active


def time_format(day_name):
    '''返回格式化后的时间列表'''
    # 将字符串转为列表，并进行处理
    time_value = active_sheet[day_name].value       # 这里只是一个容器，存放字符串形式的数据
    if time_value == None :
        time_value = ["00:00", "00:00"]
        return time_value
    else:
        # 处理奇偶次打卡
        if len(time_value) % 10 != 0:
            time_value = time_value[:-5]
        # 转为列表
        punch_times = int(len(time_value) / 5)
        time_value_list = []
        for i in range(punch_times):            # i的范围在 0 ~ punch_times-1之间
            time_value_list = time_value_list + [time_value[i*5:i*5 + 5]]
        return time_value_list


def calculate_day_time(format_time):
    '''返回日打卡时间，输入格式：[”XX:XX“, ”XX:XX“]，输出格式：[XX,XX]'''
    # 时间提取
    summary_time = [00, 00]
    for i in range(int(len(format_time) / 2)):
        time_begin = format_time[i*2]
        time_end = format_time[i*2 + 1]
        diff_time = calculate_single_time(time_begin, time_end)

        # 当天总时间计算
        summary_time = sum_time(summary_time, diff_time)
    return summary_time


def calculate_single_time(time_begin, time_end):
    ''' 计算单次打卡时间，输入格式为"XX:XX",返回格式为[XX,XX] '''
    one = int(time_end[:2])*60 + int(time_end[3:5])
    two = int(time_begin[:2])*60 + int(time_begin[3:5])
    summary = one - two
    diff_time = [int(summary / 60)] + [int(summary % 60)]
    return diff_time


def sum_time(time_1, time_2):
    '''将两段时间相加，输入格式为[XX,XX]，返回格式为[XX,XX]的时间'''
    one = int(time_1[0])*60 + int(time_1[1])
    two = int(time_2[0])*60 + int(time_2[1])
    summary = one + two
    return [int(summary / 60)] + [int(summary % 60)]


def write_time(series, time_value):
    '''给定序列与值，写入表格中'''
    hum_value = str(time_value[0]) + "小时" + str(time_value[1]) + "分钟"
    active_sheet_1 = work_book.active
    active_sheet_1[series] = hum_value
    print('单元格{}的值是：{}'.format(series, hum_value))

def top_print():
    '''打印开头信息'''
    monday = 'A'
    tuesday = "B"
    wednesday = "C"
    thursday = "D"
    friday = "E"
    saturday = "F"
    sunday = "G"
    week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
    Week = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    for day in week:
        time_series = chr(ord(day[0]) + 8) + str(4)
        active_sheet_1 = work_book.active
        Day = Week[week.index(day)]
        active_sheet_1[time_series] = Day
    work_book.active["Q4"] = "总计"


# --------------------------------------------------------------------------------------
# 开头信息打印
top_print()

for player_number in range(6, 262, 2):
    # 打卡时间
    monday = 'A' + str(player_number)
    tuesday = "B" + str(player_number)
    wednesday = "C" + str(player_number)
    thursday = "D" + str(player_number)
    friday = "E" + str(player_number)
    saturday = "F" + str(player_number)
    sunday = "G" + str(player_number)
    week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]


    # 计算周打卡时间
    week_time = [00, 00]
    for day in week:
        time_list = time_format(day)
        day_time = calculate_day_time(time_list)
        week_time = sum_time(week_time, day_time)
        # 通过ASCII码确定数据写入的位置
        time_series = chr(ord(day[0]) + 8) + str(player_number)
        write_time(time_series, day_time)
    # 确定周打卡时间的位置
    week_series = "Q" + str(player_number)
    write_time(week_series, week_time)

print("文件处理完成")
work_book.save(modified_address)