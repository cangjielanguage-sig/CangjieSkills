## 自定义规则样例说明

正确的规则样例如下：

| 强密码规则样例| 规则释义|
|:-------- |:---------- |
|begin:[upper],special:[yes],len:[maxlen:32,minlen:12]|以大写字母开头，包含大小写字母、数字、特殊字符，长度为12-32之间（包含12和32）的随机数值。|
|begin:[lower],special:[yes],len:[maxlen:14]|以小写字母开头，包含大小写字母、数字、特殊字符，长度为14-32之间（包含14和32）的随机数值。|
|begin:[digit],special:[yes],len:[fixedlen:15]|以数字开头，包含大小写字母、数字、特殊字符，长度为15。|
|begin:[upper]|以大写字母开头，包含大小写字母、数字，长度为16。|
|special:[yes]|以任意字母或数字开头，包含大小写字母、数字、特殊字符，长度为16。|
|len:[fixedlen:15]|以任意字母或数字开头，包含大小写字母、数字，长度为15。|
|begin:[upper],special:[yes]|以大写字母开头，包含大小写字母、数字、特殊字符,长度为16。|
|begin:[lower],len:[maxlen:25,minlen:12]|以小写字母开头，包含大小写字母、数字，长度为12-25之间（包含12和25）的随机数值。|
|special:[yes],len:[fixedlen:15]|以任意字母或数字开头，包含大小写字母、数字、特殊字符，长度为15。|

错误的规则样例如下：

| 强密码规则错误用例| 规则释义|
|:-------- |:---------- |
|begin:[uppper]|begin属性的取值upper拼写错误。|
|began:[upper]|begin属性拼写错误。|
|len:[15]|len属性语法错误，未使用三种长度关键词。|
|len:[fixedlen:15,maxlen:18]|len属性语法错误，fixedlen与maxlen不可混用。|
|len:[maxlen:15,minlen:18]|len属性参数值错误，maxlen的取值不能小于minlen。|

## 示例

```cangjie
TextInput(placeholder: "新密码")
   .enableAutoFill(true)
   .setType(InputType.NEW_PASSWORD)
   .passwordRules('begin:[lower],special:[yes],len:[maxlen:32,minlen:12]')
   .placeholderColor(0x182431)
   .width(100.percent)
   .opacity(0.6)
   .showPasswordIcon(true)
   .placeholderFont(size: 16, weight: FontWeight.Regular)
   .margin(bottom: 36)
```