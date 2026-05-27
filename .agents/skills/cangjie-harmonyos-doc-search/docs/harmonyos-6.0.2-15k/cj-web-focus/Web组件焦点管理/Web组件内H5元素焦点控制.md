## Web组件内H5元素焦点控制

- W3C标准事件focus，前端感知网页获焦

```html
addEventListener("focus", (event) => {});

onfocus = (event) => {};
```

- W3C标准事件blur，前端感知网页失焦

```html
addEventListener("blur", (event) => {});

onblur = (event) => {};
```

- W3C autofocus，表示元素应在页面加载时或其所属的 `dialog` 显示时被聚焦

```html
<input name="q" autofocus />
```

在文档或对话框中，最多只能有一个元素具有 autofocus 属性。如果应用于多个元素，第一个元素将获得焦点。

**示例：**

```cangjie
// index.cj
import ohos.state_macro_manage.*
import kit.LocalizationKit.{__GenerateResource__}
import kit.ArkWeb.WebviewController
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    func build() {
        Column {
            Web(src: @rawfile("index.html"), controller: webController)
        }
    }
}
```

```html
<!-- main/resources/rawfile/index.html-->
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>test</title>
</head>
<body>
  <form id="form">
    <input type="text" placeholder="text input" />
    <input type="password" placeholder="password" />
  </form>
</body>
<script>
const form = document.getElementById("form");

form.addEventListener(
  "focus",
  (event) => {
    event.target.style.background = "pink";
  },
  true,
);

form.addEventListener(
  "blur",
  (event) => {
    event.target.style.background = "";
  },
  true,
);
</script>
</html>
```

通过监听W3C接口focus、blur事件，改变输入背景色。

**图2**  Web组件内元素焦点获焦/失焦事件

![web-focus2.gif](figures/web-focus2.gif)