# 第三步：加载数据（在Colab的新代码块中运行）

# 方法1：尝试从GitHub加载数据（推荐）
try:
    print("正在尝试从GitHub加载数据...")
    data_url = "https://raw.githubusercontent.com/XSX-SXS/wheel-detection-platform/main/data.json"
    df = pd.read_json(data_url)
    print(f"✅ 从GitHub成功加载数据！共有 {len(df)} 条记录")
    
except Exception as e:
    print(f"❌ 从GitHub加载数据失败: {e}")
    print("正在创建示例数据进行演示...")
    
    # 创建示例数据（基于您的实际数据结构）
    sample_data = [
        {"id": "202503110001", "diameter": 650, "average_bolt": 48, "center": 80, "pcd": 280, "type": "合格"},
        {"id": "202503110002", "diameter": 650, "average_bolt": 48, "center": 80, "pcd": 280, "type": "合格"},
        {"id": "202503110003", "diameter": 650, "average_bolt": 48, "center": 80, "pcd": 280, "type": "不合格"},
        {"id": "202503110004", "diameter": 650, "average_bolt": 48, "center": 80, "pcd": 280, "type": "合格"},
        {"id": "202503110005", "diameter": 650, "average_bolt": 47, "center": 79, "pcd": 279, "type": "不合格"},
        {"id": "202503110006", "diameter": 650, "average_bolt": 48, "center": 80, "pcd": 280, "type": "合格"},
        {"id": "202503110007", "diameter": 651, "average_bolt": 48, "center": 80, "pcd": 280, "type": "合格"},
        {"id": "202503110008", "diameter": 649, "average_bolt": 48, "center": 80, "pcd": 280, "type": "合格"},
        {"id": "202503110009", "diameter": 650, "average_bolt": 49, "center": 80, "pcd": 280, "type": "合格"},
        {"id": "202503110010", "diameter": 650, "average_bolt": 48, "center": 81, "pcd": 281, "type": "不合格"},
    ]
    
    df = pd.DataFrame(sample_data)
    print(f"✅ 示例数据创建完成！共有 {len(df)} 条记录")

# 显示数据基本信息
print("\n📋 数据预览：")
print(df.head())
print(f"\n📊 数据形状: {df.shape}")
print(f"\n🔍 数据类型:")
print(df.dtypes)