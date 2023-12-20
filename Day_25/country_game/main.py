import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "../country_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_state = data["state"].to_list()
# print(all_state)

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()
    # print(answer_state)

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        print(missing_state)
        break

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == answer_state]
        t.goto(int(state_date.x.iloc[0]), int(state_date.y.iloc[0]))
        t.write(answer_state)

