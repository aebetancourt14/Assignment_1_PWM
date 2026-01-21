#Assignment_1_code
import time, asyncio

pin_blue = 1
pin_green = 2
pin_red = 3
pwm_freq_hz = 50.0
duty_cycle_fixed = 25.0      
on_blink = 1.0      
off_blink = 1.0

running = True
current_color_pin = pin_red

def all_off():
    pmoda_write(pin_red, 0)
    pmoda_write(pin_green, 0)
    pmoda_write(pin_blue, 0)
    
def set_color_on(pin_pwm):
    if pin_pwm == pin_red:
        pmoda_write(pin_green, 0)
        pmoda_write(pin_blue, 0)
    elif pin_pwm == pin_green:
        pmoda_write(pin_red, 0)
        pmoda_write(pin_blue, 0)
    elif pin_pwm == pin_blue:
        pmoda_write(pin_red, 0)
        pmoda_write(pin_green, 0)

async def pwm_cycle(pin_pwm=3, freq_hz=100, duty_cycle=10, duration_s=1):  
    global current_color_pin
    ## force pmoda pins 2 & 4 low; only have green on
    ##pmoda_write(2, 0)
    ##pmoda_write(4, 0)
    if freq_hz <= 0:
        freq_hz = 1.0
    if duty_cycle < 0:
        duty_cycle = 0.0
    if duty_cycle > 100:
        duty_cycle = 100.0
    if duration_s <= 0:
        return
    #set_color_on(pin_pwm)
    
    #edge cases for 0 and 100 duty_cycle
    if duty_cycle <= 0.0:
        all_off()
        await asyncio.sleep(duration_s)
        return
    if duty_cycle >= 100.0:
        pin = current_color_pinent_color_pin
        set_color_on(pin)
        pmoda_write(pin, 1)
        await asyncio.sleep(duration_s)
        all_off()
        return
    
    period = 1.0 / freq_hz
    T_on = period * (duty_cycle / 100.0)
    T_off = period - T_on
    end_time = time.perf_counter() + duration_s
    #pmoda_write(pin_pwm, 0 )
    #print("before while\r\n")
  
    while time.perf_counter() < end_time:
        pin = current_color_pin
        set_color_on(pin)
       #pmoda_write(pin_pwm, 1)
       #await asyncio.sleep(T_on)
       #pmoda_write(pin_pwm, 0)
       #await asyncio.sleep(T_off)
            
    #print("outside while\r\n")        
    all_off()  
    
async def blinking_state():
    global running #current_color_pin
    
    while running:
        await pwm_cycle(pwm_freq_hz, duty_cycle_fixed, on_blink)#current_color_pin
        
        all_off()
        await asyncio.sleep(off_blink)
    all_off()
    
async def button_tasking (loop):
    # Button mapping: BTN0->RED; BTN1->GREEN; BTN2->BLUE; BTN3->STOP
    global running, current_color_pin
    #last = 0
    while running:
        await asyncio.sleep(0.01)
        val = btns.read()
        #pressed = val & ~last
        #last = val
        if val & 0x1:
            current_color_pin = pin_red
        elif val & 0x2:
            current_color_pin = pin_green
        elif val & 0x4:
            current_color_pin = pin_blue
        elif val & 0x8:
            running = False
            loop.stop()
            break
      
async def stop_after(loop, seconds=20):
    global running
    await asyncio.sleep(seconds)
    running = False
    loop.stop()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.create_task(blinking_state())
loop.create_task(button_tasking(loop))
loop.create_task(stop_after(loop, 20)) #timeout after 20 secs

loop.run_forever()
loop.close()

all_off()
print("Stopped blinking (BTN3).")      
      
    