import matplotlib.pyplot as plt
import numpy as np


def load_csv(filename: str, question_count: int):
    """Make a list from .csv file."""
    answers = [[] for _ in range(0, question_count)]
    with open(filename, "r") as csv:
        for line in csv:
            temp = line.split('","')
            for i in range(0, question_count):
                # check for empty strings
                if temp[i+2] != '':
                    answers[i].append(temp[i+2])
    return answers


def file_write(answers: list, i: int):
    """Write answers to open questions to a .txt file."""
    with open(f"answers.txt", "a") as file:
        file.write(f"{answers[i - 1][0]}\n")
        for ans in answers[i][1:]:
            file.write(f"    {ans}\n")
        file.write("\n")


def bar_chart(answers: list, i: int):
    """Make a bar graph."""
    counts = [0, 0, 0, 0, 0]
    for a in answers[i][1:]:
        counts[int(a) - 1] += 1

    fig, ax = plt.subplots()
    ax.axis([0.5, 5.5, 0, int(len(answers[i][1:])/1.75)])
    ax.bar((1, 2, 3, 4, 5), counts, color=[0.2, 0.2, 1])
    ax.margins(0, 0.25)
    ax.set_xlabel("Odpověď")
    ax.set_ylabel("Počet")


    plt.title(answers[i][0])
    fig.canvas.draw()
    fig.savefig(f"graf{int(i/2)}.png")


def pie_chart(answers: list, i: int, e: bool):
    """Make a pie graph."""
    colors = [[0.1, 0.8, 0.1], [1, 0.2, 0.2], [0.2, 0.2, 1]]
    if e:
        counts = [0, 0, 0]
        for a in answers[i]:
            if a == "Útěk do bezpečí":
                counts[0] += 1
            elif a == "Zapojit se":
                counts[1] += 1
            elif a == "Nevím":
                counts[2] += 1

        fig, ax = plt.subplots()
        ax.axis([0.5, 3.5, 0, len(answers[i][1:])])
        ax.pie(counts, colors=colors, labels=["Útěk", "Zapojit se", "Nevím"])
    else:
        counts = [0, 0]
        for a in answers[i]:
            if a == "Ano":
                counts[0] += 1
            elif a == "Ne":
                counts[1] += 1

        fig, ax = plt.subplots()
        ax.axis([0.5, 2.5, 0, len(answers[i][1:])])
        ax.pie(counts, colors=colors, labels=["Ano", "Ne"])

    ax.legend(bbox_to_anchor=(0, 1))

    plt.title(answers[i][0])
    fig.canvas.draw()
    fig.savefig(f"graf{int(i/2)}.png")
