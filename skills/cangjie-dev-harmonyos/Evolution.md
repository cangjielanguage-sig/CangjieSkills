# Evolution - 项目重难点记录

## 项目: MyApplication6
### 初始日期: 2025-02-24

## 重难点记录

### 2. Entry/Component/State 未声明
**日期**: 02-24
**现象**: `error: undeclared identifier 'Entry'`
**原因**:
1. 缺少 `ohos.arkui.state_macro_manage` 包的导入
2. 使用了 ArrayList 导致编译提前失败
**解决方案**:
1. 添加正确的导入语句
2. 按照标准格式导入
**正确语法**:
```cangjie
import ohos.arkui.state_macro_manage.Entry
import ohos.arkui.state_macro_manage.Component
import ohos.arkui.state_macro_manage.State

// 或者使用通配符
import ohos.arkui.state_macro_manage.*
```

### 3. Array 字面量初始化语法
**日期**: 02-24
**现象**: Array 初始化语法报错
**原因**: 不是标准的字面量格式
**解决方案**: 使用方括号 `[]` 包围元素
**正确语法**:
```cangjie
// 使用方括号字面量
var stockData: Array<StockData> = [
    StockData("01-15", 100.0, 0.0),
    StockData("01-16", 102.5, 2.5)
]

// 或者使用构造函数
let a = Array<Int64>(3, repeat: 0)
```

**参考文档**:
- Array 类型: `./scripts/hm-docs/syntax/source_zh_cn/basic_data_type/array.md`
- State 导入: `./scripts/hm-docs/ui-dev/arkui-cj/cj-animation-smoothing.md`

### 4. UI组件中不能使用普通for循环
**日期**: 02-24
**现象**: `error: does not meet UI component` 在 `for (datum in this.stockData)` 处
**原因**: 在 ArkUI 的 `build` 函数中，不能使用普通的 `for` 循环来生成 UI 组件。必须使用 `ForEach` UI 组件
**解决方案**: 使用 `ForEach` 组件替代 for 循环
**正确语法**:
```cangjie
// 错误 - 普通for循环不能在UI中使用
Row {
    for (datum in this.stockData) {
        Text(datum.date)
    }
}

// 正确 - 使用ForEach组件
Row {
    ForEach(this.stockData, itemGeneratorFunc: { datum: StockData, _: Int64 =>
        Text(datum.date)
    })
}
```

**ForEach 语法**:
- 参数1: 要遍历的数据源（Array）
- `itemGeneratorFunc`: lambda 函数，接收 `item`（元素）和 `index`（索引）两个参数
- 不需要 import，属于 `kit.ArkUI.*`

**参考文档**:
- ForEach: `./scripts/hm-docs/ui-dev/arkui-cj/cj-layout-development-create-list.md`

### 5. Int64 转 Float64 方法名错误
**日期**: 02-24
**现象**: `error: undeclared identifier 'toFloat64'`
**原因**: Int64 类型没有 `toFloat64()` 方法，应该使用 `toFloat()`
**解决方案**: 使用 `toFloat()` 代替 `toFloat64()`
**正确语法**:
```cangjie
// 错误
let x: Float64 = i.toFloat64() * xStep

// 正确
let x: Float64 = i.toFloat * xStep
let xStep: Float64 = width / (data.size - 1).toFloat
```

### 6. flex 属性不存在
**日期**: 02-24
**现象**: `error: 'flex' is not a member of class 'Column'`
**原因**: ArkUI 中没有 `.flex()` 方法，应该使用 `.layoutWeight()`
**解决方案**: 使用 `.layoutWeight()` 代替 `.flex()`
**正确语法**:
```cangjie
// 错误
Column().flex(1)

// 正确
Column().layoutWeight(1)
```

**参考文档**:
- layoutWeight: `./scripts/hm-docs/ui-dev/arkui-cj/cj-layout-development-linear.md`

### 7. Float64 与 Int64 比较类型不匹配
**日期**: 02-24
**现象**: `error: invalid binary operator '>=' on type 'Float64' and 'Int64'`
**原因**: 仓颉中 Float64 和 Int64 不能直接比较，需要类型转换
**解决方案**: 使用浮点数字面量进行比较
**正确语法**:
```cangjie
// 错误
if (datum.change >= 0) { ... }

// 正确
if (datum.change >= 0.0) { ... }
```

### 8. Color.LightGray 不存在
**日期**: 02-24
**现象**: `error: 'LightGray' is not a member of class 'Color'`
**原因**: Color 类型没有 LightGray 属性
**解决方案**: 使用十六进制颜色值替代
**正确语法**:
```cangjie
// 错误
.backgroundColor(Color.LightGray)

// 正确 - 使用十六进制颜色
.backgroundColor(0xF5F5F5)
```

