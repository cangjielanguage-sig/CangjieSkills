# （可选）使用canOpenLink判断应用是否可访问

## 使用场景

在应用A想要拉起应用B的场景中，应用A可先调用canOpenLink接口判断应用B是否可访问，如果可访问，再拉起应用B。

## 约束限制

在entry模块的module.json5文件中的[querySchemes](../cj-start/basic-knowledge/module-configuration-file.md)字段中，最多允许配置50个URL scheme。

## 接口说明

canOpenLink是[bundleManager](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-bundle_manager.md)提供的支持判断目标应用是否可访问的接口。
匹配规则请参见[显式Want与隐式Want匹配规则](cj-explicit-implicit-want-mappings.md)。

## 操作步骤

### 调用方操作步骤

1. 在entry模块的module.json5文件中配置[querySchemes](../cj-start/basic-knowledge/module-configuration-file.md)属性，声明想要查询的URL scheme。

    ```json
    {
      "module": {
        //...
        "querySchemes": [
          "app1Scheme"
        ]
      }
    }
    ```

2. 导入ohos.bundle.bundleManager模块。

3. 调用canOpenLink接口。

    ```cangjie
    import kit.AbilityKit.BundleManager
    import kit.UIKit.{AppLog, BusinessException}

    @Entry
    @Component
    class EntryView {
        @State
        var message: String = "Hello World"

        func build() {
            Row {
                Column {
                    Text("canOpenLink").fontSize(50).fontWeight(FontWeight.Bold).onClick {
                        evt =>
                        let link = "app1Scheme://test.example.com/home"
                        try {
                            let canOpen = BundleManager.canOpenLink(link)
                            AppLog.info("canOpenLink successfully: ${canOpen}")
                        } catch (e: BusinessException) {
                            AppLog.error("canOpenLink failed: ${e.message}")
                        }
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

### 目标方操作步骤

在module.json5文件中配置[uris](../cj-start/basic-knowledge/module-configuration-file.md)属性。

```json
{
  "module": {
    //...
    "abilities": [
      {
        //...
        "skills": [
          {
            "uris": [
              {
                "scheme": "app1Scheme",
                "host": "test.example.com",
                "pathStartWith": "home"
              }
            ]
          }
        ]
      }
    ]
  }
}
```
