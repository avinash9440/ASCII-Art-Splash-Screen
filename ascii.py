import random
import os
i = random.randrange(9) + 1 
website="https://github.com/avinash9440/ASCII-Art-Splash-Screen/tree/master/art"+ str(i) + ".txt"
os.system("curl " +  website)
