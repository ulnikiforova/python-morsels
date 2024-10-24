def compare_dates(date1_str, date2_str):
    m1, d1, y1 = tuple(list(date1_str.split('/')))
    m2, d2, y2 =  tuple(list(date2_str.split('/')))
    date1_ordered = (y1, m1, d1)
    date2_ordered = (y2, m2, d2)
    if date1_ordered <= date2_ordered:
        return date1_str
    else:
        return date2_str

def get_earliest(*dates):
    earliest_date = dates[0]
    for item in dates:
        earliest_date = compare_dates(item, earliest_date)
    return earliest_date
