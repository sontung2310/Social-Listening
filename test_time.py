from datetime import datetime, timedelta

margin_time = datetime.now() - timedelta(days=7)
print(margin_time.timestamp())