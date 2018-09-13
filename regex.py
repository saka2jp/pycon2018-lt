import re


def replace_substring(text) -> str:
    # 改行
    text = re.sub(r'\n', '', text)
    # 半角空白
    text = re.sub(r' ', '', text)
    # 全角空白
    text = re.sub(r'　', '', text)
    # 空白行
    text = re.sub(r'\n\s*\r', '', text)
    # 引用
    text = re.sub(r'&gt;', '', text)
    # URL
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)
    # Twitterユーザ名
    text = re.sub(r'@[\w_\-.]{3,15}', '', text)
    return text
