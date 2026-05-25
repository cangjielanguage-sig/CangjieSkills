## enum FlexDirection

```cangjie
public enum FlexDirection <: Equatable<FlexDirection> {
    | Row
    | Column
    | RowReverse
    | ColumnReverse
    | ...
}
```

**功能：** Flex布局容器方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[FlexDirection](#enum-flexdirection)>

### Row

```cangjie
Row
```

**功能：** 主轴与行方向一致作为布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Column

```cangjie
Column
```

**功能：** 主轴与列方向一致作为布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### RowReverse

```cangjie
RowReverse
```

**功能：** 与Row方向相反方向进行布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ColumnReverse

```cangjie
ColumnReverse
```

**功能：** 与Column相反方向进行布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(FlexDirection)

```cangjie
public operator func ==(other: FlexDirection): Bool
```

**功能：** 判断两个FlexDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FlexDirection](#enum-flexdirection)|是|-|要比较的另一个FlexDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(FlexDirection)

```cangjie
public operator func !=(other: FlexDirection): Bool
```

**功能：** 判断两个FlexDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FlexDirection](#enum-flexdirection)|是|-|要比较的另一个FlexDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|