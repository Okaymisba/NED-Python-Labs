from datetime import datetime

sample_datetime = datetime(2018, 7, 13, 21, 40)

# a) Format: "Thursday, July 13 2018"
formatted_a = sample_datetime.strftime("%A, %B %d %Y")
print(f"(a) {formatted_a}")

# b) Format: "09:40 PM Central Daylight Time on 07/13/2018"
import pytz

central_timezone = pytz.timezone("America/Chicago")
sample_datetime_cdt = central_timezone.localize(sample_datetime)
formatted_b = sample_datetime_cdt.strftime("%I:%M %p %Z on %m/%d/%Y")
print(f"(b) {formatted_b}")

# c) Format: "I will meet you on Thu July 13 at 09:40 PM."
formatted_c = sample_datetime.strftime("I will meet you on %a %B %d at %I:%M %p.")
print(f"(c) {formatted_c}")
