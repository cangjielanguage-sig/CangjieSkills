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

import std.collection.HashMap
import ohos.business_exception.BusinessException

const INVALID_PARA: Int32 = 401
const AAFWK_SERVICE_ERR_OFFSET: Int32 = 2097152
/**
 * Result(2097152) for StartAbility: An error of the Want could not be resolved
 * to ability info from BMS or DistributedMS.
 */
const RESOLVE_ABILITY_ERR: Int32 = AAFWK_SERVICE_ERR_OFFSET
/**
 * Result(2097159) for StartAbility: The ability to start is waiting.
 */
const START_ABILITY_WAITING: Int32 = 2097159
/**
 * Result(2097170) for ConnectAbility:target ability is not service ability.
 */
const TARGET_ABILITY_NOT_SERVICE: Int32 = 2097170
/**
 * Result(2097177) for check permission failed.
 */
const CHECK_PERMISSION_FAILED: Int32 = 2097177
/**
 * Result(2097179) for ability visible attribute is false.
 */
const ABILITY_VISIBLE_FALSE_DENY_REQUEST: Int32 = 2097179
/**
 * Result(2097182) for mission not found.
 */
const MISSION_NOT_FOUND: Int32 = 2097182
// for call ability

/**
 * Result(2097187) for resolve ability failed, target ability not page or singleton
 */
const RESOLVE_CALL_ABILITY_TYPE_ERR: Int32 = 2097187
/**
 * Result(2097199) for for implicit start ability is failed.
 */
const ERR_IMPLICIT_START_ABILITY_FAIL: Int32 = 2097199
/**
 * Result(2097202) for wrong interface call.
 */
const ERR_WRONG_INTERFACE_CALL: Int32 = 2097202
/**
 * Result(2097203) for crowdtest expired.
 */
const ERR_CROWDTEST_EXPIRED: Int32 = 2097203
/**
 * Result(2097204) for application abnormal.
 */
const ERR_APP_CONTROLLED: Int32 = 2097204
/**
 * Result(2097205) for invalid caller.
 */
const ERR_INVALID_CALLER: Int32 = 2097205
/**
 * Result(2097206) for not allowed continuation flag.
 */
const ERR_INVALID_CONTINUATION_FLAG: Int32 = 2097206
/**
 * Result(2097207) for not allowed to cross user.
 */
const ERR_CROSS_USER: Int32 = 2097207
/**
 * Result(2097208) for not granted for static permission.
 */
const ERR_STATIC_CFG_PERMISSION: Int32 = 2097208
/**
 * Result(2097209) for non-system-app use system-api.
 */
const ERR_NOT_SYSTEM_APP: Int32 = 2097209
/**
 * Result(2097212) for URI flag invalid.
 */
const ERR_CODE_INVALID_URI_FLAG: Int32 = 2097212
/**
 * Result(2097213) for URI type invalid.
 */
const ERR_CODE_INVALID_URI_TYPE: Int32 = 2097213
/**
 * Result(2097214) for start not self application.
 */
const ERR_NOT_SELF_APPLICATION: Int32 = 2097214
/**
 * Result(2097215) for edm application abnormal.
 */
const ERR_EDM_APP_CONTROLLED: Int32 = 2097215
/**
 * Result(2097216) for sandbox application grant URI permission.
 */
const ERR_CODE_GRANT_URI_PERMISSION: Int32 = 2097216
/**
 * Result(2097220) for starting invalid component.
 */
const ERR_INSIGHT_INTENT_START_INVALID_COMPONENT: Int32 = 2097220
/**
 * Result(2097224) for the target to restart does not belong to the current app or is not a UIAbility.
 */
const ERR_RESTART_APP_INCORRECT_ABILITY: Int32 = 2097224
/**
 * Result(2097225) for restart too frequently. Try again at least 3s later.
 */
const ERR_RESTART_APP_FREQUENT: Int32 = 2097225
/**
 * Result(2097227) for ability is not foreground state.
 */
