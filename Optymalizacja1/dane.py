class Dane:

    Pa = 0.7 #m^2 Pole podstawy zbiornika A
    Va = 5.0 #m^3 Objetosc zbiornika A
    Ta = 90.0 #*C Temp wody zbiornika A

    Pb = 1.0 #m^2 Pole podstawy zbiornika B
    Vb = 1.0 #m^3 Objetosc zbiornika B
    Tb = 10.0 #*C Temp wody zbiornika B

    Tbin = 10 #*C Temp wody ktora sie wlewa do zbiornika B
    Fbin = 0.01 #*c l/s szybkość wplywania wody do zbiornika B

    Db = 0.00365665  #m^2 prędkość wylewania sie wody z zbiornika B

    a = 0.98 #wspolczynnik odpowiadajacy za lepkosc cieczy
    b = 0.63 #wsp odpowiadajacy za zwężenie strumienia cieczy
    g = 9.81 # przyspieszenie ziemskie

    # szukana: Celem optymalizacji jest znalezienie takiego pola przekroju 𝐷𝐴, dla którego maksymalna temperatura
    # wody w zbiorniku B będzie równa 50℃ .
    # Da nalezy [1,100] cm^2
    t0 = 0 # czas poczatkowy
    tend = 1000 #s czas koncowy
    dt = 1 #s skok czasu