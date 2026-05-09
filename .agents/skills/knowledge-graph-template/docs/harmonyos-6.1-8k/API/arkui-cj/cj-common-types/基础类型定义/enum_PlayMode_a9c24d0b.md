## enum PlayMode

```cangjie
public enum PlayMode <: Equatable<PlayMode> {
    | Normal
    | Reverse
    | Alternate
    | AlternateReverse
    | ...
}
```

**功能：** 动画播放方向设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[PlayMode](#enum-playmode)>

### Normal

```cangjie
Normal
```

**功能：** 动画正向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Reverse

```cangjie
Reverse
```

**功能：** 动画反向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Alternate

```cangjie
Alternate
```

**功能：** 动画在奇数次（1, 3, 7...）正向播放，在偶数次（2, 4, 6...）反向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### AlternateReverse

```cangjie
AlternateReverse
```

**功能：** 动画在奇数次（1, 3, 7...）反向播放，在偶数次（2, 4, 6...）正向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(PlayMode)

```cangjie
public operator func ==(other: PlayMode): Bool
```

**功能：** 判断两个PlayMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlayMode](#enum-playmode)|是|-|要比较的另一个PlayMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(PlayMode)

```cangjie
public operator func !=(other: PlayMode): Bool
```

**功能：** 判断两个PlayMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlayMode](#enum-playmode)|是|-|要比较的另一个PlayMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|