### func style(LinearStyleOptions)

```cangjie
public func style(linearStyle: LinearStyleOptions): This
```

**功能：** 设置进度条Linear的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|linearStyle|[LinearStyleOptions](#class-linearstyleoptions)|是|-|设置Linear的样式。|

### func style(CapsuleStyleOptions)

```cangjie
public func style(capsuleStyle: CapsuleStyleOptions): This
```

**功能：** 设置进度条Capsule的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|capsuleStyle|[CapsuleStyleOptions](#class-capsulestyleoptions)|是|-|设置Capsule的样式。|

### func value(Float64)

```cangjie
public func value(baseValue: Float64): This
```

**功能：** 设置当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。非法数值不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|baseValue|Float64|是|-|当前进度值。<br/>初始值：0|