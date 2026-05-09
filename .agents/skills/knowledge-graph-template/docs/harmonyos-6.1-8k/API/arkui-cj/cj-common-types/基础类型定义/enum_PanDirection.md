## enum PanDirection

```cangjie
public enum PanDirection <: Equatable<PanDirection> {
    | None
    | Left
    | Right
    | Horizontal
    | Up
    | Down
    | Vertical
    | All
    | Computed(UInt32)
    | ...
}
```

**功能：** 拖动手势方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[PanDirection](#enum-pandirection)>

### None

```cangjie
None
```

**功能：** 所有方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Left

```cangjie
Left
```

**功能：** 向左拖动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 向右拖动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Horizontal

```cangjie
Horizontal
```

**功能：** 水平方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Up

```cangjie
Up
```

**功能：** 向上拖动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Down

```cangjie
Down
```

**功能：** 向下拖动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Vertical

```cangjie
Vertical
```

**功能：** 竖直方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### All

```cangjie
All
```

**功能：** 所有方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Computed(UInt32)

```cangjie
Computed(UInt32)
```

**功能：** 支持逻辑与(&)和逻辑或(|)运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(PanDirection)

```cangjie
public operator func ==(other: PanDirection): Bool
```

**功能：** 判断两个PanDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PanDirection](#enum-pandirection)|是|-|要比较的另一个PanDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(PanDirection)

```cangjie
public operator func !=(other: PanDirection): Bool
```

**功能：** 判断两个PanDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PanDirection](#enum-pandirection)|是|-|要比较的另一个PanDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

### operator func |(PanDirection)

```cangjie
public operator func |(right: PanDirection): PanDirection
```

**功能：** 对PanDirection执行逻辑或(|)运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|right|[PanDirection](#enum-pandirection)|是|-|要进行逻辑或运算的PanDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|[PanDirection](#enum-pandirection)|逻辑或运算的结果。|

### operator func &(PanDirection)

```cangjie
public operator func &(right: PanDirection): PanDirection
```

**功能：** 对PanDirection执行逻辑与(&)运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|right|[PanDirection](#enum-pandirection)|是|-|要进行逻辑与运算的PanDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|[PanDirection](#enum-pandirection)|逻辑与运算的结果。|