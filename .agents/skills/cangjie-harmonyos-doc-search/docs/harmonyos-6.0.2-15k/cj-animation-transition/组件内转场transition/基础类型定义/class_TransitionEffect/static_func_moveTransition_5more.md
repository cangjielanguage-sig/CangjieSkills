#### static func move(TransitionEdge)

```cangjie
public static func move(edge: TransitionEdge): TransitionEffect
```

**功能：** 指定组件转场时从屏幕边缘滑入和滑出的效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|edge|[TransitionEdge](#enum-transitionedge)|是|-|指定组件转场时从屏幕边缘滑入和滑出的效果，本质为平移效果，为插入时起点和删除时终点的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|组件转场效果。|

#### static func opacity(Float64)

```cangjie
public static func opacity(number: Float64): TransitionEffect
```

**功能：** 设置组件转场时的透明度效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|number|Float64|是|-|设置组件转场时的透明度效果，为插入时起点和删除时终点的值。取值范围：[0, 1]。<br> **说明：** <br>设置小于0的非法值按0处理，大于1的非法值按1处理。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|组件转场效果。|

#### static func rotate(RotateOptions)

```cangjie
public static func rotate(options: RotateOptions): TransitionEffect
```

**功能：** 设置组件转场时的旋转效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[RotateOptions](#class-rotateoptions)|是|-|设置组件转场时的旋转效果，为插入时起点和删除时终点的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|组件转场效果。|

#### static func scale(ScaleOptions)

```cangjie
public static func scale(options: ScaleOptions): TransitionEffect
```

**功能：** 设置组件转场时的缩放效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[ScaleOptions](#class-scaleoptions)|是|-|设置组件转场时的缩放效果，为插入时起点和删除时终点的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|组件转场效果。|

#### static func translate(TranslateOptions)

```cangjie
public static func translate(options: TranslateOptions): TransitionEffect
```

**功能：** 设置组件转场时的平移效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[TranslateOptions](#class-translateoptions)|是|-|设置组件转场时的平移效果，为插入时起点和删除时终点的值。|

**返回值：**

|类型|说明|
|:----|:----|
|[TransitionEffect](#class-transitioneffect)|组件转场效果。|