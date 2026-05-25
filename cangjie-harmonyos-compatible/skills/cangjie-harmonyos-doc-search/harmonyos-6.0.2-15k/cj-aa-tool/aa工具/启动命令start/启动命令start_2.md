> **说明：**
>
> 本例中仅介绍了部分字段的使用。关于Ability匹配的详细规则参考[显式Want与隐式Want匹配规则](../application-models/cj-explicit-implicit-want-mappings.md)。

- **目标应用：**

    修改module.json5配置，为目标Ability配置uris。

    ```json
    {
      "name": "TargetAbility",
      // ......
      "exported": true,
      "skills": [
        {
          "actions":[
            "ohos.want.action.viewData"
          ],
          "uris":[
            {
              "scheme": "myscheme",
              "host": "www.test.com",
              "port": "8080",
              "path": "path",
            }
          ]
        }
      ]
    }
    ```

- **拉起方应用：**

    隐式启动Ability。

    - 如果需要拉起应用的页面，可以使用-U命令，示例如下：

        ```bash
        aa start -U myscheme://www.test.com:8080/path
        ```

    - 在上述基础上，如果需要携带参数，可以使用如下命令：

        ```bash
        aa start -U myscheme://www.test.com:8080/path --pi paramNumber 1 --pb paramBoolean true --ps paramString teststring  --psn paramNullString
        ```

        UIAbility获取传入参数示例如下：

        ```cangjie
        import kit.AbilityKit.*
        import ohos.base.*
        import ohos.ability.*

        class TargetAbility <: Ability {
            public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
                hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
                let paramNumber = want.parameters.paramNumber
                let paramBoolean = want.parameters.paramBoolean
                let paramString = want.parameters.paramString
                let paramNullString = want.parameters.paramNullString
            }
        }
        ```

    - 如果需要拉起浏览器并跳转指定页面，可以使用-A -U命令，示例如下：

        本例中以`https://www.example.com`为例，请根据实际情况替换为真实的网址。

        ```bash
        aa start -A ohos.want.action.viewData -U https://www.example.com
        ```