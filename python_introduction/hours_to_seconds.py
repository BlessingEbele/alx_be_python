#author: Blessing Ebele Anochili 
#date: 11/09/2024
#purpose: this python script that converts a specific number of hours into seconds.
 

hours = 2
seconds_per_minutes = 60
minutes_in_two_hours = 120

#converting 2 hours to seconds
#since 60 seconds make 1 minutes, 60 minutes is equal to 1 hours. therefore seconds in 2 hours eguals:
 
seconds = minutes_in_two_hours * seconds_per_minutes
print("2 hour(s) is", seconds, 'seconds')
