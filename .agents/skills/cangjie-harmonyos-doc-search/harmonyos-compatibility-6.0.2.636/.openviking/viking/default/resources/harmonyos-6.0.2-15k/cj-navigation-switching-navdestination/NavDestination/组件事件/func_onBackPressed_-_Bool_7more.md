### func onBackPressed(() -> Bool)

```cangjie
public func onBackPressed(callback: ()->Bool): This
```

**功能：** 当与Navigation绑定的页面栈中存在内容时，此回调生效。当点击返回键时，触发该事件。返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Bool|是|-|回调函数，当点击返回键时，触发该回调。<br/> 返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。|

### func onReady((NavDestinationContext) -> Unit)

```cangjie
public func onReady(callback: (NavDestinationContext) -> Unit): This
```

**功能：** 当NavDestination即将构建子组件之前会触发此事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([NavDestinationContext](#class-navdestinationcontext))->Unit|是|-|回调函数，即将构建子组件之前会触发此回调。|

### func onShown((VisibilityChangeReason) -> Unit)

```cangjie
public func onShown(callback: (VisibilityChangeReason) -> Unit): This
```

**功能：** 当该NavDestination页面显示时触发此事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 21

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([VisibilityChangeReason](#enum-visibilitychangereason))->Unit|是|-|回调函数，即显示该NavDestination页面时会触发此回调。回调会提供入参VisibilityChangeReason以说明onShown触发的原因。|

### func onHidden((VisibilityChangeReason) -> Unit)

```cangjie
public func onHidden(callback: (VisibilityChangeReason) -> Unit): This
```

**功能：** 当该NavDestination页面隐藏时触发此事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 21

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([VisibilityChangeReason](#enum-visibilitychangereason))->Unit|是|-|回调函数，即隐藏该NavDestination页面时会触发此回调。回调会提供入参VisibilityChangeReason以说明onShown触发的原因。|

### func onWillAppear(() -> Unit)

```cangjie
public func onWillAppear(callback: ()->Unit): This
```

**功能：** 当该Destination挂载之前触发此事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|() -> Unit|是|-|回调函数，当该Destination挂载之前触发此回调。在该回调中允许修改页面栈，当前帧生效。|

### func onWillShow(() -> Unit)

```cangjie
public func onWillShow(callback: ()->Unit): This
```

**功能：** 当该Destination显示之前触发此事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|() -> Unit|是|-|回调函数，当该Destination显示之前触发此回调。|

### func onWillHide(() -> Unit)

```cangjie
public func onWillHide(callback: ()->Unit): This
```

**功能：** 当该Destination隐藏之前触发此事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|() -> Unit|是|-|回调函数，当该Destination隐藏之前触发此回调。|