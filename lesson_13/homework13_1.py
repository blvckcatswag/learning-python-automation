import pandas as pd

def remove_duplicates(file1, file2, output_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    result = pd.concat([df1, df2]).drop_duplicates()

    result.to_csv(output_file, index=False)

if __name__ == "__main__":
    file1 = r"C:\Users\User.PC-475\Desktop\homework_task\work_with_csv\r-m-c.csv"
    file2 = r"C:\Users\User.PC-475\Desktop\homework_task\work_with_csv\rmc.csv"
    output = r"C:\Users\User.PC-475\PycharmProjects\learning-python-automation\lesson_13\result_masenko.csv"

    remove_duplicates(file1, file2, output)
    print("Готово!")
