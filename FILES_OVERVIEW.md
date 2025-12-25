# 制造业AI智慧检测物联网平台 - 文件功能说明

## 一、项目配置文件

### 1. package.json
- **用途**：项目核心配置文件，定义了项目名称、版本、依赖包、脚本命令等
- **关键内容**：
  - 前端依赖：Next.js 14、React 18、TypeScript、Tailwind CSS
  - 后端依赖：Prisma、Node.js
  - 3D依赖：Three.js、React Three Fiber、React Three Drei
  - 数据可视化：ECharts、ECharts for React
  - 脚本命令：开发、构建、数据库操作等

### 2. next.config.js
- **用途**：Next.js框架配置文件，用于自定义Next.js的行为
- **功能**：可以配置路由、环境变量、构建选项等

### 3. tsconfig.json
- **用途**：TypeScript配置文件，定义TypeScript的编译选项
- **功能**：配置类型检查、模块解析、编译目标等

### 4. tailwind.config.ts
- **用途**：Tailwind CSS配置文件，用于自定义Tailwind的行为
- **功能**：配置主题颜色、字体、间距、插件等

### 5. postcss.config.js
- **用途**：PostCSS配置文件，用于处理CSS的工具链
- **功能**：配置Autoprefixer等PostCSS插件

### 6. .gitignore
- **用途**：Git版本控制忽略文件配置
- **功能**：指定不需要被Git跟踪的文件和目录（如依赖、环境变量、构建产物等）

### 7. _redirects
- **用途**：Next.js重定向配置文件
- **功能**：定义URL重定向规则，用于路由管理

### 8. netlify.toml
- **用途**：Netlify部署配置文件
- **功能**：配置Netlify的构建和部署选项

## 二、前端应用核心文件

### 1. app/目录
- **用途**：Next.js 13+的App Router应用目录结构
- **核心子目录**：
  - `app/layout.tsx`：应用根布局组件
  - `app/page.tsx`：应用首页
  - `app/globals.css`：全局样式文件

### 2. app/page.tsx
- **用途**：应用的首页组件
- **功能**：显示平台的欢迎信息和主要入口

### 3. app/home/page.tsx
- **用途**：平台的主页内容组件
- **功能**：展示平台的核心功能和统计信息

### 4. app/login/page.tsx
- **用途**：登录页面组件
- **功能**：提供用户登录界面和认证功能

### 5. app/monitor/page.tsx
- **用途**：监控页面组件
- **功能**：展示实时监控数据和摄像头画面

### 6. app/digital-twin/page.tsx
- **用途**：数字孪生页面组件
- **功能**：展示3D模型和数字孪生功能

### 7. app/visualize/page.tsx
- **用途**：数据可视化页面组件
- **功能**：展示各类数据图表和统计信息

### 8. app/admin/目录
- **用途**：管理员功能页面集合
- **核心子目录**：
  - `admin/page.tsx`：管理员首页
  - `admin/wheels/page.tsx`：轮毂数据管理
  - `admin/alerts/page.tsx`：告警管理
  - `admin/inspections/page.tsx`：检测记录管理
  - `admin/data-import/page.tsx`：数据导入功能

## 三、后端API文件

### 1. app/api/目录
- **用途**：Next.js API Routes后端API集合
- **核心子目录**：
  - `api/wheels/route.ts`：轮毂数据API
  - `api/imports/route.ts`：数据导入API
  - `api/statistics/route.ts`：统计数据API
  - `api/logs/route.ts`：日志数据API
  - `api/sync/route.ts`：数据同步API

### 2. lib/prisma.ts
- **用途**：Prisma客户端实例配置
- **功能**：创建和导出Prisma客户端实例，用于数据库操作

## 四、数据库相关文件

### 1. prisma/schema.prisma
- **用途**：Prisma数据库模型定义文件
- **功能**：定义数据库表结构、关系和字段类型
- **核心模型**：Wheel（轮毂数据）、Log（日志）等

### 2. scripts/import-data.ts
- **用途**：数据导入脚本
- **功能**：将CSV或JSON数据导入到数据库中

### 3. types/imports.ts
- **用途**：TypeScript类型定义文件
- **功能**：定义数据导入相关的类型接口

## 五、组件文件

### 1. app/components/Charts/目录
- **用途**：图表组件集合
- **核心组件**：
  - `LineChart.tsx`：折线图组件
  - `PieChart.tsx`：饼图组件

### 2. app/components/DataTable/目录
- **用途**：数据表格组件集合
- **核心组件**：
  - `WheelList.tsx`：轮毂数据列表组件
  - `LogList.tsx`：日志数据列表组件

### 3. app/components/Layout/目录
- **用途**：布局组件集合
- **核心组件**：
  - `Header.tsx`：页面头部组件
  - `Footer.tsx`：页面底部组件
  - `Navigation.tsx`：导航菜单组件
  - `Card.tsx`：卡片容器组件

### 4. app/components/ThreeViewer/目录
- **用途**：3D模型查看器组件
- **核心组件**：
  - `ModelViewer.tsx`：3D模型查看器组件

### 5. app/components/Stats/目录
- **用途**：统计信息组件集合
- **核心组件**：
  - `StatsCards.tsx`：统计卡片组件

### 6. app/visualize/components/目录
- **用途**：可视化页面专用组件
- **核心组件**：
  - `DailyChart.tsx`：每日数据图表
  - `QualityChart.tsx`：质量统计图表
  - `SizeDistributionChart.tsx`：尺寸分布图表

## 六、数据文件

