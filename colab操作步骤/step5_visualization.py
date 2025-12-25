# 第五步：数据可视化（在Colab的新代码块中运行）

print("=== 🎨 创建数据可视化 ===\n")

# 1. 质量分布饼图
plt.figure(figsize=(10, 8))
quality_counts = df['type'].value_counts()
colors = ['#2ecc71', '#e74c3c']  # 绿色表示合格，红色表示不合格

plt.pie(quality_counts.values, 
        labels=quality_counts.index, 
        autopct='%1.1f%%', 
        colors=colors, 
        startangle=90,
        textprops={'fontsize': 12})

plt.title('产品质量分布', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')
plt.show()

print("📊 质量分布可视化完成！")
print(f"合格产品: {quality_counts['合格']} 件 ({quality_counts['合格']/len(df)*100:.1f}%)")
print(f"不合格产品: {quality_counts['不合格']} 件 ({quality_counts['不合格']/len(df)*100:.1f}%)")

# 2. 参数分布直方图
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.ravel()

numeric_cols = ['diameter', 'average_bolt', 'center', 'pcd']
colors = ['skyblue', 'lightgreen', 'orange', 'pink']
titles = ['直径分布', '螺栓平均分布', '中心孔分布', 'PCD分布']

for i, (col, color, title) in enumerate(zip(numeric_cols, colors, titles)):
    axes[i].hist(df[col], bins=10, alpha=0.7, color=color, edgecolor='black')
    axes[i].set_title(title, fontsize=12, fontweight='bold')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('频次')
    axes[i].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n📈 参数分布可视化完成！")