## enum AnimatorDirection

```cangjie
public enum AnimatorDirection <: Equatable<AnimatorDirection> {
    | Normal
    | Reverse
    | Alternate
    | AlternateReverse
    | ...
}
```

**功能：** 动画播放模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[AnimatorDirection](#enum-animatordirection)>

### Normal

```cangjie
Normal
```

**功能：** 动画正向循环播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Reverse

```cangjie
Reverse
```

**功能：** 动画反向循环播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Alternate

```cangjie
Alternate
```

**功能：** 动画交替循环播放，奇数次正向播放，偶数次反向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### AlternateReverse

```cangjie
AlternateReverse
```

**功能：** 动画反向交替循环播放，奇数次反向播放，偶数次正向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(AnimatorDirection)

```cangjie
public operator func !=(other: AnimatorDirection): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AnimatorDirection](#enum-animatordirection)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

### operator func ==(AnimatorDirection)

```cangjie
public operator func ==(other: AnimatorDirection): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AnimatorDirection](#enum-animatordirection)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|