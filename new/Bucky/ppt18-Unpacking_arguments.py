def health_Calculator(age, apples_ate, Cig_smoked):
    cal_avg=(100-age)+(apples_ate*3.5)-(Cig_smoked*2)
    print(cal_avg)

bucky_data = [27, 20, 0]
health_Calculator(bucky_data[0], bucky_data[1], bucky_data[2])
health_Calculator(*bucky_data)