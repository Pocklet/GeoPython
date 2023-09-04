def convert_kph_ms(speed):
    """Converts velocity (speed) in km/hr to m/s"""
    assert speed >= 0.0, "Wind speed values must be positive"
    return speed * 1000 / 3600


wind_speed_km = -27
wind_speed_ms = convert_kph_ms(wind_speed_km)

print(f"A wind speed of {wind_speed_km} km/hr is {wind_speed_ms} m/s.")