### 1. data.json
- **用途**：核心数据集文件
- **功能**：存储轮毂检测的历史数据，用于测试和演示
- **内容**：包含轮毂ID、直径、螺栓孔径、中心距、PCD等检测参数

### 2. defects.csv
- **用途**：缺陷数据CSV文件
- **功能**：存储轮毂缺陷检测数据

### 3. inspections.csv
- **用途**：检测记录CSV文件
- **功能**：存储轮毂检测记录数据

### 4. logs.csv
- **用途**：日志数据CSV文件
- **功能**：存储系统操作日志数据

### 5. parts_spec.csv
- **用途**：零件规格CSV文件
- **功能**：存储轮毂零件的规格参数

### 6. projects.csv
- **用途**：项目数据CSV文件
- **功能**：存储相关项目信息

### 7. cemian.STL
- **用途**：3D模型文件
- **功能**：轮毂的3D模型，用于数字孪生展示

## 七、文档和教程文件

### 1. README.md
- **用途**：项目说明文档
- **内容**：项目简介、快速上手、环境要求、功能说明等

### 2. CHANGELOG.md
- **用途**：版本变更日志
- **内容**：记录项目的版本更新历史和变更内容

### 3. docs/DEPLOY.md
- **用途**：部署说明文档
- **内容**：项目部署的详细步骤和配置说明

### 4. 教学指南.md
- **用途**：平台使用教学指南
- **内容**：平台的使用方法和操作流程

### 5. colab说明/目录
- **用途**：Google Colab使用说明文件集合
- **核心文件**：
  - `colab_usage_guide.md`：Colab使用指南
  - `colab_troubleshooting_guide.md`：Colab故障排除指南
  - `colab_experiment.ipynb`：Colab实验笔记本
  - `详细使用说明书.md`：详细的使用说明

### 6. colab操作步骤/目录
- **用途**：Colab操作步骤脚本集合
- **核心文件**：
  - `step1_environment_setup.py`：环境搭建脚本
  - `step2_import_libraries.py`：库导入脚本
  - `step3_load_data.py`：数据加载脚本
  - `step4_basic_analysis.py`：基础分析脚本
  - `step5_visualization.py`：可视化脚本
  - `step6_advanced_viz.py`：高级可视化脚本
  - `step7_machine_learning.py`：机器学习脚本
  - `step8_ml_visualization.py`：机器学习可视化脚本
  - `step9_anomaly_detection.py`：异常检测脚本
  - `step10_advanced_features.py`：高级功能脚本
  - `step11_final_results.py`：最终结果脚本

## 八、其他辅助文件

### 1. Admin_Index.html
- **用途**：管理员界面HTML文件
- **功能**：管理员界面的静态HTML版本

### 2. Data_Import.html
- **用途**：数据导入界面HTML文件
- **功能**：数据导入功能的静态HTML版本

### 3. Digital_Twin.html
- **用途**：数字孪生界面HTML文件
- **功能**：数字孪生功能的静态HTML版本

### 4. Home_Page.html
- **用途**：首页HTML文件
- **功能**：平台首页的静态HTML版本

### 5. Monitor.html
- **用途**：监控界面HTML文件
- **功能**：监控功能的静态HTML版本

### 6. Visualize.html
- **用途**：可视化界面HTML文件
- **功能**：数据可视化功能的静态HTML版本

### 7. paper.pdf
- **用途**：相关技术论文
- **内容**：平台相关的技术研究或论文

### 8. js/目录
- **用途**：JavaScript脚本文件集合
- **核心文件**：
  - `echarts.js`/`echarts.min.js`：ECharts图表库
  - `jquery-2.1.1.min.js`：jQuery库
  - `three.core.js`：Three.js核心库
  - `digitaltwin.js`：数字孪生功能脚本
  - `visual.js`：可视化功能脚本

### 9. css/目录
- **用途**：CSS样式文件集合
- **核心文件**：
  - `admin.css`：管理员界面样式
  - `common.css`：通用样式
  - `digitaltwin.css`：数字孪生界面样式
  - `monitor.css`：监控界面样式
  - `visualize.css`：可视化界面样式

### 10. push-to-github.sh
- **用途**：GitHub推送脚本
- **功能**：自动化将代码推送到GitHub的脚本

## 九、核心功能模块说明

### 1. 数据管理模块
- **文件位置**：`app/admin/wheels/`、`app/api/wheels/`
- **功能**：管理轮毂检测数据，包括增删改查、导入导出等

### 2. 实时监控模块
- **文件位置**：`app/monitor/`、`app/components/Monitor/`
- **功能**：实时监控生产过程和检测数据

### 3. 数据可视化模块
- **文件位置**：`app/visualize/`、`app/components/Charts/`
- **功能**：通过图表展示检测数据的统计信息和趋势

### 4. 数字孪生模块
- **文件位置**：`app/digital-twin/`、`app/components/ThreeViewer/`
- **功能**：通过3D模型展示轮毂的数字孪生

### 5. 质量检测模块
- **文件位置**：`app/admin/inspections/`、`app/api/statistics/`
- **功能**：管理质量检测记录和统计质量数据

### 6. 告警管理模块
- **文件位置**：`app/admin/alerts/`
- **功能**：管理系统告警和通知

### 7. 数据导入模块
- **文件位置**：`app/admin/data-import/`、`app/api/imports/`
- **功能**：导入外部数据到系统中

## 总结

这个制造业AI智慧检测物联网平台是一个基于Next.js的全栈应用，整合了前端、后端、数据库、3D数字孪生、数据可视化和AI检测等多种技术。各个文件和目录分工明确，共同构成了一个功能完整的工业物联网平台。