### 9. Color.Gray200 不存在
**日期**: 02-24
**现象**: `error: 'Gray200' is not a member of class 'Color'`
**原因**: Color 类型不支持 Material Design 的颜色命名（如 Gray200）
**解决方案**: 使用十六进制颜色值替代（Gray200 ≈ 0xEEEEEE）
**正确语法**:
```cangjie
// 错误
.backgroundColor(Color.Gray200)

// 正确 - 使用十六进制颜色
.backgroundColor(0xEEEEEE)
```

### 10. Float64 与 Int64 乘法类型不匹配
**日期**: 02-24
**现象**: `error: invalid binary operator '*' on type 'Float64' and 'Int64'`
**原因**: 仓颉中 Float64 和 Int64 不能直接进行算术运算
**解决方案**: 使用浮点数字面量进行计算
**正确语法**:
```cangjie
// 错误
let step: Float64 = (maxPrice - minPrice) / 4.0
return (minPrice + step * 3).toString()

// 正确
let step: Float64 = (maxPrice - minPrice) / 4.0
return (minPrice + step * 3.0).toString()
```

### 11. divider() 方法缺少参数
**日期**: 02-24
**现象**: `error: missing argument for parameter list '(Enum-Option<Class-ListDividerOptions>)'`
**原因**: List 的 divider() 方法需要提供 ListDividerOptions 参数，不能无参调用
**解决方案**: 移除 divider() 调用或提供正确参数
**正确语法**:
```cangjie
// 错误
List() { ... }.divider()

// 正确 - 移除或提供参数
List() { ... }
// 或
List() { ... }.divider(strokeWidth: 1, color: 0xFFE0E0E0)
```

### 12. Path 折线图不可见（布局问题）
**日期**: 02-24
**现象**: Path 组件虽然有 `.layoutWeight(1)` 但折线图不可见
**原因**: 父组件 Row 设置了固定高度，导致 Path 使用 `.layoutWeight(1)` 时无法获得实际渲染高度
**解决方案**: 为 Path 设置具体的高度，或重新设计布局结构使用固定高度
**正确语法**:
```cangjie
// 错误 - layoutWeight 在固定高度的父组件中无效
Row {
    Column { ... }  // 固定高度 300
}
Path()
    .width(100.percent)
    .layoutWeight(1)  // 父组件固定高度，无法生效

// 正确 - 设置具体高度
Path()
    .width(100.percent)
    .height(220.px)
    .stroke(Color.Red)
    .strokeWidth(2)
```

---

## 项目: MyApplication8 (计算器应用)
### 初始日期: 2025-02-25

## 重难点记录

### 13. .onClick 事件语法格式错误
**日期**: 02-25
**现象**: `}) does not meet UI component` 在 Button 的链式调用中
**原因**: ArkUI 宏处理器要求 `.onClick` 必须使用多行格式，不能使用单行闭包
**解决方案**: 改为多行格式，使用类型推导而非显式类型注解
**正确语法**:
```cangjie
// 错误 - 单行格式 + 显式类型注解
Button("AC")
    .width(70.vp)
    .height(70.vp)
    ..onClick({ evt: ClickEvent => this.onButtonClicked("AC") })

// 正确 - 多行格式 + 类型推导
Button("AC")
    .width(70.vp)
    .height(70.vp)
    .onClick ({
        evt => this.onButtonClicked("AC")
    })
```

**关键点**:
1. 必须使用 `.onClick` 而不是 `..onClick`
2. 闭包参数使用类型推导 `evt =>` 而不是 `evt: ClickEvent =>`
3. 必须写成多行格式，单行会触发宏处理错误

### 14. 类型转换方法不存在
**日期**: 02-25
**现象**: `error: undeclared identifier 'toUInt32'`, `error: undeclared identifier 'toInt64'`
**原因**: 仓颉语言中类型转换使用 `T(e)` 语法，而不是 `e.toT()` 方法调用
**解决方案**: 使用类型构造函数进行转换
**正确语法**:
```cangjie
// 错误
let charValue = ch.toUInt32()
let intPart = absValue.toInt64()

// 正确
let charValue = UInt32(ch)
let intPart = Int64(absValue)
```

**支持的数值类型转换**:
- `Int64(e)`, `Int32(e)`, `Int16(e)`, `Int8(e)`
- `UInt64(e)`, `UInt32(e)`, `UInt16(e)`, `UInt8(e)`
- `Float64(e)`, `Float32(e)`, `Float16(e)`

**Rune 转换**:
```cangjie
let x: Rune = 'a'
let r1 = UInt32(x)  // Rune 到 UInt32
let r2 = Rune(65)   // Int64 到 Rune
```

### 15. String 下标返回 Byte 类型
**日期**: 02-25
**现象**: `error: invalid binary operator '==' on type 'UInt8' and 'Rune'`
**原因**: `String[Int64]` 下标访问返回 `UInt8` 类型（字节），不能直接与 `Rune` 类型字面量比较
**解决方案**: 使用 ASCII 码值或 String 方法比较
**正确语法**:
```cangjie
// 错误 - 类型不匹配
if (s[0] == r'-') { ... }
if (ch == r'.') { ... }

// 正确方案1 - 使用 ASCII 码值
if (s[0] == 45u8) { ... }  // '-' 的 ASCII 码是 45
if (ch == 46u8) { ... }     // '.' 的 ASCII 码是 46

// 正确方案2 - 使用 String 方法
if (s.startsWith("-")) { ... }
```

