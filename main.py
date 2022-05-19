def Spin(direction: str):
    if direction.substr(0, 1) == "L":
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.LEFT, speed)
    else:
        Kitronik_Move_Motor.spin(Kitronik_Move_Motor.SpinDirections.RIGHT, speed)
    basic.pause(pause2)
    Kitronik_Move_Motor.stop()
# Used to back out of the situation

def on_data_received():
    global Exit, action, moveMotorZIP
    Exit = 1
    action = serial.read_until(serial.delimiters(Delimiters.HASH))
    if action == "F":
        Move()
    else:
        # Spin the opposite way to when you went in
        if action == "L":
            Spin("R")
        else:
            moveMotorZIP = Kitronik_Move_Motor.create_move_motor_zipled(4)
            moveMotorZIP.show_rainbow(1, 360)
    basic.pause(pause2)
serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)

def Move():
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, speed)
    basic.pause(pause2)
    Kitronik_Move_Motor.stop()
distance = 0
moveMotorZIP: Kitronik_Move_Motor.MoveMotorZIP = None
action = ""
pause2 = 0
speed = 0
Exit = 0
Exit = 0
speed = 50
pause2 = 250
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
serial.write_line("S")
basic.show_icon(IconNames.CHESSBOARD)

def on_forever():
    global distance
    if Exit == 0:
        distance = Kitronik_Move_Motor.measure()
        if distance > 10:
            Move()
            serial.write_line("F")
        elif distance < 10:
            serial.write_line("L")
            Spin("L")
basic.forever(on_forever)
