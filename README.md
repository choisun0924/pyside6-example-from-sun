# pyside6-example-from-sun
파이썬으로 쉽게 UI 제작하는 방법을 배워보고자 합니다.
pyside6를 쉬운 예제로 공유합니다.

1. pyside6를 설치 해줍니다.

![image](https://user-images.githubusercontent.com/86217603/181402685-91995943-cd40-46a8-9851-0849d80b5441.png)

2. 아래와 같이 간단한 코드로 윈도우를 띄울 수 있습니다. 하지만 우리가 원하는건 이런 간단하게 끝나는게 아니겠죠?

![image](https://user-images.githubusercontent.com/86217603/181404166-9560ad5a-cbce-4f56-bf12-9a3515557c3a.png)

3. Qt Designer를 다운로드 받고 열어줍니다. 우리는 이 툴을 이용하여 쉽게 UI를 만들어볼겁니다.

![image](https://user-images.githubusercontent.com/86217603/181404411-9062a67d-bd59-48de-80ba-3f0e4080ddac.png)

4. Create Main Window를 하고,  간단하게 버튼 하나만 넣어보겠습니다.

![image](https://user-images.githubusercontent.com/86217603/181404608-e5b28078-0c1d-4044-8b69-8428b0816a8f.png)

![image](https://user-images.githubusercontent.com/86217603/181404786-cf759d01-af77-4c4f-8fc4-4c52246f919c.png)

- 버튼의 이름은 아래의 objectName이 되는데 프로그램 실행시 위의 이름으로 코드 내에 Class가 생성되기 때문에 해당 Class의 Methods를 사용할 수 있습니다.
- Test Button은 UI에 표기되는 text이며 우측의 objectName이 Class명이 됩니다.

5. 다음 UI 폴더에 세이브 해주도록 하겠습니다.

![image](https://user-images.githubusercontent.com/86217603/181405144-2ef4adfd-e352-4bba-809a-d86216865edf.png)

![image](https://user-images.githubusercontent.com/86217603/181405244-cd002e1b-94ce-4fd7-8d07-936c6b2248c7.png)

6. pyside6는 해당 ui 파일을 바로 사용할수 없습니다. ui/main.ui를 ui_main.py로 변환을 해주도록 하겠습니다.
- 프로그램 실행시 ui_main.py가 업데이트 되면서 실행됨
- ui_main의 Ui_MainWindow Class를 import