const ERR_ABILITY_NOT_FOREGROUND: Int32 = 2097227
/**
 * Result(2097228) for in wukong mode, ability can not move to foreground or background.
 */
const ERR_WUKONG_MODE_CANT_MOVE_STATE: Int32 = 2097228
/**
 * Result(2097229) for operation not supported on current device.
 */
const ERR_OPERATION_NOT_SUPPORTED_ON_CURRENT_DEVICE: Int32 = 2097229
/**
 * Result(2097230) for capability not support.
 */
const ERR_CAPABILITY_NOT_SUPPORT: Int32 = 2097230
/**
 * Result(2097231) for not allow implicit start.
 */
const ERR_NOT_ALLOW_IMPLICIT_START: Int32 = 2097231
/**
 * Result(2097232) for start options check failed.
 */
const ERR_START_OPTIONS_CHECK_FAILED: Int32 = 2097232
/**
 * Result(2097233) for ability already running.
 */
const ERR_ABILITY_ALREADY_RUNNING: Int32 = 2097233
/**
 * Native error(2097239) for start other app failed.
 */
const ERR_START_OTHER_APP_FAILED: Int32 = 2097239
/**
 * Native error(2097241) for target bundle not exist.
 */
const ERR_TARGET_BUNDLE_NOT_EXIST: Int32 = 2097241

/**
 * Native error(2097249) no resident process permissions set.
 */
const ERR_NO_RESIDENT_PERMISSION: Int32 = 2097249
/**
 * Result(2097250) for app clone index does not exist.
 */
const ERR_APP_CLONE_INDEX_INVALID: Int32 = 2097250
/**
 * Result(2097251) not support twin.
 */
const ERR_MULTI_APP_NOT_SUPPORTED: Int32 = 2097251
/*
 * Result(2097254) for extension blocked by third party app flag
 */
const EXTENSION_BLOCKED_BY_THIRD_PARTY_APP_FLAG: Int32 = 2097254
/*
 * Result(2097255) for extension blocked by service list
 */
const EXTENSION_BLOCKED_BY_SERVICE_LIST: Int32 = 2097255
/**
 * Native error(2097258) for target bundle not exist.
 */
const ERR_BUNDLE_NOT_EXIST: Int32 = 2097258
/*
 * Result (2097260) for target free install task does not exist.
 */
const ERR_FREE_INSTALL_TASK_NOT_EXIST: Int32 = 2097260
/*
 * Result (2097262) caller not exists.
 */
const ERR_CALLER_NOT_EXISTS: Int32 = 2097262
/*
 * Result (2097263) Not support back to caller.
 */
const ERR_NOT_SUPPORT_BACK_TO_CALLER: Int32 = 2097263
/**
 * Result(2097271) not support multi-instance.
 */
const ERR_MULTI_INSTANCE_NOT_SUPPORTED: Int32 = 2097271
/*
 * Result (2097272) for not support app instance key.
 */
const ERR_APP_INSTANCE_KEY_NOT_SUPPORT: Int32 = 2097272
/*
 * Result (2097273) for reach the upper limit.
 */
const ERR_UPPER_LIMIT: Int32 = 2097273
/*
 * Result (2097274) for not support to create a new instance.
 */
const ERR_CREATE_NEW_INSTANCE_NOT_SUPPORT: Int32 = 2097274
/*
 * Result (2097275) for invalid app instance key.
 */
const ERR_INVALID_APP_INSTANCE_KEY: Int32 = 2097275
/*
 * Result (2097276) for not support app clone.
 */
const ERR_NOT_SUPPORT_APP_CLONE: Int32 = 2097276
/*
 * Result (2097279) for get target bundle info failed.
 */
const ERR_GET_TARGET_BUNDLE_INFO_FAILED: Int32 = 2097279
/*
 * Result (2097280) for UIAbility in starting state.
 */
