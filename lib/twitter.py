import re


def get_user_timeline(api, screen_name, max_id=None, text=None) -> str:
    if text is None:
        text = ''
    tweets = api.GetUserTimeline(screen_name=screen_name, count=200, max_id=max_id)
    for tweet in tweets:
        text += replace_substring(tweet.text)
    if len(tweets) == 1:
        return text
    max_id = tweets[-1].id
    return get_user_timeline(api, screen_name, max_id, text)


def replace_substring(text) -> str:
    # RT
    text = re.sub(r'^RT(.*\n*)*', '', text)
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
