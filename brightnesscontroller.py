import screen_brightness_control as sbc
current_brightness = sbc.get_brightness()
print(current_brightness)

primary_brightness = sbc.get_brightness(display=0)
print(primary_brightness)