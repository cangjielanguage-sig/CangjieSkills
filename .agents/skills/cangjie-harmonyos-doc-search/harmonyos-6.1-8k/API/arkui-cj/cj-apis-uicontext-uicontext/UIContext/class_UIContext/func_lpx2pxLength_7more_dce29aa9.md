### func lpx2px(Length)

```cangjie
public func lpx2px(value: Length): Option<Length>
```

**功能：** 将lpx单位的值转换为px单位的值。

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

### func px2fp(Length)

```cangjie
public func px2fp(value: Length): Option<Length>
```

**功能：** 将px单位的值转换为fp单位的值。

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

### func px2lpx(Length)

```cangjie
public func px2lpx(value: Length): Option<Length>
```

**功能：** 将px单位的值转换为lpx单位的值。

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

### func px2vp(Length)

```cangjie
public func px2vp(value: Length): Option<Length>
```

**功能：** 将px单位的值转换为vp单位的值。

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

### func showActionSheet(ActionSheetOptions)

```cangjie
public func showActionSheet(value: ActionSheetOptions): Unit
```

**功能：** 定义列表弹窗并弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ActionSheetOptions](./cj-dialog-actionsheet.md#class-actionsheetoptions)|是|-|操作表参数。|

### func showAlertDialog(AlertDialogParamWithConfirm)

```cangjie
public func showAlertDialog(options: AlertDialogParamWithConfirm): Unit
```

**功能：** 显示警告对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AlertDialogParamWithConfirm](./cj-dialog-alertdialog.md#class-alertdialogparamwithconfirm)|是|-|警告对话框参数。|

### func showAlertDialog(AlertDialogParamWithButtons)

```cangjie
public func showAlertDialog(options: AlertDialogParamWithButtons): Unit
```

**功能：** 显示警告对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AlertDialogParamWithButtons](./cj-dialog-alertdialog.md#class-alertdialogparamwithbuttons)|是|-|警告对话框参数。|