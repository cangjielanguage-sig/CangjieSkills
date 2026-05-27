例如在文档应用中，可以为不同的文档实例内容绑定不同的Key值。每次新建文档时，可以传入一个新的Key值（例如可以将文件的路径作为一个Key标识），此时[AbilityStage](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilitystage)中启动[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)时都会创建一个新的UIAbility实例；当新建的文档保存之后，回到桌面，或者新打开一个已保存的文档，回到桌面，此时再次打开该已保存的文档，此时AbilityStage中再次启动该UIAbility时，打开的仍然是之前原来已保存的文档界面。

    以如下步骤所示进行举例说明。

    1. 打开`文件A`，对应启动一个新的UIAbility实例，例如启动`UIAbility实例1`。
    2. 在最近任务列表中关闭`文件A`的任务进程，此时`UIAbility实例1`被销毁，回到桌面，再次打开`文件A`，此时对应启动一个新的UIAbility实例，例如启动`UIAbility实例2`。
    3. 回到桌面，打开`文件B`，此时对应启动一个新的UIAbility实例，例如启动`UIAbility实例3`。
    4. 回到桌面，再次打开`文件A`，此时仍然启动之前的`UIAbility实例2`，因为系统会自动匹配UIAbility实例的Key值，如果存在与之匹配的Key，则会启动与之绑定的UIAbility实例。在此例中，之前启动的`UIAbility实例2`与`文件A`绑定的Key是相同的，因此系统会拉回`UIAbility实例2`并让其获焦，而不会创建新的实例。