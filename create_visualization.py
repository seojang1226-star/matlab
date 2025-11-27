"""
시각화 예제 - matplotlib으로 그래프 생성
"""
import matplotlib.pyplot as plt
import math

# 데이터 생성
x = [i * 0.1 for i in range(0, 63)]  # 0 to 2π
y_sin = [math.sin(val) for val in x]
y_cos = [math.cos(val) for val in x]

# Figure 생성
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# 첫 번째 그래프: Sin 곡선
ax1.plot(x, y_sin, 'b-', linewidth=2, label='sin(x)')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.set_title('Sine Wave', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5)

# 두 번째 그래프: Sin & Cos 비교
ax2.plot(x, y_sin, 'r-', linewidth=2, label='sin(x)')
ax2.plot(x, y_cos, 'g-', linewidth=2, label='cos(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Sin vs Cos', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.axhline(y=0, color='k', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.savefig('/home/user/matlab/visualization_demo.png', dpi=150, bbox_inches='tight')
print("그래프 저장 완료: visualization_demo.png")

# 두 번째 그래프: 막대 그래프
plt.figure(figsize=(10, 6))

categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [45, 38, 52, 61, 55, 48]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']

bars = plt.bar(categories, sales, color=colors, edgecolor='black', linewidth=1.5)

# 막대 위에 값 표시
for bar, value in zip(bars, sales):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{value}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (Million ₩)', fontsize=12)
plt.title('Monthly Sales Report', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.ylim(0, max(sales) * 1.15)

plt.tight_layout()
plt.savefig('/home/user/matlab/bar_chart_demo.png', dpi=150, bbox_inches='tight')
print("막대 그래프 저장 완료: bar_chart_demo.png")

# 세 번째 그래프: 산점도 (Scatter plot)
plt.figure(figsize=(10, 6))

# 데이터 생성 (시뮬레이션)
import random
random.seed(42)

temperature = [20 + random.uniform(-3, 3) + i*0.5 for i in range(30)]
ice_cream_sales = [50 + (t-20)*10 + random.uniform(-20, 20) for t in temperature]

plt.scatter(temperature, ice_cream_sales,
           s=100, c=temperature, cmap='coolwarm',
           edgecolors='black', linewidth=1.5, alpha=0.7)

plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Ice Cream Sales', fontsize=12)
plt.title('Temperature vs Ice Cream Sales', fontsize=14, fontweight='bold')
plt.colorbar(label='Temperature (°C)')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/user/matlab/scatter_demo.png', dpi=150, bbox_inches='tight')
print("산점도 저장 완료: scatter_demo.png")

print("\n모든 그래프 생성 완료!")
