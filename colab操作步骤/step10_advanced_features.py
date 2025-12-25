# 第十步：高级特征工程与模型优化（在Colab的新代码块中运行）

print("=== 🧠 高级特征工程与模型优化 ===\n")

# 1. 创建新特征
df_features = df.copy()

# 比率特征
df_features['diameter_center_ratio'] = df_features['diameter'] / df_features['center']
df_features['pcd_diameter_ratio'] = df_features['pcd'] / df_features['diameter']
df_features['bolt_density'] = df_features['average_bolt'] / df_features['diameter']

# 偏差特征（与标准值的差值）
standard_values = {'diameter': 650, 'average_bolt': 48, 'center': 80, 'pcd': 280}
for col in ['diameter', 'average_bolt', 'center', 'pcd']:
    df_features[f'{col}_deviation'] = abs(df_features[col] - standard_values[col])

# 异常值标记
for col in ['diameter', 'average_bolt', 'center', 'pcd']:
    df_features[f'{col}_outlier'] = detect_outliers_iqr(df_features, col).astype(int)

print("🔧 新创建的特征：")
new_features = ['diameter_center_ratio', 'pcd_diameter_ratio', 'bolt_density', 
                'diameter_deviation', 'average_bolt_deviation', 'center_deviation', 'pcd_deviation']
for feature in new_features:
    print(f"  {feature}: 均值={df_features[feature].mean():.3f}, 标准差={df_features[feature].std():.3f}")

# 2. 使用扩展特征训练模型
print("\n🌲 训练扩展特征模型...")
feature_cols = (['diameter', 'average_bolt', 'center', 'pcd'] + 
                new_features + 
                [f'{col}_outlier' for col in ['diameter', 'average_bolt', 'center', 'pcd']])

X_extended = df_features[feature_cols]
y_extended = (df_features['type'] == '合格').astype(int)

# 数据分割
X_train_ext, X_test_ext, y_train_ext, y_test_ext = train_test_split(
    X_extended, y_extended, test_size=0.3, random_state=42, stratify=y_extended
)

# 训练扩展模型
rf_extended = RandomForestClassifier(n_estimators=200, random_state=42, max_depth=5)
rf_extended.fit(X_train_ext, y_train_ext)

# 3. 模型性能对比
y_pred_original = rf_model.predict(X_test)
y_pred_extended = rf_extended.predict(X_test_ext)

accuracy_original = (y_pred_original == y_test).mean()
accuracy_extended = (y_pred_extended == y_test_ext).mean()

print(f"\n📊 模型性能对比：")
print(f"基础模型准确率: {accuracy_original:.2%}")
print(f"扩展模型准确率: {accuracy_extended:.2%}")
print(f"性能提升: {(accuracy_extended - accuracy_original) * 100:.1f} 个百分点")

# 4. 扩展特征重要性
print(f"\n🔍 扩展特征重要性（前8位）：")
importance_extended = pd.DataFrame({
    '特征': X_extended.columns,
    '重要性': rf_extended.feature_importances_
}).sort_values('重要性', ascending=False)

for i, (_, row) in enumerate(importance_extended.head(8).iterrows()):
    print(f"  {i+1}. {row['特征']}: {row['重要性']:.3f}")

print("\n✅ 高级特征工程完成！")