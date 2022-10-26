def correct_hour(hour):
    """
    Returns the correct hour (If it exceeds 23, normalize it to 0..23)
    """
    if isinstance(hour, str):
        _hour = hour
        hour = int(hour)
        if hour > 23:
            _hour = hour - 24
            if _hour < 10:
                _hour = "0" + str(_hour)
            else:
                _hour = str(_hour)
            return _hour
        return _hour
    else:
        if hour > 23:
            return hour - 24
        return hour
