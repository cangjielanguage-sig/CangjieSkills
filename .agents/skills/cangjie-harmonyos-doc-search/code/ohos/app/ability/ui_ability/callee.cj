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

package ohos.app.ability.ui_ability

import ohos.rpc.RemoteObject

const EVENT_CALL_NOTIFY: UInt32 = 1
const REQUEST_SUCCESS: Int32 = 0
const PERMISSION_ABILITY_BACKGROUND_COMMUNICATION = 'ohos.permission.ABILITY_BACKGROUND_COMMUNICATION'

foreign func FfiOHOSAbilityAccessCtrlCheckAccessTokenSync(tokenID: UInt32, cPermissionName: CString): Int32

class Callee <: RemoteObject {
    init() {
        super("rpc.application.callee")
    }
}
