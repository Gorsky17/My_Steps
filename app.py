

def res_4_20_cur(val_current):
    result_val = ((val_current * 100)/16)-25
    print(result_val)

def res_4_20_val(val_value):
    result_cur = ((val_value * 16)/100) + 4
    print(result_cur)
 
def res_0_20_cur(val_current):
    result_val = (val_current * 100)/20
    print(result_val)

def res_0_10_val(val_value):
    result_volt = (val_value * 10)/100
    print(result_volt)

def res_0_10_volt(val_voltage):
    result_val = (val_voltage * 100)/10
    print(result_val)

def res_2_10_volt(val_voltage):
    result_val = ((val_voltage * 100)/8)-25
    print(result_val)

def res_2_10_val(val_value):
    result_volt = ((val_value * 8)/100) + 2
    print(result_volt)
    

