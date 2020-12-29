## Adding days to date in Python
import datetime
from datetime import date
## Date object
# date_original = datetime.date(2019, 7, 20)

date_original = date.today()

## Days to add
days_to_add = 16

## Add
date_new = date_original + datetime.timedelta(days_to_add)

print("\n Original Date: ", date_original, "\n")
print("\n New Date: ", date_new, "\n")

print("######################")

print(date_original)
print(date_new)