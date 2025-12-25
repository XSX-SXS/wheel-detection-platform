# 第六步：相关性分析和交互式可视化（在Colab的新代码块中运行）

print("=== 🔥 高级可视化分析 ===\n")

# 1. 相关性热力图
plt.figure(figsize=(10, 8))
numeric_cols = ['diameter', 'average_bolt', 'center', 'pcd']
correlation_matrix = df[numeric_cols].corr()

sns.heatmap(correlation_matrix, 
            annot=True, 
            cmap='coolwarm', 
            center=0,
            square=True, 
            linewidths=0.5,
            fmt='.3f',
            cbar_kws={'shrink': 0.8})

plt.title('参数相关性热力图', fontsize=16, fontweight='bold', pad=20)
plt.show()

print("📈 相关性分析完成！")
print("🔍 观察要点：")
for i in range(len(numeric_cols)):
    for j in range(i+1, len(numeric_cols)):
        corr_val = correlation_matrix.iloc[i, j]
        if abs(corr_val) > 0.5:
            print(f"  {numeric_cols[i]} 与 {numeric_cols[j]}: {corr_val:.3f} (强相关)")
        elif abs(corr_val) > 0.3:
            print(f"  {numeric_cols[i]} 与 {numeric_cols[j]}: {corr_val:.3f} (中等相关)")

# 2. 交互式散点图（如果Plotly可用）
try:
    print("\n=== 🎯 创建交互式图表 ===")
    
    # 散点图：直径 vs PCD
    fig = px.scatter(df, 
                      x='diameter', 
                      y='pcd', 
                      color='type',
                      size='average_bolt',
                      hover_data=['id', 'center'],
                      title='直径 vs PCD 散点图 (按质量分类)',
                      labels={'diameter': '直径 (mm)', 'pcd': 'PCD (mm)', 'type': '质量'})
    
    fig.show()
    print("✅ 交互式散点图创建完成！")
    
except Exception as e:
    print(f"Plotly图表创建失败: {e}")
    print("继续创建静态图表...")
    
    # 备用静态散点图
    plt.figure(figsize=(10, 8))
    for quality in df['type'].unique():
        subset = df[df['type'] == quality]
        plt.scatter(subset['diameter'], subset['pcd'], 
                   s=subset['average_bolt']*10,
                   alpha=0.7, 
                   label=f'质量: {quality}')
    
    plt.xlabel('直径 (mm)')
    plt.ylabel('PCD (mm)')
    plt.title('直径 vs PCD 关系图')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

print("\n🎨 高级可视化完成！")