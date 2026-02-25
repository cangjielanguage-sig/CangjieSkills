# Cangjie Assistant - Query & Build Template

当用户询问关于仓颉(HarmonyOS Next)开发的问题时，请按照以下模板执行：

---

## 📋 Phase 0: 需求技术化分析 (L0)

### 用户原始需求
> $USER_REQUEST

### 技术需求分析

| 分析维度 | 内容 |
|---------|------|
| **界面分析** | $UI_ANALYSIS |
| **数据分析** | $DATA_ANALYSIS |
| **交互分析** | $INTERACTION_ANALYSIS |
| **问题类型** | $PROBLEM_TYPE |

### 技术关键词细化

| 组件/功能 | 导包关键词 | 初始化关键词 | 使用/事件关键词 |
|----------|-----------|-------------|-----------------|
| $COMPONENT_1 | $IMPORT_1 | $INIT_1 | $USAGE_1 |
| $COMPONENT_2 | $IMPORT_2 | $INIT_2 | $USAGE_2 |
| $COMPONENT_3 | $IMPORT_3 | $INIT_3 | $USAGE_3 |

---

## 🔍 Phase 1: RAG 查询 (L1)

### 查询计划

```bash
# 进入 workflow 目录
cd cangjie-dev-workflow

# 按组件分组查询
python ask_cangjie.py "$IMPORT_1"
python ask_cangjie.py "$INIT_1"
python ask_cangjie.py "$USAGE_1"

# ... 其他组件查询
```

### 查询结果

#### 查询1: $QUERY_1
```
$RESULT_1
```
**状态**: $STATUS_1 (✅ / ⚠️ / ❌)

#### 查询2: $QUERY_2
```
$RESULT_2
```
**状态**: $STATUS_2 (✅ / ⚠️ / ❌)

### 评估决策

- [ ] 获得足够的核心组件API → **开始编码**
- [ ] 结果不相关/不完整 → **进入 Phase 3**

---

## 🏠 Phase 2: 本地文档搜索 (L3)

### 搜索策略

**问题类型判断**: $PROBLEM_TYPE

**搜索路径**: $SEARCH_PATH

### 搜索命令

```powershell
# PowerShell 搜索
$SEARCH_COMMAND
```

### 搜索结果

**找到的文档**: $FOUND_DOCS

**关键信息**:
- $KEY_INFO_1
- $KEY_INFO_2
- $KEY_INFO_3

### 评估决策

- [ ] 在本地文档找到相关信息 → **基于文档编码**
- [ ] 本地文档无相关信息 → **告知"该功能可能不支持或文档未包含"**

---

## 💻 编码实现

### 代码结构

```cangjie
// 文件: $FILENAME
// 说明: $DESCRIPTION

$CODE_IMPLEMENTATION
```

### 关键技术点

1. $POINT_1
2. $POINT_2
3. $POINT_3

---

## 🏗️ 构建验证

### 构建命令

```powershell
.\build.ps1
```

### 构建结果

$BUILD_RESULT

**状态**: $BUILD_STATUS (✅ BUILD SUCCESSFUL / ❌ BUILD FAILED)

### 错误处理 (如失败)

**错误信息**: $ERROR_MESSAGE

**错误类型**: $ERROR_TYPE

**解决方案**: $SOLUTION

---

## 📝 总结

本次开发重难点记录（用于 Evolution.md）:

### 1. $ISSUE_TITLE_1
**问题描述**: $DESCRIPTION_1
**解决方案**: $SOLUTION_1
**正确语法**: `$CORRECT_CODE_1`

### 2. $ISSUE_TITLE_2
**问题描述**: $DESCRIPTION_2
**解决方案**: $SOLUTION_2
**正确语法**: `$CORRECT_CODE_2`
