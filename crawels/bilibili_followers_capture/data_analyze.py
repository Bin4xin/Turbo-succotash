#  Copyright (c) 2022.
#
#  @Bin4xin. SENTINEL CYBER SEC All Rights Reserved.
#  @Link https://github.com/Bin4xin
import csv
import time
import data_capture_bilibili_for_followers as blf


def getDataFromCsv(file):
    followersReduceData_rate = []
    with open(file, "r", encoding="utf-8") as openfile:
        read = csv.reader(openfile)
        for i in read:
            followersReduceData_rate.append(i[3])
    followersReduceData_rate.remove(followersReduceData_rate[0])
    # delete list header, then return a list from a csv file.
    return followersReduceData_rate


def data_analyze(data):
    data_init_list = list(map(int, data))
    avgFloatNumber: float = sum(data_init_list) / len(data)
    print("According to loss followers rate: {}/min(s)".format(avgFloatNumber))
    # avg_float => int/min
    return avgFloatNumber


def year_Jugdement(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                # 整百年能被400整除的是闰年
                return True
            else:
                # print("{0} 不是闰年".format(year))
                return False
        else:
            return True
            # 非整百年能被4整除的为闰年
    else:
        return False


def main(expected_number, calculationBasis):
    data = getDataFromCsv("reduce_log_2hours.csv")
    avgFloatNumber = data_analyze(data)
    # Average algorithm
    # maybe there is another algorithm.
    """
    content above args => avgFloatNumber means numbers(int)/mins.
    then int/Hour, Days etc...
    """
    hours_reduce = avgFloatNumber * 60
    days_reduce = hours_reduce * 24
    week_reduce = days_reduce * 7
    time_local_year = int(time.strftime("%Y", time.localtime()))
    if year_Jugdement(time_local_year):
        # 闰年
        year_reduce = (366 * days_reduce)
    else:
        year_reduce = (365 * days_reduce)
    follower = blf.parseContentByBS(blf.requestUri("https://api.bilibili.com/x/relation/stat?vmid=122879"))
    theory_number = follower - expected_number
    print("Based on <<{}>> theory, from {} reduce to {} lost number is {}".format(calculationBasis, follower,
                                                                                  expected_number, theory_number))
    # For now, we have some reduce rate numbers. Time = Length / Speed e.g.
    print("So, need more time:\nIn {} Year(s),\nOr {} Month(s),\nOr {} day(s).".format(
        theory_number / year_reduce, theory_number / week_reduce, theory_number / days_reduce
    ))


if __name__ == '__main__':
    targetNumbers = int(input("Plz type in your target numbers:"))
    # 999999
    calculationBasis = input("Plz type in your calculation Basis:")
    # Less than one million followers
    main(targetNumbers, calculationBasis)
