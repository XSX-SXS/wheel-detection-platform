# 🔧 Colab实验故障排除指南

## 🚨 常见问题快速解决方案

### ❌ 问题1：无法连接到Google Colab

#### 错误现象：
- 页面无法加载
- 显示"无法访问此网站"
- 连接超时

#### 解决方案：
```
🔧 解决步骤：
1️⃣ 检查网络连接
   • 确保WiFi/网络正常
   • 尝试访问其他网站

2️⃣ 使用VPN（如需要）
   • 某些地区可能需要VPN
   • 推荐稳定可靠的VPN服务

3️⃣ 更换浏览器
   • 推荐Chrome、Firefox、Edge
   • 清除浏览器缓存和Cookie

4️⃣ 检查Google服务状态
   • 访问：https://www.google.com/appsstatus
   • 查看Colab服务是否正常
```

---

### ❌ 问题2：运行时断开连接

#### 错误现象：
- 显示"运行时断开连接"
- 代码执行中断
- 变量丢失

#### 解决方案：
```
🔧 解决步骤：
1️⃣ 重新连接运行时
   • 点击"重新连接"按钮
   • 等待连接恢复

2️⃣ 防止自动断开
   • 定期运行简单代码（如：print("keep alive")）
   • 每10-15分钟操作一次

3️⃣ 保存工作进度
   • 定期保存笔记本
   • 导出重要结果到本地

4️⃣ 使用Colab Pro（可选）
   • 更长的运行时间
   • 更好的稳定性
```

---

### ❌ 问题3：数据加载失败

#### 错误现象：
- `FileNotFoundError: data.json not found`
- `HTTPError: 404 Client Error`
- 数据文件无法读取

#### 解决方案：
```python
🔧 解决代码：

# 方法1：手动上传数据文件
from google.colab import files
uploaded = files.upload()

# 方法2：使用本地路径
try:
    df = pd.read_json('data.json')
except FileNotFoundError:
    print("❌ 文件未找到，请上传数据文件")
    uploaded = files.upload()
    df = pd.read_json(list(uploaded.keys())[0])

# 方法3：创建示例数据（演示用）
import pandas as pd
df = pd.DataFrame([
    {"id": "202503110001", "diameter": 650, "average_bolt": 48, "center": 80, "pcd": 280, "type": "合格"},
    {"id": "202503110002", "diameter": 650, "average_bolt": 48, "center": 80, "pcd": 280, "type": "合格"},
    {"id": "202503110003", "diameter": 650, "average_bolt": 48, "center": 80, "pcd": 280, "type": "不合格"}
])
```

---

### ❌ 问题4：依赖包安装失败

#### 错误现象：
- `ERROR: Could not find a version that satisfies the requirement`
- `ERROR: Failed building wheel for package`
- 安装超时

#### 解决方案：
```python
🔧 解决代码：

# 方法1：使用国内镜像源
!pip install pandas numpy matplotlib seaborn plotly scikit-learn -i https://pypi.tuna.tsinghua.edu.cn/simple

# 方法2：分别安装包
!pip install pandas -q
!pip install numpy -q
!pip install matplotlib -q
!pip install seaborn -q
!pip install plotly -q
!pip install scikit-learn -q

# 方法3：升级pip后再安装
!pip install --upgrade pip
!pip install pandas numpy matplotlib seaborn plotly scikit-learn

# 方法4：使用conda（如果可用）
!conda install pandas numpy matplotlib seaborn scikit-learn -y
```

---

### ❌ 问题5：中文显示乱码

#### 错误现象：
- 图表中中文显示为方框
- 中文标签无法显示
- 报错：`findfont: Font family ['SimHei'] not found`

#### 解决方案：
```python
🔧 解决代码：

# 方法1：使用DejaVu Sans字体
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 方法2：安装中文字体
!apt-get install fonts-noto-cjk -y
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC']
plt.rcParams['axes.unicode_minus'] = False

# 方法3：使用英文标签（备用方案）
# 将中文标签替换为英文
df['quality'] = df['type'].map({'合格': 'Qualified', '不合格': 'Unqualified'})
```

---

### ❌ 问题6：内存不足错误

#### 错误现象：
- `MemoryError`
- `RuntimeError: CUDA out of memory`
- 运行时突然崩溃

#### 解决方案：
```python
🔧 解决代码：

# 方法1：减少数据量
def reduce_data_size(df, sample_size=1000):
    """减少数据量以节省内存"""
    if len(df) > sample_size:
        return df.sample(sample_size, random_state=42)
    return df

# 方法2：优化数据类型
def optimize_memory(df):
    """优化数据类型以减少内存使用"""
    for col in df.select_dtypes(include=['int64']).columns:
        df[col] = df[col].astype('int32')
    for col in df.select_dtypes(include=['float64']).columns:
        df[col] = df[col].astype('float32')
    return df

# 方法3：分批处理数据
def process_in_batches(df, batch_size=100):
    """分批处理大数据集"""
    results = []
    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i+batch_size]
        # 处理批次数据
        result = process_batch(batch)
        results.append(result)
    return pd.concat(results)

# 方法4：清理内存
import gc
def clear_memory():
    """清理内存"""
    gc.collect()
    print("内存清理完成")
```

