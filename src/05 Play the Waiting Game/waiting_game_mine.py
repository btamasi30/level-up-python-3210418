# # Python Code Challenge #5: Play the Waiting Game

# Your goal is to implement a function, `waiting_game()`, that prints a message for the player to wait a random amount of time, somewhere between two to four seconds. When the player presses Enter, that starts a timer. The player's goal is to wait the specified number of seconds and then press Enter again. That displays the elapsed time, along with a message about whether the player was too fast, too slow, or right on target. 

# ## Example Test Output
# ```console
# >>> waiting_game()

# Your target time is 2 seconds
#  ---Press Enter to Begin---

# ...Press Enter again after 2 seconds...

# Elapsed time: 1.680 seconds
# (0.320 seconds too fast)
# ```

import random
from datetime import datetime, timedelta


def waiting_game():
  waitingtime = random.randint(2, 4)

  print(f'''Welcome in the Waiting game!
        Your target time is {waitingtime} seconds        
        ''')
  input(f'\n---Press Enter to Begin---')
  start = datetime.now()

  input(f'\n...Press Enter again after {waitingtime} seconds...')

  stop = datetime.now()
  delta = stop-start
  d = delta.total_seconds()
  diff = d-waitingtime

  print(f"Elapsed time: {d:.3f} seconds")
  if diff == 0:
    print('(Unbelievable! Perfect timing!)')
  else:
    postfix = "fast" if diff < 0 else "slow" 
    print(f"({diff: .3f} seconds too {postfix})")



waiting_game()