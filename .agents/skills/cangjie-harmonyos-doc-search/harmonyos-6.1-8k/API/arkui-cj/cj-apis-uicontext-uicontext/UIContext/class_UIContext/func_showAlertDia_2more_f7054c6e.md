### func showAlertDialog(AlertDialogParamWithOptions)

```cangjie
public func showAlertDialog(options: AlertDialogParamWithOptions): Unit
```

**功能：** 显示警告对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AlertDialogParamWithOptions](./cj-dialog-alertdialog.md#class-alertdialogparamwithbuttons)|是|-|警告对话框参数。|

### func vp2px(Length)

```cangjie
public func vp2px(value: Length): Option<Length>
```

**功能：** 将vp单位的值转换为px单位的值。

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