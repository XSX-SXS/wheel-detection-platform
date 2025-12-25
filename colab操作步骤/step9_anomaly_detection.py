# 第九步：异常检测和高级特征工程（在Colab的新代码块中运行）

print("=== 🔍 异常检测与高级分析 ===\n")

# 1. 异常值检测函数
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (data[column] < lower_bound) | (data[column] > upper_bound)

# 2. 检测每个参数的异常值
print("📊 异常值检测结果：")
numeric_cols = ['diameter', 'average_bolt', 'center', 'pcd']
outlier_results = {}

for col in numeric_cols:
    outliers = detect_outliers_iqr(df, col)
    outlier_results[col] = outliers.sum()
    
    print(f"\n{col}:")
    print(f"  异常值数量: {outliers.sum()}")
    
    if outliers.sum() > 0:
        outlier_values = df.loc[outliers, col]
        print(f"  异常值范围: {outlier_values.min()} - {outlier_values.max()}")
        normal_values = df.loc[~outliers, col]
        print(f"  正常值范围: {normal_values.min()} - {normal_values.max()}")
        
        # 检查异常值与质量的关系
        outlier_quality = df.loc[outliers, 'type'].value_counts()
        print(f"  异常值中不合格产品: {outlier_quality.get('不合格', 0)} 个")

# 3. 异常值可视化
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.ravel()

for i, col in enumerate(numeric_cols):
    outliers = detect_outliers_iqr(df, col)
    
    # 箱线图
    box_data = [df.loc[~outliers, col], df.loc[outliers, col]]
    bp = axes[i].boxplot(box_data, 
                        labels=['正常值', '异常值'],
                        patch_artist=True)
    
    # 设置颜色
    bp['boxes'][0].set_facecolor('lightblue')
    if outliers.sum() > 0:
        bp['boxes'][1].set_facecolor('red')
        bp['boxes'][1].set_alpha(0.7)
    
    axes[i].set_title(f'{col} 异常值检测', fontsize=12, fontweight='bold')
    axes[i].set_ylabel(col)
    axes[i].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n✅ 异常值检测完成！")