### class TabsController

```cangjie
public class TabsController {
    public init()
}
```

**功能：** Tabs组件的控制器，用于控制Tabs组件进行页签切换。不支持一个TabsController控制多个Tabs组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init()

```cangjie
public init()
```

**功能：** 创建一个tabs控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func changeIndex(Int32)

```cangjie
public func changeIndex(index: Int32): Unit
```

**功能：** 控制Tabs切换到指定页签。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|页签在Tabs里的索引值，索引值从0开始。<br> **说明：** <br>设置小于0或大于最大数量的值时，取初始值0。|

#### func preloadItems(?Array\<Int32>)

```cangjie
public func preloadItems(indices: ?Array<Int32>): Unit
```

**功能：** 控制Tabs预加载指定子节点。调用该接口后会一次性加载所有指定的子节点，因此为了性能考虑，建议分批加载子节点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|indices|?Array\<Int32>|是|-|需预加载的子节点的下标数组。<br> 初始值：空数组|

#### func setTabBarOpacity(Float64)

```cangjie
public func setTabBarOpacity(opacity: Float64): Unit
```

**功能：** 设置TabBar的不透明度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|opacity|Float64|是|-|设置TabBar的不透明度，取值范围为[0.0, 1.0]。|

#### func setTabBarTranslate(TranslateOptions)

```cangjie
public func setTabBarTranslate(translate: TranslateOptions): Unit
```

**功能：** 设置TabBar的平移距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|translate|[TranslateOptions](cj-apis-matrix4.md#class-translateoption)|是|-|设置TabBar的平移距离。|