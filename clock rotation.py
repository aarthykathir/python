user_input=input("Enter the Time:")
splited_input=list(map(int, user_input.split(":")))
minute_hand=splited_input[1]
hour_hand=splited_input[0]
angle_of_hour_hand=(hour_hand*30)+(minute_hand*0.5)
angle_of_minute_hand=minute_hand*6
net_angle=angle_of_minute_hand-angle_of_hour_hand
if(net_angle<0):
    net_angle*=-1
print("The Minimum Angle between Hour Hand and Minute Hand is:",end="")
if(net_angle<360-net_angle):
    print(net_angle)
else:
    print(360-net_angle)
