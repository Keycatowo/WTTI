import pandas as pd
import uuid
from time import time

class Content:
    def __init__(self):
        self.uuid = uuid.uuid4()
        self.created_timestamp = int(time())
        self.modified_timestamp = self.created_timestamp
        self.data = {
            "uuid": self.uuid,
            "created_timestamp": self.created_timestamp,
            "modified_timestamp": self.modified_timestamp,
        }

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        # 檢查是否為內建屬性
        if key in ["uuid", "created_timestamp", "modified_timestamp"]:
            raise KeyError(f"Can not modify {key}")
        
        # 檢查要修改的屬性是無變化
        if key in self.data and self.data[key] == value:
            return
        # 更新 modified_timestamp
        else:
            self.modified_timestamp = int(time())
            self.data["modified_timestamp"] = self.modified_timestamp
            # 更新屬性
            self.data[key] = value

    def to_series(self):
        return pd.Series(self.data)
