from datetime import datetime

def convert_to_timestamp(time_input):
    try:
        # 假設輸入是timestamp格式
        timestamp = datetime.fromtimestamp(int(time_input))
    except (ValueError, TypeError):
        try:
            # 假設輸入是常見的日期時間格式
            timestamp = datetime.strptime(time_input, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            # 如果都不是上述格式，拋出例外
            # raise ValueError
            raise ValueError("Invalid time format, please use timestamp or '%Y-%m-%d %H:%M:%S' format.")
    return int(timestamp.timestamp())
