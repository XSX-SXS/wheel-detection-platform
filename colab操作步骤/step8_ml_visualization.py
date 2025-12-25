# 第八步：机器学习结果可视化（在Colab的新代码块中运行）

print("=== 📊 机器学习结果可视化 ===\n")

# 1. 特征重要性可视化
plt.figure(figsize=(10, 6))
feature_importance_sorted = feature_importance.sort_values('重要性', ascending=True)

plt.barh(feature_importance_sorted['特征'], feature_importance_sorted['重要性'], 
         color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
plt.xlabel('重要性')
plt.title('特征重要性分析', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# 在条形上显示数值
for i, v in enumerate(feature_importance_sorted['重要性']):
    plt.text(v + 0.01, i, f'{v:.3f}', va='center')

plt.show()

print("📊 特征重要性图表已生成！")
print("💡 关键发现：")
top_feature = feature_importance.iloc[0]
print(f"  最重要特征: {top_feature['特征']} (重要性: {top_feature['重要性']:.3f})")

# 2. 混淆矩阵可视化
from sklearn.metrics import confusion_matrix
import seaborn as sns

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['不合格', '合格'], 
            yticklabels=['不合格', '合格'],
            cbar_kws={'shrink': 0.8})

plt.xlabel('预测标签')
plt.ylabel('真实标签')
plt.title('混淆矩阵', fontsize=14, fontweight='bold')
plt.show()

# 计算并显示详细指标
tn, fp, fn, tp = cm.ravel()
precision_qualified = tp / (tp + fp) if (tp + fp) > 0 else 0
recall_qualified = tp / (tp + fn) if (tp + fn) > 0 else 0
precision_unqualified = tn / (tn + fn) if (tn + fn) > 0 else 0
recall_unqualified = tn / (tn + fp) if (tn + fp) > 0 else 0

print(f"\n📈 详细性能指标：")
print(f"  合格产品 - 精确率: {precision_qualified:.2%}, 召回率: {recall_qualified:.2%}")
print(f"  不合格产品 - 精确率: {precision_unqualified:.2%}, 召回率: {recall_unqualified:.2%}")

# 3. 预测概率分布
y_proba = rf_model.predict_proba(X_test)[:, 1]  # 合格的概率

plt.figure(figsize=(10, 6))
plt.hist(y_proba, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
plt.xlabel('预测为合格的概率')
plt.ylabel('频次')
plt.title('预测概率分布', fontsize=14, fontweight='bold')
plt.axvline(x=0.5, color='red', linestyle='--', label='决策边界')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\n✅ 机器学习结果可视化完成！")