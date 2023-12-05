import matplotlib.pyplot as plt
import numpy as np
import math

# eps =
#Tc1 = 1073  # 200 - 300 по Цельсьсию
Tc1 = 300  # 200 - 300 по Цельсьсию
#T_f_max = 2000  # в Градусах Цельсия
T_f_max = 3421  # в Градусах Цельсия
f_k = 3  # Это по госту 19671-91 для проволоки ВА-I-Б1-200-3-Р Яе0.021.119ТУ
ff = 10  # не еби мозг возьми эту херь
V = 6 # л/мин - расход жидкости
Tj = 40 # Это в градусах Цельсия - средняя температура охлаждающей жидкости
# ld_med = 330 # ккал/(м * ч * град) Это для меди
lb_med = 3.7 # Вт/(см * град) Это для меди
lb_wol = 1.2 # Вт/(см * град) Это для вольфрама
lb_masl = 0.094 # ккал/(м * ч * град) Это для масла
Pr = 43.9  # для масла при 100 градусах
nu_masl = 10.3 * (10 ** -6) # м^2/c кинематическая вязкость масла
k0 = 2.2 * (10 ** -9) # Размерная константа в формуле Крамерса
e_el = 1.6 * (10 ** -19) # заряд электрона
Z_vol = 74 # Атомный номер вольфрама (мишени)

tabl_vod = {1.16 * (10 ** -33): 1000,
            6.81 * (10 ** -30): 1100,
            1.01 * (10 ** -26): 1200,
            4.22 * (10 ** -24): 1300,
            7.88 * (10 ** -22): 1400,
            7.42 * (10 ** -20): 1500,
            3.92 * (10 ** -18): 1600,
            1.31 * (10 ** -16): 1700,
            2.97 * (10 ** -15): 1800,
            4.62 * (10 ** -14): 1900,
            5.51 * (10 ** -13): 2000,
            4.95 * (10 ** -12): 2100,
            3.92 * (10 ** -11): 2200,
            2.45 * (10 ** -10): 2300,
            1.37 * (10 ** -9): 2400,
            6.63 * (10 ** -9): 2500,
            2.76 * (10 ** -8): 2600,
            9.95 * (10 ** -7): 2700,
            3.51 * (10 ** -7): 2800,
            1.08 * (10 ** -6): 2900,
            3.04 * (10 ** -6): 3000}

def el_para_kat():
    d_n = 0.2 #mm - это стандарт
    t = 2000 #ч - это долговечность катода
    # так как t = 2,4 * (10 ** -4) * (d_n / M), где М - это скорость испарения вольфрама
    M = 2,4 * (10 ** -4) * (d_n / t)
    print("Скорость испарения Вольфрама: ", t)

    #print("len_tabl: ", len(tabl_vod))
    print("len_tabl[1]: ", tabl_vod[1])
    #for i in range(0, len(tabl_vod)):
    #тут должн быть автоматизированный выбор

# def Rich_Dah(T: int):
#     print("Рассчет формулы Ричардсона-Дэшмана")
#     # print("Термоэлектронная постоянная: ", A_t_c)
#     # print("Прозрачность потенциального барьера: ", D_proz)
#     print("Произведение А на D(термоэлктронная постоянная на прозрачность): ", A_n)
#     print("Температура выхода (степень экспоненты): ", efk)
#     j_e = A_n * (T ** 2) * np.exp(-1 * (efk) / T)
#     print("Плотность термоэликтрической эмиссии: ", j_e)
#
#     return j_e
#
# def f_I_sh_e(j_e):
#     I_sh_e = np.pi * j_e
#     print("Ток эмиссии единичного электрода: ", I_sh_e)
#
#     return I_sh_e
#
# def f_L(I_sh_e, d, I_e):
#         L = I_e / (I_sh_e * d)
#         print("Длина спирали: ", L)
#
#         return L
# def f_I_n(T):
#     print("По закону Стефана-Больцмана расчет светимость вольфрама")
#     print("Постоянная Стефана-Больцмана: ", sigma)
#     eps = sigma * (T ** 4)
#     print("Светимость вольфрама: ", eps)
#     rho = 70.39 * (10 ** -6)     #надо делать по нормальному - в таблице данные
#     print("Удельное сопротивление вольфрама в Ом на см (ВНИМАНИЕ): ", rho)
#     I_n = (np.pi / 2) * ((eps / rho) ** 0.5)
#     print("Ток накала единичного катода: ", I_n)
#
#     return I_n
#
#
# def f_U_n():
#     rho = 70.39 * (10 ** -6)  # надо делать по нормальному - в таблице данные
#     print("Удельное сопротивление вольфрама в Ом на см (ВНИМАНИЕ): ", rho)
#     U_n = 2 * ((eps * rho) ** 0.5)
#     print("Напряжение накала единичного катода: ", U_n)
#
#     return U_n
#
# def f_P_n(I_n, U_n):
#     # print("По закону Стефана-Больцмана расчет светимость вольфрама")  #это по формуле, посчитано чесно, нооо можно просто перемножить :b
#     # print("Постоянная Стефана-Больцмана: ", sigma)
#     # eps = sigma * (T ** 4)
#     # print("Светимость вольфрама: ", eps)
#     # P_n = np.pi * eps
#     # print("Мощность накала единичного катода: ", P_n)
#     P_n = I_n * U_n
#
#     return P_n

