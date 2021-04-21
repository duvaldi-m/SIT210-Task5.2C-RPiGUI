import tkinter as tk
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

## hardware
led_blue = LED(17)
led_red = LED(27)
led_green = LED(22)

## GUI DEFFINITIONS ##
win = tk.Tk()


win.title("LED switch")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

### EVENT FUNCTIONS ###

def ledBlueToggle():
	if led_blue.is_lit:
		led_blue.off()
		led_blue_button["text"] = "Turn blue on"

	else:
		led_blue.on()
		led_blue_button["text"] = "Turn blue off"

def ledRedToggle():
	if led_red.is_lit:
		led_red.off()
		led_red_button["text"] = "Turn red on"

	else:
		led_red.on()
		led_red_button["text"] = "Turn red off"

def ledGreenToggle():
	if led_green.is_lit:
		led_green.off()
		led_green_button["text"] = "Turn green on"

	else:
		led_green.on()
		led_green_button["text"] = "Turn green off"

def close():
	GPIO.cleanup()
	win.destroy()

### WIDGETS ###

led_blue_button = tk.Button(win, text = 'Turn blue on', 
font = myFont, command = ledBlueToggle,bg = 'blue', 
height = 1, width = 12)

led_red_button = tk.Button(win, text = 'Turn red on', 
font = myFont, command = ledRedToggle,bg = 'red', 
height = 1, width = 12)

led_green_button = tk.Button(win, text = 'Turn green on', 
font = myFont, command = ledGreenToggle,bg = 'green', 
height = 1, width = 12)

exit_button = tk.Button(win, text = 'close', 
font = myFont, command = close,bg = 'grey', 
height = 1, width = 6)

led_blue_button.grid(row = 0, column = 20)
led_red_button.grid(row = 4, column = 20)
led_green_button.grid(row = 8, column = 20)
exit_button.grid(row = 300, column = 300)

win.protocol("WM DELETE WINDOW",close)
win.geometry("300x200+10+20")
win.mainloop()



