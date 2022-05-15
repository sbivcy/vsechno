from time import perf_counter
from funcs import load_csv, file_write, bar_chart, pie_chart
from settings import *


def main():
    answers = load_csv(csv_name, question_count)
    for i in range(0, question_count):
        t = perf_counter()
        if i in open_questions:
            file_write(answers, out_name, i)
        elif i in range_questions:
            bar_chart(answers, colors, i)
        elif i in yes_no_questions:
            pie_chart(answers, colors, i)
        elif i in yes_no_idk_questions:
            pie_chart(answers, colors, i, True)
        if color_terminal:
            print(f"\033[9{i%2+2}mQuestion {i} processed in: {round(perf_counter()-t, 4)} s")
        else:
            print(f"Question {i} processed in: {round(perf_counter()-t, 4)} s")
                

if __name__ == "__main__":
    main()
