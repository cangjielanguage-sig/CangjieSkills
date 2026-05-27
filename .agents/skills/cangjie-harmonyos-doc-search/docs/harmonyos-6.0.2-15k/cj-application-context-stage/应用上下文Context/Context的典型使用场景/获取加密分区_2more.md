### 获取加密分区

应用文件加密是一种保护数据安全的方法，可以使得文件在未经授权访问的情况下得到保护。在不同的场景下，应用需要不同程度的文件保护。

在实际应用中，开发者需要根据不同场景的需求选择合适的加密分区，从而保护应用数据的安全。通过合理使用不同级别的加密分区，可以有效提高应用数据的安全性。关于不同分区的权限说明，详情请参见[AreaMode](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#enum-areamode)。

- EL1：对于私有文件，如闹铃、壁纸等，应用可以将这些文件放到设备级加密分区（EL1）中，以保证在用户输入密码前就可以被访问。
- EL2：对于更敏感的文件，如个人隐私信息等，应用可以将这些文件放到更高级别的加密分区（EL2）中，以保证更高的安全性。
- EL3：对于应用中的记录步数、文件下载、音乐播放，需要在锁屏时读写和创建新文件，适合放在（EL3）的加密分区。
- EL4：对于用户安全信息相关的文件，锁屏时不需要读写文件、也不能创建文件，适合放在（EL4）的加密分区。
- EL5：对于用户隐私敏感数据文件，锁屏后默认不可读写，如果锁屏后需要读写文件，则锁屏前可以调用[Access](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-screen_lock_file_manager.md#static-func-acquireaccess)接口申请继续读写文件，或者锁屏后也需要创建新文件且可读写，适合放在（EL5）的应用级加密分区。

要实现获取当前加密分区，可以通过读[Context](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-context)的`area`属性来实现。

```cangjie
// main_ability.cj
import kit.UIKit.AppLog
import kit.AbilityKit.{UIAbility, Want, LaunchParam}

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info(this.context.area)
    }
}
```

### 获取本应用中其他Module的Context

调用[createModuleContext(context: Context, moduleName: String)](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-createmodulecontextcontext-string)方法，获取本应用中其他Module的Context。获取到其他Module的Context之后，即可获取到相应Module的资源信息。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

  ```cangjie
  import kit.AbilityKit.{UIAbilityContext, createModuleContext}
  import kit.UIKit.{AppLog, Button, BusinessException}

  // 见获取UIAbility的上下文信息章节
  func getContext(): UIAbilityContext {
      return globalContext.getOrThrow()
  }

  @Entry
  @Component
  class EntryView {
      @State
      var message: String = "Hello World"

      func build() {
          Row {
              Column {
                  Text(this.message)
                  // ...
                  Button("create module context").onClick(
                      {
                      evt => try {
                          let ctx = createModuleContext(getContext(), "entry")
                          AppLog.info("CreateModuleContext success, data: ${ctx.applicationInfo.name}")
                      } catch (err: BusinessException) {
                          AppLog.error("CreateModuleContext failed, err code:${err.code}, err msg: ${err.message}")
                      }
                  })
              }.width(100.percent)
          }.height(100.percent)
      }
  }
  ```