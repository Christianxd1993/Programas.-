import os
import time

# ___________ VARIABLES ____________
dancer_1 = '''
 ___
(*_*)
<) )-
/  \_

'''
dancer_2 = '''
  ___
 (*_*(
√(  (>
 /  \_

'''

dancer_3 = '''
  ___
 (*_*)/
 <) )
 /  \_

'''
conejo = '''

(\\(\\
(-.-)
O(")(")
'''

k = 1
while True:
    os.system("cls")
    print(f"{dancer_1}")
    time.sleep(0.4)
    os.system("cls")
    print(f"{dancer_2}")
    time.sleep(0.4)
    os.system("cls")
    print(f"{dancer_3}")
    time.sleep(0.4)

    if k <= 10:
        k += 1
    else:
        break
