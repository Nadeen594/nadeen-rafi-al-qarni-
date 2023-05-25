basic.showString("Nadeen")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    basic.showNumber(input.temperature())
})
for (let i = 0; i < 10; i++) {
    basic.showNumber(i)
}
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
})
