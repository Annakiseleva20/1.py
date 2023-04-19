def remove_parentheses(text):
    while '(' in text:
        start = text.find('(')
        end = text.find(')', start)
        text = text[:start] + text[end+1:]
    return text

text = "Привет, (пробное удаление)мир!"
result = remove_parentheses(text)
print(result)
