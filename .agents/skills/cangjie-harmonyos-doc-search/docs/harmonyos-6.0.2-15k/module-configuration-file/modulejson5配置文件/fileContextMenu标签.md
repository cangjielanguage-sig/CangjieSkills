## fileContextMenu标签

该标签标识当前HAP的右键菜单配置项，是一个profile文件资源，用于指定描述应用注册右键菜单配置文件。仅在PC/2in1设备上生效。

fileContextMenu标签示例

```json
{
  "module": {
    // ...
    "fileContextMenu": "$profile:menu" // 通过profile下的资源文件配置
  }
}
```

在开发视图的resources/base/profile下面定义配置文件menu.json，其中文件名“menu.json”可自定义，需要和fileContextMenu标签指定的信息对应。配置文件中描述了当前应用注册的右键菜单的项目和响应行为。
配置文件根节点名称为fileContextMenu，为对象数组，标识当前module注册右键菜单的数量。（单模块和单应用注册数量不能超过5个，配置超过数量当前只解析随机5个）

**表22** fileContextMenu标签配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| abilityName | 表示当前右键菜单对应的需要拉起的ability名称。 | 字符串 | 不可缺省。 |
| menuItem | 右键菜单显示的信息。命名建议：<br/>原则一：[动作]+[应用名]，中文示例：用{App}打开、用{App} ({Plugin}插件) 打开；英文示例：Open with {App}、Open with {App} ({Plugin})。<br/>原则二：[动作]+[目的]，示例：压缩为{文件名}、压缩至{路径}、用{App}转换为{格式}。 | 资源id | 不可缺省。 |
| menuHandler | 一个ability可以创建多个右键菜单， 用该字段来区分用户拉起的不同右键菜单项。该字段在用户点击右键菜单执行时，会作为参数传递给右键菜单应用。 | 字符串 | 不可缺省。 |
| menuContext | 定义展示该菜单项需要的上下文，可以支持多种情况，类型为数组。 | 对象数组 | 不可缺省。 |

**表23* menuContext标签配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| menuKind | 表示单击如下类型时会触发右键菜单。取值范围如下：<br/>-&nbsp;0：空白处<br/>-&nbsp;1：文件<br/>-&nbsp;2：文件夹<br/>-&nbsp;3：文件和文件夹 | 数值 | 不可缺省。 |
| menuRule | 表示采用什么方式选择文件或文件夹时，会触发右键菜单。取值范围如下：<br/>-&nbsp;single：单选<br/>-&nbsp;multi：多选<br/>-&nbsp;both：单选或多选 | 字符串 | 仅当menuKind为1或2时，才会读取该字段，此时不可缺省。 |
| fileSupportType | 表示当选中的文件列表里包含指定的文件类型时，显示右键菜单。<br/>当该字段取值为["*"]时，将会读取fileNotSupportType字段。<br/>当该字段取值为[]时，将不做任何处理。 | 字符串数组 | 仅当menuKind为1时，才会读取该字段，此时不可缺省。 |
| fileNotSupportType |  表示当选中的文件列表里包含这些文件类型时，不显示该右键菜单。<br/>仅当menuKind为1、且fileSupportType为["*"]时，才会读取该字段。 | 字符串数组 | 可缺省，缺省值为空。 |

resources/base/profile路径下的menu.json资源文件示例如下：

```json
{
  "fileContextMenu": [
    {
      "abilityName": "EntryAbility",
      "menuItem": "$string:module_desc",
      "menuHandler": "openCompress",
      "menuContext": [
        {
          "menuKind": 0
        },
        {
          "menuKind": 1,
          "menuRule": "both",
          "fileSupportType": [
            ".rar",
            ".zip"
          ],
          "fileNotSupportType": [
            ""
          ]
        },
        {
          "menuKind": 2,
          "menuRule": "single"
        },
        {
          "menuKind": 3
        }
      ]
    }
  ]
}
```

**响应行为**

应用进行右键扩展菜单注册后，在文件管理器通过右键操作拉起菜单，该菜单中会有“更多”选项。单击“更多”选项后，会出现注册后的menuItem列表，单击任意一个选项后，文件管理器默认通过startAbility的方式拉起三方应用，除了指定三方应用的包名和ability名之外，want中的parameter中，也会传入如下字段：

**表24** want中parameter字段说明

| 参数名 | 值 | 类型 |
| -------- | -------- | -------- |
| menuHandler | 对应注册配置文件中menuHandler的值。 | 字符串 |
| uriList | 用户在具体文件上触发右键的uri值，如果空白处响应，此值为空，单个文件响应，数组长度1，多个文件响应则传入对应所有文件的uri值。 | 字符串数组 |