import time
import webbrowser

total_breaks = 3
breack_count = 0
print ("This Program started on "+time.ctime())
while breack_count < total_breaks:
    
      time.sleep(2*60*60)
      webbrowser.open("https://www.youtube.com/watch?v=TbSHGRidV-I&t=15s")
      breack_count = breack_count + 1
