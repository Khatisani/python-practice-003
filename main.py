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

    weather_data = {}
    weeks_info = []


    attributes = ["RAIN", "CLOUDS", "WIND", "SUN"]
    symbols = ["🌧️", "☁️", "🍃", "☀️"]


    with open("weather.txt", "r") as f:
        file = f.read()
        lines = file.splitlines()
        lines = lines[1:]

    for line in lines:
        line = line.strip()
        if line == "---":
            if weather_data:
                weeks_info.append(weather_data)
                weather_data = {}
            continue
        if ":" in line:
            day, percentage = line.split(":")
            weather_data[day.strip()] = int(percentage.strip())
    if weather_data:
        weeks_info.append(weather_data)

    for week_number in range(len(weeks_info)):
            week = weeks_info[week_number]
            attribute = attributes[week_number]
            symbol = symbols[week_number]
            print(f"\nWEEK {week_number + 1}: {attribute}")
            for day, percentage in week.items():
                calculation = percentage // 10
                conversion = symbol * calculation
                print (f"{day}: {conversion}")



weather_graph()
    
