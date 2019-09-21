# Find the angle made by the hour hand and the minute
# hand at any given time. Assume it is an analog clock

def calculateAngle(hour, minute):
  if hour < 0 or minute < 0 or hour > 12 or minute > 60:
    print("Wrong inputs given...")
    return
  else:

    if hour == 12:
      hour = 0
    if minute == 60:
      minute = 0

    hour_angle = (hour * 60 + minute) * 0.5
    minute_angle = minute * 6

    difference = abs(hour_angle - minute_angle)

    return min(difference, 360 - difference)

input_time = (9, 30)
print("The angle between hour and minute hand is: ", calculateAngle(input_time[0], input_time[1]), '\u00b0')
