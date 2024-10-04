import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game.")

image = "/home/sumon/Documents/Python/Pandas/US tates Game/blank_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("/home/sumon/Documents/Python/Pandas/US tates Game/50_states.csv")
# print(data)
data_list = data.state.to_list()


guess_states = []

while len(guess_states) < 50:
    ans_states = screen.textinput(title=f"{len(guess_states)}/ 50 Guess The States.", prompt="What's another states name.").title()
    # print(ans_states)

    if ans_states == "Exit":
        break

    if ans_states in data_list:
        guess_states.append(ans_states)
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()

        state_data = data[data.state == ans_states]

        tur.goto(int(state_data.x), int(state_data.y))
        tur.write(state_data.state.item())

# screen.exitonclick()