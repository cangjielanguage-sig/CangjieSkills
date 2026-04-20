### class GestureRecognizer

```cangjie
public open class GestureRecognizer {
    public init()
}
```

**功能：** 手势识别器对象。

**系统能力：**  SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### init()

```cangjie
public init()
```

**功能：** 构建一个手势识别器对象。

**起始版本：** 20

#### func getEventTargetInfo()

```cangjie
public func getEventTargetInfo(): EventTargetInfo
```

**功能：** 返回当前手势识别器对应组件的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[EventTargetInfo](#class-eventtargetinfo)|当前手势识别器对应组件的信息。|

#### func getState()

```cangjie
public func getState(): GestureRecognizerState
```

**功能：** 返回当前手势识别器的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[GestureRecognizerState](#enum-gesturerecognizerstate)|当前手势识别器的状态。|

#### func getTag()

```cangjie
public func getTag(): String
```

**功能：** 返回当前手势识别器的tag。

**系统能力：**  SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|当前手势识别器的tag。|

#### func getType()

```cangjie
public func getType(): GestureTypes
```

**功能：** 返回当前手势识别器的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[GestureTypes](./cj-universal-gesture-judge.md#enum-gesturetypes)|当前手势识别器的类型。|

#### func isBuiltIn()

```cangjie
public func isBuiltIn(): Bool
```

**功能：** 返回当前手势识别器是否为系统内置手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前手势识别器是否为系统内置手势。true表示手势识别器为系统内置手势，false表示非系统内置手势。|

#### func isValid()

```cangjie
public func isValid(): Bool
```

**功能：** 返回当前手势识别器是否有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前手势识别器是否有效。当该识别器绑定的组件被析构或者该识别器不在响应链上时返回false。|

#### func isEnabled()

```cangjie
public func isEnabled(): Bool
```

**功能：** 返回当前手势识别器的使能状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前手势识别器的使能状态。true表示当前手势识别器能够回调应用事件，false表示当前手势识别器不回调应用事件。|

#### func setEnabled(Bool)

```cangjie
public func setEnabled(isEnabled: Bool): Unit
```

**功能：** 设置当前手势识别器的使能状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isEnabled|Bool|是|-|手势识别器的使能状态。true表示当前手势识别器能够回调应用事件，false表示当前手势识别器不回调应用事件。|