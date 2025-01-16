import pandas as pd
import unicodedata

def calculate_width(text):
    width = 0
    for char in text:
        if unicodedata.east_asian_width(char) in {'F', 'W'}:
            width += 2
        else:
            width += 1
    return width

def print_df(df):
    column_widths = [calculate_width(string) for string in df["course_name"]]
    max_width = max(column_widths)

    print(f'{"course_name":<{max_width}} | students')
    print('-'*(max_width+11))
    for index in range(df.shape[0]):
        print(f"{df.iloc[index]['course_name']}{' ' * (max_width - column_widths[index])} | {df.iloc[index]['students']}")


watch_list_path = "watch_list.txt"
with open(watch_list_path, "r", encoding="utf8") as file:
    watch_list = [line.rstrip('\n') for line in file]

# print(watch_list)

data_path = "register.csv"
df = pd.read_csv(data_path)
result = df[df["course_name"].isin(watch_list)].sort_values(by="students", ascending=False)

print_df(result)
