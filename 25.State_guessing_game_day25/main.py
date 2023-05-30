import turtle
import pandas

screen = turtle.Screen()
screen.title("States guessing game (type exit to exit)")
image = "india-state.gif"
screen.addshape(image)
screen.setup(width=500, height=500)
turtle.shape(image)


data = pandas.read_csv("states_data.csv")
state_names = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 29:
    guess = screen.textinput(title=f"{len(guessed_states)}/29 Guess the state", prompt="Whats another states name").title()
    if guess in guessed_states:
        pass
    else:
        if guess in state_names:
            guessed_states.append(guess)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == guess]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(guess)
        elif guess == "Exit":
            break

states_to_learn = []
for state in state_names:
    if state not in guessed_states:
        states_to_learn.append(state)
missing_data = pandas.DataFrame(states_to_learn)
missing_data.to_csv("states_to_learn.csv")
print(states_to_learn)
