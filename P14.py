import numpy as np
import matplotlib.pyplot as plt

# 함수: 총 지연
def total_delay(L, R, I):
    queuing_delay = (L * I) / R * (1 - I)
    transmission_delay = 1 / R
    return queuing_delay + transmission_delay

# L/R 값 범위 설정
L_R_values = np.linspace(0, 0.95, 100)  # 0 <= L/R < 1

# 각 L/R 값에 대한 총 지연 계산
total_delays = []
for L_R in L_R_values:
    I = L_R  # Traffic intensity I = L/R
    total_delays.append(total_delay(1, 1, I))  # Assume L = R = 1 for simplicity

# 그래프 그리기
plt.plot(L_R_values, total_delays, label='Total Delay')
plt.xlabel('L/R')
plt.ylabel('Total Delay')
plt.title('Total Delay as a Function of L/R')
plt.legend()
plt.grid(True)
plt.show()
