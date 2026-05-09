## enum ItemState

```cangjie
public enum ItemState <: Equatable<ItemState> {
    | Normal
    | Disabled
    | Waiting
    | Skip
    | ...
}
```

**功能：** 项目状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ItemState](#enum-itemstate)>

### Normal

```cangjie
Normal
```

**功能：** 正常状态，右侧文本按钮正常显示，可点击进入下一个StepperItem。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Disabled

```cangjie
Disabled
```

**功能：** 不可用状态，右侧文本按钮灰度显示，不可点击进入下一个StepperItem。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Waiting

```cangjie
Waiting
```

**功能：** 等待状态，右侧文本按钮不显示，显示等待进度条，不可点击进入下一个StepperItem。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Skip

```cangjie
Skip
```

**功能：** 跳过状态，右侧文本按钮默认显示"跳过"，此时可在Stepper的onSkip回调中自定义相关逻辑。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ItemState)

```cangjie
public operator func ==(other: ItemState): Bool
```

**功能：** 判断两个ItemState枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ItemState](#enum-itemstate)|是|-|要比较的另一个ItemState枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ItemState)

```cangjie
public operator func !=(other: ItemState): Bool
```

**功能：** 判断两个ItemState枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ItemState](#enum-itemstate)|是|-|要比较的另一个ItemState枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|