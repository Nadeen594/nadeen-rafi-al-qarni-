def on_button_pressed_a():
    pass
basic.show_string("Nadeen")
input.on_button_pressed (Button.A,on_button_pressed_a )



def on_button_pressed_b ():
    pass
    basic.show_number(input.temperature ())
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_gesture_shake():
   pass 
for i in range(10):
    basic.show_number (i)
input.on_gesture (Gesture.SHAKE, on_gesture_shake) 