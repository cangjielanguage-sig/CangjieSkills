# 文本输入（TextInput/TextArea）

TextInput、TextArea是输入框组件，通常用于响应用户的输入操作，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参见[TextInput](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-textinput.md)、[TextArea](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-textarea.md)。

## 创建输入框

TextInput为单行输入框、TextArea为多行输入框。通过以下接口来创建。

```cangjie
init(placeholder!: String = "", text!: String = "", controller!: TextInputController = TextInputController())
```

```cangjie
init(placeholder!: String = "", text!: String = "", controller!: TextAreaController = TextAreaController())
```

- 单行输入框。

    ```cangjie
    TextInput()
    ```

    ![Text](figures/Text.png)

- 多行输入框。

    ```cangjie
    TextArea()
    ```

    ![Text1](figures/Text1.png)

- 多行输入框文字超出一行时会自动折行。

    ```cangjie
    TextArea(text: "我是TextArea我是TextArea我是TextArea我是TextArea" ).width(300)
    ```

    ![Text2](figures/Text2.png)

## 设置输入框类型

TextInput有以下类型可选择：Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式、USER_NAME用户名输入模式、NEW_PASSWORD新密码输入模式、NUMBER_PASSWORD纯数字密码输入模式、NUMBER_DECIMAL带小数点的数字输入模式、带URL的输入模式。通过setType属性进行设置：

- 基本输入模式（默认类型）

    ```cangjie
    TextInput()
    .setType(InputType.Normal)
    ```

    ![Text3](figures/Text3.png)

- 密码输入模式

    ```cangjie
    TextInput()
    .setType(InputType.Password)
    ```

    ![Text4](figures/Text4.png)

- 邮箱地址输入模式。

    ```cangjie
    TextInput()
    .setType(InputType.Email)
    ```

    ![Text5](figures/Text5.png)

- 纯数字输入模式。

    ```cangjie
    TextInput()
    .setType(InputType.Number)
    ```

    ![Text6](figures/Text6.png)

- 电话号码输入模式。

    ```cangjie
    TextInput()
    .setType(InputType.PhoneNumber)
    ```

    ![Text7](figures/Text7.png)

- 带小数点的数字输入模式。

    ```cangjie
    TextInput()
    .setType(InputType.NUMBER_DECIMAL)
    ```

    ![Text8](figures/Text8.png)

- 带URL的输入模式。

    ```cangjie
    TextInput()
    .setType(InputType.URL)
    ```

    ![Text9](figures/Text9.png)

## 自定义样式

- 设置无输入时的提示文本。

    ```cangjie
    TextInput(placeholder: '我是提示文本')
    ```

    ![Text10](figures/Text10.png)

- 设置输入框当前的文本内容。

    ```cangjie
    TextInput( placeholder: '我是提示文本', text: '我是当前文本内容' )
    ```

    ![Text11](figures/Text11.png)

- 添加backgroundColor改变输入框的背景颜色。

    ```cangjie
    TextInput( placeholder: '我是提示文本', text: '我是当前文本内容' )
    .backgroundColor(Color.PINK)
    ```

    ![Text12](figures/Text12.png)

    更丰富的样式可以结合通用属性实现。