const ERR_UI_ABILITY_IS_STARTING: Int32 = 2097280
/**
 * FA distribution center processing timeout(30s).
 */
const FA_TIMEOUT: Int32 = 0x820103
/**
 * HAP package download timed out.
 */
const HAP_PACKAGE_DOWNLOAD_TIMED_OUT: Int32 = -9
/**
 * There are concurrent tasks, waiting for retry.
 */
const CONCURRENT_TASKS_WAITING_FOR_RETRY: Int32 = -6
/**
 * FA package does not support free installation.
 */
const FA_PACKAGE_DOES_NOT_SUPPORT_FREE_INSTALL: Int32 = -10
/**
 * The app is not allowed to pull this FA.
 */
const NOT_ALLOWED_TO_PULL_THIS_FA: Int32 = -901
/**
 * Not support cross-device free install PA
 */
const NOT_SUPPORT_CROSS_DEVICE_FREE_INSTALL_PA: Int32 = -12
/**
 * Free install timeout
 */
const FREE_INSTALL_TIMEOUT: Int32 = 29360300
/**
 * Not top ability
 */
const NOT_TOP_ABILITY: Int32 = 0x500001
/**
 * Target bundle name is not exist in targetBundleList.
 */
const TARGET_BUNDLE_NOT_EXIST: Int32 = 0x500002
/**
 * Permission denied.
 */
const DMS_PERMISSION_DENIED: Int32 = 29360157
/**
 * Result(29360176) for component access permission check failed.
 */
const DMS_COMPONENT_ACCESS_PERMISSION_DENIED: Int32 = 29360176
/**
 * Result(29360175) for account access permission check failed.
 */
const DMS_ACCOUNT_ACCESS_PERMISSION_DENIED: Int32 = 29360175
/**
 * Native error(29360135) for target bundle has no main ability.
 */
const ERR_NO_MAIN_ABILITY: Int32 = 29360135
/**
 * Native error(29360136) for target app has no status-bar ability.
 */
const ERR_NO_STATUS_BAR_ABILITY: Int32 = 29360136
/**
 * Native error(29360137) for target app is not attached to a status bar.
 */
