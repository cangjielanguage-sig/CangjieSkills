# UIAbility组件与UI的数据同步

基于当前的应用模型，可以通过以下几种方式来实现[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)组件与UI之间的数据同步。

- [使用EventHub进行数据通信](#使用eventhub进行数据通信)：在[基类Context](cj-application-context-stage.md)中提供了[EventHub](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-eventhub.md)对象，可以通过发布订阅方式来实现事件的传递。在事件传递前，订阅者需要先进行订阅，当发布者发布事件时，订阅者将接收到事件并进行相应处理。
- [使用AppStorage/LocalStorage进行数据同步](#使用appstoragelocalstorage进行数据同步)：ArkUI提供了[AppStorage](../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-appstatemanagement.md#class-appstorage)和[LocalStorage](../../API_Reference/source_zh_cn/arkui-cj/cj-state-rendering-appstatemanagement.md#class-localstorage)两种应用级别的状态管理方案，可用于实现应用级别和Ability级别的数据同步。