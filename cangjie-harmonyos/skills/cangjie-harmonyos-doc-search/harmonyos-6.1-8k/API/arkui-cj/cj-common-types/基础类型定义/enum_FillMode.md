## enum FillMode

```cangjie
public enum FillMode <: Equatable<FillMode> {
    | None
    | Forwards
    | Backwards
    | Both
    | ...
}
```

**功能：** 当前播放方向下，动画开始前和结束后的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[FillMode](#enum-fillmode)>

### None

```cangjie
None
```

**功能：** 动画未执行时不会将任何样式应用于目标，动画播放完成之后恢复初始默认状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Forwards

```cangjie
Forwards
```

**功能：** 目标将保留动画执行期间最后一个关键帧的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Backwards

```cangjie
Backwards
```

**功能：** 动画将在应用于目标时立即应用第一个关键帧中定义的值，并在delay期间保留此值。第一个关键帧取决于playMode，playMode为Normal或Alternate时为from的状态，playMode为Reverse或AlternateReverse时为to的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Both

```cangjie
Both
```

**功能：** 动画将遵循Forwards和Backwards的规则，从而在两个方向上扩展动画属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(FillMode)

```cangjie
public operator func ==(other: FillMode): Bool
```

**功能：** 判断两个FillMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FillMode](#enum-fillmode)|是|-|要比较的另一个FillMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(FillMode)

```cangjie
public operator func !=(other: FillMode): Bool
```

**功能：** 判断两个FillMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FillMode](#enum-fillmode)|是|-|要比较的另一个FillMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|