import pandas as pd

def print_df(df):
    column_widths = [len(string) for string in df["course_name"]]
    max_width = max(column_widths)

    print("course_name", end='')
    print(' '*(max_width*2-11), end='')
    print(" | students")
    print('-'*(max_width*2+11))
    for index in range(df.shape[0]):
        print(f"{df.iloc[index]['course_name']}", end='')
        print(' '*(max_width-column_widths[index])*2, end='')
        print(f" | {df.iloc[index]['students']}")


watch_list_path = "watch_list.txt"
with open(watch_list_path, "r", encoding="utf8") as file:
    watch_list = [line.rstrip('\n') for line in file]

# print(watch_list)

data_path = "register.csv"
df = pd.read_csv(data_path)
result = df[df["course_name"].isin(watch_list)].sort_values(by="students", ascending=False)

print_df(result)
