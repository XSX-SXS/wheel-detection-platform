# 第七步：机器学习实验（在Colab的新代码块中运行）

print("=== 🤖 机器学习质量预测实验 ===\n")

# 1. 准备训练数据
X = df[['diameter', 'average_bolt', 'center', 'pcd']]
y = df['type']

# 将分类标签转换为数值（合格=1，不合格=0）
y_numeric = (y == '合格').astype(int)

print("📊 数据准备完成：")
print(f"特征矩阵形状: {X.shape}")
print(f"目标向量形状: {y.shape}")
print(f"合格样本数: {y_numeric.sum()}")
print(f"不合格样本数: {(y_numeric == 0).sum()}")

# 2. 分割训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y_numeric, test_size=0.3, random_state=42, stratify=y_numeric
)

print(f"\n📂 数据分割完成：")
print(f"训练集: {len(X_train)} 样本")
print(f"测试集: {len(X_test)} 样本")
print(f"训练集合格率: {y_train.mean():.2f}")
print(f"测试集合格率: {y_test.mean():.2f}")

# 3. 训练随机森林模型
print("\n🌲 训练随机森林模型...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 4. 模型预测和评估
y_pred = rf_model.predict(X_test)
accuracy = (y_pred == y_test).mean()

print(f"\n📈 模型评估结果：")
print(f"测试集准确率: {accuracy:.2%}")
print(f"\n详细分类报告：")
print(classification_report(y_test, y_pred, target_names=['不合格', '合格']))

# 5. 特征重要性分析
print("\n🔍 特征重要性分析：")
feature_importance = pd.DataFrame({
    '特征': X.columns,
    '重要性': rf_model.feature_importances_
}).sort_values('重要性', ascending=False)

for idx, row in feature_importance.iterrows():
    print(f"  {row['特征']}: {row['重要性']:.3f}")

print("\n✅ 机器学习实验完成！")