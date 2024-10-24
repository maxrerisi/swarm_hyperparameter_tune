def ascii_loading_bar(current, total, bar_length=50):
    if current > total or current < 0:
        raise ValueError("Current value must be between 0 and total.")
    
    fraction_complete = current / total
    
    filled_length = int(bar_length * fraction_complete)
    
    bar = '█' * int(filled_length) + '-' * (bar_length - filled_length)

    percent_complete = round(fraction_complete * 100, 2)
    return f"[{bar}] {percent_complete}% Complete"
