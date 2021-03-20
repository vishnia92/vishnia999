# узнать продолжительность в секундах
sec_min = (60)
sec_hour = (sec_min * 60)
sec_day = (sec_hour * 24)

duration = int(input('duration:'))

days = duration // sec_day
duration = duration - (days * sec_day)

hours = duration // sec_hour
duration = duration - (hours * sec_hour)

mins = duration // sec_min
duration = duration - (mins * sec_min)

print('{0: 0f}дн., {1: 0f}мин., {3: 0f} сек.'.format(days, hours, mins, duration))
