# Changelog

## 0.6.0 (2025-04-14)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/atla-ai/atla-sdk-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([d36b35f](https://github.com/atla-ai/atla-sdk-python/commit/d36b35f1dc198ae41c2a5c741976aa5b105b93be))
* **api:** api update ([bc2fee5](https://github.com/atla-ai/atla-sdk-python/commit/bc2fee50961317625e0801641dcd1762887995ae))
* **api:** api update ([3437472](https://github.com/atla-ai/atla-sdk-python/commit/3437472ae5ce073ba03ac9bc4cabb36f3297b613))


### Bug Fixes

* **perf:** optimize some hot paths ([5aa8b57](https://github.com/atla-ai/atla-sdk-python/commit/5aa8b57e1269fa922d7a90a2726894260ad6014d))
* **perf:** skip traversing types for NotGiven values ([1e145ff](https://github.com/atla-ai/atla-sdk-python/commit/1e145ffe222c82df9f0fd5bec1574655bfd4fc3f))


### Chores

* fix typos ([#132](https://github.com/atla-ai/atla-sdk-python/issues/132)) ([3979281](https://github.com/atla-ai/atla-sdk-python/commit/39792812e510be336d6d74f31a281cd1acb553a2))
* **internal:** expand CI branch coverage ([01ff614](https://github.com/atla-ai/atla-sdk-python/commit/01ff6144b55bf27bc0c14c23d01e66d982003b12))
* **internal:** reduce CI branch coverage ([04351c0](https://github.com/atla-ai/atla-sdk-python/commit/04351c006008368d6e45c860ca7908948727f3eb))
* **internal:** remove trailing character ([#133](https://github.com/atla-ai/atla-sdk-python/issues/133)) ([d361d1a](https://github.com/atla-ai/atla-sdk-python/commit/d361d1a47095eb3e3f7c81477718d4ecaa70f088))
* **internal:** slight transform perf improvement ([#134](https://github.com/atla-ai/atla-sdk-python/issues/134)) ([ff95726](https://github.com/atla-ai/atla-sdk-python/commit/ff9572643717f2513877d78a3c6ed48c44314b52))

## 0.5.0 (2025-03-24)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/atla-ai/atla-sdk-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([#129](https://github.com/atla-ai/atla-sdk-python/issues/129)) ([47886f5](https://github.com/atla-ai/atla-sdk-python/commit/47886f567eb23d7ef4e4668a0b4b19f29b97d34b))
* **client:** allow passing `NotGiven` for body ([#115](https://github.com/atla-ai/atla-sdk-python/issues/115)) ([42b0301](https://github.com/atla-ai/atla-sdk-python/commit/42b0301bab95732525434c2233abf09f75f1ecc0))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#113](https://github.com/atla-ai/atla-sdk-python/issues/113)) ([e8a8b0d](https://github.com/atla-ai/atla-sdk-python/commit/e8a8b0dfddea06bf732a18510efb275d9828a4cd))
* **ci:** ensure pip is always available ([#127](https://github.com/atla-ai/atla-sdk-python/issues/127)) ([d4a29bb](https://github.com/atla-ai/atla-sdk-python/commit/d4a29bb03a0d77d2714cf76c355c35030fdf6e10))
* **ci:** remove publishing patch ([#128](https://github.com/atla-ai/atla-sdk-python/issues/128)) ([fd583e8](https://github.com/atla-ai/atla-sdk-python/commit/fd583e8a85b0df636221b5a966ef1ea52a94bbcb))
* **client:** mark some request bodies as optional ([42b0301](https://github.com/atla-ai/atla-sdk-python/commit/42b0301bab95732525434c2233abf09f75f1ecc0))
* **types:** handle more discriminated union shapes ([#126](https://github.com/atla-ai/atla-sdk-python/issues/126)) ([09dc7cc](https://github.com/atla-ai/atla-sdk-python/commit/09dc7cc0d4df84559e763ce6ee7fa9b40c72c5d2))


### Chores

* **docs:** update client docstring ([#120](https://github.com/atla-ai/atla-sdk-python/issues/120)) ([c68ffad](https://github.com/atla-ai/atla-sdk-python/commit/c68ffadd49615f5fd400b4ccfd85eab5ea77494f))
* **internal:** bump rye to 0.44.0 ([#125](https://github.com/atla-ai/atla-sdk-python/issues/125)) ([d599e2d](https://github.com/atla-ai/atla-sdk-python/commit/d599e2d4c95cd873968ecba553d442ce7d538480))
* **internal:** codegen related update ([#124](https://github.com/atla-ai/atla-sdk-python/issues/124)) ([9b02ee6](https://github.com/atla-ai/atla-sdk-python/commit/9b02ee6626795e824d95be2862d8eb56d864c2d9))
* **internal:** fix devcontainers setup ([#116](https://github.com/atla-ai/atla-sdk-python/issues/116)) ([ace8fbc](https://github.com/atla-ai/atla-sdk-python/commit/ace8fbc98af22e073f3ba1c17cd1085c28c30001))
* **internal:** properly set __pydantic_private__ ([#118](https://github.com/atla-ai/atla-sdk-python/issues/118)) ([e3bf33d](https://github.com/atla-ai/atla-sdk-python/commit/e3bf33d82de7bf00668e3a4d58806ab2053136d3))
* **internal:** remove extra empty newlines ([#123](https://github.com/atla-ai/atla-sdk-python/issues/123)) ([f15108d](https://github.com/atla-ai/atla-sdk-python/commit/f15108da001b20d22508106010a9c42bc1b5f0c8))
* **internal:** remove unused http client options forwarding ([#121](https://github.com/atla-ai/atla-sdk-python/issues/121)) ([ef050d0](https://github.com/atla-ai/atla-sdk-python/commit/ef050d0299db92fa7a322325d0e60b4ad687f260))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#119](https://github.com/atla-ai/atla-sdk-python/issues/119)) ([525d208](https://github.com/atla-ai/atla-sdk-python/commit/525d208598a477330996c1b34694b855a3f4d7bc))

## 0.4.0 (2025-02-13)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/atla-ai/atla-sdk-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([#107](https://github.com/atla-ai/atla-sdk-python/issues/107)) ([7c549a7](https://github.com/atla-ai/atla-sdk-python/commit/7c549a7a72f1afa44de89fdf2e0c1d7eec094335))
* **api:** api update ([#109](https://github.com/atla-ai/atla-sdk-python/issues/109)) ([2cf5286](https://github.com/atla-ai/atla-sdk-python/commit/2cf52860d2087b00f1d1edb306292c7970133722))
* **api:** api update ([#110](https://github.com/atla-ai/atla-sdk-python/issues/110)) ([5e4a76c](https://github.com/atla-ai/atla-sdk-python/commit/5e4a76c147a71f25c81b87c382d5cc6596d71b58))
* **api:** update via SDK Studio ([#101](https://github.com/atla-ai/atla-sdk-python/issues/101)) ([4c91ac0](https://github.com/atla-ai/atla-sdk-python/commit/4c91ac0c9721aebf0d7fb532f5fd79ef834729c8))


### Chores

* **internal:** codegen related update ([#104](https://github.com/atla-ai/atla-sdk-python/issues/104)) ([0d2ae0c](https://github.com/atla-ai/atla-sdk-python/commit/0d2ae0cc5f606f449691acdf1b3bc82fbc88c1a8))
* **internal:** update client tests ([#111](https://github.com/atla-ai/atla-sdk-python/issues/111)) ([2a4ef2b](https://github.com/atla-ai/atla-sdk-python/commit/2a4ef2b89a6803601b35042535a96c37c805b79a))
* remove custom code ([f5af251](https://github.com/atla-ai/atla-sdk-python/commit/f5af251e2ddadeda7e423cfa88219ac772645389))

## 0.3.0 (2024-06-12)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/atla-ai/atla-sdk-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** update via SDK Studio ([#82](https://github.com/atla-ai/atla-sdk-python/issues/82)) ([6b96dfa](https://github.com/atla-ai/atla-sdk-python/commit/6b96dfa591433d54d3c3aec24218f280a3f3d196))
* **api:** update via SDK Studio ([#84](https://github.com/atla-ai/atla-sdk-python/issues/84)) ([a1a70ce](https://github.com/atla-ai/atla-sdk-python/commit/a1a70ce32f06295e525e5ce6ae176a4849aa70ae))

## 0.2.0 (2024-05-30)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.1...v0.2.0)

### Features

* **api:** update via SDK Studio ([#79](https://github.com/atla-ai/atla-sdk-python/issues/79)) ([3870c36](https://github.com/atla-ai/atla-sdk-python/commit/3870c3677f3b403cfdd63741f57722d5a4f9baf3))

## 0.1.1 (2024-05-29)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.0...v0.1.1)

### Chores

* **internal:** version bump ([#58](https://github.com/atla-ai/atla-sdk-python/issues/58)) ([1c17782](https://github.com/atla-ai/atla-sdk-python/commit/1c1778288406160d685f4955f96ca6558e76f777))

## 0.1.0 (2024-05-29)

Full Changelog: [v0.1.0-alpha.7...v0.1.0](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.0-alpha.7...v0.1.0)

### Features

* **api:** update via SDK Studio ([#54](https://github.com/atla-ai/atla-sdk-python/issues/54)) ([7919869](https://github.com/atla-ai/atla-sdk-python/commit/7919869c75fc5f127bb16f068d86afa95c4de37a))
* **api:** update via SDK Studio ([#56](https://github.com/atla-ai/atla-sdk-python/issues/56)) ([fcd0dc4](https://github.com/atla-ai/atla-sdk-python/commit/fcd0dc47c433d716c8dc422cf5b71ab24d77effb))
* **api:** update via SDK Studio ([#57](https://github.com/atla-ai/atla-sdk-python/issues/57)) ([b5c2c86](https://github.com/atla-ai/atla-sdk-python/commit/b5c2c860da233cee7012cb15420cc412498ddff6))

## 0.1.0-alpha.7 (2024-05-29)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** update via SDK Studio ([#46](https://github.com/atla-ai/atla-sdk-python/issues/46)) ([22e29c6](https://github.com/atla-ai/atla-sdk-python/commit/22e29c691130bbd51f3a3bdf6db903c7f12e8106))
* **api:** update via SDK Studio ([#51](https://github.com/atla-ai/atla-sdk-python/issues/51)) ([5ee9198](https://github.com/atla-ai/atla-sdk-python/commit/5ee91985015bf8acfffe6b57ebdd57de160cd539))

## 0.1.0-alpha.6 (2024-05-28)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** update via SDK Studio ([#28](https://github.com/atla-ai/atla-sdk-python/issues/28)) ([820512c](https://github.com/atla-ai/atla-sdk-python/commit/820512cfd3da00bb2dc8e8c88810b4e93c01aeb8))
* **api:** update via SDK Studio ([#29](https://github.com/atla-ai/atla-sdk-python/issues/29)) ([6ccb1e9](https://github.com/atla-ai/atla-sdk-python/commit/6ccb1e9ceea8320ee39959c30bbcb14ee6e7a514))
* **api:** update via SDK Studio ([#31](https://github.com/atla-ai/atla-sdk-python/issues/31)) ([9121c0a](https://github.com/atla-ai/atla-sdk-python/commit/9121c0aead8165a3a1e5fbabeb11b94111d359cb))
* **api:** update via SDK Studio ([#32](https://github.com/atla-ai/atla-sdk-python/issues/32)) ([1375a6a](https://github.com/atla-ai/atla-sdk-python/commit/1375a6ab13219e5fa13042bde50f23726c8afb0f))
* **api:** update via SDK Studio ([#33](https://github.com/atla-ai/atla-sdk-python/issues/33)) ([c6787f5](https://github.com/atla-ai/atla-sdk-python/commit/c6787f52efe37a28da5ba84710cba9c3d5e07a66))
* **api:** update via SDK Studio ([#34](https://github.com/atla-ai/atla-sdk-python/issues/34)) ([f8a762f](https://github.com/atla-ai/atla-sdk-python/commit/f8a762fba5ca9eeee0b63bf9765e2d3ad4788b31))
* **api:** update via SDK Studio ([#35](https://github.com/atla-ai/atla-sdk-python/issues/35)) ([33ef5b2](https://github.com/atla-ai/atla-sdk-python/commit/33ef5b225e91643ecb32b3104b55d795c6be5c78))
* **api:** update via SDK Studio ([#36](https://github.com/atla-ai/atla-sdk-python/issues/36)) ([6b1b9c7](https://github.com/atla-ai/atla-sdk-python/commit/6b1b9c79476a16bfd752a59ab646685e89ac4bb8))
* **api:** update via SDK Studio ([#37](https://github.com/atla-ai/atla-sdk-python/issues/37)) ([d17cf40](https://github.com/atla-ai/atla-sdk-python/commit/d17cf40fe3d4ed60b3bc3022d1cc19bc916c94f8))
* **api:** update via SDK Studio ([#38](https://github.com/atla-ai/atla-sdk-python/issues/38)) ([71d1fbb](https://github.com/atla-ai/atla-sdk-python/commit/71d1fbbb4c6767ac464842d1babb7337af0f5f0b))
* **api:** update via SDK Studio ([#39](https://github.com/atla-ai/atla-sdk-python/issues/39)) ([b12bc41](https://github.com/atla-ai/atla-sdk-python/commit/b12bc4178a3928a6c4f6843d292150861fd21d7c))
* **api:** update via SDK Studio ([#40](https://github.com/atla-ai/atla-sdk-python/issues/40)) ([4f9e873](https://github.com/atla-ai/atla-sdk-python/commit/4f9e873745b98956ca45c67bb7c63c9763a355bc))
* **api:** update via SDK Studio ([#41](https://github.com/atla-ai/atla-sdk-python/issues/41)) ([8e5b758](https://github.com/atla-ai/atla-sdk-python/commit/8e5b758f6328ec013fb2592cffd637837ba1be19))
* **api:** update via SDK Studio ([#42](https://github.com/atla-ai/atla-sdk-python/issues/42)) ([83fd6b6](https://github.com/atla-ai/atla-sdk-python/commit/83fd6b6c09d26fdaa201be59fa6ac0704a10d4a6))

## 0.1.0-alpha.5 (2024-05-24)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** update via SDK Studio ([#25](https://github.com/atla-ai/atla-sdk-python/issues/25)) ([ee0f639](https://github.com/atla-ai/atla-sdk-python/commit/ee0f639ac33731b874ca847ad66373f0023156e1))

## 0.1.0-alpha.4 (2024-05-24)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([#19](https://github.com/atla-ai/atla-sdk-python/issues/19)) ([c89ef0b](https://github.com/atla-ai/atla-sdk-python/commit/c89ef0beffc1e9e56d805e477f78b1ce7032a5b8))
* **api:** update via SDK Studio ([#21](https://github.com/atla-ai/atla-sdk-python/issues/21)) ([29cc5b7](https://github.com/atla-ai/atla-sdk-python/commit/29cc5b74d3c286085994acecc4f45fea577471cc))
* **api:** update via SDK Studio ([#22](https://github.com/atla-ai/atla-sdk-python/issues/22)) ([bda5abd](https://github.com/atla-ai/atla-sdk-python/commit/bda5abda7ed271f623a0e7fa331e6826dfe0b187))
* **api:** update via SDK Studio ([#23](https://github.com/atla-ai/atla-sdk-python/issues/23)) ([9020e3f](https://github.com/atla-ai/atla-sdk-python/commit/9020e3f0257497b687b299a8f694bbf2868bcf93))

## 0.1.0-alpha.3 (2024-05-24)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([#13](https://github.com/atla-ai/atla-sdk-python/issues/13)) ([4582f5f](https://github.com/atla-ai/atla-sdk-python/commit/4582f5fa7ba2ebe3062a73683d8af11197ce8699))
* **api:** update via SDK Studio ([#15](https://github.com/atla-ai/atla-sdk-python/issues/15)) ([d811cd1](https://github.com/atla-ai/atla-sdk-python/commit/d811cd118c661e1c6846a4d2ad1226a95e6af56c))
* **api:** update via SDK Studio ([#16](https://github.com/atla-ai/atla-sdk-python/issues/16)) ([60f0712](https://github.com/atla-ai/atla-sdk-python/commit/60f07124e2ddc22b727e8ae77e5f665325f2934d))
* **api:** update via SDK Studio ([#17](https://github.com/atla-ai/atla-sdk-python/issues/17)) ([b1e0240](https://github.com/atla-ai/atla-sdk-python/commit/b1e0240351379822bb4d4cb8fd7fde15ef27749f))

## 0.1.0-alpha.2 (2024-05-23)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/atla-ai/atla-sdk-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#10](https://github.com/atla-ai/atla-sdk-python/issues/10)) ([9c319c4](https://github.com/atla-ai/atla-sdk-python/commit/9c319c4f935ac1d1c77a7b6aa0ec4331950cc7db))

## 0.1.0-alpha.1 (2024-05-23)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/atla-ai/atla-sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([7f6c5c3](https://github.com/atla-ai/atla-sdk-python/commit/7f6c5c385ec17bd6bd779d810ffd607a7275401d))
* **api:** update via SDK Studio ([99e4e30](https://github.com/atla-ai/atla-sdk-python/commit/99e4e30197e659d5ddfe3628b064888dd2df7c59))
* **api:** update via SDK Studio ([55783db](https://github.com/atla-ai/atla-sdk-python/commit/55783db425b9614edd88ab4c612a417f80122e90))
* **api:** update via SDK Studio ([613b3ba](https://github.com/atla-ai/atla-sdk-python/commit/613b3baed516bd0ec05951869e88bcd299e84a2e))
* **api:** update via SDK Studio ([1f594e5](https://github.com/atla-ai/atla-sdk-python/commit/1f594e55146024225762d048e6e5fcbf90137a1f))
* **api:** update via SDK Studio ([ce69aac](https://github.com/atla-ai/atla-sdk-python/commit/ce69aac5e2fb07e5d998ea40df1b896cb5a463fa))
* **api:** update via SDK Studio ([4cd9eed](https://github.com/atla-ai/atla-sdk-python/commit/4cd9eede22c730e2d248ca3575ce5b207c9cf985))
* **api:** update via SDK Studio ([#2](https://github.com/atla-ai/atla-sdk-python/issues/2)) ([d880576](https://github.com/atla-ai/atla-sdk-python/commit/d8805768fd122dd32522364f39145b1cf34a0743))
* **api:** update via SDK Studio ([#3](https://github.com/atla-ai/atla-sdk-python/issues/3)) ([dd10809](https://github.com/atla-ai/atla-sdk-python/commit/dd10809ab95ad6c673254cb1aac2d5b294aed9e9))
* **api:** update via SDK Studio ([#4](https://github.com/atla-ai/atla-sdk-python/issues/4)) ([3df4102](https://github.com/atla-ai/atla-sdk-python/commit/3df4102c8d097ac505ce0c210553e78ec580f7ef))
* **api:** update via SDK Studio ([#5](https://github.com/atla-ai/atla-sdk-python/issues/5)) ([7c21df4](https://github.com/atla-ai/atla-sdk-python/commit/7c21df4f45e31b9b563c6f0689ffc58264f8a439))
* **api:** update via SDK Studio ([#6](https://github.com/atla-ai/atla-sdk-python/issues/6)) ([98fa332](https://github.com/atla-ai/atla-sdk-python/commit/98fa332a8c798a2b98716e473695dd7374b6d184))
* **api:** update via SDK Studio ([#7](https://github.com/atla-ai/atla-sdk-python/issues/7)) ([2176287](https://github.com/atla-ai/atla-sdk-python/commit/2176287960faf0771e62b42094b3622110ca4521))
* **api:** update via SDK Studio ([#8](https://github.com/atla-ai/atla-sdk-python/issues/8)) ([3763ff4](https://github.com/atla-ai/atla-sdk-python/commit/3763ff499e63cf3945097920f35d20d4490b5c48))


### Chores

* configure new SDK language ([cb0d831](https://github.com/atla-ai/atla-sdk-python/commit/cb0d8317083e3bef4fb612b339e591198b9e1880))
* update SDK settings ([0d996b0](https://github.com/atla-ai/atla-sdk-python/commit/0d996b03c1c975713c556f39be8b088ce935a81e))
