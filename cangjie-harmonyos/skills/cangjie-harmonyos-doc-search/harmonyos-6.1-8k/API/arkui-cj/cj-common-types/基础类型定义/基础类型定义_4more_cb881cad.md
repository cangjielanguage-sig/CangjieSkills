# 基础类型定义

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

此页面记录UI框架使用的公共类型定义。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## interface CollectionEx\<T>

```cangjie
public interface CollectionEx<T> {
    prop size: Int64
    operator func [](idx: Int64, value!: T): Unit
    operator func [](idx: Int64): T
}
```

**功能：** 集合扩展接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### extend\<T> Array\<T> <: CollectionEx\<T>

```cangjie
extend<T> Array<T> <: CollectionEx<T> {}
```

**功能：** 扩展泛型Array为CollectionEx子类型。

### extend\<T> ArrayList\<T> <: CollectionEx\<T>

```cangjie
extend<T> ArrayList<T> <: CollectionEx<T> {}
```

**功能：** 扩展泛型ArrayList为CollectionEx子类型。

### prop size

```cangjie
prop size: Int64
```

**功能：** 集合大小。

**类型：** Int64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func [](Int64, T)

```cangjie
operator func [](idx: Int64, value!: T): Unit
```

**功能：** 设置指定索引位置的元素值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|idx|Int64|是|-|元素索引。|
|value|T|是|-|**命名参数。** 元素值。|

### operator func [](Int64)

```cangjie
operator func [](idx: Int64): T
```

**功能：** 获取指定索引位置的元素值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|idx|Int64|是|-|元素索引。|

**返回值：**

|类型|说明|
|:----|:----|
|T|指定索引位置的元素值。|

## interface Length

```cangjie
public interface Length {
    prop value: Float64
    prop unitType: LengthUnit
}
```

**功能：** Float64、Int64、AppResource 均实现了 Length 接口类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop value

```cangjie

prop value: Float64
```

**功能：** 长度属性的值。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop unitType

```cangjie
prop unitType: LengthUnit
```

**功能：** 长度属性的单位。

**类型：** [LengthUnit](#enum-lengthunit)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22