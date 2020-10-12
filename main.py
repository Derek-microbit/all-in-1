def on_button_pressed_a():
    basic.show_number(step)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(input.compass_heading())
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global step
    step += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_three_g():
    basic.show_number(input.light_level())
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

step = 0
step = 0