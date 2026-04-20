## enum SlideEffect

```cangjie
public enum SlideEffect <: Equatable<SlideEffect> {
    | Left
    | Right
    | Top
    | Bottom
    | ...
}
```

**功能：** 页面转场时的滑入滑出效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SlideEffect](#enum-slideeffect)>

### Left

```cangjie
Left
```

**功能：** 入场时表示从左边滑入，出场时表示滑出到左边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 入场时表示从右边滑入，出场时表示滑出到右边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Top

```cangjie
Top
```

**功能：** 入场时表示从上边滑入，出场时表示滑出到上边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 入场时表示从下边滑入，出场时表示滑出到下边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(SlideEffect)

```cangjie
public operator func !=(other: SlideEffect): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SlideEffect](#enum-slideeffect)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

### operator func ==(SlideEffect)

```cangjie
public operator func ==(other: SlideEffect): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SlideEffect](#enum-slideeffect)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|

## type PageTransitionCallback

```cangjie
public type PageTransitionCallback = (RouteType, Float64) -> Unit
```

**功能：** 页面转场事件回调。

**类型：** ([RouteType](#enum-routetype) , Float64) -> Unit

|类型参数|说明|
|:---|:---|
|[RouteType](#enum-routetype)|页面转场类型。|
|Float64|转场进度，从0变化到1。|