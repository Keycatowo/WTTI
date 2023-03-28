#%%
from .Content import Content
from .utils import convert_to_timestamp
import pandas as pd


class Text(Content):
    """
    Text 為一個內容物的抽象類別, 定義了一個內容物的基本屬性

    Attributes:
        text_content: 內容的文字內容
        author: 內容的作者
        published_timestamp: 內容的發布時間
        likes: 內容的讚數
        platform: 內容所在的平台
        url: 內容所在的網址
    
    Methods:
        to_series: 將內容物轉換成 pandas.Series
    """
    
    def __init__(self, text="", url="", author="", platform="", likes=-1, published_time=None):
        super().__init__()
        self.data.update({
            "text_content": text,
            "author": author,
            "published_timestamp": convert_to_timestamp(published_time) if published_time else None,
            "likes": likes,
            "platform": platform,
            "url": url,
        })
        
    @property
    def text(self):
        return self.data["text_content"]
    
    @text.setter
    def text(self, value):
        super().__setitem__("text_content", value)
        self["text_content"] = value

    @property
    def author(self):
        return self.data["author"]
    
    @author.setter
    def author(self, value):
        super().__setitem__("author", value)
        self["author"] = value
    
    @property
    def published_time(self):
        return self.data["published_timestamp"]
    
    @published_time.setter
    def published_time(self, value):
        super().__setitem__("published_timestamp", value)
        self["published_timestamp"] = value
    
    @property
    def likes(self):
        return self.data["likes"]
    
    @likes.setter
    def likes(self, value):
        super().__setitem__("likes", value)
        self["likes"] = value
    
    @property
    def platform(self):
        return self.data["platform"]
    
    @platform.setter
    def platform(self, value):
        super().__setitem__("platform", value)
        self["platform"] = value
    
    @property
    def url(self):
        return self.data["url"]
    
    @url.setter
    def url(self, value):
        self["url"] = value

    
