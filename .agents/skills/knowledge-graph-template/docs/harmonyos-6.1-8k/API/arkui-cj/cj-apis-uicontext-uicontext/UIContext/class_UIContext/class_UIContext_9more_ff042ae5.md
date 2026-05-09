## class UIContext

```cangjie
public class UIContext {}
```

**功能：** UI上下文类，提供各种UI相关功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func animateTo(AnimateParam, VoidCallback)

```cangjie
public func animateTo(value: AnimateParam, event: VoidCallback): Unit
```

**功能：** 提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AnimateParam](./cj-common-types.md#class-animateparam)|是|-|动画参数。|
|event|[VoidCallback](./cj-common-types.md#type-voidcallback)|是|-|动画执行的回调函数。|

### func createAnimator(AnimatorOptions)

```cangjie
public func createAnimator(options: AnimatorOptions): AnimatorResult
```

**功能：** 创建animator动画结果对象（AnimatorResult）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AnimatorOptions](./cj-apis-uicontext-animator.md#class-animatoroptions)|是|-|动画选项。|

**返回值：**

|类型|说明|
|:----|:----|
|[AnimatorResult](./cj-apis-uicontext-animator.md#class-animatorresult)|动画结果对象。|

### func fp2px(Length)

```cangjie
public func fp2px(value: Length): Option<Length>
```

**功能：** 将fp单位的值转换为px单位的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|要转换的值。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<[Length](./cj-common-types.md#interface-length)>|转换后的值。|

### func getContextMenuController()

```cangjie
public func getContextMenuController(): ContextMenuController
```

**功能：** 获取上下文菜单控制器对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ContextMenuController](./cj-apis-uicontext-contextmenucontroller.md#class-contextmenucontroller)|上下文菜单控制器对象。|

### func getFont()

```cangjie
public func getFont(): Font
```

**功能：** 获取字体对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Font](cj-common-types.md#class-font)|字体对象。|

### func getMeasureUtils()

```cangjie
public func getMeasureUtils(): MeasureUtils
```

**功能：** 获取测量工具对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[MeasureUtils](./cj-apis-uicontext-measureutils.md#class-measureutils)|MeasureUtils对象。|

### func getPromptAction()

```cangjie
public func getPromptAction(): PromptAction
```

**功能：** 获取PromptAction对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[PromptAction](./cj-apis-uicontext-promptaction.md#class-promptaction)|PromptAction对象。|

### func getRouter()

```cangjie
public func getRouter(): Router
```

**功能：** 获取路由对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Router](./cj-apis-uicontext-router.md#class-router)|路由对象。|