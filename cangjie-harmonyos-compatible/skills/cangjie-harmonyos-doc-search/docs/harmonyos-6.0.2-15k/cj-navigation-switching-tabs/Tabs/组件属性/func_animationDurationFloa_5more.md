### func animationDuration(Float32)

```cangjie
public func animationDuration(duration: Float32): This
```

**功能：** 设置点击TabBar页签和调用TabsController的changeIndex接口切换TabContent的动画时长。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Float32|是|-|点击TabBar页签和调用TabsController的changeIndex接口切换TabContent的动画时长。<br> 初始值：不设置该属性或设置为异常值，且设置TabBar为BottomTabBarStyle样式时，初始值为0。设置TabBar为其他样式时，初始值为300。<br>单位：ms <br> 取值范围：[0, +∞)。|

### func animationDuration(Int32)

```cangjie
public func animationDuration(duration: Int32): This
```

**功能：** 设置点击TabBar页签和调用TabsController的changeIndex接口切换TabContent的动画时长。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Int32|是|-|点击TabBar页签和调用TabsController的changeIndex接口切换TabContent的动画时长。<br> 初始值：不设置该属性或设置为异常值，且设置TabBar为BottomTabBarStyle样式时，初始值为0。设置TabBar为其他样式时，初始值为300。<br>单位：ms <br> 取值范围：[0, +∞)。|

### func animationMode(AnimationMode)

```cangjie
public func animationMode(mode: AnimationMode): This
```

**功能：** 设置点击TabBar页签或调用TabsController的changeIndex接口时切换TabContent的动画形式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[AnimationMode](#enum-animationmode)|是|-|点击TabBar页签或调用TabsController的changeIndex接口时切换TabContent的动画形式。<br> 初始值： AnimationMode.CONTENT_FIRST，表示在点击TabBar页签或调用TabsController的changeIndex接口切换TabContent时，先加载目标页内容，再开始切换动画。|

### func barBackgroundBlurStyle(BlurStyle)

```cangjie
public func barBackgroundBlurStyle(blurStyle: BlurStyle): This
```

**功能：** 设置TabBar的背景模糊材质。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|blurStyle|[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)|是|-|TabBar的背景模糊材质。<br> 初始值：BlurStyle.NONE|

### func barBackgroundBlurStyle(BlurStyle, BackgroundBlurStyleOptions)

```cangjie
public func barBackgroundBlurStyle(blurStyle: BlurStyle, options: BackgroundBlurStyleOptions): This
```

**功能：** 为TabBar提供一种在背景和内容之间的模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|blurStyle|[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)|是|-|背景模糊样式。模糊样式中封装了模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度五个参数。|
|options|[BackgroundBlurStyleOptions](cj-universal-attribute-background.md#class-backgroundblurstyleoptions)|是|-|背景模糊选项。|