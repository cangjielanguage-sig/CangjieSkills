```bash
        aa start -U myscheme://www.test.com:8080/path --pi paramNumber 1 --pb paramBoolean true --ps paramString teststring  --psn paramNullString
        ```

        UIAbility获取传入参数示例如下：

        <!-- compile -->

        ```cangjie
        import kit.AbilityKit.*
        import ohos.base.*
        import ohos.ability.*

        class TargetAbility <: UIAbility {
          public override func onCreate(want:Want, launchParam: LaunchParam): Unit {
            Hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
            let paramNumber = want.parameters.get("paramNumber")
            let paramBoolean = want.parameters.get("paramBoolean")
            let paramString = want.parameters.get("paramString")
            let paramNullString = want.parameters.get("paramNullString")
          }
        }
        ```

    - 如果需要拉起浏览器并跳转指定页面，可以使用-A -U命令，示例如下：

        本例中以`https://www.example.com`为例，请根据实际情况替换为真实的网址。

        ```bash
        aa start -A ohos.want.action.viewData -U https://www.example.com
        ```