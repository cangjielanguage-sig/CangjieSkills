### class TextMenuItemId

```cangjie
public class TextMenuItemId {}
```

**功能：** 菜单Id值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static prop AI_WRITER

```cangjie
public static prop AI_WRITER: TextMenuItemId
```

**功能：** 表示可对选中的文本进行润色、摘要提取、排版等。该菜单项依赖大模型能力，否则不生效。

**类型：** [TextMenuItemId](#class-textmenuitemid)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static prop CAMERA_INPUT

```cangjie
public static prop CAMERA_INPUT: TextMenuItemId
```

**功能：** 表示拍摄输入。

**类型：** [TextMenuItemId](#class-textmenuitemid)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static prop COLLABORATION_SERVICE

```cangjie
public static prop COLLABORATION_SERVICE: TextMenuItemId
```

**功能：** 表示互通服务。

**类型：** [TextMenuItemId](#class-textmenuitemid)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static prop COPY

```cangjie
public static prop COPY: TextMenuItemId
```

**功能：** 表示默认复制。

**类型：** [TextMenuItemId](#class-textmenuitemid)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static prop CUT

```cangjie
public static prop CUT: TextMenuItemId
```

**功能：** 表示默认裁剪。

**类型：** [TextMenuItemId](#class-textmenuitemid)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static prop PASTE

```cangjie
public static prop PASTE: TextMenuItemId
```

**功能：** 表示默认粘贴。

**类型：** [TextMenuItemId](#class-textmenuitemid)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static prop SELECT_ALL

```cangjie
public static prop SELECT_ALL: TextMenuItemId
```

**功能：** 表示默认全选。

**类型：** [TextMenuItemId](#class-textmenuitemid)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### static func of(AppResource)

```cangjie
public static func of(id: AppResource): TextMenuItemId
```

**功能：** 返回根据id创建的TextMenuItemId对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|菜单的id。|

**返回值：**

|类型|说明|
|:----|:----|
|[TextMenuItemId](#class-textmenuitemid)|根据id创建的TextMenuItemId对象|

#### static func of(String)

```cangjie
public static func of(id: String): TextMenuItemId
```

**功能：** 返回根据id创建的TextMenuItemId对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|菜单的id。|

**返回值：**

|类型|说明|
|:----|:----|
|[TextMenuItemId](#class-textmenuitemid)|根据id创建的TextMenuItemId对象|

#### func equals(TextMenuItemId)

```cangjie
public func equals(id: TextMenuItemId): Bool
```

**功能：** 判断TextMenuItemId是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|[TextMenuItemId](#class-textmenuitemid)|是|-|TextMenuItemId的id。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个TextMenuItemId是否相等。|