#resursive function
def show(n):
    if n == 0:
        return
    print(n)    # پہلے پرنٹ کریں
    show(n - 1) # پھر فنکشن کو دوبارہ کال کریں
    print("END")

show(5)







