from machine import RTC
import utime

def setRTCLocalTime():
    rtc = machine.RTC()
    rtc.ntp_sync("pool.ntp.org")
    utime.sleep_ms(750)
    print('\nRTC Set from NTP to UTC:', rtc.now())
    utime.timezone(3600)
    print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')
def setRTCLocalTime2():
    rtc = machine.RTC()
    rtc.ntp_sync("pool.ntp.org")

setRTCLocalTime2()
