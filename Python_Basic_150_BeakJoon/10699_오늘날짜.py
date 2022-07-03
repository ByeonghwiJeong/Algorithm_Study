from datetime import datetime
print(str(datetime.now())[:11])
now = datetime.now()
print(now.strftime('%Y-%m-%d'))

import time
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))

