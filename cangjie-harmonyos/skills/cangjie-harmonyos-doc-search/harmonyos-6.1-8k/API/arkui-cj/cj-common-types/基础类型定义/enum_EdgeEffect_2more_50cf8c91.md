## enum EdgeEffect

```cangjie
public enum EdgeEffect <: Equatable<EdgeEffect> {
    | Spring
    | Fade
    | None
    | ...
}
```

**功能：** 边缘滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[EdgeEffect](#enum-edgeeffect)>

### Spring

```cangjie
Spring
```

**功能：** 弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松手后回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Fade

```cangjie
Fade
```

**功能：** 阴影效果，滑动到边缘后会有圆弧状的阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 滑动到边缘后无效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(EdgeEffect)

```cangjie
public operator func ==(other: EdgeEffect): Bool
```

**功能：** 判断两个EdgeEffect枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[EdgeEffect](#enum-edgeeffect)|是|-|要比较的另一个EdgeEffect枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(EdgeEffect)

```cangjie
public operator func !=(other: EdgeEffect): Bool
```

**功能：** 判断两个EdgeEffect枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[EdgeEffect](#enum-edgeeffect)|是|-|要比较的另一个EdgeEffect枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum Edge

```cangjie
public enum Edge <: Equatable<Edge> {
    | Top
    | Start
    | Bottom
    | End
    | ...
}
```

**功能：** 滚动到容器边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[Edge](#enum-edge)>

### Top

```cangjie
Top
```

**功能：** 竖直方向上边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Start

```cangjie
Start
```

**功能：** 水平方向起始位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 竖直方向下边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 水平方向末尾位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(Edge)

```cangjie
public operator func ==(other: Edge): Bool
```

**功能：** 判断两个Edge枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Edge](#enum-edge)|是|-|要比较的另一个Edge枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(Edge)

```cangjie
public operator func !=(other: Edge): Bool
```

**功能：** 判断两个Edge枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Edge](#enum-edge)|是|-|要比较的另一个Edge枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|