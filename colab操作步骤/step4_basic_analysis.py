# 第四步：基础数据分析（在Colab的新代码块中运行）

print("=== 📊 数据探索分析 ===\n")

# 1. 基本统计信息
print("1️⃣ 基本统计信息：")
print(df.describe())

print("\n2️⃣ 质量分布统计：")
quality_counts = df['type'].value_counts()
print(quality_counts)

# 计算百分比
print("\n📈 质量百分比：")
for quality, count in quality_counts.items():
    percentage = (count / len(df)) * 100
    print(f"  {quality}: {count} 件 ({percentage:.1f}%)")

# 2. 参数范围分析
print("\n3️⃣ 参数范围分析：")
numeric_cols = ['diameter', 'average_bolt', 'center', 'pcd']
for col in numeric_cols:
    min_val = df[col].min()
    max_val = df[col].max()
    mean_val = df[col].mean()
    std_val = df[col].std()
    print(f"  {col}:")
    print(f"    范围: {min_val} - {max_val}")
    print(f"    平均值: {mean_val:.1f} ± {std_val:.1f}")

print("\n✅ 基础分析完成！")