def f_D_ker(d_p = 0.2):
    print("Для выбранной проволоки фактор керна составляет ", f_k)
    d_p = 0.2 #это в мм, по ГОСТу (рекомендуется) - по словам Ильи ;b
    D_ker = f_k * d_p
    print("Для выбранной проволооки диаметр составляет: ", d_p)
    print("Диаметр керна: ", D_ker)
    return D_ker

def f_D_sp(D_ker, d_p = 0.2):
    D_sp = D_ker + d_p
    print("Диаметр спирали:", D_sp)
    return D_sp

def f_L_vint():
    h_sh = 0.5 # ЭТО В ММ!!!
    print("Так как шаг спирали должен быть не меньше диаметра проволоки, то для данной задачи был выбран шаг: ", h_sh)
    L_vint = np.pi * ((((np.pi ** 2) * (f_D_sp(f_D_ker()) ** 2)) + (h_sh ** 2)) ** 0.5)
    print(f"Длина спирали: {L_vint} мм")

    return L_vint

def BreakDownVol(U_pit: float, C: float = 47, k: float = 0.6):
    print("Расчет пробивного напряжения для трубки с массивным анодом с чехлом")
    print("Для трубки с массивным анодом с чехлом считается, что на кажлые 10 кВ питающего напряжения необходимо выжелить 1 мм зазора")
    print("Питающее напряжение: ", U_pit)
    d = U_pit / 10
    print("Расстояние между катодом и анодом: ", d)
    # C = 47 кВ/мм
    # k = 0.6
    print(f"Приняты следующие коффициенты: C {C} кВ/мм и k: {k}")
    U_pob = C * (d ** k)
    print(f"Пробивное напряжение: {U_pob} кВ")

    return U_pob

def potential_graph(Elec_distance: float, Tube_length: float, Katod_length: float, U_prob: float):
    k1 = U_prob / Tube_length
    b1 = 0
    k2 = U_prob / Elec_distance
    b2 = -1 * Katod_length * k2
    k1 = round(k1, 2)

    print(f"Формула первой прямой: y = {k1}x")
    print(f"Формула второй прямой: y = {k2}x {b2}")

    #x1 = range(0, int(Tube_length), 0.1)
    len1 = int(Tube_length / 0.01)
    x1 = [0] * len1
    y1 = [0] * len1
    for i in range(0, len1):
        x1[i] = 0.01 * i
    for i in range(0, len1):
        y1[i] = k1 * x1[i] + b1

    len2 = int(Elec_distance / 0.01)
    x2 = [0] * len2
    y2 = [0] * len2
    #x2 = range(Katod_length, (Katod_length + 10), 0.1)
    for i in range(0, len2):
        x2[i] = Katod_length + 0.01 * i
    for i in range(0, len2):
        y2[i] = k2 * x2[i] + b2

    #plt.plot([0, Tube_length], [0, U_prob])
    plt.plot(x1, y1)
    plt.plot(x2, y2)

    plt.plot([Katod_length, Katod_length], [0, (k1 * Katod_length + b1)], '--k')
    plt.plot([(Katod_length + Elec_distance), (Katod_length + Elec_distance)], [0, U_prob], '--k')

    #plt.plot(x2, y2)
    plt.grid(True)
    plt.xlabel("Длина,  мм")
    plt.ylabel("Напряжение, кВ")
    plt.legend(['U1', 'U2'])
    plt.show()

    U01 = round((k1 * Katod_length + b1), 2)
    U02 = round((U_prob - (k1 * (Katod_length + 10) + b1)), 2)

    return U01, U02

