# 第十一步：结果导出与实验总结（在Colab的新代码块中运行）

print("=== 📊 实验结果导出与总结 ===\n")

# 1. 生成完整实验报告
results = {
    "实验概况": {
        "实验时间": "2025年12月25日",
        "数据集大小": len(df),
        "特征数量": len(X.columns),
        "目标类别": list(df['type'].unique())
    },
    
    "数据质量分析": {
        "合格率": (df['type'] == '合格').mean(),
        "不合格率": (df['type'] == '不合格').mean(),
        "总异常值": sum(outlier_results.values()),
        "各参数异常值": outlier_results
    },
    
    "机器学习模型性能": {
        "基础模型": {
            "准确率": accuracy_original,
            "算法": "RandomForestClassifier",
            "参数数量": len(X.columns)
        },
        "扩展模型": {
            "准确率": accuracy_extended,
            "算法": "RandomForestClassifier_Extended",
            "参数数量": len(X_extended.columns),
            "性能提升": accuracy_extended - accuracy_original
        }
    },
    
    "关键发现": {
        "最重要特征": importance_extended.iloc[0]['特征'],
        "异常检测效果": "发现多个参数的异常值",
        "特征工程价值": f"{(accuracy_extended - accuracy_original) * 100:.1f}% 准确率提升"
    },
    
    "技术统计": {
        "使用库": ["pandas", "numpy", "matplotlib", "seaborn", "plotly", "scikit-learn"],
        "可视化图表数量": 8,
        "机器学习模型": 2,
        "新创建特征": len(new_features)
    }
}

# 2. 显示完整报告
print("📋 完整实验报告：")
print("=" * 60)

for category, data in results.items():
    print(f"\n🎯 {category}:")
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, float):
                print(f"  • {key}: {value:.3f}")
            else:
                print(f"  • {key}: {value}")
    else:
        print(f"  • {data}")

# 3. 保存结果到文件
import json
with open('experiment_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n💾 结果已保存到 experiment_results.json")

# 4. 生成建议和改进方向
print(f"\n🚀 下一步实验建议：")
suggestions = [
    "增加更多数据样本以提高模型准确性",
    "尝试其他机器学习算法（如XGBoost、LightGBM）",
    "收集时间序列数据以分析质量趋势",
    "实施在线学习系统以实时更新模型",
    "添加更多工程特征（如移动平均、趋势指标）",
    "使用深度学习模型处理复杂非线性关系",
    "建立自动化质量预警系统",
    "集成实时数据流处理"
]

for i, suggestion in enumerate(suggestions, 1):
    print(f"  {i}. {suggestion}")

# 5. 创建简化版结果摘要
print(f"\n📈 实验结果摘要：")
print(f"✅ 数据加载: 成功加载 {len(df)} 条记录")
print(f"✅ 质量分析: 合格率 {(df['type'] == '合格').mean():.1%}")
print(f"✅ 异常检测: 发现 {sum(outlier_results.values())} 个异常值")
print(f"✅ 机器学习: 基础模型准确率 {accuracy_original:.1%}")
print(f"✅ 特征工程: 扩展模型准确率 {accuracy_extended:.1%} (提升 {(accuracy_extended - accuracy_original) * 100:.1f}%)")
print(f"✅ 结果导出: 完整报告已保存")

print(f"\n🎉 恭喜！实验已全部完成！")
print(f"📊 您现在可以在Colab中下载 experiment_results.json 文件，")
print(f"🔍 或者继续探索更多数据分析功能！")

# 6. 可选：保存所有图表
print(f"\n💡 提示：要保存图表，可以在每个plt.show()之前添加：")
print(f"   plt.savefig('图表名称.png', dpi=300, bbox_inches='tight')")
print(f"\n   这样可以将图表保存为高质量的PNG文件！")