import turtle

INPUT_STR = "Hello world python cool hello"
CIRCLE_RADIUS = 100
TITLE_X = -300
TITLE_Y = 250
TITLE_PEN_SIZE = 2
LEGEND_CIRCLE_RADIUS = 7
LEGEND_CIRCLE_X = CIRCLE_RADIUS+50
LEGEND_CIRCLE_Y = CIRCLE_RADIUS*2+3
LEGEND_DESC_X = CIRCLE_RADIUS+80
LEGEND_DESC_Y = CIRCLE_RADIUS*2+5
MAX_DEGREE = 360
COLORS = ["red", "green", "blue", "orange", "violet", "yellow", "brown"]
RAYS_LEN = 100
RAYS_CIRCLE_RADIUS = 2


def get_uniq_words(str):
    words = str.split(" ")
    uniq_words= dict()
    for word in words:
        if word in uniq_words.keys():
            uniq_words[word] += 1
        else:
            uniq_words[word] = 1
    return uniq_words


def get_num_words(str):
    total = float(len(str.split(" ")))
    return total


def get_word_perc(str):
    words_perc = get_uniq_words(str)
    all_words = get_num_words(str)

    for word, perc in words_perc.items():
        perc /= all_words
        words_perc[word] = perc
    return words_perc


def draw_title(str, t):
    t.penup()
    t.pencolor("black")
    t.pensize(TITLE_PEN_SIZE)
    t.goto(TITLE_X, TITLE_Y)
    t.pendown()
    t.write("Input text: '"+str+"'", font=("Times New Roman", 14))
    t.penup()
    t.home()


def draw_legend(uniq_words, t):
    step = 0
    current_color = -1
    for key, val in uniq_words.items():
        t.penup()
        t.goto(LEGEND_CIRCLE_X, LEGEND_CIRCLE_Y - step)
        current_color += 1
        if current_color > len(COLORS):
            current_color = 0
        t.color(COLORS[current_color])
        t.begin_fill()
        t.circle(LEGEND_CIRCLE_RADIUS)
        t.end_fill()
        t.goto(LEGEND_DESC_X, LEGEND_DESC_Y - step)
        str = "%s - %s time(s)" % (key,val)
        t.write(str)
        step += 30


def draw_diagram(str, diagr_type, t):
    draw_title(str, t)
    str = str.lower()
    if diagr_type == 'sectors':
        word_percentage = get_word_perc(str)
        word_angle = dict()
        for word, perc in word_percentage.items():
            word_angle[word] = MAX_DEGREE*perc

        t.color("black")
        t.begin_fill()
        t.circle(CIRCLE_RADIUS)
        t.end_fill()

        current_perc = 0
        current_color = -1
        for word_perc in word_angle.values():
            current_perc += word_perc
            current_color += 1
            if current_color > len(COLORS):
                current_color = 0
            t.color(COLORS[current_color])
            t.begin_fill()
            t.circle(CIRCLE_RADIUS, word_perc)
            t.goto(0,CIRCLE_RADIUS)
            t.end_fill()
            t.penup()
            t.home()
            t.circle(CIRCLE_RADIUS, current_perc)

    elif diagr_type == 'rays':
        current_color = -1
        uniq_words = get_uniq_words(str)
        uniq_words_count = len(uniq_words)
        i=0
        for num in uniq_words.values():
            t.home()
            i += 1
            current_color += 1
            if current_color > len(COLORS):
                current_color = 0
            t.color(COLORS[current_color])
            t.pendown()
            t.rt(MAX_DEGREE/uniq_words_count*i)
            for j in range(num):
                t.fd(RAYS_LEN)
                t.circle(RAYS_CIRCLE_RADIUS)
            t.penup()

    draw_legend(get_uniq_words(str), t)


def init():
    wn = turtle.Screen()
    Turtle = turtle.Turtle()
    draw_diagram(INPUT_STR, 'sectors', Turtle)
    input()
    Turtle.clear()
    draw_diagram(INPUT_STR, 'rays', Turtle)
    input()

if __name__ == "__main__":
    init()
