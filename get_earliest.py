def compare_dates(date1_str, date2_str):
    m1, d1, y1 = tuple(list(date1_str.split('/')))
    m2, d2, y2 =  tuple(list(date2_str.split('/')))
    if y1 < y2:
        return date1_str
    elif y1 > y2:
        return date2_str
    else:
        if m1 < m2:
            return date1_str
        elif m1 > m2:
            return date2_str
        else:
            if d1 < d2:
                return date1_str
            else:
                return date2_str

def get_earliest(*dates):
    earliest_date = dates[0]
    for item in dates:
        earliest_date = compare_dates(item, earliest_date)
    return earliest_date