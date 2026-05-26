### func editMenuOptions((Array\<TextMenuItem>) -> Array\<TextMenuItem>, (TextMenuItem,Int32,Int32) -> Bool)

```cangjie
public func editMenuOptions(onCreateMenu: (Array<TextMenuItem>) -> Array<TextMenuItem>,
    onMenuItemClick: (TextMenuItem, Int32, Int32) -> Bool): This
```

**功能：** Web组件自定义文本选择菜单。用户可以通过该属性设置自定义的文本菜单。<!--在onCreateMenu中，可以修改、增加、删除菜单选项，如果希望不显示文本菜单，需要返回空数组。在onMenuItemClick中，可以自定义菜单选项的回调函数。-->该函数在菜单选项被点击后触发，并根据返回值决定是否执行系统默认的回调。返回true不执行系统回调，返回false继续执行系统回调。本接口在与[selectionMenuOptions](#func-selectionmenuoptionsarrayexpandedmenuitemoptions)同时使用时，会使selectionMenuOptions不生效。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onCreateMenu|(Array\<[TextMenuItem](../arkui-cj/cj-text-input-text.md)>)->Array\<[TextMenuItem](../arkui-cj/cj-text-input-text.md)>|是|-|可以修改、增加、删除菜单选项，如果希望不显示文本菜单，需要返回空数组。|
|onMenuItemClick|([TextMenuItem](../arkui-cj/cj-text-input-text.md),Int32,Int32)->Bool|是|-|可以自定义菜单选项的回调函数。该函数在菜单选项被点击后触发，并根据返回值决定是否执行系统默认的回调。返回true不执行系统回调，返回false继续执行系统回调。|

### func enableNativeEmbedMode(Bool)

```cangjie
public func enableNativeEmbedMode(mode: Bool): This
```

**功能：** 设置是否开启同层渲染功能，默认不开启。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|Bool|是|-|是否开启同层渲染功能。true表示开启同层渲染功能，false表示不开启同层渲染功能。<br> 初始值：false。|

### func enableNativeMediaPlayer(Bool, Bool)

```cangjie
public func enableNativeMediaPlayer(enable!: Bool = false, shouldOverlay!: Bool = false): This
```

**功能：** 开启应用接管网页媒体播放功能。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enable|Bool|否|false| **命名参数。** 是否开启该功能。true：开启，false：关闭。<br> 初始值：false。|
|shouldOverlay|Bool|否|false| **命名参数。** 该功能开启后， 应用接管网页视频的播放器画面是否覆盖网页内容。true：开启，false：关闭。<br> 初始值：false。|

### func fileAccess(Bool)

```cangjie
public func fileAccess(fileAccess: Bool): This
```

**功能：** 设置是否开启应用中文件系统的访问，默认启用。rawfile路径的文件不受该属性影响而限制访问。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fileAccess|Bool|是|-|是否开启应用中文件系统的访问，默认启用。|

### func forceDarkAccess(Bool)

```cangjie
public func forceDarkAccess(access: Bool): This
```

**功能：** 设置网页是否开启强制深色模式。默认关闭。该属性仅在darkMode开启深色模式时生效。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|access|Bool|是|-|设置网页是否开启强制深色模式。true：开启，false：关闭。|