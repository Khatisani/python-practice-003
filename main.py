def weather_graph():
    """
    This function draws a weather graph for four weeks.
    each week will be observing a specific attribute.
    WEEK 1: RAIN 🌧️ , WEEK 2: CLOUDS ☁️, WEEK 3: WIND 🍃, WEEK 4: SUN ☀️
    
    Returns:
        str: A string representation of the weather graph.
        
    i.e for RAIN: each character represents 10% of rain/attribute observed that day.
    0% - no character
    10% - 1 character
    20% - 2 characters
    ...
    
    Week 1: RAIN
    MON: 🌧️
    TUE: 🌧️🌧️🌧️🌧️🌧️
    WED: 🌧️🌧️🌧️
    THU: 🌧️🌧️🌧️🌧️
    FRI: 🌧️🌧️🌧️🌧️🌧️
    
    your task is to read data from a file 'weather.txt' and draw the graphs accordingly.
    """

    week_info = {}
    weeks = []


    attributes = ["RAIN", "CLOUDS", "WIND", "SUN"]
    symbols = ["🌧️", "☁️", "🍃", "☀️"]


    with open("weather.txt", "r") as f:
        file = f.read()
        lines = file.splitlines()
        lines = lines[1:]

    for line in lines:
        line = line.strip()
        if line == "---":
            if week_info:
                weeks.append(week_info)
                week_info = {}
            continue
        if ":" in line:
            day, percentage = line.split(":")
            week_info[day.strip()] = int(percentage.strip())
    if week_info:
        weeks.append(week_info)

    for week_number, week in enumerate(weeks):
            attribute = attributes[week_number]
            symbol = symbols[week_number]
            print(f"\nWEEK {week_number + 1}: {attribute}")
            for day, percentage in week.items():
                print (f"{day}: {symbol * (percentage // 10)}")


weather_graph()
    
