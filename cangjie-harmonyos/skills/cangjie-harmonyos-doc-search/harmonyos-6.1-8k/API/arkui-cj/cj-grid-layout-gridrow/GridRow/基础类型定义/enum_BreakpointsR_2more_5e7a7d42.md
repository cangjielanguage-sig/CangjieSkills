### enum BreakpointsReference

```cangjie
public enum BreakpointsReference <: Equatable<BreakpointsReference> {
    | WindowSize
    | ComponentSize
    | ...
}
```

**功能：** 设置以窗口为参照或以容器为参照。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：** Equatable\<[BreakpointsReference](#enum-breakpointsreference)>

#### ComponentSize

```cangjie
ComponentSize
```

**功能：** 以容器为参照。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### WindowSize

```cangjie
WindowSize
```

**功能：** 以窗口为参照。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(BreakpointsReference)

```cangjie
public operator func !=(other: BreakpointsReference): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BreakpointsReference](#enum-breakpointsreference)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(BreakpointsReference)

```cangjie
public operator func ==(other: BreakpointsReference): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BreakpointsReference](#enum-breakpointsreference)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|

### enum GridRowDirection

```cangjie
public enum GridRowDirection <: Equatable<GridRowDirection> {
    | Row
    | RowReverse
    | ...
}
```

**功能：** 栅格元素按照行或列方向排列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：** Equatable\<[GridRowDirection](#enum-gridrowdirection)>

#### Row

```cangjie
Row
```

**功能：** 主轴与行方向一致作为布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### RowReverse

```cangjie
RowReverse
```

**功能：** 与Row方向相反方向进行布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(GridRowDirection)

```cangjie
public operator func !=(other: GridRowDirection): Bool
```

**功能：** 比较两个枚举值是否不相等

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GridRowDirection](#enum-gridrowdirection)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(GridRowDirection)

```cangjie
public operator func ==(other: GridRowDirection): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GridRowDirection](#enum-gridrowdirection)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|