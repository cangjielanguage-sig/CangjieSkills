## 场景介绍

键值型数据库存储键值对形式的数据，当需要存储的数据没有复杂的关系模型，比如存储商品名称及对应价格、员工工号及今日是否已出勤等，由于数据复杂度低，更容易兼容不同数据库版本和设备类型，因此推荐使用键值型数据库持久化此类数据。

## 约束限制

- 设备协同数据库，针对每条记录，Key的长度≤896 Byte，Value的长度&lt;4 MB。
- 单版本数据库，针对每条记录，Key的长度≤1 KB，Value的长度&lt;4 MB。
- 每个应用程序最多支持同时打开16个键值型分布式数据库。
- 键值型数据库事件回调方法中不允许进行阻塞操作，例如修改UI组件。

## 接口说明

以下是键值型数据库持久化功能的相关接口，大部分为异步接口。异步接口均有callback和Promise两种返回形式，下表均以callback形式为例，更多接口及使用方式请参见[分布式键值数据库](../../API_Reference/source_zh_cn/apis/ArkData/cj-apis-distributed_kv_store.md)。

| 接口名称 | 描述 |
| -------- | -------- |
| createKVManager(config: KVManagerConfig): KVManager | 创建一个KVManager对象实例，用于管理数据库对象。 |
| getSingleKVStore(storeId: String, options: KVOptions): SingleKVStore | 指定options和storeId，创建并获取单版本分布式键值数据库。 |
| getDeviceKVStore(storeId: String, options: KVOptions): DeviceKVStore | 指定Options和storeId，创建并获取多设备协同数据库。|
| put(key: String, value: KVValueType): Unit | 添加指定类型的键值对到数据库。 |
| get(key: String): KVValueType | 获取指定键的值。 |
| delete(key: String): Unit | 从数据库中删除指定键值的数据。 |
| closeKVStore(appId: String, storeId: String): Unit | 通过storeId的值关闭指定的分布式键值数据库。 |
| deleteKVStore(appId: String, storeId: String): Unit | 通过storeId的值删除指定的分布式键值数据库。 |