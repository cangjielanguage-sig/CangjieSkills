/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// The Cangjie API is in Beta. For details on its capabilities and limitations, please refer to the README file.

package ohos.app.ability.configuration

import ohos.labels.Hide

@C
protected struct CConfiguration {
    protected CConfiguration(
        var language: CString,
        var colorMode: Int32,
        var direction: Int32,
        var screenDensity: Int32,
        var displayId: Int32,
        var hasPointerDevice: Bool,
        var fontSizeScale: Float64,
        var fontWeightScale: Float64,
        var mcc: CString,
        var mnc: CString
    ) {}

    protected init() {
        language = CString(CPointer())
        colorMode = 0
        direction = 0
        screenDensity = 0
        displayId = 0
        hasPointerDevice = false
        fontSizeScale = 0.0
        fontWeightScale = 0.0
        mcc = CString(CPointer())
        mnc = CString(CPointer())
    }

    protected unsafe func free(): Unit {
        LibC.free(language)
        LibC.free(mcc)
        LibC.free(mnc)
    }
}

@C
protected struct CJConfiguration {
    protected CJConfiguration(
        let isValid: Bool,
        let language: CString,
        let colorMode: Int32,
        let direction: Int32,
        let screenDensity: Int32,
        let displayId: Int32
    ) {}
}

@!Hide[isChecked: true]
protected class Configuration {
    protected init() {}
}