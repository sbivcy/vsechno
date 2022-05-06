from other import load_csv, file_write, bar_chart, pie_chart


def main():
    question_count = 12

    answers = load_csv("ans.csv", question_count)

    for i in range(0, question_count):
        if i in (1, 3, 5, 7, 9, 11):
            file_write(answers, i)
        elif i in (0, 10):
            bar_chart(answers, i)
        elif i == 6:
            pie_chart(answers, i, True)
        else:
            pie_chart(answers, i, False)


if __name__ == "__main__":
    main()
