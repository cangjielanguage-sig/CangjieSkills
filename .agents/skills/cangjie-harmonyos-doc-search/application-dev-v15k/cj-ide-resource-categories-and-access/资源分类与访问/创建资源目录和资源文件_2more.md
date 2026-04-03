## 创建资源目录和资源文件

在resources目录下，可按照限定词目录命名规则，以及资源组目录支持的文件类型和说明，创建资源目录和资源组目录，添加特定类型资源。DevEco Studio支持同时创建资源目录和资源文件，也支持单独创建资源目录或资源文件。

在resources目录右键菜单选择“New > Resource File”，可同时创建资源目录和资源文件，文件默认创建在base目录的对应资源组。如果选择了限定词，则会按照命名规范自动生成限定词和资源组目录，并将文件创建在限定词目录中。

图中File name为需要创建的文件名。Resource type为资源组类型，默认是Element。Root element为资源类型。Avaliable qualifiers为供选择的限定词目录，通过右侧的小箭头可添加或者删除。

创建的目录名自动生成，格式固定为“限定词.资源组”，例如：创建一个限定词为dark的element目录，自动生成的目录名称为“dark.element”。

![newResFolder](../figures/start-newResFolder.png)

### 创建资源目录

在resources目录右键菜单选择“New > Resource Directory”，可创建资源目录，默认创建的是base目录。如果选择了限定词，则会按照命名规范自动生成限定词和资源组目录。确定限定词后，选择资源组类型，当前资源组类型支持Element、Media、Profile三种，创建后生成资源目录。

![newResFolder2](../figures/start-newResFolder2.png)

### 创建资源文件

在base>element资源目录的右键菜单选择“New > Element Resource File”，即可创建Element Resource File。

![newResFile](../figures/start-newResFile.png)

## 资源可翻译特性

### 功能介绍

资源需要翻译时，可使用attr属性标记字符串翻译范围和翻译状态。attr属性不参与资源编译，只标记字符串是否翻译。

未配置attr属性，默认需要翻译。

```json
"attr": {
  "translatable": false|true
  "priority": "code|translate|LT|customer"
}
```

**attr支持属性**

| **名称** | **类型** | **说明** |
| ---------- | ------------------------- | --------------------------------- |
| translatable  | boolean。 | 标记字符串是否需要翻译。<br>true：需要翻译。<br>false：不需要翻译。 |
| media  | 表示媒体资源，包括图片、音频、视频等非文本格式的文件（目录下只支持文件类型）。<br>图片和音视频的类型说明见[资源组目录](#资源组目录)。 | 文件名可自定义，例如：icon.png。 |
| priority  | string。 | 标记字符串翻译状态。<br>code：未翻译。<br>translate：翻译未验证。<br>LT：翻译已验证。<br>customer：用户定制字符串。 |

### 使用约束

可翻译特性使能范围：base目录下string、strarray、plural类型资源。

```text
resources
|---base
|   |---element
|   |   |---string.json
|   |   |---strarray.json
|   |   |---plural.json
```

### 示例

string资源配置attr属性示例如下：

```json
{
  "string": [
    {
      "name": "string1",
      "value": "1",
      "attr": {
        "translatable": false
      }
    },
    {
      "name": "string2",
      "value": "Hello world!",
      "attr": {
        "translatable": true,
        "priority": "LT"
      }
    }
  ]
}
```