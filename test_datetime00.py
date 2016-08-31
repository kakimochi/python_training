#! /usr/bin/python
# -*- coding: utf-8 -*-

import datetime

if __name__ == "__main__":

    today = datetime.date.today()
    todaydetail = datetime.datetime.today()

    # 今日の日付
    print today
    print todaydetail
    print todaydetail.isoformat()
    print todaydetail.strftime("%Y-%m-%d_%H:%M:%S")

    # 100日後の日付
    print today + datetime.timedelta(days=100)
