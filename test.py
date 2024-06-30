from Fuzzy import FuzzyLogic
from datetime import datetime
import time

start_time = time.time()
now = datetime.now()
seconds = now.second
milliseconds = now.microsecond // 1000  # converting microseconds to milliseconds

fuzzy_logic = FuzzyLogic()
new_cog = int(fuzzy_logic.compute_new_cog(seconds, milliseconds))
print(new_cog)

print(f"Current seconds: {seconds}")
print(f"Current milliseconds: {milliseconds}")

depth = new_cog % 3
depth = depth + 3

print(depth)

end_time1 = time.time()

time_difference1 = end_time1 - start_time
print(time_difference1*1000)