---

### ❌ 问题7：机器学习模型报错

#### 错误现象：
- `ValueError: Input contains NaN, infinity or a value too large`
- `ValueError: could not convert string to float`
- 模型训练失败

#### 解决方案：
```python
🔧 解决代码：

# 方法1：数据预处理
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# 检查并处理缺失值
def preprocess_data(X):
    """数据预处理"""
    # 处理缺失值
    imputer = SimpleImputer(strategy='mean')
    X_clean = imputer.fit_transform(X)
    
    # 标准化数据
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_clean)
    
    return X_scaled

# 方法2：标签编码
def encode_labels(y):
    """标签编码"""
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    return le.fit_transform(y)

# 方法3：处理类别不平衡
def balance_dataset(X, y):
    """平衡数据集"""
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(random_state=42)
    X_balanced, y_balanced = smote.fit_resample(X, y)
    return X_balanced, y_balanced
```

---

### ❌ 问题8：图表显示异常

#### 错误现象：
- 图表不显示
- 图表显示为空白
- 图表样式异常

#### 解决方案：
```python
🔧 解决代码：

# 方法1：强制显示图表
%matplotlib inline
import matplotlib.pyplot as plt

# 方法2：重启matplotlib
import matplotlib
matplotlib.rcdefaults()

# 方法3：检查并修复数据
def validate_plot_data(df, x_col, y_col):
    """验证绘图数据"""
    if x_col not in df.columns or y_col not in df.columns:
        print(f"❌ 列不存在: {x_col}, {y_col}")
        return False
    
    if df[x_col].isnull().all() or df[y_col].isnull().all():
        print("❌ 数据全为NaN")
        return False
    
    return True

# 方法4：简化图表
plt.figure(figsize=(8, 6))
plt.plot([1, 2, 3], [1, 4, 9])  # 简单测试图表
plt.show()
```

---

### ❌ 问题9：文件保存和下载问题

#### 错误现象：
- 文件无法保存
- 下载失败
- 文件损坏

#### 解决方案：
```python
🔧 解决代码：

# 方法1：多种格式保存
import pandas as pd

# JSON格式
df.to_json('results.json', orient='records', force_ascii=False)

# CSV格式
df.to_csv('results.csv', index=False, encoding='utf-8')

# Excel格式
df.to_excel('results.xlsx', index=False)

# 方法2：压缩保存
import zipfile
import os

def save_compressed(df, filename='results.zip'):
    """压缩保存文件"""
    with zipfile.ZipFile(filename, 'w') as zipf:
        # 保存多个格式
        df.to_json('temp.json', orient='records', force_ascii=False)
        df.to_csv('temp.csv', index=False, encoding='utf-8')
        
        zipf.write('temp.json', 'results.json')
        zipf.write('temp.csv', 'results.csv')
        
        # 清理临时文件
        os.remove('temp.json')
        os.remove('temp.csv')
    
    print(f"✅ 文件已压缩保存: {filename}")

# 方法3：分批下载大文件
def download_large_file(filepath, chunk_size=1024*1024):
    """分批下载大文件"""
    from google.colab import files
    
    try:
        files.download(filepath)
        print(f"✅ 文件下载成功: {filepath}")
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        print("建议：")
        print("1. 检查文件大小")
        print("2. 分批处理数据")
        print("3. 使用压缩格式")
```

---

## 🚨 紧急情况处理

### 🔥 完全无法运行时

1. **保存所有代码**
   ```python
   # 导出所有代码到文件
   with open('backup_code.py', 'w') as f:
       f.write("# 备份所有实验代码\n")
       # 添加您的代码
   ```

2. **重启运行时**
   - 菜单：Runtime → Restart runtime
   - 重新运行所有代码

3. **使用备用方案**
   - 本地Python环境
   - 其他云平台（Kaggle、Azure Notebooks）

### 📞 获取帮助

1. **查看错误详情**
   ```python
   import traceback
   try:
       # 您的代码
       pass
   except Exception as e:
       print(f"错误类型: {type(e).__name__}")
       print(f"错误信息: {str(e)}")
       traceback.print_exc()
   ```

2. **记录问题信息**
   - 错误类型和完整信息
   - 出现问题的代码位置
   - 运行环境信息

3. **寻求帮助渠道**
   - 向我咨询具体问题
   - Stack Overflow
   - Google Colab官方文档

---

## ✅ 预防措施

### 🛡️ 实验前准备
1. **备份数据文件**
2. **保存代码副本**
3. **检查网络连接**
4. **了解运行时限制**

### 🔄 实验中监控
1. **定期保存结果**
2. **监控内存使用**
3. **分批处理大数据**
4. **及时备份重要发现**

### 📋 实验后整理
1. **导出所有结果**
2. **整理代码版本**
3. **记录实验参数**
4. **总结关键发现**

记住：遇到问题时不要慌张，按照指南逐步排查，大部分问题都可以解决！🔧✨