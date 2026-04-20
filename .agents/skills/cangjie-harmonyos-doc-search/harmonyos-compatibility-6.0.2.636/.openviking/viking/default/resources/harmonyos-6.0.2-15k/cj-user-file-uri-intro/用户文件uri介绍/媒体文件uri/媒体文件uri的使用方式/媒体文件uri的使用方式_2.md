func uriGetAssets() {
    let phAccessHelper = getPhotoAccessHelper(context)
    let predicates: DataSharePredicates = DataSharePredicates()
    // 配置查询条件，使用PhotoViewPicker选择图片返回的uri进行查询
    predicates.equalTo("uri", VBValueType.Str(uris.value[0]))
    let fetchOption = FetchOptions(
        fetchColumns: [PhotoKeys.WIDTH.toString(), PhotoKeys.HEIGHT.toString(), PhotoKeys.TITLE.toString(),
            PhotoKeys.DURATION.toString()],
        predicates: predicates
    )
    let fetchResult: FetchResult<PhotoAsset> = phAccessHelper.getAssets(fetchOption)
    // 得到uri对应的PhotoAsset对象，读取文件的部分信息
    let asset: PhotoAsset = fetchResult.getFirstObject()
    AppLog.info('asset displayName: ${asset.displayName}')
    AppLog.info('asset uri: ${asset.uri}')
    AppLog.info('asset photoType: ${asset.photoType}')
    AppLog.info('asset width: ${asset.get(PhotoKeys.WIDTH.toString()).toString()}')
    AppLog.info('asset height: ${asset.get(PhotoKeys.HEIGHT.toString()).toString()}')
    AppLog.info('asset title: ${asset.get(PhotoKeys.TITLE.toString()).toString()}')
    // 获取缩略图
    let pixelMap = asset.getThumbnail()
}

extend MemberType {
    func toString() {
        match (this) {
            case INT64(v) => "${v}"
            case STRING(v) => "${v}"
            case BOOL(v) => "${v}"
            case _ => ""
        }
    }
}
```