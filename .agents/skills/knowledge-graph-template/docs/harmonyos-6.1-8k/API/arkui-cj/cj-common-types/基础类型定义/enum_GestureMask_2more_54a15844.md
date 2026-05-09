## enum GestureMask

```cangjie
public enum GestureMask <: Equatable<GestureMask> {
    | Normal
    | IgnoreInternal
    | ...
}
```

**功能：** 手势掩码。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[GestureMask](#enum-gesturemask)>

### Normal

```cangjie
Normal
```

**功能：** 不屏蔽子组件的手势，按照默认手势识别顺序进行识别。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### IgnoreInternal

```cangjie
IgnoreInternal
```

**功能：** 屏蔽子组件的手势，包括子组件上系统内置的手势，如子组件为List组件时，内置的滑动手势同样会被屏蔽。若父子组件区域存在部分重叠，则只会屏蔽父子组件重叠的部分。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(GestureMask)

```cangjie
public operator func ==(other: GestureMask): Bool
```

**功能：** 判断两个GestureMask枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GestureMask](#enum-gesturemask)|是|-|要比较的另一个GestureMask枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(GestureMask)

```cangjie
public operator func !=(other: GestureMask): Bool
```

**功能：** 判断两个GestureMask枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GestureMask](#enum-gesturemask)|是|-|要比较的另一个GestureMask枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum SwipeDirection

```cangjie
public enum SwipeDirection <: Equatable<SwipeDirection> {
    | Horizontal
    | Vertical
    | All
    | ...
}
```

**功能：** 触发滑动手势的滑动方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SwipeDirection](#enum-swipedirection)>

### Horizontal

```cangjie
Horizontal
```

**功能：** 水平方向，手指滑动方向与x轴夹角小于45度时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Vertical

```cangjie
Vertical
```

**功能：** 竖直方向，手指滑动方向与y轴夹角小于45度时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### All

```cangjie
All
```

**功能：** 所有方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SwipeDirection)

```cangjie
public operator func ==(other: SwipeDirection): Bool
```

**功能：** 判断两个SwipeDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwipeDirection](#enum-swipedirection)|是|-|要比较的另一个SwipeDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SwipeDirection)

```cangjie
public operator func !=(other: SwipeDirection): Bool
```

**功能：** 判断两个SwipeDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwipeDirection](#enum-swipedirection)|是|-|要比较的另一个SwipeDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|