const ERR_NOT_ATTACHED_TO_STATUS_BAR: Int32 = 29360137
// no such permission.
const ERROR_CODE_PERMISSION_DENIED: Int32 = 201
// non-system-app use system-api.
const ERROR_CODE_NOT_SYSTEM_APP: Int32 = 202
// capability not support.
const ERROR_CODE_CAPABILITY_NOT_SUPPORT: Int32 = 801
// common inner error.
const ERROR_CODE_INNER: Int32 = 16000050
// can not find target ability.
const ERROR_CODE_RESOLVE_ABILITY: Int32 = 16000001
// ability type is wrong.
const ERROR_CODE_INVALID_ABILITY_TYPE: Int32 = 16000002
// id does not exist.
const ERROR_CODE_INVALID_ID: Int32 = 16000003
// no start invisible ability permission.
const ERROR_CODE_NO_INVISIBLE_PERMISSION: Int32 = 16000004
// check static permission failed.
const ERROR_CODE_STATIC_CFG_PERMISSION: Int32 = 16000005
// no permission to cross user.
const ERROR_CODE_CROSS_USER: Int32 = 16000006
// crowdtest app expiration.
const ERROR_CODE_CROWDTEST_EXPIRED: Int32 = 16000008
// not allowed for continuation flag.
const ERROR_CODE_CONTINUATION_FLAG: Int32 = 16000010
// context is invalid.
const ERROR_CODE_INVALID_CONTEXT: Int32 = 16000011
// application is controlled.
const ERROR_CODE_CONTROLLED: Int32 = 16000012
// edm application is controlled.
const ERROR_CODE_EDM_CONTROLLED: Int32 = 16000013
// ability wait start.
const ERROR_START_ABILITY_WAITTING: Int32 = 16000017
// jump to other applicaiton is not enable.
const ERROR_CODE_NOT_SUPPORT_CROSS_APP_START: Int32 = 16000018
// implicit start can not match any component.
const ERROR_CODE_CANNOT_MATCH_ANY_COMPONENT: Int32 = 16000019
// free install network abnormal.
const ERROR_CODE_NETWORK_ABNORMAL: Int32 = 16000051
// not support free install.
const ERROR_CODE_NOT_SUPPORT_FREE_INSTALL: Int32 = 16000052
// not top ability, not enable to free install.
const ERROR_CODE_NOT_TOP_ABILITY: Int32 = 16000053
// too busy for free install.
const ERROR_CODE_FREE_INSTALL_TOO_BUSY: Int32 = 16000054
// free install timeout.
const ERROR_CODE_FREE_INSTALL_TIMEOUT: Int32 = 16000055
// free install other ability.
const ERROR_CODE_FREE_INSTALL_OTHERS: Int32 = 16000056
// Cross-device installation-free is not supported.
const ERROR_CODE_FREE_INSTALL_CROSS_DEVICE: Int32 = 16000057
// Uri flag invalid.
const ERROR_CODE_INVALID_URI_FLAG: Int32 = 16000058
// Uri type invalid, only support file uri currently.
const ERROR_CODE_INVALID_URI_TYPE: Int32 = 16000059
// Sandbox application can not grant URI permission.
const ERROR_CODE_GRANT_URI_PERMISSION: Int32 = 16000060
// Operation not supported.
const ERROR_CODE_OPERATION_NOT_SUPPORTED: Int32 = 16000061
// The target to restart does not belong to the current app or is not a UIAbility.
const ERROR_CODE_RESTART_APP_INCORRECT_ABILITY: Int32 = 16000063
// Restart too frequently. Try again at least 3s later.
const ERROR_CODE_RESTART_APP_FREQUENT: Int32 = 16000064
// ability not foreground.
const ERROR_CODE_ABILITY_NOT_FOREGROUND: Int32 = 16000065
// wukong mode, can not move to foreground or background.
const ERROR_CODE_WUKONG_MODE_CANT_MOVE_STATE: Int32 = 16000066
// Start options check failed.
const ERROR_START_OPTIONS_CHECK_FAILED: Int32 = 16000067
// Ability already running.
const ERROR_ABILITY_ALREADY_RUNNING: Int32 = 16000068
// extension start third party app has been controlled.
const ERROR_CODE_EXTENSION_START_THIRD_PARTY_APP_CONTROLLED: Int32 = 16000069
// extension start service has been controlled.
const ERROR_CODE_EXTENSION_START_SERVICE_CONTROLLED: Int32 = 16000070
// app is not Clone.
const ERROR_NOT_APP_CLONE: Int32 = 16000071
// not support Clone app.
const ERROR_CODE_MULTI_APP_NOT_SUPPORTED: Int32 = 16000072
// app clone index does not exist.
const ERROR_APP_CLONE_INDEX_INVALID: Int32 = 16000073
// Caller does not exists.
const ERROR_CODE_CALLER_NOT_EXIST: Int32 = 16000074
// Not support back to caller.
const ERROR_CODE_NOT_SUPPROT_BACK_TO_CALLER: Int32 = 16000075
// invalid app instance key.
const ERROR_CODE_INVALID_APP_INSTANCE_KEY: Int32 = 16000076
// upper limit.
const ERROR_CODE_UPPER_LIMIT: Int32 = 16000077
// The multi-instance is not supported.
const ERROR_MULTI_INSTANCE_NOT_SUPPORTED: Int32 = 16000078
// APP_INSTANCE_KEY cannot be specified.
const ERROR_CODE_APP_INSTANCE_KEY_NOT_SUPPORT: Int32 = 16000079
// Not support to create a new instance.
const ERROR_CODE_CREATE_NEW_INSTANCE_NOT_SUPPORT: Int32 = 16000080
// Target application not found.
const ERROR_CODE_GET_BUNFLE_INFO_FAILED: Int32 = 16000081
// UIAbility is in starting state.
const ERROR_CODE_UI_ABILITY_IS_STARTING: Int32 = 16000082
// invalid caller.
const ERROR_CODE_INVALID_CALLER: Int32 = 16200001
const ERROR_CODE_FUNC_REGISTERED: Int32 = 16200004
const ERROR_CODE_FUNC_NOT_EXIST: Int32 = 16200005
// Setting permissions for resident processes
const ERROR_CODE_NO_RESIDENT_PERMISSION: Int32 = 16200006
// no such mission id.
const ERROR_CODE_NO_MISSION_ID: Int32 = 16300001
// not self application.
const ERROR_NOT_SELF_APPLICATION: Int32 = 16300003
// target bundle not exist.
const ERROR_CODE_TARGET_BUNDLE_NOT_EXIST: Int32 = 16300005
// target free install task does not exist.
const ERROR_CODE_FREE_INSTALL_TASK_NOT_EXIST: Int32 = 16300007
// target bundle has no main ability.
const ERROR_CODE_NO_MAIN_ABILITY: Int32 = 16300008
// target application has no status-bar ability.
const ERROR_CODE_NO_STATUS_BAR_ABILITY: Int32 = 16300009
// target application is not attached to a status bar.
const ERROR_CODE_NOT_ATTACHED_TO_STATUS_BAR: Int32 = 16300010
const ERROR_CODE_BUNDLE_NAME_INVALID: Int32 = 18500001
// follow ERR_BUNDLE_MANAGER_BUNDLE_NOT_EXIST in bundle_framework
const ERR_BUNDLE_MANAGER_BUNDLE_NOT_EXIST: Int32 = 8521220
let INNER_TO_CJ_ERROR_CODE_MAP = HashMap<Int32, Int32>(
    [
        (CHECK_PERMISSION_FAILED, ERROR_CODE_PERMISSION_DENIED),
        (ERR_NOT_SYSTEM_APP, ERROR_CODE_NOT_SYSTEM_APP),
        (RESOLVE_ABILITY_ERR, ERROR_CODE_RESOLVE_ABILITY),
        (ERR_WRONG_INTERFACE_CALL, ERROR_CODE_INVALID_ABILITY_TYPE),
        (TARGET_ABILITY_NOT_SERVICE, ERROR_CODE_INVALID_ABILITY_TYPE),
        (RESOLVE_CALL_ABILITY_TYPE_ERR, ERROR_CODE_INVALID_ABILITY_TYPE),
        (ABILITY_VISIBLE_FALSE_DENY_REQUEST, ERROR_CODE_NO_INVISIBLE_PERMISSION),
        (ERR_STATIC_CFG_PERMISSION, ERROR_CODE_STATIC_CFG_PERMISSION),
        (ERR_CROSS_USER, ERROR_CODE_CROSS_USER),
        (ERR_CROWDTEST_EXPIRED, ERROR_CODE_CROWDTEST_EXPIRED),
        (ERR_INVALID_CONTINUATION_FLAG, ERROR_CODE_CONTINUATION_FLAG),
        (ERR_INVALID_CALLER, ERROR_CODE_INVALID_CALLER),
        (ERR_CODE_INVALID_URI_FLAG, ERROR_CODE_INVALID_URI_FLAG),
        (ERR_CODE_INVALID_URI_TYPE, ERROR_CODE_INVALID_URI_TYPE),
        (ERR_CODE_GRANT_URI_PERMISSION, ERROR_CODE_GRANT_URI_PERMISSION),
        (ERR_GET_TARGET_BUNDLE_INFO_FAILED, ERROR_CODE_GET_BUNFLE_INFO_FAILED),
        (ERR_NOT_SELF_APPLICATION, ERROR_NOT_SELF_APPLICATION),
        // Installation-free error code transfer
        (HAP_PACKAGE_DOWNLOAD_TIMED_OUT, ERROR_CODE_NETWORK_ABNORMAL),
        (FA_PACKAGE_DOES_NOT_SUPPORT_FREE_INSTALL, ERROR_CODE_NOT_SUPPORT_FREE_INSTALL),
        (NOT_TOP_ABILITY, ERROR_CODE_NOT_TOP_ABILITY),
        (CONCURRENT_TASKS_WAITING_FOR_RETRY, ERROR_CODE_FREE_INSTALL_TOO_BUSY),
        (FREE_INSTALL_TIMEOUT, ERROR_CODE_FREE_INSTALL_TIMEOUT),
        (NOT_ALLOWED_TO_PULL_THIS_FA, ERROR_CODE_FREE_INSTALL_OTHERS),
        (MISSION_NOT_FOUND, ERROR_CODE_NO_MISSION_ID),
        (FA_TIMEOUT, ERROR_CODE_FREE_INSTALL_TIMEOUT),
        (NOT_SUPPORT_CROSS_DEVICE_FREE_INSTALL_PA, ERROR_CODE_FREE_INSTALL_CROSS_DEVICE),
        (TARGET_BUNDLE_NOT_EXIST, ERROR_CODE_RESOLVE_ABILITY),
        (DMS_PERMISSION_DENIED, ERROR_CODE_PERMISSION_DENIED),
        (DMS_COMPONENT_ACCESS_PERMISSION_DENIED, ERROR_CODE_PERMISSION_DENIED),
        (DMS_ACCOUNT_ACCESS_PERMISSION_DENIED, ERROR_CODE_PERMISSION_DENIED),
        (START_ABILITY_WAITING, ERROR_START_ABILITY_WAITTING),
        (ERR_APP_CONTROLLED, ERROR_CODE_CONTROLLED),
        (ERR_EDM_APP_CONTROLLED, ERROR_CODE_EDM_CONTROLLED),
        (ERR_INSIGHT_INTENT_START_INVALID_COMPONENT, ERROR_CODE_OPERATION_NOT_SUPPORTED),
        (ERR_RESTART_APP_INCORRECT_ABILITY, ERROR_CODE_RESTART_APP_INCORRECT_ABILITY),
        (ERR_RESTART_APP_FREQUENT, ERROR_CODE_RESTART_APP_FREQUENT),
        (ERR_CAPABILITY_NOT_SUPPORT, ERROR_CODE_CAPABILITY_NOT_SUPPORT),
        (ERR_NOT_ALLOW_IMPLICIT_START, ERROR_CODE_RESOLVE_ABILITY),
        (ERR_START_OPTIONS_CHECK_FAILED, ERROR_START_OPTIONS_CHECK_FAILED),
        (ERR_ABILITY_ALREADY_RUNNING, ERROR_ABILITY_ALREADY_RUNNING),
        (ERR_ABILITY_NOT_FOREGROUND, ERROR_CODE_ABILITY_NOT_FOREGROUND),
        (ERR_WUKONG_MODE_CANT_MOVE_STATE, ERROR_CODE_WUKONG_MODE_CANT_MOVE_STATE),
        (ERR_OPERATION_NOT_SUPPORTED_ON_CURRENT_DEVICE, ERROR_CODE_OPERATION_NOT_SUPPORTED),
        (ERR_IMPLICIT_START_ABILITY_FAIL, ERROR_CODE_CANNOT_MATCH_ANY_COMPONENT),
        (ERR_BUNDLE_MANAGER_BUNDLE_NOT_EXIST, ERROR_CODE_INVALID_ID),
        (ERR_START_OTHER_APP_FAILED, ERROR_CODE_NOT_SUPPORT_CROSS_APP_START),
        (ERR_TARGET_BUNDLE_NOT_EXIST, ERROR_CODE_TARGET_BUNDLE_NOT_EXIST),
        (ERR_NO_MAIN_ABILITY, ERROR_CODE_NO_MAIN_ABILITY),
        (ERR_NO_STATUS_BAR_ABILITY, ERROR_CODE_NO_STATUS_BAR_ABILITY),
        (ERR_NOT_ATTACHED_TO_STATUS_BAR, ERROR_CODE_NOT_ATTACHED_TO_STATUS_BAR),
        (ERR_NO_RESIDENT_PERMISSION, ERROR_CODE_NO_RESIDENT_PERMISSION),
        (ERR_MULTI_APP_NOT_SUPPORTED, ERROR_CODE_MULTI_APP_NOT_SUPPORTED),
        (ERR_APP_CLONE_INDEX_INVALID, ERROR_APP_CLONE_INDEX_INVALID),
        (ERR_CALLER_NOT_EXISTS, ERROR_CODE_CALLER_NOT_EXIST),
        (ERR_NOT_SUPPORT_BACK_TO_CALLER, ERROR_CODE_NOT_SUPPROT_BACK_TO_CALLER),
        (EXTENSION_BLOCKED_BY_THIRD_PARTY_APP_FLAG, ERROR_CODE_EXTENSION_START_THIRD_PARTY_APP_CONTROLLED),
        (EXTENSION_BLOCKED_BY_SERVICE_LIST, ERROR_CODE_EXTENSION_START_SERVICE_CONTROLLED),
        (ERR_BUNDLE_NOT_EXIST, ERROR_CODE_BUNDLE_NAME_INVALID),
        (ERR_FREE_INSTALL_TASK_NOT_EXIST, ERROR_CODE_FREE_INSTALL_TASK_NOT_EXIST),
        (ERR_MULTI_INSTANCE_NOT_SUPPORTED, ERROR_MULTI_INSTANCE_NOT_SUPPORTED),
        (ERR_NOT_SUPPORT_APP_CLONE, ERROR_NOT_APP_CLONE),
        (ERR_INVALID_APP_INSTANCE_KEY, ERROR_CODE_INVALID_APP_INSTANCE_KEY),
        (ERR_UPPER_LIMIT, ERROR_CODE_UPPER_LIMIT),
        (ERR_APP_INSTANCE_KEY_NOT_SUPPORT, ERROR_CODE_APP_INSTANCE_KEY_NOT_SUPPORT),
        (ERR_CREATE_NEW_INSTANCE_NOT_SUPPORT, ERROR_CODE_CREATE_NEW_INSTANCE_NOT_SUPPORT),
        (ERR_UI_ABILITY_IS_STARTING, ERROR_CODE_UI_ABILITY_IS_STARTING)
    ]
)
let ERROR_MSG_MAP = HashMap<Int32, String>(
    [
        (16000001, "The specified ability does not exist."),
        (16000002, "Incorrect Ability type."),
        (16000003, "The specified ID does not exist."),
        (16000004, "Failed to start the invisible ability."),
        (16000005, "The specified process does not have the permission."),
        (16000006, "Cross-user operations are not allowed."),
        (16000007, "Service busy, there are concurrent tasks, waiting for retry."),
        (16000008, "The crowdtesting application expires."),
        (16000009, "An ability cannot be started or stopped in Wukong mode."),
        (16000010, "The call with the continuation flag is forbidden."),
        (ERROR_CODE_INVALID_CONTEXT, "The context does not exist."),
        (16000012, "The application is controlled."),
        (16000013, "The application is controlled by EDM."),
        (16000015, "Service timeout."),
        (16000017, "Another ability is being started. Wait until it finishes starting."),
        (16000018, "Redirection to a third-party application is not allowed in API version 11 or later."),
        (16000019, "No matching ability is found."),
        (ERROR_CODE_INNER, "Internal error."),
        (16000051, "Network error."),
        (16000052, "Installation-free is not supported."),
        (16000053, "The ability is not on the top of the UI."),
        (16000054, "The installation-free service is busy. Try again later."),
        (16000055, "Installation-free timed out."),
        (16000056, "Installation-free is not allowed for other applications."),
        (16000057, "Cross-device installation-free is not supported."),
        (16000058, "Invalid URI flag."),
        (16000059, "Invalid URI type."),
        (16000060, "A sandbox application cannot grant URI permission."),
        (16000061, "Operation not supported."),
        (16000062, "The number of child processes exceeds the upper limit."),
        (16000063, "The target to restart does not belong to the current application or is not a UIAbility."),
        (16000064, "Restart too frequently. Try again at least 3s later."),
        (16000065, "The API can be called only when the ability is running in the foreground."),
        (16000066, "An ability cannot switch to the foreground or background in Wukong mode."),
        (16000067, "The StartOptions check failed."),
        (16000068, "The ability is already running."),
        (16000069, "The extension cannot start the third party application."),
        (16000070, "The extension cannot start the service."),
        (16000071, "App clone is not supported."),
        (16000072, "App clone or multi-instance is not supported."),
        (16000073, "The app clone index is invalid."),
        (16000074, "The caller does not exist."),
        (16000075, "Not support back to caller."),
        (16000076, "The APP_INSTANCE_KEY is invalid."),
        (16000077, "The number of app instances reaches the limit."),
        (16000078, "The multi-instance is not supported."),
        (16000079, "The APP_INSTANCE_KEY cannot be specified."),
        (16000080, "Creating an instance is not supported."),
        (16000081, "Get target application info failed."),
        (16000082, "The UIAbility is being started."),
        (16000100, "Calling AddAbilityMonitor failed."),
        (16000101, "Failed to run the shell command."),
        (16000151, "Invalid wantAgent object."),
        (16000152, "The wantAgent object does not exist."),
        (16000153, "The wantAgent object has been canceled."),
        (16100001, "The ability with the specified URI does not exist."),
        (16100002, "Incorrect ability type."),
        (16200001, "The caller has been released."),
        (16200002, "The callee does not exist."),
        (16200003, "Release error. The caller does not call any callee."),
        (16200004, "The method has been registered."),
        (16200005, "The method has not been registered."),
        (16200006, "The caller application can only set the resident status of the configured process."),
        (16300001, "Mission not found."),
        (16300002, "The specified mission listener does not exist."),
        (16300003, "The target application is not the current application."),
        (18500001, "The bundle does not exist or no patch has been applied."),
        (18500002, "Invalid patch package."),
        (18500003, "Failed to deploy the patch."),
        (18500004, "Failed to enable the patch package."),
        (18500005, "Failed to remove the patch package."),
        (18500006, "Failed to load the patch."),
        (18500007, "Failed to unload the patch."),
        (18500008, "Internal error."),
        (18500009, "The application has an ongoing quick fix task."),
        (16300004, "observer not found."),
        (16300005, "The target bundle does not exist."),
        (16300008, "The target bundle has no main uiability."),
        (16300009, "The target bundle has no status-bar ability."),
        (16300010, "The target application is not attached to status bar."),
        (29600001, "Internal error."),
        (29600002, "Image input error."),
        (29600003, "Image too big."),
        (16300007, "The target free install task does not exist."),
        (201, "Permission verification failed, usually the result returned by VerifyAccessToken."),
        (202, "Permission verification failed, application which is not a system application uses system API."),
        (INVALID_PARA, "Parameter error."),
        (801, "Capability not supported.")
    ]
)

func innerToErrorCode(code: Int32): Int32 {
    match (INNER_TO_CJ_ERROR_CODE_MAP.get(code)) {
        case Some(v) => v
        case None => code
    }
}

func getErrorMsg(code: Int32): String {
    match (ERROR_MSG_MAP.get(code)) {
        case Some(v) => v
        case None => "Unknown error. Error code is ${code}"
    }
}

func checkCodeAndThrow(code: Int32): Unit {
    if (code != 0) {
        let errorCode = innerToErrorCode(code)
        throw BusinessException(errorCode, getErrorMsg(errorCode))
    }
}