**常用 ASCII 码值**:
- `'-'` = 45u8
- `'.'` = 46u8
- `'0'` ~ `'9'` = 48u8 ~ 57u8

### 16. String.isEmpty 不是属性
**日期**: 02-25
**现象**: `error: expected 'Bool', found '() -> Bool'`
**原因**: String 类型没有 `isEmpty` 属性，是方法调用但通常用 `.size == 0` 代替
**解决方案**: 使用 `.size` 属性判断
**正确语法**:
```cangjie
// 错误
if (this.calcOperator.isEmpty) { ... }

// 正确
if (this.calcOperator.size == 0) { ... }
```

### 17. .padding 不支持对象语法
**日期**: 02-25
**现象**: `error: expected type name after ':', found literal '10'`
**原因**: ArkUI 的 `.padding()` 方法不支持 `{top: 10}` 这种对象语法
**解决方案**: 使用简单的 `.padding(20)` 或使用布局组合来实现不同的边距
**正确语法**:
```cangjie
// 错误 - 对象语法不支持
Text("Hello")
    .padding({top: 10, left: 20})

// 正确 - 使用统一边距
Text("Hello")
    .padding(20)

// 正确 - 使用外层容器实现不同边距
Row() {
    Column() {
        Text("历史")
        Text("结果")
    }
    .padding(20)
}
.justifyContent(FlexAlign.Center)
```

### 18. .height(100.percent) 导致子元素占满全部空间
**日期**: 02-25
**现象**: 显示区设置 `.height(100.percent)` 后，按钮区无法显示
**原因**: 子元素使用固定百分比高度会占据外层容器的全部空间，无法与兄弟元素共存
**解决方案**: 使用 `.layoutWeight()` 替代 `.height()` 进行灵活布局比例分配
**正确语法**:
```cangjie
// 错误 - 子元素使用 height(100.percent) 会占满全屏
Column() {
    Text("显示")
        .height(100.percent)  // 占满全部空间
    Column() { ... }         // 按钮区无法显示
}

// 正确 - 使用 layoutWeight 分配比例
Column() {
    Text("显示")
        .layoutWeight(2)     // 占约 28% (2/7)
    Column() { ... }
        .layoutWeight(5)     // 占约 71% (5/7)
}
```

**layoutWeight 说明**:
- 在 flex 布局（Column/Row）中分配剩余空间
- 数值越大，分配的空间越多
- 所有子元素 layoutWeight 之和决定各自占比

---

## 项目: MyApplication12 (聊天界面应用)
### 初始日期: 2026-02-27

## 重难点记录

### 19. @Component 的 build 方法只能编写 UI 组件语法
**日期**: 02-27
**现象**: `error: Only UI component syntax can be written in build method`
**原因**: ArkUI 的 `@Component` 宏要求 `build` 方法只能编写 UI 组件语法，不能包含 let 变量声明等
**解决方案**: 为不同场景创建独立的组件，或在外层计算后传入
**正确语法**:
```cangjie
// 错误 - build 中不能声明 let
@Component
class MessageBubble {
    func build() {
        let color = if ...  // 错误
        Text(...).backgroundColor(color)
    }
}

// 正确 - 创建两个组件
@Component
class MyMessageBubble {
    func build() {
        Text(...).backgroundColor(0x0A59F7)
    }
}
```

### 20. 不支持三元运算符
**日期**: 02-27
**现象**: `error: expected operator or end of expression, found ':'`
**原因**: 仓颉语言不支持 `condition ? v1 : v2` 三元运算符
**解决方案**: 使用 `if` 表达式或创建独立组件
**正确语法**:
```cangjie
// 正确 - 使用 if 表达式
.backgroundColor(if (message.isMine) { 0x0A59F7 } else { 0xFFFFFF })

// 或在 ForEach 中使用条件渲染
ListItem() {
    if (message.isMine) {
        MyMessageBubble(message: message)
    } else {
        OtherMessageBubble(message: message)
    }
}
```

### 21. Text 组件没有 maxWidth 方法
**日期**: 02-27
**现象**: `error: 'maxWidth' is not a member of class 'Text'`
**原因**: Text 组件不支持 `.maxWidth()` 方法
**解决方案**: 移除 maxWidth，让文本自然显示

### 22. 使用 spawn + sleep 实现延迟操作
**日期**: 02-27
**现象**: `error: undeclared identifier 'Timer'`
**原因**: 仓颉语言没有 JS 风格的 Timer API
**解决方案**: 使用 `spawn` 创建新线程 + `sleep()` 实现延迟
**正确语法**:
```cangjie
spawn {
    sleep(800 * Duration.millisecond)
    // 延迟后的操作
}
```

---## 开发总结
