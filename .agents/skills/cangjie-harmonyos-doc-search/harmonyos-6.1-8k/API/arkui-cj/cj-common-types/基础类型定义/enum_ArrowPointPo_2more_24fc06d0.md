## enum ArrowPointPosition

```cangjie
public enum ArrowPointPosition <: Equatable<ArrowPointPosition> {
    | Start
    | Center
    | End
    | ...
}
```

**功能：** 箭头指向位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ArrowPointPosition](#enum-arrowpointposition)>

### Start

```cangjie
Start
```

**功能：** 水平方向：位于父组件最左侧，垂直方向：位于父组件最上侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 位于父组件居中位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 水平方向：位于父组件最右侧，垂直方向：位于父组件最下侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ArrowPointPosition)

```cangjie
public operator func ==(other: ArrowPointPosition): Bool
```

**功能：** 判断两个ArrowPointPosition枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ArrowPointPosition](#enum-arrowpointposition)|是|-|要比较的另一个ArrowPointPosition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ArrowPointPosition)

```cangjie
public operator func !=(other: ArrowPointPosition): Bool
```

**功能：** 判断两个ArrowPointPosition枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ArrowPointPosition](#enum-arrowpointposition)|是|-|要比较的另一个ArrowPointPosition枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum TitleHeight

```cangjie
public enum TitleHeight <: Equatable<TitleHeight> {
    | MainOnly
    | MainWithSub
    | ...
}
```

**功能：** 设置标题栏高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TitleHeight](#enum-titleheight)>

### MainOnly

```cangjie
MainOnly
```

**功能：** 只有主标题时标题栏的推荐高度（56vp）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### MainWithSub

```cangjie
MainWithSub
```

**功能：** 同时有主标题和副标题时标题栏的推荐高度（82vp）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TitleHeight)

```cangjie
public operator func ==(other: TitleHeight): Bool
```

**功能：** 判断两个TitleHeight枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TitleHeight](#enum-titleheight)|是|-|要比较的另一个TitleHeight枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TitleHeight)

```cangjie
public operator func !=(other: TitleHeight): Bool
```

**功能：** 判断两个TitleHeight枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TitleHeight](#enum-titleheight)|是|-|要比较的另一个TitleHeight枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|