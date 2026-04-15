## enum SwipeEdgeEffect

```cangjie
public enum SwipeEdgeEffect <: Equatable<SwipeEdgeEffect> {
    | Spring
    | None
    | ...
}
```

**功能：** 滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SwipeEdgeEffect](#enum-swipeedgeeffect)>

### Spring

```cangjie
Spring
```

**功能：** ListItem划动距离超过划出组件大小后可以继续划动，松手后按照弹簧阻尼曲线回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** ListItem划动距离不能超过划出组件大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SwipeEdgeEffect)

```cangjie
public operator func ==(other: SwipeEdgeEffect): Bool
```

**功能：** 判断两个SwipeEdgeEffect枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwipeEdgeEffect](#enum-swipeedgeeffect)|是|-|要比较的另一个SwipeEdgeEffect枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SwipeEdgeEffect)

```cangjie
public operator func !=(other: SwipeEdgeEffect): Bool
```

**功能：** 判断两个SwipeEdgeEffect枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwipeEdgeEffect](#enum-swipeedgeeffect)|是|-|要比较的另一个SwipeEdgeEffect枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|