def DistanceElectrodeBallone(Elec_distance: float, Tube_length: float, Katod_length: float, U_prob: float, B: float = 1.25):
    print("Рассчет расстояния между электродом и баллоном")
    print("Построение графика распределение потенциала вдоль трубки")
    U01, U02 = potential_graph(Elec_distance, Tube_length, Katod_length, U_prob)
    print("U01: ", U01)
    print("U02: ", U02)
    print("Коэффициент В: ", B)
    r_eb1 = 0.1 * B * U01
    r_eb2 = 0.1 * B * U02
    print(f"rэб >= {r_eb1} мм")
    print(f"rэб >= {r_eb2} мм")

def f_d_ekv(S: float, L: float):
    d_ekv = (4 * S) / L
    print("Эквивалентный диаметр", d_ekv)

    return d_ekv

def f_liquid_speed(n: float, d_ekv: float):
    print("Для расчета скорость жидкости в турбулентном режиме число Рейнольдса принято равным 2200")
    Re = 2200
    w =(n * Re) / d_ekv
    print("Cкоростm жидкости для турбулентного потока: ", w)

    return w

def Reynolds_numb(d: float, w:float, n: float):
    print("Расчет числа Рейнольдса")
    Re  = (w * d) / n
    print("Число Рейнольдса: ", Re)

    return Re

def Prandtl_numb(n: float, a: float):
    print("Число Пранделя взято из таблицы в Хараджа")
    print("Расчет числа Прандтля")
    Pr = n / a
    print("Число Прандтля: ", Pr)

    return Pr

def heat_transfer_coefficient(lb: float, d1: float, d2: float, Re1: float, Re2: float):
    print("Рассчет коэффициентов теплоотдачи")
    #d_ekv = f_d_ekv(S, L)
    # Re = Reynolds_numb(lb, S, L, w, n)
    #w = f_liquid_speed(n, d_ekv)
    #Re = 2200
    #Pr = Prandtl_numb(n, a)

    a1 = 1.68 * (Re1 ** 0.46) * (Pr ** 0.4) * (lb / d1)
    a2 = 0.22 * (Re2 ** 0.6) * (Pr ** 0.4) * (lb / d2)

    print("Первый коэффициент теплопередачи: ", a1)
    print("Второй коэффициент теплопередачи: ", a2)

    return a1, a2

def in_perimeter(D2: float):
    l = np.pi * D2
    print("Внутренний периметр сеччения: ", l)

    return l

def liquid_speed_2(V: float, S: float):
    w = ((10 ** -4) * V) / (6 * S)
    print("Скорость жидкости: ", w)

    return w

def temp_in_the_fok_midl(Tc: float, P: float, R: float, lb_a: float):
    Tf = round(Tc + (P / (np.pi * R * lb_a)) * ff, 3)
    print(f"Температура в центре фокусного пятна: {Tf} градусов Цельсия")

    return Tf


def temp_in_the_sl_midl(Tc: float, P: float, R: float, lb_a: float):
    Tm = round(Tc + (P / (np.pi * R * lb_a)) * ff, 3)
    print(f"Температура в центре спая мишени: {Tm} градусов Цельсия")

    return Tm

def temp_in_point(Tc1: float, P: float, R: float, H: float, lb_a: float):
    Tc = round(Tc1 + ((P * (H - 2 * R)) / (np.pi * (R ** 2) * lb_a)), 3)
    print(f"Температура в сечении: {Tc} градусов Цельсия")

    return Tc

def f_P_max(R: float, H: float, lb: float):
    P_max = round(((T_f_max - Tc1) * np.pi * (R ** 2) * lb) / (H - 2 * R + ff * R), 3)
    print("Максимальная мощность, приложенная к цилиндрическому аноду: ", P_max)

    return P_max

def sq_torc(D1: float, D2: float):
    print(D2)
    F1 = round((np.pi * (D2 ** 2)) / 4, 6)
    #F2 = round((np.pi * ((D1 ** 2) - (D2 ** 2))) / 4, 6)
    F2 = round((np.pi * ((D1 ** 2))) / 4, 6)
    print("Площадь сечения торцевой поверхности: ", F1)
    print("Площадь сечения меднои трубчатой части анода: ", F2)

    return F1, F2

