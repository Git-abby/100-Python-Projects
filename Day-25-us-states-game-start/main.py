import turtle
import pandas as pd

# Setup screen with background image
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load states data
data = pd.read_csv("50_states.csv")
all_states = data["state"].str.title().tolist()
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Guess a state:").title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        for state in missing_states:
            state_data = data[data.state == state]
            marker = turtle.Turtle()
            marker.hideturtle()
            marker.penup()
            marker.goto(state_data.x.item(), state_data.y.item())
            marker.color("red")
            marker.write(state_data.state.item(), align="center", font=("Arial", 8, "italic"))
        pd.DataFrame(missing_states, columns=["Missing States"]).to_csv("missing_states.csv", index=False)
        break

    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        state_data = data[data.state.str.title() == answer]

        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(state_data.iloc[0].x, state_data.iloc[0].y)
        marker.write(answer, align="center", font=("Arial", 10, "normal"))

screen.exitonclick()