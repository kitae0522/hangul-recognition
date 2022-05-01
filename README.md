# hangul-recognition
한글 인식기

## TODO
- [x] 손글씨 폰트로 117,500개의 글자 이미지 제작
- [ ] 모델 제작
- [ ] 모델 API 배포
- [ ] 테스트

## 사용된 손글씨 폰트 목록

![font_list](./docs/font_list.png)

총 50개의 손글씨 폰트를 사용했으며, 사용한 폰트는 아래와 같습니다.

| # | 폰트명 | Key |
|---|---|---|
| 1 | [손편지체](https://noonnu.cc/font_page/546) | `0` |
| 2 | [김남윤체](https://noonnu.cc/font_page/22) | `1` |
| 3 | [온글잎 윤우체](https://noonnu.cc/font_page/668) | `2` |
| 4 | [곰신체](https://noonnu.cc/font_page/540) | `3` |
| 5 | [온글잎 민혜체](https://noonnu.cc/font_page/675) | `4` |
| 6 | [몽돌](https://noonnu.cc/font_page/574) | `5` |
| 7 | [강원교육현옥샘체](https://noonnu.cc/font_page/804) | `6` |
| 8 | [어비 마이센체](https://noonnu.cc/font_page/178) | `7` |
| 9 | [봉숭아틴트](https://noonnu.cc/font_page/259) | `8` |
| 10 | [심경하체](https://noonnu.cc/font_page/873) | `9` |
| 11 | [카페24 빛나는별](https://noonnu.cc/font_page/343) | `10` |
| 12 | [중학생](https://noonnu.cc/font_page/570) | `11` |
| 13 | [강원교육새음체](https://noonnu.cc/font_page/806) | `12` |
| 14 | [어비 율체](https://noonnu.cc/font_page/207) | `13` |
| 15 | [어비 둘둘체](https://noonnu.cc/font_page/144) | `14` |
| 16 | [다행체](https://noonnu.cc/font_page/529) | `15` |
| 17 | [고딕 아니고 고딩](https://noonnu.cc/font_page/542) | `16` |
| 18 | [강인한 위로](https://noonnu.cc/font_page/560) | `17` |
| 19 | [꽃내음](https://noonnu.cc/font_page/541) | `18` |
| 20 | [갈맷글](https://noonnu.cc/font_page/604) | `19` |
| 21 | [가람연꽃](https://noonnu.cc/font_page/605) | `20` |
| 22 | [강부장님체](https://noonnu.cc/font_page/559) | `21` |
| 23 | [고려글꼴](https://noonnu.cc/font_page/564) | `22` |
| 24 | [미래나무](https://noonnu.cc/font_page/603) | `23` |
| 25 | [북극성](https://noonnu.cc/font_page/582) | `24` |
| 26 | [사랑해 아들](https://noonnu.cc/font_page/567) | `25` |
| 27 | [소미체](https://noonnu.cc/font_page/595) | `26` |
| 28 | [소방관의 기도](https://noonnu.cc/font_page/601) | `27` |
| 29 | [손편지체](https://noonnu.cc/font_page/546) | `28` |
| 30 | [아름드리 꽃나무](https://noonnu.cc/font_page/602) | `29` |
| 31 | [아빠의 연애편지](https://noonnu.cc/font_page/539) | `30` |
| 32 | [안쌍체](https://noonnu.cc/font_page/512) | `31` |
| 33 | [아줌마 자유](https://noonnu.cc/font_page/556) | `32` |
| 34 | [암스테르담](https://noonnu.cc/font_page/511) | `33` |
| 35 | [열일체](https://noonnu.cc/font_page/550) | `34` |
| 36 | [와일드](https://noonnu.cc/font_page/614) | `35` |
| 37 | [옥비체](https://noonnu.cc/font_page/579) | `36` |
| 38 | [자부심지우](https://noonnu.cc/font_page/584) | `37` |
| 39 | [장미체](https://noonnu.cc/font_page/586) | `38` |
| 40 | [점꼴체](https://noonnu.cc/font_page/536) | `39` |
| 41 | [칠백삼체 유서연](https://noonnu.cc/font_page/777) | `40` |
| 42 | [교보손글씨 2019](https://noonnu.cc/font_page/419) | `41` |
| 43 | [교보손글씨 2020 박도연](https://noonnu.cc/font_page/782) | `42` |
| 44 | [HS겨울눈꽃체2.0](https://noonnu.cc/font_page/810) | `43` |
| 45 | [주아체](https://noonnu.cc/font_page/53) | `44` |
| 46 | [도현체](https://noonnu.cc/font_page/55) | `45` |
| 47 | [을지로체](https://noonnu.cc/font_page/321) | `46` |
| 48 | [정묵바위체](https://noonnu.cc/font_page/395) | `47` |
| 49 | [어그로체](https://noonnu.cc/font_page/740) | `48` |
| 50 | [수트](https://noonnu.cc/font_page/844) | `49` |
