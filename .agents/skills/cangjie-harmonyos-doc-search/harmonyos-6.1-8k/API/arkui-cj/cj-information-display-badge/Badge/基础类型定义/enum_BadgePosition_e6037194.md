### enum BadgePosition

```cangjie
public enum BadgePosition <: Equatable<BadgePosition> {
    | RightTop
    | Right
    | Left
    | ...
}
```

**功能：** 定义badge位置属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[BadgePosition](#enum-badgeposition)>

#### Left

```cangjie
Left
```

**功能：** badge显示在父组件的左侧纵向居中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### Right

```cangjie
Right
```

**功能：** badge显示在父组件的右侧纵向居中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### RightTop

```cangjie
RightTop
```

**功能：** badge显示在父组件的右上角。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(BadgePosition)

```cangjie
public operator func !=(other: BadgePosition): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BadgePosition](#enum-badgeposition)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(BadgePosition)

```cangjie
public operator func ==(other: BadgePosition): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BadgePosition](#enum-badgeposition)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|