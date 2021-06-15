def add_time(start, duration,day=None):
    new_time = []
    init_min = int(start.split()[0].split(':')[0])*60 + int(start.split()[0].split(':')[1])
    duration_min = int(duration.split(':')[0])*60 + int(duration.split(':')[1])
    time12 = start.split()[1]
    
    # maybe export as a function that returns new_h, new_m
    new_h = (init_min + duration_min)//60
    new_m = (init_min + duration_min)%60
    
    # maybe export as a function that returns the right format for the hh:mm
    if new_m < 10:
        final_min = '0' + str(new_m)
    elif new_m > 10:
        final_min = str(new_m)
    
    n_days = new_h // 24
    
    # AM<->PM flip
    if n_days == 0 :
        if new_h >= 12:
            if time12 == 'PM':
                time12 = 'AM'
                n_days += 1
                if new_h == 12:
                    final_h = 0
                else:
                    final_h = new_h - 12
            elif time12 == 'AM':
                time12 = 'PM'
                if new_h > 12: final_h = new_h - 12
                elif new_h == 12: final_h = new_h
        else:
            final_h = new_h
    elif n_days > 0:
        final_h = new_h - n_days*24
        if final_h >= 12:
            if time12 == 'PM':
                n_days += 1
                time12 = 'AM'
                if final_h == 12: pass
                else: final_h -= 12
            elif time12 == 'AM':
                time12 = 'PM'
                if final_h > 12: final_h -= final_h - 12

    # a function that takes n_days and returns day_text
    day_text = ''
    if n_days == 1:
        day_text = '(next day)'
    elif n_days > 1:
        day_text = '(' + str(n_days) + ' days later)'
    
    if day != None:
        if n_days > 0:
            days = ['Sunday','Monday','tuesday','Wednesday','Thursday','Friday','saturDay']
            sum_day = days.index(day) + n_days
            while sum_day >= 7:
                sum_day -= 7
            day = days[sum_day]
                
    # connect all the different pieces
    new_time.append(str(final_h) + ':' + final_min)
    if day ==  None: new_time.append(time12)
    else: new_time.append(time12+',')
    if day != None:
        new_time.append(day)
    if day_text != '':
        new_time.append(day_text)
    new_time = ' '.join(new_time)

    return new_time