def R_m(lb: float, D_anod: float, a2: float, F2: float, Lp: float):
    #a1, a2 = heat_transfer_coefficient(lb, S, L, n, a)
    #F1, F2 = sq_torc(D1, D2)
    m = (((a2 * Lp) / (lb * F2)) ** 0.5)
    print("Расчет m: ", m)

    return m

#def  power_density(P: float, )

def f_Q_1_2(a1: float, F1: float, F2: float, tst: float, Tj: float, m: float, l:float):
    Q1 = a1 * F1 * (tst - Tj)
    Q2 = (tst - Tj) * lb_med * F2 * m * tst * l
    print("Тепло отдаваемое торцевой частью охлаждаемой поверхности: ", Q1)
    print("Тепло отдаваемое цилиндрической частью: ", Q2)

    return Q1, Q2

def thermal_mode_of_anode(P: float, R: float, H: float):
    print("Расчет теплового режима анода")
    Pr = 220
    print("Критерий Пранделя: ", Pr)
    print("Расход жидкости: ", V)
    Tc = temp_in_point(Tc1, P, R, H, lb_med)
    Tf = temp_in_the_fok_midl(Tc, P, R, lb_wol)
    Tm = temp_in_the_sl_midl(Tc, P, R, lb_med)
    print(f"При этом максимальная температура для вольфрама составляет: {T_f_max} градусов Цельсия")

    P_max = f_P_max(R, H, lb_wol)

def cooling_sys(D1: float, D2: float, V: float):
    print("Расчет охлаждающей системы")
    F1, F2 = sq_torc(D1, D2)
    w1 = liquid_speed_2(V, F1)
    w2 = liquid_speed_2(V, F2)
    Re1 = Reynolds_numb(D1, w1, nu_masl)
    Re2 = Reynolds_numb(D2, w2, nu_masl)
    Lp = in_perimeter(D2)
    a1, a2 = heat_transfer_coefficient(lb_masl, D1, D2, Re1, Re2)
    m = R_m(lb_med, D2, a2, F2, Lp)
    Q1, Q2 = f_Q_1_2(a1, F1, F2, 100, 40, m, Lp)

# def radiation_patterns(max_fi: float, begin_fi: float):
#     print("Расчет диаграммы направленности")
#     fi = [0] * 720
#     I = [0] * 720
#     delta = max_fi / 720
#     for i in range(0, 720):
#         fi[i] = i * delta + begin_fi
#     I = P / Ua
#     for i in range(0, 720):
#         I[i] = ((k0 * (e_el ** 2) * (Ua ** 2) * I * Z_vol) / (2 * (r ** 2))) * math.e(-1 * ((mu * x0) / math.cos(fi)))


if __name__ == '__main__':
    #Хараджа страница 144 - таблица констант по охлождению
    #el_para_kat()
    print("Ну давай, посчитай мне эту пупу!")
    #U_prob = int(input("Введите пробивное напряжение в киловольтах: "))

    #n = float(input("Введите кинематическую вязкость жидкости: "))
    n = 10.3 * (10 ** -6) #Внимание! это в размерности [м^2 / с]

    # lb = float(input("Введите коэффициент теплопроводности жидкости[ккал / (м*ч*К)]: "))
    #lb = 0.094 #Внимание! это в размерности [ккал / (м^2 * ч * град)]

    # a = float(input("Введите коэффициент теплопроводности жидкости[м^2 / с]: "))
    # a =

    #P = float(input("Введите мощность трубки (в Вт): "))
    P = 1000 # Вт

    # H = float(input("Введите высоту анода (в см): "))
    H = 1.777

    # R = float(input("Введите в см радиус анода (мишени): "))
    R = 0.971

    # D1 = float(input("Введите в м диаметр внутренней трубки: "))
    D1 = 0.02

    # D1 = float(input("Введите в м наружный диаметр подводящей трубки: "))
    D2 = 0.01011

    # V = float(input("Введите расход жидкости в л/мин: "))
    V = 6

    U_prob = 100

    #f_L_vint()
    #BreakDownVol(U_prob)
    #DistanceElectrodeBallone(10, 147.8, 80, U_prob)
    #thermal_mode_of_anode(P, R, H)
    cooling_sys(D1, D2, V)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
