## 场景介绍

用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。当用户希望有一个全局唯一存储的地方，可以采用用户首选项来进行存储。Preferences会将该数据缓存在内存中。当用户读取时，能够快速从内存中获取数据。当需要持久化时，可以使用flush接口将内存中的数据写入持久化文件中。Preferences会随着存放的数据量越多而导致应用占用的内存越大。因此，Preferences不适合存放过多的数据，也不支持通过配置加密，适用的场景一般为应用保存用户的个性化设置（字体大小，是否开启夜间模式）等。

## 运作机制

如图所示，用户程序通过仓颉接口调用用户首选项读写对应的数据文件。开发者可以将用户首选项持久化文件的内容加载到Preferences实例，每个文件唯一对应到一个Preferences实例，系统会通过静态容器将该实例存储在内存中，直到主动从内存中移除该实例或者删除该文件。

应用首选项的持久化文件保存在应用沙箱内部，可以通过context获取其路径。具体请参见[获取应用文件路径](../application-models/cj-application-context-stage.md#获取应用文件路径)。

**图1** 用户首选项运作机制

![preferences](figures/preferences.png)

## 约束限制

- 首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。
- Key键为string类型，要求非空且长度不超过1024个字节。
- 如果Value值为string类型，请使用UTF-8编码格式，可以为空，不为空时长度不超过16MB。
- 当存储的数据中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。
- 当调用removePreferencesFromCache或者deletePreferences后，订阅的数据变更会主动取消订阅，重新getPreferences后需要重新订阅数据变更。
- 不允许deletePreferences与其他接口多线程、多进程并发调用，否则会发生不可预期行为。
- 内存会随着存储数据量的增大而增大，所以存储的数据量应该是轻量级的，建议存储的数据不超过一万条，否则会在内存方面产生较大的开销。

## 接口说明

以下是用户首选项持久化功能的相关接口，更多接口及使用方式请参见[用户首选项](../../API_Reference/source_zh_cn/apis/ArkData/cj-apis-preferences.md)。

| 接口名称                                             | 描述                                         |
| --------------------------------------------------- | ----------------------------------------------|
| getPreferences(context: StageContext, options: PreferencesOptions): Preferences | 获取Preferences实例。|
| put(key: String, value: PreferencesValueType): Unit   | 将数据写入Preferences实例，可通过flush将Preferences实例持久化。 |
| has(key: String): Bool  | 检查Preferences实例是否包含名为给定Key的存储键值对。给定的Key值不能为空。 |
| get(key: String, defValue: PreferencesValueType): PreferencesValueType   | 获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。 |
| delete(key: String): Unit  | 从Preferences实例中删除名为给定Key的存储键值对。 |
| flush(): Unit   | 将当前Preferences实例的数据异步存储到用户首选项持久化文件中。 |
| on(tp: String, callback: Callback1Argument\<String>): Unit | 订阅数据变更，订阅的数据发生变更后，在执行flush方法后，触发callback回调。 |
| off(tp: String, callback: Callback1Argument\<String>): Unit | 取消订阅数据变更。  |
| deletePreferences(context: StageContext, options: PreferencesOptions): Unit | 从内存中移除指定的Preferences实例。若Preferences实例有对应的持久化文件，则同时删除其持久化文件。 |