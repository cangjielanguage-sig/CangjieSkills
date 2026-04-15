## enum AnimatorFill

```cangjie
public enum AnimatorFill <: Equatable<AnimatorFill> {
    | None
    | Forwards
    | Backwards
    | Both
    | ...
}
```

**功能：** 动画执行后的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[AnimatorFill](#enum-animatorfill)>

### None

```cangjie
None
```

**功能：** 在动画执行之前和之后都不会应用任何样式到目标上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Forwards

```cangjie
Forwards
```

**功能：** 在动画结束后，目标将保留动画结束时的状态（在最后一个关键帧中定义）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Backwards

```cangjie
Backwards
```

**功能：** 动画将在[AnimatorOptions](#class-animatoroptions)中的delay期间应用第一个关键帧中定义的值。当[AnimatorOptions](#class-animatoroptions)中的direction为Normal或Alternate时应用from关键帧中的值，当[AnimatorOptions](#class-animatoroptions)中的direction为Reverse或AlternateReverse时应用to关键帧中的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Both

```cangjie
Both
```

**功能：** 动画将遵循Forwards和Backwards的规则，从而在两个方向上扩展动画属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(AnimatorFill)

```cangjie
public operator func !=(other: AnimatorFill): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AnimatorFill](#enum-animatorfill)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

### operator func ==(AnimatorFill)

```cangjie
public operator func ==(other: AnimatorFill): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AnimatorFill](#enum-animatorfill)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|