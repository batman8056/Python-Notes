favorite_lang={
    'jen':'python',
    'sara':'c',
    'edwar':'ruby',
    'phil':'java',
    'manish':'python'
}
friends=['jen','edwar','manish']
for name in favorite_lang.keys():
    if name in friends:
       print("hi i'm "+name.title()+" this is my favoriate lang "+favorite_lang[name].title()) 